from __future__ import annotations

from dataclasses import dataclass

from contribution_compass.domain.contributions import rank_contributions
from contribution_compass.domain.importance import importance_score, rank_updates
from contribution_compass.domain.models import (
    ContributionLead,
    ObservationEvent,
    RepositoryDataset,
    Signal,
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
        }


class CatalogQueries:
    """Deep read interface used identically by CLI views, MCP tools, and tests."""

    def __init__(self, catalog: Catalog) -> None:
        self._catalog = catalog

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
            )
            for dataset in datasets
        ]

    def project_context(self, repository: str, date: str | None = None) -> RepositoryDataset | None:
        return self._catalog.project(repository, date)

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
        project_keywords = {
            dataset.repository: dataset.keywords for dataset in self._catalog.repositories(date)
        }
        leads = rank_contributions(self._catalog.signals(date), 1000)
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
