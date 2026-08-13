from __future__ import annotations

import asyncio
import logging
from datetime import datetime
from typing import Any

import httpx

from contribution_compass.domain.models import (
    CollectionBatch,
    ProjectContext,
    ProjectNewsSnapshot,
    RepoConfig,
    RepoGroup,
    Signal,
    SignalKind,
    SignalMetrics,
)
from contribution_compass.domain.news import build_project_news

LOGGER = logging.getLogger(__name__)


class GitHubCollector:
    """Collect normalized GitHub evidence with bounded pagination and per-repository isolation."""

    def __init__(
        self,
        token: str,
        *,
        client: httpx.AsyncClient | None = None,
        page_size: int = 100,
        max_pages: int = 5,
        concurrency: int = 4,
    ) -> None:
        self._token = token
        self._client = client
        self._page_size = page_size
        self._max_pages = max_pages
        self._concurrency = concurrency

    def _headers(self) -> dict[str, str]:
        return {
            "Authorization": f"Bearer {self._token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "contribution-compass/0.2",
        }

    async def _json(
        self, client: httpx.AsyncClient, path: str, params: dict[str, str] | None = None
    ) -> Any:
        response = await client.get(path, params=params, headers=self._headers())
        if response.is_error:
            detail = response.text[:500]
            raise RuntimeError(f"GitHub API {response.status_code} for {path}: {detail}")
        return response.json()

    @staticmethod
    def _labels(raw_labels: list[Any]) -> tuple[str, ...]:
        labels: list[str] = []
        for label in raw_labels:
            if isinstance(label, str):
                labels.append(label)
            elif isinstance(label, dict) and isinstance(label.get("name"), str):
                labels.append(label["name"])
        return tuple(labels)

    @staticmethod
    def _issue(item: dict[str, Any], repo: RepoConfig, group: RepoGroup) -> Signal:
        kind: SignalKind = "pull_request" if "pull_request" in item else "issue"
        body = item.get("body")
        text = " ".join(body.split()) if isinstance(body, str) and body.strip() else None
        created = item.get("created_at")
        updated = item.get("updated_at")
        return Signal(
            id=f"github:{repo.repo}:{kind}:{item['number']}",
            source="github",
            group=group.id,
            project=repo.repo,
            kind=kind,
            title=str(item["title"]).strip(),
            text=text,
            url=str(item["html_url"]),
            created_at=created,
            updated_at=updated,
            timestamp=updated or created,
            metrics=SignalMetrics(
                comments=int(item.get("comments", 0)),
                reactions=int((item.get("reactions") or {}).get("total_count", 0)),
            ),
            labels=GitHubCollector._labels(item.get("labels") or []),
            author=(item.get("user") or {}).get("login"),
            state=item.get("state"),
            assignees=tuple(
                assignee["login"]
                for assignee in item.get("assignees") or []
                if isinstance(assignee, dict) and isinstance(assignee.get("login"), str)
            ),
        )

    @staticmethod
    def _release(item: dict[str, Any], repo: RepoConfig, group: RepoGroup) -> Signal:
        published = item.get("published_at") or item.get("created_at")
        body = item.get("body")
        return Signal(
            id=f"github:{repo.repo}:release:{item['id']}",
            source="github",
            group=group.id,
            project=repo.repo,
            kind="release",
            title=str(item.get("name") or item["tag_name"]).strip(),
            text=" ".join(body.split()) if isinstance(body, str) and body.strip() else None,
            url=str(item["html_url"]),
            created_at=published,
            updated_at=published,
            timestamp=published,
            author=(item.get("author") or {}).get("login"),
        )

    @staticmethod
    def _context(item: dict[str, Any], collected_at: str) -> ProjectContext:
        license_value = item.get("license") or {}
        return ProjectContext(
            repository=str(item["full_name"]),
            url=str(item["html_url"]),
            description=item.get("description"),
            homepage=item.get("homepage") or None,
            language=item.get("language"),
            topics=tuple(str(topic) for topic in item.get("topics") or []),
            license=license_value.get("spdx_id") if isinstance(license_value, dict) else None,
            default_branch=item.get("default_branch"),
            stars=int(item.get("stargazers_count", 0)),
            forks=int(item.get("forks_count", 0)),
            open_issues=int(item.get("open_issues_count", 0)),
            archived=bool(item.get("archived", False)),
            collected_at=collected_at,
        )

    async def _repository(
        self,
        client: httpx.AsyncClient,
        repo: RepoConfig,
        group: RepoGroup,
        since: datetime,
    ) -> tuple[list[Signal], ProjectContext, ProjectNewsSnapshot]:
        max_pages = self._max_pages if repo.paginated else 1
        signals: list[Signal] = []
        release_items: list[dict[str, Any]] = []
        context_raw = await self._json(client, f"/repos/{repo.repo}")

        for page in range(1, max_pages + 1):
            items = await self._json(
                client,
                f"/repos/{repo.repo}/issues",
                {
                    "state": "all",
                    "sort": "updated",
                    "direction": "desc",
                    "since": since.isoformat().replace("+00:00", "Z"),
                    "per_page": str(self._page_size),
                    "page": str(page),
                },
            )
            signals.extend(self._issue(item, repo, group) for item in items)
            oldest = items[-1].get("updated_at") if items else None
            if (
                len(items) < self._page_size
                or not oldest
                or datetime.fromisoformat(oldest.replace("Z", "+00:00")) < since
            ):
                break

        for page in range(1, min(max_pages, 3) + 1):
            releases = await self._json(
                client,
                f"/repos/{repo.repo}/releases",
                {"per_page": str(self._page_size), "page": str(page)},
            )
            release_items.extend(releases)
            recent = [
                item
                for item in releases
                if (timestamp := item.get("published_at") or item.get("created_at"))
                and datetime.fromisoformat(timestamp.replace("Z", "+00:00")) >= since
            ]
            signals.extend(self._release(item, repo, group) for item in recent)
            oldest = (
                releases[-1].get("published_at") or releases[-1].get("created_at")
                if releases
                else None
            )
            if (
                len(releases) < self._page_size
                or not oldest
                or datetime.fromisoformat(oldest.replace("Z", "+00:00")) < since
            ):
                break

        try:
            milestones = await self._json(
                client,
                f"/repos/{repo.repo}/milestones",
                {
                    "state": "open",
                    "sort": "due_on",
                    "direction": "asc",
                    "per_page": "5",
                },
            )
        except Exception as error:
            LOGGER.warning("[github] %s milestone news unavailable: %s", repo.repo, error)
            milestones = []

        collected_at = datetime.now().astimezone().isoformat()
        return (
            signals,
            self._context(context_raw, collected_at),
            build_project_news(repo.repo, release_items, milestones, collected_at),
        )

    async def collect(self, groups: tuple[RepoGroup, ...], since: datetime) -> CollectionBatch:
        owns_client = self._client is None
        client = self._client or httpx.AsyncClient(base_url="https://api.github.com", timeout=30)
        semaphore = asyncio.Semaphore(self._concurrency)

        async def collect_one(
            group: RepoGroup, repo: RepoConfig
        ) -> tuple[list[Signal], ProjectContext | None, ProjectNewsSnapshot | None, str | None]:
            async with semaphore:
                try:
                    signals, context, news = await self._repository(client, repo, group, since)
                    LOGGER.info("[github] %s: %d recent signals", repo.repo, len(signals))
                    return signals, context, news, None
                except Exception as error:
                    message = f"{repo.repo}: {error}"
                    LOGGER.error("[github] %s", message)
                    return [], None, None, message

        try:
            results = await asyncio.gather(
                *(collect_one(group, repo) for group in groups for repo in group.repos)
            )
        finally:
            if owns_client:
                await client.aclose()

        return CollectionBatch(
            signals=tuple(signal for signals, _, _, _ in results for signal in signals),
            contexts=tuple(context for _, context, _, _ in results if context is not None),
            failures=tuple(failure for _, _, _, failure in results if failure is not None),
            news=tuple(news for _, _, news, _ in results if news is not None),
        )
