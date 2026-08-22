from __future__ import annotations

import json
from pathlib import Path

from contribution_compass.views.site import StaticSitePublisher


def test_static_site_honestly_publishes_the_v2_reset(tmp_path: Path) -> None:
    output = tmp_path / "site"
    build = StaticSitePublisher(
        output_root=output,
        site_url="https://example.test/compass",
        repository_url="https://github.com/example/compass",
    ).build()

    page = (output / "index.html").read_text(encoding="utf-8")
    status = json.loads((output / "status.json").read_text(encoding="utf-8"))
    assert build.pages == 1
    assert "Project first" in page
    assert "personalized OSS investment recommender" in page
    assert "activity feed and issue-ranking prototype has been retired" in page
    assert status["phase"] == "v2-rewrite"
    assert status["specification"].endswith("/docs/product-spec-v2.md")


def test_static_site_refuses_a_workspace_output_directory(tmp_path: Path) -> None:
    publisher = StaticSitePublisher(
        output_root=Path.cwd(),
        site_url="https://example.test",
        repository_url="https://github.com/example/compass",
    )

    try:
        publisher.build()
    except ValueError as error:
        assert "Unsafe site output directory" in str(error)
    else:
        raise AssertionError("expected unsafe output directory to fail")
