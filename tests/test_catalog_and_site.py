from __future__ import annotations

import json
from pathlib import Path

from conftest import make_dataset

from contribution_compass.adapters.catalog import LocalJsonCatalog
from contribution_compass.application.catalog import CatalogQueries
from contribution_compass.views.site import StaticSitePublisher


def write_catalog(root: Path) -> LocalJsonCatalog:
    dataset = make_dataset()
    directory = root / "2026-08-13/runtime-tools"
    directory.mkdir(parents=True)
    (directory / "widget.json").write_text(json.dumps(dataset.to_dict()), encoding="utf-8")
    (root / "2026-08-13/manifest.json").write_text(
        json.dumps(
            {
                "version": 2,
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
    assert queries.contribution_leads()[0].signal.url.endswith("/issues/42")
    assert queries.signal_timeline("github:acme/widget:issue:42")[0].event == "discovered"


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
    repository = (output / "updates/2026-08-13/runtime-tools/widget.html").read_text()
    api = json.loads((output / "api/v1/index.json").read_text())
    opportunities = json.loads((output / "api/v1/opportunities.json").read_text())
    repository_api = json.loads(
        (
            output / "api/v1/dates/2026-08-13/groups/runtime-tools/repositories/widget.json"
        ).read_text()
    )

    assert build.pages == 5
    assert "Follow important projects" in home
    assert "Maintainer invited" in contribution
    assert "Observation trail" in repository
    assert "https://github.com/acme/widget/issues/42" in repository
    assert api["schemaVersion"] == 2
    assert opportunities["leads"][0]["evidenceUrl"].endswith("/issues/42")
    assert repository_api["dataset"]["events"][0]["event"] == "discovered"
    assert json.loads((output / "api/v1/schema.json").read_text())["title"].startswith(
        "Contribution Compass"
    )
    assert json.loads((output / "feed.json").read_text())["items"][0]["external_url"].endswith(
        "/issues/42"
    )
    assert "+0000" in (output / "feed.xml").read_text()
    assert "widget.html" in (output / "sitemap.xml").read_text()
    assert "Observation Events" in (output / "llms.txt").read_text()
