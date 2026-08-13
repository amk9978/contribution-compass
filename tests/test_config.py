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
                            "hackernews_keywords": [],
                        }
                    ],
                }
            },
        }
    )
    assert config.hackernews_enabled is True
    assert config.hackernews_story_limit == 75
    assert config.repo_groups[0].repos[0].hackernews_keywords == ()


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
    ],
)
def test_malformed_config_fails_clearly(value: object, message: str) -> None:
    with pytest.raises(ValueError, match=message):
        parse_config(value)
