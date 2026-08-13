from __future__ import annotations

import hashlib
import json
import os
from datetime import datetime
from pathlib import Path
from typing import Any, cast

from contribution_compass.domain.models import (
    ChangeKind,
    ChangeSet,
    CompassConfig,
    CrawlRun,
    ObservationEvent,
    ProjectContext,
    ProjectNewsSnapshot,
    RepositoryDataset,
    Signal,
)

FINGERPRINT_FIELDS = (
    "title",
    "text",
    "updatedAt",
    "metrics",
    "labels",
    "url",
    "state",
    "assignees",
)


def _atomic_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(f"{path.suffix}.tmp")
    temporary.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    os.replace(temporary, path)


def _fingerprint(snapshot: dict[str, Any]) -> str:
    stable = {field: snapshot.get(field) for field in FINGERPRINT_FIELDS}
    encoded = json.dumps(stable, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(encoded.encode()).hexdigest()


class JsonObservationStore:
    """Persist fingerprints and full snapshots so changed fields remain explainable."""

    def __init__(self, root: str | Path = ".state") -> None:
        self._path = Path(root) / "github.json"

    def _load(self) -> dict[str, Any]:
        if not self._path.exists():
            return {"version": 2, "items": {}}
        value = json.loads(self._path.read_text(encoding="utf-8"))
        if not isinstance(value.get("items"), dict):
            raise ValueError(f"Unsupported observation state: {self._path}")
        return cast(dict[str, Any], value)

    def detect_changes(self, signals: tuple[Signal, ...], observed_at: datetime) -> ChangeSet:
        state = self._load()
        items: dict[str, Any] = state["items"]
        changed_signals: list[Signal] = []
        events: list[ObservationEvent] = []
        observed_iso = observed_at.isoformat().replace("+00:00", "Z")

        for signal in signals:
            snapshot = signal.to_dict()
            fingerprint = _fingerprint(snapshot)
            previous = items.get(signal.id)
            if previous is None or previous.get("fingerprint") != fingerprint:
                previous_snapshot = (
                    previous.get("snapshot", {}) if isinstance(previous, dict) else {}
                )
                changed_fields = tuple(
                    field
                    for field in FINGERPRINT_FIELDS
                    if previous_snapshot and previous_snapshot.get(field) != snapshot.get(field)
                )
                change: ChangeKind = "new" if previous is None else "updated"
                changed_signal = signal.with_change(change)
                event_hash = hashlib.sha256(
                    f"{signal.id}\0{observed_iso}\0{fingerprint}".encode()
                ).hexdigest()[:20]
                changed_signals.append(changed_signal)
                events.append(
                    ObservationEvent(
                        id=f"event:{event_hash}",
                        signal_id=signal.id,
                        event="discovered" if previous is None else "changed",
                        observed_at=observed_iso,
                        changed_fields=changed_fields,
                        signal=changed_signal,
                    )
                )
            items[signal.id] = {
                "fingerprint": fingerprint,
                "lastSeen": observed_iso,
                "snapshot": snapshot,
            }

        _atomic_json(self._path, {"version": 2, "items": items})
        return ChangeSet(signals=tuple(changed_signals), events=tuple(events))


class JsonDatasetWriter:
    """Write folder-separated repository snapshots plus append-only Observation Events."""

    def __init__(self, root: str | Path = "data") -> None:
        self._root = Path(root)

    @staticmethod
    def _read_dataset(
        path: Path, date: str, group_id: str, group_name: str, repo_id: str, repo: str, name: str
    ) -> RepositoryDataset:
        if not path.exists():
            return RepositoryDataset(
                date=date,
                group_id=group_id,
                group_name=group_name,
                repository_id=repo_id,
                repository=repo,
                repository_name=name,
            )
        return RepositoryDataset.from_dict(json.loads(path.read_text(encoding="utf-8")))

    def persist(
        self,
        *,
        date: str,
        collected_at: datetime,
        since: datetime,
        config: CompassConfig,
        observed: tuple[Signal, ...],
        changes: ChangeSet,
        contexts: tuple[ProjectContext, ...],
        news: tuple[ProjectNewsSnapshot, ...],
    ) -> str:
        directory = self._root / date
        manifest_repositories: list[dict[str, Any]] = []
        context_by_repo = {context.repository: context for context in contexts}
        news_by_repo = {snapshot.repository: snapshot for snapshot in news}
        event_by_repo: dict[str, list[ObservationEvent]] = {}
        for event in changes.events:
            if event.signal.project:
                event_by_repo.setdefault(event.signal.project, []).append(event)

        for group in config.repo_groups:
            for repo in group.repos:
                relative = Path(group.id) / f"{repo.id}.json"
                destination = directory / relative
                dataset = self._read_dataset(
                    destination, date, group.id, group.name, repo.id, repo.repo, repo.name
                )
                observed_repo = [signal for signal in observed if signal.project == repo.repo]
                changed_repo = [signal for signal in changes.signals if signal.project == repo.repo]
                merged = {signal.id: signal for signal in dataset.signals}
                current = {signal.id: signal for signal in observed_repo}
                current.update({signal.id: signal for signal in changed_repo})
                merged.update(current)
                known_events = {event.id for event in dataset.events}
                dataset.events.extend(
                    event
                    for event in event_by_repo.get(repo.repo, [])
                    if event.id not in known_events
                )
                dataset.signals = sorted(merged.values(), key=lambda signal: signal.id)
                dataset.context = context_by_repo.get(repo.repo, dataset.context)
                dataset.news = news_by_repo.get(repo.repo, dataset.news)
                dataset.runs.append(
                    CrawlRun(
                        collected_at=collected_at.isoformat().replace("+00:00", "Z"),
                        since=since.isoformat().replace("+00:00", "Z"),
                        observed_count=len(observed_repo),
                        changed_count=len(changed_repo),
                    )
                )
                _atomic_json(destination, dataset.to_dict())
                manifest_repositories.append(
                    {
                        "group": group.id,
                        "repository": repo.repo,
                        "path": relative.as_posix(),
                        "observedCount": len(observed_repo),
                        "changedCount": len(changed_repo),
                        "eventCount": len(event_by_repo.get(repo.repo, [])),
                    }
                )

        _atomic_json(
            directory / "manifest.json",
            {
                "version": 2,
                "date": date,
                "collectedAt": collected_at.isoformat().replace("+00:00", "Z"),
                "since": since.isoformat().replace("+00:00", "Z"),
                "repositories": manifest_repositories,
            },
        )
        return str(directory)
