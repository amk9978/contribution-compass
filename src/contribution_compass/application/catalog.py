from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from contribution_compass.domain.contributions import rank_contributions
from contribution_compass.domain.importance import importance_score, rank_updates
from contribution_compass.domain.models import (
    ContributionLead,
    ObservationEvent,
    RepositoryDataset,
    Signal,
)
from contribution_compass.domain.policies import (
    DEFAULT_CONTRIBUTION_POLICY,
    ContributionPolicy,
)
from contribution_compass.ports import Catalog


@dataclass(frozen=True, slots=True)
class ProjectSummary:
    id: str
    repository: str
    name: str
    group: str
    keywords: tuple[str, ...]
    signal_count: int
    event_count: int
    context: dict[str, object] | None
    provenance: dict[str, object] | None

    def to_dict(self) -> dict[str, object]:
        return {
            "id": self.id,
            "repository": self.repository,
            "name": self.name,
            "group": self.group,
            "keywords": list(self.keywords),
            "signalCount": self.signal_count,
            "eventCount": self.event_count,
            "context": self.context,
            "provenance": self.provenance,
        }


@dataclass(frozen=True, slots=True)
class ProjectComparison:
    """Factual row for comparing Project Sensors without a composite score."""

    id: str
    repository: str
    name: str
    repository_url: str
    group_id: str
    group_name: str
    language: str | None
    license: str | None
    stars: int | None
    forks: int | None
    latest_release: dict[str, str] | None
    recent_leads_observed: int
    recent_maintainer_invited_observed: int
    recent_triage_leads_observed: int
    snapshot_date: str
    collected_at: str | None
    since: str | None

    def to_dict(self) -> dict[str, object]:
        return {
            "id": self.id,
            "repository": self.repository,
            "name": self.name,
            "url": self.repository_url,
            "group": {"id": self.group_id, "name": self.group_name},
            "language": self.language,
            "license": self.license,
            "stars": self.stars,
            "forks": self.forks,
            "latestRelease": self.latest_release,
            "recentLeadsObserved": self.recent_leads_observed,
            "recentMaintainerInvitedObserved": self.recent_maintainer_invited_observed,
            "recentTriageLeadsObserved": self.recent_triage_leads_observed,
            "snapshot": {
                "date": self.snapshot_date,
                "collectedAt": self.collected_at,
                "since": self.since,
            },
        }


