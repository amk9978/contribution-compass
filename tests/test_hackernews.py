from __future__ import annotations

import asyncio
from datetime import UTC, datetime

import httpx

from contribution_compass.adapters.hackernews import HackerNewsCollector
from contribution_compass.domain.models import RepoConfig, RepoGroup


def test_hackernews_collects_current_configured_project_discussions_only() -> None:
    def response(request: httpx.Request) -> httpx.Response:
        if request.url.path.endswith("topstories.json"):
            return httpx.Response(200, json=[101, 102, 103])
        if request.url.path.endswith("beststories.json"):
            return httpx.Response(200, json=[101, 104])
        stories = {
            101: {
                "id": 101,
                "type": "story",
                "by": "dev",
                "time": 1786586400,
                "title": "FoundationDB gets a new storage engine",
                "url": "https://example.test/fdb",
                "score": 180,
                "descendants": 72,
            },
            102: {
                "id": 102,
                "type": "story",
                "time": 1786586400,
                "title": "Unrelated database release",
                "url": "https://example.test/other",
            },
            104: {
                "id": 104,
                "type": "story",
                "time": 1786586400,
                "title": "Repository discussion",
                "url": "https://github.com/apple/foundationdb/pull/1",
                "score": 10,
            },
        }
        story_id = int(request.url.path.split("/")[-1].split(".")[0])
        return httpx.Response(200, json=stories.get(story_id))

    async def collect() -> object:
        async with httpx.AsyncClient(
            base_url="https://hacker-news.test/v0", transport=httpx.MockTransport(response)
        ) as client:
            collector = HackerNewsCollector(client=client)
            return await collector.collect(
                (
                    RepoGroup(
                        "databases",
                        "Databases",
                        (
                            RepoConfig(
                                "foundationdb",
                                "apple/foundationdb",
                                "FoundationDB",
                                hackernews_keywords=("FoundationDB",),
                            ),
                        ),
                    ),
                ),
                datetime(2026, 8, 12, tzinfo=UTC),
                story_limit=4,
            )

    batch = asyncio.run(collect())
    assert [discussion.id for discussion in batch.discussions] == [
        "hackernews:101",
        "hackernews:104",
    ]
    assert batch.discussions[0].discussion_url == "https://news.ycombinator.com/item?id=101"
    assert batch.discussions[0].comments == 72
    assert batch.discussions[0].matched_by == ("keyword:FoundationDB",)


def test_hackernews_skips_old_dead_and_unmatched_stories() -> None:
    def response(request: httpx.Request) -> httpx.Response:
        if request.url.path.endswith(("topstories.json", "beststories.json")):
            return httpx.Response(200, json=[1, 2])
        story_id = int(request.url.path.split("/")[-1].split(".")[0])
        return httpx.Response(
            200,
            json={
                "id": story_id,
                "type": "story",
                "time": 1 if story_id == 1 else 1786586400,
                "title": "FoundationDB" if story_id == 1 else "FoundationDB is dead",
                "dead": story_id == 2,
            },
        )

    async def collect() -> object:
        async with httpx.AsyncClient(
            base_url="https://hacker-news.test/v0", transport=httpx.MockTransport(response)
        ) as client:
            return await HackerNewsCollector(client=client).collect(
                (
                    RepoGroup(
                        "db",
                        "DB",
                        (
                            RepoConfig(
                                "fdb",
                                "apple/foundationdb",
                                "FoundationDB",
                                hackernews_keywords=("FoundationDB",),
                            ),
                        ),
                    ),
                ),
                datetime(2026, 8, 12, tzinfo=UTC),
                story_limit=2,
            )

    assert asyncio.run(collect()).discussions == ()


def test_hackernews_keyword_mentions_inside_story_body_do_not_create_news_matches() -> None:
    item = {
        "id": 10,
        "type": "story",
        "time": 1786586400,
        "title": "Launch HN: A different coding tool",
        "text": "We compare ourselves with Claude Code and several other tools.",
        "url": "https://different-tool.example",
    }
    repo = RepoConfig(
        "claude-code",
        "anthropics/claude-code",
        "Claude Code",
        hackernews_keywords=("Claude Code",),
    )
    assert HackerNewsCollector._matches(item, repo) == ()
