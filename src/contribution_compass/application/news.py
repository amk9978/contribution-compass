from __future__ import annotations

from dataclasses import dataclass

from contribution_compass.domain.models import ProjectNewsSnapshot
from contribution_compass.ports import Catalog


@dataclass(frozen=True, slots=True)
class ProjectNewsEntry:
    date: str
    project_id: str
    repository: str
    project_name: str
    group_id: str
    group_name: str
    news: ProjectNewsSnapshot

    def to_dict(self) -> dict[str, object]:
        return {
            "date": self.date,
            "project": {
                "id": self.project_id,
                "repository": self.repository,
                "name": self.project_name,
            },
            "group": {"id": self.group_id, "name": self.group_name},
            "news": self.news.to_dict(),
        }


class NewsQueries:
    """Deep read interface for factual release and public-roadmap news."""

    def __init__(self, catalog: Catalog) -> None:
        self._catalog = catalog

    def list(
        self,
        *,
        project: str | None = None,
        group: str | None = None,
        query: str = "",
        date: str | None = None,
        limit: int = 100,
    ) -> list[ProjectNewsEntry]:
        needle = query.casefold().strip()
        entries = [
            ProjectNewsEntry(
                date=dataset.date,
                project_id=dataset.repository_id,
                repository=dataset.repository,
                project_name=dataset.repository_name,
                group_id=dataset.group_id,
                group_name=dataset.group_name,
                news=dataset.news,
            )
            for dataset in self._catalog.repositories(date)
            if dataset.news is not None
            and (project is None or dataset.repository == project)
            and (group is None or dataset.group_id == group)
        ]
        if needle:
            entries = [entry for entry in entries if needle in self._search_text(entry)]
        entries.sort(key=lambda entry: entry.repository)
        entries.sort(
            key=lambda entry: (
                bool(entry.news.upcoming),
                (entry.news.latest_release.published_at if entry.news.latest_release else ""),
            ),
            reverse=True,
        )
        return entries[: min(max(limit, 1), 100)]

    @staticmethod
    def _search_text(entry: ProjectNewsEntry) -> str:
        release = entry.news.latest_release
        parts = [entry.repository, entry.project_name, entry.group_name]
        if release:
            parts.extend((release.title, release.tag, *release.highlights))
        for item in entry.news.upcoming:
            parts.extend((item.title, item.description or "", item.tag or ""))
        return " ".join(parts).casefold()
