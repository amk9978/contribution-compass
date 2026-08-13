from __future__ import annotations

import json
from dataclasses import replace
from pathlib import Path

from conftest import make_dataset

from contribution_compass.adapters.catalog import LocalJsonCatalog
from contribution_compass.application.catalog import CatalogQueries
from contribution_compass.application.news import NewsQueries
from contribution_compass.views.site import StaticSitePublisher


def write_catalog(root: Path) -> LocalJsonCatalog:
    dataset = make_dataset()
    directory = root / "2026-08-13/runtime-tools"
    directory.mkdir(parents=True)
    (directory / "widget.json").write_text(json.dumps(dataset.to_dict()), encoding="utf-8")
    (root / "2026-08-13/manifest.json").write_text(
        json.dumps(
            {
                "version": 3,
                "date": "2026-08-13",
                "repositories": [{"group": "runtime-tools", "path": "runtime-tools/widget.json"}],
            }
        ),
        encoding="utf-8",
    )
    return LocalJsonCatalog(root)


def test_catalog_queries_preserve_context_evidence_and_timeline(tmp_path: Path) -> None:
    queries = CatalogQueries(write_catalog(tmp_path / "data"))
    assert queries.list_projects()[0].context["language"] == "Python"  # type: ignore[index]
    assert queries.list_projects()[0].keywords == ("resource lifecycle", "async runtime")
    assert queries.search_updates(query="resource lifecycle")[0].project == "acme/widget"
    assert queries.contribution_leads(query="async runtime")[0].signal.url.endswith("/issues/42")
    assert queries.contribution_leads()[0].signal.url.endswith("/issues/42")
    assert queries.signal_timeline("github:acme/widget:issue:42")[0].event == "discovered"
    assert NewsQueries(write_catalog(tmp_path / "news-data")).list()[0].news.latest_release.tag == (
        "v2.0.0"
    )
    assert (
        NewsQueries(write_catalog(tmp_path / "keyword-news"))
        .list(query="resource lifecycle")[0]
        .repository
        == "acme/widget"
    )


def test_site_builds_human_and_machine_views(tmp_path: Path) -> None:
    catalog = write_catalog(tmp_path / "data")
    output = tmp_path / "site"
    build = StaticSitePublisher(
        catalog,
        output_root=output,
        site_url="https://example.github.io/contribution-compass",
        repository_url="https://github.com/example/contribution-compass",
    ).build()

    home = (output / "index.html").read_text()
    contribution = (output / "contribute/index.html").read_text()
    news_page = (output / "news/index.html").read_text()
    repository = (output / "updates/2026-08-13/runtime-tools/widget.html").read_text()
    api = json.loads((output / "api/v1/index.json").read_text())
    opportunities = json.loads((output / "api/v1/opportunities.json").read_text())
    repository_api = json.loads(
        (
            output / "api/v1/dates/2026-08-13/groups/runtime-tools/repositories/widget.json"
        ).read_text()
    )

    assert build.pages == 6
    assert "Follow important projects" in home
    assert "Maintainer invited" in contribution
    assert "Widget 2.0" in news_page
    assert "Widget 2.1" in news_page
    assert "Hacker News discussions" in news_page
    assert "https://news.ycombinator.com/item?id=123" in news_page
    assert "Observation trail" in repository
    assert "keyword: resource lifecycle" in repository
    assert "https://github.com/acme/widget/issues/42" in repository
    assert api["schemaVersion"] == 3
    assert opportunities["leads"][0]["evidenceUrl"].endswith("/issues/42")
    assert repository_api["dataset"]["events"][0]["event"] == "discovered"
    assert repository_api["dataset"]["repository"]["keywords"] == [
        "resource lifecycle",
        "async runtime",
    ]
    group_api = json.loads(
        (output / "api/v1/dates/2026-08-13/groups/runtime-tools/index.json").read_text()
    )
    assert group_api["repositories"][0]["keywords"] == [
        "resource lifecycle",
        "async runtime",
    ]
    assert repository_api["dataset"]["news"]["latestRelease"]["tag"] == "v2.0.0"
    assert (
        json.loads((output / "api/v1/news.json").read_text())["projects"][0]["news"]["upcoming"][0][
            "title"
        ]
        == "Widget 2.1"
    )
    assert json.loads((output / "news/feed.json").read_text())["items"][0][
        "external_url"
    ].startswith(("https://github.com/acme/widget/", "https://news.ycombinator.com/"))
    assert "Project News" in (output / "news/feed.xml").read_text()
    assert json.loads((output / "api/v1/schema.json").read_text())["title"].startswith(
        "Contribution Compass"
    )
    assert json.loads((output / "feed.json").read_text())["items"][0]["external_url"].endswith(
        "/issues/42"
    )
    assert "+0000" in (output / "feed.xml").read_text()
    assert "widget.html" in (output / "sitemap.xml").read_text()
    assert "/news/" in (output / "sitemap.xml").read_text()
    assert "Observation Events" in (output / "llms.txt").read_text()


