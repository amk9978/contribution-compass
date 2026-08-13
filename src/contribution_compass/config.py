from __future__ import annotations

import re
from pathlib import Path
from typing import Any, NoReturn

import yaml

from contribution_compass.domain.models import CompassConfig, RepoConfig, RepoGroup

SAFE_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")
REPO_SLUG = re.compile(r"^[^/\s]+/[^/\s]+$")


def _fail(path: str, message: str) -> NoReturn:
    raise ValueError(f"Invalid config at {path}: {message}")


def _record(value: Any, path: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        _fail(path, "expected an object")
    return value


def _text(record: dict[str, Any], key: str, path: str) -> str:
    value = record.get(key)
    if not isinstance(value, str) or not value.strip():
        _fail(f"{path}.{key}", "expected a non-empty string")
    return value.strip()


def _string_array(record: dict[str, Any], key: str, path: str) -> tuple[str, ...]:
    value = record.get(key, [])
    if not isinstance(value, list) or any(
        not isinstance(item, str) or not item.strip() for item in value
    ):
        _fail(f"{path}.{key}", "expected an array of non-empty strings")
    return tuple(dict.fromkeys(item.strip() for item in value))


def parse_config(value: Any) -> CompassConfig:
    root = _record(value, "root")
    raw_groups = _record(root.get("repo_groups"), "repo_groups")
    seen_ids: set[str] = set()
    groups: list[RepoGroup] = []

    for group_id, raw_group in raw_groups.items():
        group_path = f"repo_groups.{group_id}"
        if not isinstance(group_id, str) or not SAFE_ID.fullmatch(group_id):
            _fail(group_path, "group id must be filesystem-safe")
        group = _record(raw_group, group_path)
        raw_repos = group.get("repos")
        if not isinstance(raw_repos, list):
            _fail(f"{group_path}.repos", "expected an array")
        repos: list[RepoConfig] = []
        for index, raw_repo in enumerate(raw_repos):
            repo_path = f"{group_path}.repos[{index}]"
            repo = _record(raw_repo, repo_path)
            repo_id = _text(repo, "id", repo_path)
            slug = _text(repo, "repo", repo_path)
            if not SAFE_ID.fullmatch(repo_id):
                _fail(f"{repo_path}.id", "expected a filesystem-safe identifier")
            if repo_id in seen_ids:
                _fail(f"{group_path}.repos", f'duplicate repository id "{repo_id}"')
            if not REPO_SLUG.fullmatch(slug):
                _fail(f"{repo_path}.repo", "expected a GitHub owner/repository slug")
            paginated = repo.get("paginated", False)
            if not isinstance(paginated, bool):
                _fail(f"{repo_path}.paginated", "expected a boolean")
            seen_ids.add(repo_id)
            repos.append(
                RepoConfig(
                    id=repo_id,
                    repo=slug,
                    name=_text(repo, "name", repo_path),
                    paginated=paginated,
                    hackernews_keywords=_string_array(repo, "hackernews_keywords", repo_path),
                )
            )
        description = group.get("description")
        if description is not None and not isinstance(description, str):
            _fail(f"{group_path}.description", "expected a string")
        groups.append(
            RepoGroup(
                id=group_id,
                name=_text(group, "name", group_path),
                repos=tuple(repos),
                description=description.strip() if isinstance(description, str) else None,
            )
        )

    lookback = root.get("lookback_hours", 24)
    if not isinstance(lookback, int) or isinstance(lookback, bool) or lookback <= 0:
        _fail("root.lookback_hours", "expected a positive integer")
    hackernews = root.get("hackernews", {})
    if not isinstance(hackernews, dict):
        _fail("root.hackernews", "expected an object")
    hackernews_enabled = hackernews.get("enabled", False)
    if not isinstance(hackernews_enabled, bool):
        _fail("root.hackernews.enabled", "expected a boolean")
    story_limit = hackernews.get("story_limit", 200)
    if (
        not isinstance(story_limit, int)
        or isinstance(story_limit, bool)
        or not 1 <= story_limit <= 500
    ):
        _fail("root.hackernews.story_limit", "expected an integer from 1 to 500")
    return CompassConfig(
        repo_groups=tuple(groups),
        lookback_hours=lookback,
        hackernews_enabled=hackernews_enabled,
        hackernews_story_limit=story_limit,
    )


def load_config(path: str | Path = "config.yml") -> CompassConfig:
    config_path = Path(path)
    try:
        return parse_config(yaml.safe_load(config_path.read_text(encoding="utf-8")))
    except OSError as error:
        raise ValueError(f"Unable to read config file {config_path}") from error
