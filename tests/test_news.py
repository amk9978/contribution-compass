from __future__ import annotations

from pathlib import Path

from conftest import make_dataset

from contribution_compass.config import parse_config
from contribution_compass.domain.news import build_project_news, release_highlights
from contribution_compass.views.markdown import MarkdownReportWriter


def test_release_highlights_extract_facts_and_skip_boilerplate() -> None:
    notes = """## Performance
- Faster compaction
- [Safer cancellation](https://example.test/change)
## New Contributors
- @someone made their first contribution
## Full Changelog
"""
    assert release_highlights(notes) == (
        "Performance",
        "Faster compaction",
        "Safer cancellation",
    )


def test_news_selects_latest_stable_and_labels_public_upcoming_evidence() -> None:
    releases = [
        {
            "tag_name": "v3.0.0-rc1",
            "name": "3.0 RC1",
            "html_url": "https://github.com/acme/widget/releases/tag/v3.0.0-rc1",
            "published_at": "2026-08-13T00:00:00Z",
            "body": "Release candidate",
            "prerelease": True,
            "draft": False,
        },
        {
            "tag_name": "v2.0.0",
            "name": "2.0",
            "html_url": "https://github.com/acme/widget/releases/tag/v2.0.0",
            "published_at": "2026-08-12T00:00:00Z",
            "body": "## Highlights\n- Stable lifecycle handling",
            "prerelease": False,
            "draft": False,
        },
    ]
    milestones = [
        {
            "title": "3.0",
            "html_url": "https://github.com/acme/widget/milestone/3",
            "description": "Public 3.0 plan",
            "due_on": "2026-09-01T00:00:00Z",
            "open_issues": 3,
            "closed_issues": 7,
        }
    ]
    news = build_project_news("acme/widget", releases, milestones, "2026-08-13T01:00:00Z")

    assert news.latest_release is not None and news.latest_release.tag == "v2.0.0"
    assert [item.kind for item in news.upcoming] == ["prerelease", "milestone"]
    assert news.upcoming[1].progress == 70
    assert all(item.url.startswith("https://github.com/") for item in news.upcoming)


def test_prerelease_older_than_latest_stable_is_not_presented_as_upcoming() -> None:
    releases = [
        {
            "tag_name": "v2.0.0",
            "html_url": "https://github.com/acme/widget/releases/tag/v2.0.0",
            "published_at": "2026-08-12T00:00:00Z",
            "prerelease": False,
            "draft": False,
        },
        {
            "tag_name": "v2.0.0-rc1",
            "html_url": "https://github.com/acme/widget/releases/tag/v2.0.0-rc1",
            "published_at": "2026-08-10T00:00:00Z",
            "prerelease": True,
            "draft": False,
        },
    ]
    news = build_project_news("acme/widget", releases, [], "2026-08-13T01:00:00Z")
    assert news.upcoming == ()


def test_open_milestone_for_already_released_version_is_not_called_upcoming() -> None:
    releases = [
        {
            "tag_name": "v2.1.3",
            "html_url": "https://github.com/acme/widget/releases/tag/v2.1.3",
            "published_at": "2026-08-12T00:00:00Z",
            "prerelease": False,
            "draft": False,
        }
    ]
    milestones = [
        {
            "title": "v2.1.0",
            "html_url": "https://github.com/acme/widget/milestone/21",
            "open_issues": 1,
            "closed_issues": 9,
        },
        {
            "title": "v2.2.0",
            "html_url": "https://github.com/acme/widget/milestone/22",
            "open_issues": 4,
            "closed_issues": 1,
        },
    ]
    news = build_project_news("acme/widget", releases, milestones, "2026-08-13T01:00:00Z")
    assert [item.title for item in news.upcoming] == ["v2.2.0"]


def test_markdown_news_stays_folder_separated_by_group_and_project(tmp_path: Path) -> None:
    dataset = make_dataset()
    config = parse_config(
        {
            "repo_groups": {
                "runtime-tools": {
                    "name": "Runtime Tools",
                    "repos": [{"id": "widget", "repo": "acme/widget", "name": "Widget"}],
                }
            }
        }
    )
    assert dataset.news is not None
    MarkdownReportWriter(tmp_path).publish(
        date=dataset.date,
        config=config,
        signals=tuple(dataset.signals),
        leads=(),
        news=(dataset.news,),
    )
    news_file = tmp_path / dataset.date / "news/runtime-tools/widget.md"
    assert "Widget 2.0" in news_file.read_text()
    assert "./runtime-tools/widget.md" in (tmp_path / dataset.date / "news/index.md").read_text()
