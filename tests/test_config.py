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
    ],
)
def test_malformed_config_fails_clearly(value: object, message: str) -> None:
    with pytest.raises(ValueError, match=message):
        parse_config(value)
