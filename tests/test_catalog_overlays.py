from __future__ import annotations

import json
from dataclasses import replace
from datetime import UTC, datetime
from pathlib import Path

import httpx
from conftest import make_dataset, make_signal

from contribution_compass.adapters.catalog import assemble_catalog
from contribution_compass.config import parse_config


def _write_local(root: Path, date: str = "2026-08-14") -> None:
    dataset = make_dataset(make_signal(title="Local evidence wins on an equal source date"))
    dataset.date = date
    directory = root / date / "local"
    directory.mkdir(parents=True)
    (directory / "widget.json").write_text(json.dumps(dataset.to_dict()))
    (root / date / "manifest.json").write_text(
        json.dumps(
            {
                "repositories": [{"path": "local/widget.json"}],
                "collectedAt": "2026-08-14T08:00:00Z",
            }
        )
    )


def _remote_client() -> httpx.Client:
    remote_widget = make_dataset(make_signal(title="Remote duplicate"))
    remote_widget.date = "2026-08-14"
    remote_only = replace(
        make_dataset(make_signal(project="acme/remote", id="github:acme/remote:issue:1")),
        date="2026-08-14",
        group_id="upstream",
        group_name="Upstream",
        repository_id="remote",
        repository="acme/remote",
        repository_name="Remote",
        keywords=("remote",),
    )
    hidden = replace(
        make_dataset(make_signal(project="acme/hidden", id="github:acme/hidden:issue:1")),
        date="2026-08-14",
        group_id="upstream",
        group_name="Upstream",
        repository_id="hidden",
        repository="acme/hidden",
        repository_name="Hidden",
    )

    def handler(request: httpx.Request) -> httpx.Response:
        path = request.url.path
        if path.endswith("/api/v1/index.json"):
            return httpx.Response(
                200,
                json={
                    "schemaVersion": 3,
                    "generatedAt": "2026-08-14T09:00:00Z",
                    "dates": [{"date": "2026-08-14"}],
                },
            )
        if path.endswith("/api/v1/dates/2026-08-14/index.json"):
            return httpx.Response(200, json={"groups": [{"id": "upstream"}]})
        if path.endswith("/api/v1/dates/2026-08-14/groups/upstream/index.json"):
            return httpx.Response(
                200,
                json={
                    "repositories": [
                        {"id": "widget", "repository": "acme/widget"},
                        {"id": "remote", "repository": "acme/remote"},
                        {"id": "hidden", "repository": "acme/hidden"},
                    ]
                },
            )
        values = {
            "widget.json": remote_widget,
            "remote.json": remote_only,
            "hidden.json": hidden,
        }
        for filename, dataset in values.items():
            if path.endswith(filename):
                return httpx.Response(200, json={"dataset": dataset.to_dict()})
        return httpx.Response(404)

    return httpx.Client(transport=httpx.MockTransport(handler))


def _config() -> object:
    return {
        "catalog_overlays": [
            {
                "id": "community",
                "url": "https://catalog.example/compass",
                "max_age_hours": 24,
            }
        ],
        "repo_groups": {
            "interests": {
                "name": "My Interests",
                "repos": [
                    {
                        "id": "widget-local",
                        "repo": "acme/widget",
                        "name": "My Widget",
                        "keywords": ["my keyword"],
                    },
                    {"id": "remote", "repo": "acme/remote", "name": "Remote Project"},
                ],
            }
        },
    }


def test_overlay_reuses_only_configured_projects_with_local_precedence(tmp_path: Path) -> None:
    _write_local(tmp_path / "data")
    config = parse_config(_config())
    assembly = assemble_catalog(
        config,
        local_root=tmp_path / "data",
        clients={"community": _remote_client()},
        now=datetime(2026, 8, 14, 10, tzinfo=UTC),
    )
    datasets = assembly.catalog.repositories()
    assert [dataset.repository for dataset in datasets] == ["acme/widget", "acme/remote"]
    assert datasets[0].signals[0].title == "Local evidence wins on an equal source date"
    assert datasets[0].repository_id == "widget-local"
    assert datasets[0].keywords == ("my keyword",)
    assert datasets[0].provenance is not None
    assert datasets[0].provenance.kind == "local"
    assert datasets[1].provenance is not None
    assert datasets[1].provenance.catalog_id == "community"
    assert "acme/hidden" not in {dataset.repository for dataset in datasets}
    assert assembly.covered_repositories == {
        "acme/widget",
        "acme/remote",
        "acme/hidden",
    }
    assert all(not group.repos for group in assembly.collection_config.repo_groups)


def test_stale_overlay_is_ignored_and_direct_collection_remains(tmp_path: Path) -> None:
    _write_local(tmp_path / "data")
    config = parse_config(_config())
    assembly = assemble_catalog(
        config,
        local_root=tmp_path / "data",
        clients={"community": _remote_client()},
        now=datetime(2026, 8, 16, 10, tzinfo=UTC),
    )
    assert assembly.active_overlays == ()
    assert "stale" in assembly.failures[0]
    delta = assembly.collection_config
    assert sum(len(group.repos) for group in delta.repo_groups) == 2
    assert [dataset.repository for dataset in assembly.catalog.repositories()] == ["acme/widget"]


def test_newer_overlay_replaces_an_older_local_snapshot(tmp_path: Path) -> None:
    _write_local(tmp_path / "data", "2026-08-13")
    config = parse_config(_config())
    assembly = assemble_catalog(
        config,
        local_root=tmp_path / "data",
        clients={"community": _remote_client()},
        now=datetime(2026, 8, 14, 10, tzinfo=UTC),
    )
    widget = assembly.catalog.project("acme/widget")
    assert widget is not None
    assert widget.signals[0].title == "Remote duplicate"
    assert widget.provenance is not None
    assert widget.provenance.kind == "overlay"
