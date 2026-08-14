from __future__ import annotations

import json
import logging
from dataclasses import dataclass, replace
from datetime import UTC, datetime, timedelta
from pathlib import Path
from typing import Any
from urllib.parse import quote

import httpx

from contribution_compass.domain.models import (
    CatalogOverlayConfig,
    CatalogProvenance,
    CompassConfig,
    ObservationEvent,
    RepositoryDataset,
    Signal,
)
from contribution_compass.ports import Catalog

LOGGER = logging.getLogger(__name__)


class LocalJsonCatalog:
    """Read a checked-in Contribution Compass data tree."""

    def __init__(self, root: str | Path = "data") -> None:
        self._root = Path(root)

    def dates(self) -> list[str]:
        if not self._root.exists():
            return []
        return sorted(
            (
                entry.name
                for entry in self._root.iterdir()
                if entry.is_dir() and len(entry.name) == 10
            ),
            reverse=True,
        )

    def _date(self, date: str | None) -> str | None:
        return date or next(iter(self.dates()), None)

    def repositories(self, date: str | None = None) -> list[RepositoryDataset]:
        selected = self._date(date)
        if selected is None:
            return []
        manifest_path = self._root / selected / "manifest.json"
        if not manifest_path.exists():
            return []
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        return [
            RepositoryDataset.from_dict(
                json.loads((self._root / selected / entry["path"]).read_text(encoding="utf-8"))
            )
            for entry in manifest.get("repositories", [])
        ]

    def project(self, repository: str, date: str | None = None) -> RepositoryDataset | None:
        return next(
            (dataset for dataset in self.repositories(date) if dataset.repository == repository),
            None,
        )

    def signals(self, date: str | None = None) -> list[Signal]:
        return [signal for dataset in self.repositories(date) for signal in dataset.signals]

    def events(self, signal_id: str) -> list[ObservationEvent]:
        events = [
            event
            for date in self.dates()
            for dataset in self.repositories(date)
            for event in dataset.events
            if event.signal_id == signal_id
        ]
        return sorted(events, key=lambda event: event.observed_at)


class RemoteJsonCatalog:
    """Read the versioned, folder-separated catalog published on GitHub Pages."""

    def __init__(self, base_url: str, *, client: httpx.Client | None = None) -> None:
        self._base_url = base_url.rstrip("/")
        self._client = client or httpx.Client(timeout=30, follow_redirects=True)
        self._cache: dict[str, dict[str, Any]] = {}

    def _get(self, path: str) -> dict[str, Any]:
        if path in self._cache:
            return self._cache[path]
        response = self._client.get(f"{self._base_url}/{path.lstrip('/')}")
        response.raise_for_status()
        value = response.json()
        if not isinstance(value, dict):
            raise ValueError(f"Expected JSON object from {path}")
        self._cache[path] = value
        return value

    def dates(self) -> list[str]:
        index = self._get("api/v1/index.json")
        return [str(entry["date"]) for entry in index.get("dates", [])]

    def metadata(self) -> tuple[int, str]:
        index = self._get("api/v1/index.json")
        generated_at = index.get("generatedAt")
        if not isinstance(generated_at, str):
            raise ValueError("Remote catalog index has no generatedAt timestamp")
        return int(index.get("schemaVersion", 0)), generated_at

    def _date(self, date: str | None) -> str | None:
        return date or next(iter(self.dates()), None)

    def repositories(self, date: str | None = None) -> list[RepositoryDataset]:
        selected = self._date(date)
        if selected is None:
            return []
        date_index = self._get(f"api/v1/dates/{selected}/index.json")
        datasets: list[RepositoryDataset] = []
        for group in date_index.get("groups", []):
            group_index = self._get(
                f"api/v1/dates/{selected}/groups/{quote(str(group['id']), safe='')}/index.json"
            )
            for repository in group_index.get("repositories", []):
                value = self._get(
                    f"api/v1/dates/{selected}/groups/{quote(str(group['id']), safe='')}/"
                    f"repositories/{quote(str(repository['id']), safe='')}.json"
                )
                datasets.append(RepositoryDataset.from_dict(value["dataset"]))
        return datasets

    def project(self, repository: str, date: str | None = None) -> RepositoryDataset | None:
        return next(
            (dataset for dataset in self.repositories(date) if dataset.repository == repository),
            None,
        )

    def signals(self, date: str | None = None) -> list[Signal]:
        return [signal for dataset in self.repositories(date) for signal in dataset.signals]

    def events(self, signal_id: str) -> list[ObservationEvent]:
        events = [
            event
            for date in self.dates()
            for dataset in self.repositories(date)
            for event in dataset.events
            if event.signal_id == signal_id
        ]
        return sorted(events, key=lambda event: event.observed_at)


@dataclass(frozen=True, slots=True)
class ActiveOverlay:
    config: CatalogOverlayConfig
    catalog: Catalog
    generated_at: str
    covered_repositories: frozenset[str]


@dataclass(frozen=True, slots=True)
class CatalogAssembly:
    catalog: Catalog
    collection_config: CompassConfig
    covered_repositories: frozenset[str]
    active_overlays: tuple[str, ...]
    failures: tuple[str, ...]


