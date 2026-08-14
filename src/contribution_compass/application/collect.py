from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime, timedelta

from contribution_compass.domain.contributions import rank_contributions
from contribution_compass.domain.models import (
    CommunityDiscussion,
    CompassConfig,
    ProjectNewsSnapshot,
)
from contribution_compass.ports import (
    CommunityNewsCollector,
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
        community_news: CommunityNewsCollector | None = None,
    ) -> None:
        self._collector = collector
        self._observations = observations
        self._datasets = datasets
        self._reports = reports
        self._community_news = community_news

    @staticmethod
    def _attach_discussions(
        news: tuple[ProjectNewsSnapshot, ...], discussions: tuple[CommunityDiscussion, ...]
    ) -> tuple[ProjectNewsSnapshot, ...]:
        by_repository: dict[str, list[CommunityDiscussion]] = {}
        for discussion in discussions:
            by_repository.setdefault(discussion.repository, []).append(discussion)
        return tuple(
            ProjectNewsSnapshot(
                repository=snapshot.repository,
                collected_at=snapshot.collected_at,
                latest_release=snapshot.latest_release,
                upcoming=snapshot.upcoming,
                community_discussions=tuple(by_repository.get(snapshot.repository, ())),
            )
            for snapshot in news
        )

    async def execute(
        self, config: CompassConfig, *, collected_at: datetime | None = None
    ) -> CollectionResult:
        now = collected_at or datetime.now(UTC)
        since = now - timedelta(hours=config.lookback_hours)
        date = now.date().isoformat()
        batch = await self._collector.collect(config.repo_groups, since)
        community_failures: tuple[str, ...] = ()
        project_news = batch.news
        if config.hackernews_enabled and self._community_news is not None:
            community = await self._community_news.collect(
                config.repo_groups,
                since,
                story_limit=config.hackernews_story_limit,
            )
            project_news = self._attach_discussions(batch.news, community.discussions)
            community_failures = community.failures
        changes = self._observations.detect_changes(batch.signals, now)
        # Contribution availability is a property of the current observation window, not whether
        # an issue happened to change since the previous run.
        leads = tuple(
            rank_contributions(
                batch.signals,
                policy=config.contribution_policy,
                as_of=now,
            )
        )
        data_directory = self._datasets.persist(
            date=date,
            collected_at=now,
            since=since,
            config=config,
            observed=batch.signals,
            changes=changes,
            contexts=batch.contexts,
            news=project_news,
        )
        report_directory = self._reports.publish(
            date=date,
            config=config,
            signals=changes.signals,
            leads=leads,
            news=project_news,
        )
        return CollectionResult(
            date=date,
            observed_count=len(batch.signals),
            changed_count=len(changes.signals),
            event_count=len(changes.events),
            contribution_lead_count=len(leads),
            failures=(*batch.failures, *community_failures),
            data_directory=data_directory,
            report_directory=report_directory,
        )
