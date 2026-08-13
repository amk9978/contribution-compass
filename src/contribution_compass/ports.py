from __future__ import annotations

from datetime import datetime
from typing import Protocol

from contribution_compass.domain.models import (
    ChangeSet,
    CollectionBatch,
    CommunityNewsBatch,
    CompassConfig,
    ContributionLead,
    ObservationEvent,
    ProjectContext,
    ProjectNewsSnapshot,
    RepoGroup,
    RepositoryDataset,
    Signal,
)


class SignalCollector(Protocol):
    async def collect(self, groups: tuple[RepoGroup, ...], since: datetime) -> CollectionBatch: ...


class CommunityNewsCollector(Protocol):
    async def collect(
        self,
        groups: tuple[RepoGroup, ...],
        since: datetime,
        *,
        story_limit: int,
    ) -> CommunityNewsBatch: ...


class ObservationStore(Protocol):
    def detect_changes(self, signals: tuple[Signal, ...], observed_at: datetime) -> ChangeSet: ...


class DatasetWriter(Protocol):
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
    ) -> str: ...


class ReportWriter(Protocol):
    def publish(
        self,
        *,
        date: str,
        config: CompassConfig,
        signals: tuple[Signal, ...],
        leads: tuple[ContributionLead, ...],
        news: tuple[ProjectNewsSnapshot, ...],
    ) -> str: ...


class Catalog(Protocol):
    """Read-only application seam shared by local data, hosted data, and MCP."""

    def dates(self) -> list[str]: ...

    def repositories(self, date: str | None = None) -> list[RepositoryDataset]: ...

    def project(self, repository: str, date: str | None = None) -> RepositoryDataset | None: ...

    def signals(self, date: str | None = None) -> list[Signal]: ...

    def events(self, signal_id: str) -> list[ObservationEvent]: ...
