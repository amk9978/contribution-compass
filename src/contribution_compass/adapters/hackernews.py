from __future__ import annotations

import asyncio
import html
import logging
import re
from datetime import UTC, datetime
from typing import Any

import httpx

from contribution_compass.domain.models import (
    CommunityDiscussion,
    CommunityNewsBatch,
    RepoConfig,
    RepoGroup,
)

LOGGER = logging.getLogger(__name__)
TAG = re.compile(r"<[^>]+>")


def _plain_text(value: object) -> str:
    if not isinstance(value, str):
        return ""
    return " ".join(html.unescape(TAG.sub(" ", value)).split())


def _contains_phrase(haystack: str, phrase: str) -> bool:
    return re.search(rf"(?<![\w]){re.escape(phrase.casefold())}(?![\w])", haystack) is not None


class HackerNewsCollector:
    """Collect current HN stories and attach only explicit configured-project matches."""

    def __init__(
        self,
        *,
        client: httpx.AsyncClient | None = None,
        concurrency: int = 12,
    ) -> None:
        self._client = client
        self._concurrency = concurrency

    @staticmethod
    def _matches(item: dict[str, Any], repo: RepoConfig) -> tuple[str, ...]:
        title = _plain_text(item.get("title"))
        story_text = _plain_text(item.get("text"))
        story_url = str(item.get("url") or "")
        haystack = f"{title} {story_text} {story_url}".casefold()
        reasons: list[str] = []
        slug = repo.repo.casefold()
        if slug in haystack or f"github.com/{slug}" in story_url.casefold():
            reasons.append(f"repository:{repo.repo}")
        reasons.extend(
            f"keyword:{keyword}"
            for keyword in repo.hackernews_keywords
            if _contains_phrase(haystack, keyword)
        )
        return tuple(dict.fromkeys(reasons))

    @staticmethod
    def _discussion(
        item: dict[str, Any], repo: RepoConfig, matched_by: tuple[str, ...]
    ) -> CommunityDiscussion:
        story_id = int(item["id"])
        discussion_url = f"https://news.ycombinator.com/item?id={story_id}"
        timestamp = (
            datetime.fromtimestamp(int(item["time"]), tz=UTC).isoformat().replace("+00:00", "Z")
        )
        return CommunityDiscussion(
            id=f"hackernews:{story_id}",
            source="hackernews",
            repository=repo.repo,
            title=_plain_text(item["title"]),
            url=str(item.get("url") or discussion_url),
            discussion_url=discussion_url,
            published_at=timestamp,
            score=int(item.get("score", 0)),
            comments=int(item.get("descendants", 0)),
            author=str(item["by"]) if item.get("by") else None,
            matched_by=matched_by,
        )

    async def collect(
        self,
        groups: tuple[RepoGroup, ...],
        since: datetime,
        *,
        story_limit: int,
    ) -> CommunityNewsBatch:
        owns_client = self._client is None
        client = self._client or httpx.AsyncClient(
            base_url="https://hacker-news.firebaseio.com/v0/", timeout=20
        )
        failures: list[str] = []

        async def json(path: str) -> Any:
            response = await client.get(path)
            response.raise_for_status()
            return response.json()

        feed_limit = max(1, (story_limit + 1) // 2)
        feed_results = await asyncio.gather(
            json("topstories.json"), json("beststories.json"), return_exceptions=True
        )
        story_ids: list[int] = []
        for name, result in zip(("topstories", "beststories"), feed_results, strict=True):
            if isinstance(result, BaseException):
                message = f"{name}: {type(result).__name__}: {result}"
                failures.append(message)
                LOGGER.warning("[hackernews] %s", message)
                continue
            if isinstance(result, list):
                story_ids.extend(int(item) for item in result[:feed_limit])
        story_ids = list(dict.fromkeys(story_ids))[:story_limit]

        semaphore = asyncio.Semaphore(self._concurrency)

        async def item(story_id: int) -> Any:
            async with semaphore:
                try:
                    return await json(f"item/{story_id}.json")
                except Exception as error:
                    failures.append(f"item {story_id}: {type(error).__name__}: {error}")
                    return None

        try:
            items = await asyncio.gather(*(item(story_id) for story_id in story_ids))
        finally:
            if owns_client:
                await client.aclose()

        repositories = [repo for group in groups for repo in group.repos]
        discussions: list[CommunityDiscussion] = []
        for raw in items:
            if (
                not isinstance(raw, dict)
                or raw.get("type") != "story"
                or raw.get("deleted")
                or raw.get("dead")
                or not raw.get("title")
                or not raw.get("time")
            ):
                continue
            published = datetime.fromtimestamp(int(raw["time"]), tz=UTC)
            if published < since.astimezone(UTC):
                continue
            for repo in repositories:
                matched_by = self._matches(raw, repo)
                if matched_by:
                    discussions.append(self._discussion(raw, repo, matched_by))

        discussions.sort(
            key=lambda discussion: (
                -discussion.score,
                -discussion.comments,
                discussion.id,
                discussion.repository,
            )
        )
        LOGGER.info(
            "[hackernews] %d project discussions from %d current stories",
            len(discussions),
            len(items),
        )
        return CommunityNewsBatch(tuple(discussions), tuple(failures))
