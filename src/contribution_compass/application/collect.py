from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime, timedelta

from contribution_compass.domain.contributions import rank_contributions
from contribution_compass.domain.models import CompassConfig
from contribution_compass.ports import (
    DatasetWriter,
    ObservationStore,
    ReportWriter,
    SignalCollector,
)


@dataclass(frozen=True, slots=True)
class CollectionResult:
    date: str
    observed_count: int
    changed_count: int
    event_count: int
    contribution_lead_count: int
    failures: tuple[str, ...]
    data_directory: str
    report_directory: str


class CollectUpdates:
    """Application controller for one reliable scheduled collection run."""

    def __init__(
        self,
        collector: SignalCollector,
        observations: ObservationStore,
        datasets: DatasetWriter,
        reports: ReportWriter,
    ) -> None:
        self._collector = collector
        self._observations = observations
        self._datasets = datasets
        self._reports = reports

    async def execute(
        self, config: CompassConfig, *, collected_at: datetime | None = None
    ) -> CollectionResult:
        now = collected_at or datetime.now(UTC)
        since = now - timedelta(hours=config.lookback_hours)
        date = now.date().isoformat()
        batch = await self._collector.collect(config.repo_groups, since)
        changes = self._observations.detect_changes(batch.signals, now)
        # Contribution availability is a property of the current observation window, not whether
        # an issue happened to change since the previous run.
        leads = tuple(rank_contributions(batch.signals))
        data_directory = self._datasets.persist(
            date=date,
            collected_at=now,
            since=since,
            config=config,
            observed=batch.signals,
            changes=changes,
            contexts=batch.contexts,
        )
        report_directory = self._reports.publish(
            date=date,
            config=config,
            signals=changes.signals,
            leads=leads,
        )
        return CollectionResult(
            date=date,
            observed_count=len(batch.signals),
            changed_count=len(changes.signals),
            event_count=len(changes.events),
            contribution_lead_count=len(leads),
            failures=batch.failures,
            data_directory=data_directory,
            report_directory=report_directory,
        )