class CatalogQueries:
    """Deep read interface used identically by CLI views, MCP tools, and tests."""

    def __init__(
        self,
        catalog: Catalog,
        contribution_policy: ContributionPolicy = DEFAULT_CONTRIBUTION_POLICY,
    ) -> None:
        self._catalog = catalog
        self.contribution_policy = contribution_policy

    @staticmethod
    def _as_of(datasets: list[RepositoryDataset]) -> datetime | None:
        values = [run.collected_at for dataset in datasets for run in dataset.runs]
        if not values:
            return None
        try:
            return max(datetime.fromisoformat(value.replace("Z", "+00:00")) for value in values)
        except ValueError:
            return None

    def dates(self) -> list[str]:
        return self._catalog.dates()

    def list_projects(
        self, group: str | None = None, date: str | None = None
    ) -> list[ProjectSummary]:
        datasets = self._catalog.repositories(date)
        if group:
            datasets = [dataset for dataset in datasets if dataset.group_id == group]
        return [
            ProjectSummary(
                id=dataset.repository_id,
                repository=dataset.repository,
                name=dataset.repository_name,
                group=dataset.group_id,
                keywords=dataset.keywords,
                signal_count=len(dataset.signals),
                event_count=len(dataset.events),
                context=dataset.context.to_dict() if dataset.context else None,
                provenance=dataset.provenance.to_dict() if dataset.provenance else None,
            )
            for dataset in datasets
        ]

    def project_context(self, repository: str, date: str | None = None) -> RepositoryDataset | None:
        return self._catalog.project(repository, date)

    def compare_projects(
        self, *, group: str | None = None, date: str | None = None
    ) -> list[ProjectComparison]:
        """Compare Project Sensors using only facts in one collected snapshot."""
        datasets = self._catalog.repositories(date)
        if group:
            datasets = [dataset for dataset in datasets if dataset.group_id == group]
        signals = [signal for dataset in datasets for signal in dataset.signals]
        leads = rank_contributions(
            signals,
            limit=max(1, len(signals)),
            policy=self.contribution_policy,
            as_of=self._as_of(datasets),
        )
        lead_counts: dict[str, dict[str, int]] = {}
        for lead in leads:
            if not lead.signal.project:
                continue
            counts = lead_counts.setdefault(
                lead.signal.project,
                {"total": 0, "maintainer-invited": 0, "triage-lead": 0},
            )
            counts["total"] += 1
            counts[lead.tier] += 1

        rows: list[ProjectComparison] = []
        for dataset in datasets:
            context = dataset.context
            release = dataset.news.latest_release if dataset.news else None
            latest_run = (
                max(dataset.runs, key=lambda run: run.collected_at) if dataset.runs else None
            )
            counts = lead_counts.get(
                dataset.repository,
                {"total": 0, "maintainer-invited": 0, "triage-lead": 0},
            )
            rows.append(
                ProjectComparison(
                    id=dataset.repository_id,
                    repository=dataset.repository,
                    name=dataset.repository_name,
                    repository_url=(
                        context.url if context else f"https://github.com/{dataset.repository}"
                    ),
                    group_id=dataset.group_id,
                    group_name=dataset.group_name,
                    language=context.language if context else None,
                    license=context.license if context else None,
                    stars=context.stars if context else None,
                    forks=context.forks if context else None,
                    latest_release=(
                        {
                            "tag": release.tag,
                            "title": release.title,
                            "publishedAt": release.published_at,
                            "url": release.url,
                        }
                        if release
                        else None
                    ),
                    recent_leads_observed=counts["total"],
                    recent_maintainer_invited_observed=counts["maintainer-invited"],
                    recent_triage_leads_observed=counts["triage-lead"],
                    snapshot_date=dataset.date,
                    collected_at=latest_run.collected_at if latest_run else None,
                    since=latest_run.since if latest_run else None,
                )
            )
        return sorted(rows, key=lambda row: (row.group_name.casefold(), row.name.casefold()))

    def project_snapshot(
        self,
        repository: str,
        *,
        date: str | None = None,
        signal_limit: int = 20,
        event_limit: int = 20,
    ) -> dict[str, object] | None:
        """Return bounded context suitable for CLIs and LLM tool responses."""
        dataset = self.project_context(repository, date)
        if dataset is None:
            return None
        signals = rank_updates(dataset.signals, min(max(signal_limit, 1), 100))
        events = sorted(dataset.events, key=lambda event: event.observed_at, reverse=True)[
            : min(max(event_limit, 1), 100)
        ]
        return {
            "schemaVersion": 2,
            "date": dataset.date,
            "project": {
                "id": dataset.repository_id,
                "repository": dataset.repository,
                "name": dataset.repository_name,
                "keywords": list(dataset.keywords),
                "group": {"id": dataset.group_id, "name": dataset.group_name},
            },
            "context": dataset.context.to_dict() if dataset.context else None,
            "provenance": dataset.provenance.to_dict() if dataset.provenance else None,
            "news": dataset.news.to_dict() if dataset.news else None,
            "runCount": len(dataset.runs),
            "signalCount": len(dataset.signals),
            "eventCount": len(dataset.events),
            "importantSignals": [self.update_dict(signal) for signal in signals],
            "recentEvents": [event.to_dict() for event in events],
        }

    def search_updates(
        self,
        *,
        query: str = "",
        project: str | None = None,
        group: str | None = None,
        kind: str | None = None,
        date: str | None = None,
        limit: int = 20,
    ) -> list[Signal]:
        needle = query.casefold().strip()
        signals = self._catalog.signals(date)
        project_keywords = {
            dataset.repository: dataset.keywords for dataset in self._catalog.repositories(date)
        }
        filtered = [
            signal
            for signal in signals
            if (project is None or signal.project == project)
            and (group is None or signal.group == group)
            and (kind is None or signal.kind == kind)
            and (
                not needle
                or needle
                in " ".join(
                    (
                        signal.title,
                        signal.text or "",
                        signal.project or "",
                        " ".join(signal.labels),
                        " ".join(project_keywords.get(signal.project or "", ())),
                    )
                ).casefold()
            )
        ]
        return rank_updates(filtered, min(max(limit, 1), 100))

    def contribution_leads(
        self,
        *,
        query: str = "",
        project: str | None = None,
        group: str | None = None,
        tier: str | None = None,
        date: str | None = None,
        limit: int = 20,
    ) -> list[ContributionLead]:
        needle = query.casefold().strip()
        datasets = self._catalog.repositories(date)
        project_keywords = {dataset.repository: dataset.keywords for dataset in datasets}
        leads = rank_contributions(
            [signal for dataset in datasets for signal in dataset.signals],
            1000,
            policy=self.contribution_policy,
            as_of=self._as_of(datasets),
        )
        return [
            lead
            for lead in leads
            if (project is None or lead.signal.project == project)
            and (group is None or lead.signal.group == group)
            and (tier is None or lead.tier == tier)
            and (
                not needle
                or needle
                in " ".join(
                    (
                        lead.signal.title,
                        lead.signal.text or "",
                        lead.signal.project or "",
                        " ".join(lead.signal.labels),
                        " ".join(project_keywords.get(lead.signal.project or "", ())),
                    )
                ).casefold()
            )
        ][: min(max(limit, 1), 1000)]

    def signal_timeline(self, signal_id: str) -> list[ObservationEvent]:
        return self._catalog.events(signal_id)

    @staticmethod
    def update_dict(signal: Signal) -> dict[str, object]:
        return {**signal.to_dict(), "importanceScore": importance_score(signal)}
