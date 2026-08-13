from __future__ import annotations

import json
from pathlib import Path
from typing import Any
from urllib.parse import quote

import httpx

from contribution_compass.domain.models import ObservationEvent, RepositoryDataset, Signal


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
