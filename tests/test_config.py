from __future__ import annotations

import pytest

from contribution_compass.config import parse_config


def test_arbitrary_groups_load_and_empty_means_empty() -> None:
    config = parse_config(
        {
            "lookback_hours": 12,
            "repo_groups": {
                "compilers": {
                    "name": "Compilers",
                    "repos": [{"id": "llvm", "repo": "llvm/llvm-project", "name": "LLVM"}],
                },
                "empty": {"name": "Empty", "repos": []},
            },
        }
    )
    assert [group.id for group in config.repo_groups] == ["compilers", "empty"]
    assert config.repo_groups[1].repos == ()
    assert all(
        "openclaw" not in repo.repo.lower() for group in config.repo_groups for repo in group.repos
    )


def test_hackernews_collection_and_keywords_are_explicit_and_empty_stays_empty() -> None:
    config = parse_config(
        {
            "hackernews": {"enabled": True, "story_limit": 75},
            "repo_groups": {
                "tools": {
                    "name": "Tools",
                    "repos": [
                        {
                            "id": "uv",
                            "repo": "astral-sh/uv",
                            "name": "uv",
                            "keywords": [],
                        }
                    ],
                }
            },
        }
    )
    assert config.hackernews_enabled is True
    assert config.hackernews_story_limit == 75
    assert config.repo_groups[0].repos[0].keywords == ()


def test_contribution_policy_is_configurable_and_empty_labels_stay_empty() -> None:
    config = parse_config(
        {
            "contributions": {
                "invitation_labels": [],
                "beginner_labels": [],
                "excluded_labels": ["do not touch"],
                "weights": {"maintainer_invitation": 41, "recent_activity": 0},
                "thresholds": {"recent_days": 30},
            },
            "repo_groups": {},
        }
    )
    policy = config.contribution_policy
    assert policy.invitation_labels == ()
    assert policy.beginner_labels == ()
    assert policy.excluded_labels == ("do not touch",)
    assert policy.weights.maintainer_invitation == 41
    assert policy.weights.reaction == 1
    assert policy.thresholds.recent_days == 30


def test_catalog_overlays_are_explicit_and_empty_stays_empty() -> None:
    assert parse_config({"catalog_overlays": [], "repo_groups": {}}).catalog_overlays == ()
    config = parse_config(
        {
            "catalog_overlays": [
                {"id": "shared", "url": "https://example.test/compass", "max_age_hours": 12}
            ],
            "repo_groups": {},
        }
    )
    assert config.catalog_overlays[0].id == "shared"
    assert config.catalog_overlays[0].max_age_hours == 12


def test_legacy_hackernews_keyword_name_loads_as_project_keywords() -> None:
    config = parse_config(
        {
            "repo_groups": {
                "tools": {
                    "name": "Tools",
                    "repos": [
                        {
                            "id": "widget",
                            "repo": "acme/widget",
                            "name": "Widget",
                            "hackernews_keywords": ["Widget Runtime"],
                        }
                    ],
                }
            }
        }
    )
    assert config.repo_groups[0].repos[0].keywords == ("Widget Runtime",)


@pytest.mark.parametrize(
    "value, message",
    [
        ({"repo_groups": {"x": {"name": "X", "repos": [{}]}}}, "expected a non-empty string"),
        (
            {
                "repo_groups": {
                    "a": {"name": "A", "repos": [{"id": "same", "repo": "a/a", "name": "A"}]},
                    "b": {"name": "B", "repos": [{"id": "same", "repo": "b/b", "name": "B"}]},
                }
            },
            "duplicate repository id",
        ),
        ({"repo_groups": {"x": {"name": "X"}}}, "expected an array"),
        (
            {
                "hackernews": {"enabled": True, "story_limit": 501},
                "repo_groups": {},
            },
            "integer from 1 to 500",
        ),
        (
            {
                "repo_groups": {
                    "tools": {
                        "name": "Tools",
                        "repos": [
                            {
                                "id": "widget",
                                "repo": "acme/widget",
                                "name": "Widget",
                                "keywords": ["Widget"],
                                "hackernews_keywords": ["Legacy Widget"],
                            }
                        ],
                    }
                }
            },
            "do not specify both keyword fields",
        ),
        (
            {
                "contributions": {"weights": {"mystery": 10}},
                "repo_groups": {},
            },
            "unknown field",
        ),
        (
            {
                "contributions": {"thresholds": {"comments_per_point": 0}},
                "repo_groups": {},
            },
            "greater than or equal to 1",
        ),
        (
            {
                "catalog_overlays": [{"id": "bad", "url": "file:///tmp/catalog"}],
                "repo_groups": {},
            },
            "absolute HTTP",
        ),
    ],
)
def test_malformed_config_fails_clearly(value: object, message: str) -> None:
    with pytest.raises(ValueError, match=message):
        parse_config(value)