def test_large_human_lists_are_split_into_static_pages(tmp_path: Path) -> None:
    root = tmp_path / "data"
    dataset = make_dataset()
    dataset.signals = [
        replace(
            dataset.signals[0],
            id=f"github:acme/widget:issue:{number}",
            url=f"https://github.com/acme/widget/issues/{number}",
            title=f"Contribution issue {number}",
        )
        for number in range(1, 56)
    ]
    directory = root / "2026-08-13/runtime-tools"
    directory.mkdir(parents=True)
    (directory / "widget.json").write_text(json.dumps(dataset.to_dict()), encoding="utf-8")
    (root / "2026-08-13/manifest.json").write_text(
        json.dumps(
            {
                "version": 3,
                "date": "2026-08-13",
                "repositories": [{"group": "runtime-tools", "path": "runtime-tools/widget.json"}],
            }
        ),
        encoding="utf-8",
    )
    output = tmp_path / "site"
    StaticSitePublisher(
        LocalJsonCatalog(root),
        output_root=output,
        site_url="https://example.test/compass",
        repository_url="https://github.com/example/compass",
    ).build()

    contribution_first = (output / "contribute/index.html").read_text()
    contribution_second = (output / "contribute/page/2/index.html").read_text()
    repository_third = (
        output / "updates/2026-08-13/runtime-tools/widget/page/2/index.html"
    ).read_text()
    assert contribution_first.count('class="contribution-card"') == 20
    assert contribution_second.count('class="contribution-card"') == 20
    assert "Page 1 of 3" in contribution_first
    assert "Page 2 of 2" in repository_third
    assert repository_third.count('class="signal-card"') == 5


def test_project_news_is_paginated_by_project(tmp_path: Path) -> None:
    root = tmp_path / "data"
    directory = root / "2026-08-13/runtime-tools"
    directory.mkdir(parents=True)
    repositories = []
    for number in range(1, 12):
        dataset = make_dataset()
        dataset.repository_id = f"widget-{number}"
        dataset.repository = f"acme/widget-{number}"
        dataset.repository_name = f"Widget {number}"
        assert dataset.news is not None
        dataset.news = replace(dataset.news, repository=dataset.repository)
        filename = f"widget-{number}.json"
        (directory / filename).write_text(json.dumps(dataset.to_dict()), encoding="utf-8")
        repositories.append({"group": "runtime-tools", "path": f"runtime-tools/{filename}"})
    (root / "2026-08-13/manifest.json").write_text(
        json.dumps({"version": 3, "date": "2026-08-13", "repositories": repositories}),
        encoding="utf-8",
    )
    output = tmp_path / "site"
    StaticSitePublisher(
        LocalJsonCatalog(root),
        output_root=output,
        site_url="https://example.test/compass",
        repository_url="https://github.com/example/compass",
    ).build()

    first = (output / "news/index.html").read_text()
    second = (output / "news/page/2/index.html").read_text()
    assert first.count('class="news-card"') == 10
    assert second.count('class="news-card"') == 1
    assert "Page 1 of 2" in first