class OverlayCatalog:
    """Compose configured catalogs with local precedence and no hidden Project Sensors."""

    def __init__(
        self,
        primary: Catalog,
        config: CompassConfig,
        overlays: tuple[ActiveOverlay, ...],
    ) -> None:
        self._primary = primary
        self._config = config
        self._overlays = overlays

    def dates(self) -> list[str]:
        values = set(self._primary.dates())
        for overlay in self._overlays:
            try:
                values.update(overlay.catalog.dates())
            except (httpx.HTTPError, ValueError, KeyError) as error:
                LOGGER.warning("[catalog:%s] %s", overlay.config.id, error)
        return sorted(values, reverse=True)

    @staticmethod
    def _source_date(catalog: Catalog, selected: str, latest: str) -> str:
        dates = catalog.dates()
        return dates[0] if selected == latest and dates else selected

    @staticmethod
    def _datasets(catalog: Catalog, date: str) -> dict[str, RepositoryDataset]:
        return {dataset.repository.casefold(): dataset for dataset in catalog.repositories(date)}

    def repositories(self, date: str | None = None) -> list[RepositoryDataset]:
        dates = self.dates()
        selected = date or next(iter(dates), None)
        if selected is None:
            return []
        latest = dates[0]
        primary_date = self._source_date(self._primary, selected, latest)
        primary = self._datasets(self._primary, primary_date)
        overlay_datasets: list[tuple[ActiveOverlay, dict[str, RepositoryDataset], str]] = []
        for overlay in self._overlays:
            try:
                source_date = self._source_date(overlay.catalog, selected, latest)
                overlay_datasets.append(
                    (overlay, self._datasets(overlay.catalog, source_date), source_date)
                )
            except (httpx.HTTPError, ValueError, KeyError) as error:
                LOGGER.warning("[catalog:%s] %s", overlay.config.id, error)

        results: list[RepositoryDataset] = []
        for group in self._config.repo_groups:
            for repo in group.repos:
                key = repo.repo.casefold()
                source = primary.get(key)
                provenance: CatalogProvenance | None = None
                selected_source_date = primary_date if source is not None else ""
                if source is not None:
                    provenance = CatalogProvenance(kind="local", source_date=source.date)
                for overlay, datasets, source_date in overlay_datasets:
                    candidate_dataset = datasets.get(key)
                    if candidate_dataset is not None and source_date > selected_source_date:
                        source = candidate_dataset
                        selected_source_date = source_date
                        provenance = CatalogProvenance(
                            kind="overlay",
                            source_date=source_date,
                            catalog_id=overlay.config.id,
                            catalog_url=overlay.config.url,
                            catalog_generated_at=overlay.generated_at,
                        )
                if source is None:
                    continue
                results.append(
                    replace(
                        source,
                        date=selected,
                        group_id=group.id,
                        group_name=group.name,
                        repository_id=repo.id,
                        repository=repo.repo,
                        repository_name=repo.name,
                        keywords=repo.keywords,
                        provenance=provenance,
                    )
                )
        return results

    def project(self, repository: str, date: str | None = None) -> RepositoryDataset | None:
        return next(
            (dataset for dataset in self.repositories(date) if dataset.repository == repository),
            None,
        )

    def signals(self, date: str | None = None) -> list[Signal]:
        return [signal for dataset in self.repositories(date) for signal in dataset.signals]

    def events(self, signal_id: str) -> list[ObservationEvent]:
        events = {
            event.id: event
            for date in self.dates()
            for dataset in self.repositories(date)
            for event in dataset.events
            if event.signal_id == signal_id
        }
        return sorted(events.values(), key=lambda event: event.observed_at)


def _timestamp(value: str) -> datetime:
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    return parsed if parsed.tzinfo else parsed.replace(tzinfo=UTC)


def assemble_catalog(
    config: CompassConfig,
    *,
    local_root: str | Path = "data",
    clients: dict[str, httpx.Client] | None = None,
    now: datetime | None = None,
) -> CatalogAssembly:
    primary = LocalJsonCatalog(local_root)
    active: list[ActiveOverlay] = []
    failures: list[str] = []
    reference = now or datetime.now(UTC)
    if not reference.tzinfo:
        reference = reference.replace(tzinfo=UTC)
    for overlay_config in config.catalog_overlays:
        try:
            remote = RemoteJsonCatalog(
                overlay_config.url,
                client=(clients or {}).get(overlay_config.id),
            )
            schema_version, generated_at = remote.metadata()
            if schema_version not in {3, 4}:
                raise ValueError(f"unsupported schemaVersion {schema_version}")
            age = reference - _timestamp(generated_at)
            if age > timedelta(hours=overlay_config.max_age_hours):
                raise ValueError(
                    f"catalog is stale ({int(age.total_seconds() // 3600)}h old; "
                    f"maximum {overlay_config.max_age_hours}h)"
                )
            # Validate complete repository payloads before suppressing direct collection. A remote
            # index alone is not sufficient evidence that its advertised snapshots are usable.
            covered = frozenset(dataset.repository for dataset in remote.repositories())
            active.append(ActiveOverlay(overlay_config, remote, generated_at, covered))
        except (httpx.HTTPError, ValueError, KeyError) as error:
            failures.append(f"{overlay_config.id}: {error}")
    covered_repositories = frozenset(
        repository.casefold() for overlay in active for repository in overlay.covered_repositories
    )
    collection_config = replace(
        config,
        repo_groups=tuple(
            replace(
                group,
                repos=tuple(
                    repo for repo in group.repos if repo.repo.casefold() not in covered_repositories
                ),
            )
            for group in config.repo_groups
        ),
    )
    return CatalogAssembly(
        catalog=OverlayCatalog(primary, config, tuple(active)),
        collection_config=collection_config,
        covered_repositories=covered_repositories,
        active_overlays=tuple(overlay.config.id for overlay in active),
        failures=tuple(failures),
    )
