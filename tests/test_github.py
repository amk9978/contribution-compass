from __future__ import annotations

import asyncio
from datetime import UTC, datetime

import httpx

from contribution_compass.adapters.github import GitHubCollector
from contribution_compass.domain.models import CollectionBatch, RepoConfig, RepoGroup


def response(request: httpx.Request) -> httpx.Response:
    if request.url.path == "/repos/acme/widget":
        return httpx.Response(
            200,
            json={
                "full_name": "acme/widget",
                "html_url": "https://github.com/acme/widget",
                "description": "A widget",
                "language": "Python",
                "topics": ["runtime"],
                "license": {"spdx_id": "MIT"},
                "default_branch": "main",
                "stargazers_count": 10,
                "forks_count": 2,
                "open_issues_count": 3,
            },
        )
    if request.url.path.endswith("/releases"):
        return httpx.Response(
            200,
            json=[
                {
                    "id": 7,
                    "tag_name": "v2.0.0",
                    "name": "Widget 2.0",
                    "body": "## Highlights\n- Faster cleanup",
                    "html_url": "https://github.com/acme/widget/releases/tag/v2.0.0",
                    "published_at": "2026-08-13T03:00:00Z",
                    "prerelease": False,
                    "draft": False,
                }
            ],
        )
    if request.url.path.endswith("/milestones"):
        return httpx.Response(
            200,
            json=[
                {
                    "number": 2,
                    "title": "Widget 2.1",
                    "description": "Cancellation improvements",
                    "html_url": "https://github.com/acme/widget/milestone/2",
                    "due_on": "2026-09-01T00:00:00Z",
                    "open_issues": 6,
                    "closed_issues": 4,
                }
            ],
        )
    return httpx.Response(
        200,
        json=[
            {
                "number": 1,
                "title": "Resource leak",
                "body": "Workers remain alive",
                "html_url": "https://github.com/acme/widget/issues/1",
                "created_at": "2026-08-12T01:00:00Z",
                "updated_at": "2026-08-13T01:00:00Z",
                "comments": 7,
                "reactions": {"total_count": 4},
                "labels": [{"name": "good first issue"}],
                "user": {"login": "dev"},
                "state": "open",
                "assignees": [],
            },
            {
                "number": 2,
                "title": "Fix leak",
                "html_url": "https://github.com/acme/widget/pull/2",
                "created_at": "2026-08-12T02:00:00Z",
                "updated_at": "2026-08-13T02:00:00Z",
                "state": "closed",
                "assignees": [{"login": "maintainer"}],
                "pull_request": {"url": "api"},
            },
        ],
    )


def test_github_normalizes_issues_prs_context_state_and_assignees() -> None:
    async def collect() -> CollectionBatch:
        async with httpx.AsyncClient(
            base_url="https://api.github.test", transport=httpx.MockTransport(response)
        ) as client:
            collector = GitHubCollector("token", client=client)
            return await collector.collect(
                (
                    RepoGroup(
                        "runtime-tools",
                        "Runtime Tools",
                        (RepoConfig("widget", "acme/widget", "Widget"),),
                    ),
                ),
                datetime(2026, 8, 12, tzinfo=UTC),
            )

    batch = asyncio.run(collect())
    assert [signal.kind for signal in batch.signals] == ["issue", "pull_request", "release"]
    assert batch.signals[0].state == "open"
    assert batch.signals[1].assignees == ("maintainer",)
    assert batch.contexts[0].language == "Python"
    assert batch.news[0].latest_release is not None
    assert batch.news[0].latest_release.highlights == ("Highlights", "Faster cleanup")
    assert batch.news[0].upcoming[0].title == "Widget 2.1"


def test_one_repository_failure_does_not_abort_other_repositories() -> None:
    def mixed(request: httpx.Request) -> httpx.Response:
        if "broken" in request.url.path:
            return httpx.Response(500, text="boom")
        return response(request)

    async def collect() -> CollectionBatch:
        async with httpx.AsyncClient(
            base_url="https://api.github.test", transport=httpx.MockTransport(mixed)
        ) as client:
            collector = GitHubCollector("token", client=client)
            return await collector.collect(
                (
                    RepoGroup(
                        "runtime-tools",
                        "Runtime Tools",
                        (
                            RepoConfig("widget", "acme/widget", "Widget"),
                            RepoConfig("broken", "acme/broken", "Broken"),
                        ),
                    ),
                ),
                datetime(2026, 8, 12, tzinfo=UTC),
            )

    batch = asyncio.run(collect())
    assert len(batch.signals) == 3
    assert len(batch.failures) == 1


def test_paginated_repository_stops_at_configured_page_limit() -> None:
    issue_pages: list[int] = []

    def paged(request: httpx.Request) -> httpx.Response:
        if request.url.path == "/repos/acme/widget":
            return response(request)
        if request.url.path.endswith("/releases"):
            return httpx.Response(200, json=[])
        if request.url.path.endswith("/milestones"):
            return httpx.Response(200, json=[])
        page = int(request.url.params["page"])
        issue_pages.append(page)
        return httpx.Response(
            200,
            json=[
                {
                    "number": page,
                    "title": f"Issue page {page}",
                    "html_url": f"https://github.com/acme/widget/issues/{page}",
                    "created_at": "2026-08-12T01:00:00Z",
                    "updated_at": "2026-08-13T01:00:00Z",
                    "state": "open",
                }
            ],
        )

    async def collect() -> CollectionBatch:
        async with httpx.AsyncClient(
            base_url="https://api.github.test", transport=httpx.MockTransport(paged)
        ) as client:
            return await GitHubCollector("token", client=client, page_size=1, max_pages=2).collect(
                (
                    RepoGroup(
                        "runtime-tools",
                        "Runtime Tools",
                        (RepoConfig("widget", "acme/widget", "Widget", paginated=True),),
                    ),
                ),
                datetime(2026, 8, 12, tzinfo=UTC),
            )

    batch = asyncio.run(collect())
    assert issue_pages == [1, 2]
    assert len(batch.signals) == 2
