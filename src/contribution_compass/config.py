from __future__ import annotations

import re
from pathlib import Path
from typing import Any, NoReturn
from urllib.parse import urlparse

import yaml

from contribution_compass.domain.models import (
    CatalogOverlayConfig,
    CompassConfig,
    RepoConfig,
    RepoGroup,
)
from contribution_compass.domain.policies import (
    DEFAULT_CONTRIBUTION_POLICY,
    ContributionPolicy,
    ContributionThresholds,
    ContributionWeights,
)

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


def _project_keywords(record: dict[str, Any], path: str) -> tuple[str, ...]:
    if "keywords" in record and "hackernews_keywords" in record:
        _fail(path, 'use "keywords" only; do not specify both keyword fields')
    key = "keywords" if "keywords" in record else "hackernews_keywords"
    return _string_array(record, key, path)


def _configured_strings(
    record: dict[str, Any], key: str, path: str, default: tuple[str, ...]
) -> tuple[str, ...]:
    return _string_array(record, key, path) if key in record else default


def _integer(record: dict[str, Any], key: str, path: str, default: int, *, minimum: int = 0) -> int:
    value = record.get(key, default)
    if not isinstance(value, int) or isinstance(value, bool) or value < minimum:
        _fail(f"{path}.{key}", f"expected an integer greater than or equal to {minimum}")
    return value


def _known_keys(record: dict[str, Any], allowed: set[str], path: str) -> None:
    unknown = sorted(set(record) - allowed)
    if unknown:
        _fail(path, f"unknown field(s): {', '.join(unknown)}")


def _contribution_policy(root: dict[str, Any]) -> ContributionPolicy:
    value = root.get("contributions")
    if value is None:
        return DEFAULT_CONTRIBUTION_POLICY
    policy = _record(value, "contributions")
    _known_keys(
        policy,
        {"invitation_labels", "beginner_labels", "excluded_labels", "weights", "thresholds"},
        "contributions",
    )
    raw_weights = _record(policy.get("weights", {}), "contributions.weights")
    weight_fields = set(ContributionWeights.__dataclass_fields__)
    _known_keys(raw_weights, weight_fields, "contributions.weights")
    defaults = DEFAULT_CONTRIBUTION_POLICY.weights
    weights = ContributionWeights(
        **{
            key: _integer(
                raw_weights,
                key,
                "contributions.weights",
                getattr(defaults, key),
            )
            for key in weight_fields
        }
    )
    raw_thresholds = _record(policy.get("thresholds", {}), "contributions.thresholds")
    threshold_fields = set(ContributionThresholds.__dataclass_fields__)
    _known_keys(raw_thresholds, threshold_fields, "contributions.thresholds")
    threshold_defaults = DEFAULT_CONTRIBUTION_POLICY.thresholds
    thresholds = ContributionThresholds(
        bug_engagement=_integer(
            raw_thresholds,
            "bug_engagement",
            "contributions.thresholds",
            threshold_defaults.bug_engagement,
        ),
        enhancement_reactions=_integer(
            raw_thresholds,
            "enhancement_reactions",
            "contributions.thresholds",
            threshold_defaults.enhancement_reactions,
        ),
        comments_per_point=_integer(
            raw_thresholds,
            "comments_per_point",
            "contributions.thresholds",
            threshold_defaults.comments_per_point,
            minimum=1,
        ),
        max_reaction_count=_integer(
            raw_thresholds,
            "max_reaction_count",
            "contributions.thresholds",
            threshold_defaults.max_reaction_count,
        ),
        max_comment_blocks=_integer(
            raw_thresholds,
            "max_comment_blocks",
            "contributions.thresholds",
            threshold_defaults.max_comment_blocks,
        ),
        recent_days=_integer(
            raw_thresholds,
            "recent_days",
            "contributions.thresholds",
            threshold_defaults.recent_days,
        ),
    )
    return ContributionPolicy(
        invitation_labels=_configured_strings(
            policy,
            "invitation_labels",
            "contributions",
            DEFAULT_CONTRIBUTION_POLICY.invitation_labels,
        ),
        beginner_labels=_configured_strings(
            policy,
            "beginner_labels",
            "contributions",
            DEFAULT_CONTRIBUTION_POLICY.beginner_labels,
        ),
        excluded_labels=_configured_strings(
            policy,
            "excluded_labels",
            "contributions",
            DEFAULT_CONTRIBUTION_POLICY.excluded_labels,
        ),
        weights=weights,
        thresholds=thresholds,
    )


def _catalog_overlays(root: dict[str, Any]) -> tuple[CatalogOverlayConfig, ...]:
    value = root.get("catalog_overlays", [])
    if not isinstance(value, list):
        _fail("root.catalog_overlays", "expected an array")
    overlays: list[CatalogOverlayConfig] = []
    seen: set[str] = set()
    for index, raw in enumerate(value):
        path = f"catalog_overlays[{index}]"
        record = _record(raw, path)
        _known_keys(record, {"id", "url", "max_age_hours"}, path)
        overlay_id = _text(record, "id", path)
        if not SAFE_ID.fullmatch(overlay_id):
            _fail(f"{path}.id", "expected a filesystem-safe identifier")
        if overlay_id in seen:
            _fail("root.catalog_overlays", f'duplicate catalog overlay id "{overlay_id}"')
        url = _text(record, "url", path).rstrip("/")
        parsed = urlparse(url)
        if parsed.scheme not in {"http", "https"} or not parsed.netloc:
            _fail(f"{path}.url", "expected an absolute HTTP(S) URL")
        max_age = _integer(record, "max_age_hours", path, 48, minimum=1)
        seen.add(overlay_id)
        overlays.append(CatalogOverlayConfig(overlay_id, url, max_age))
    return tuple(overlays)


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
                    keywords=_project_keywords(repo, repo_path),
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
        contribution_policy=_contribution_policy(root),
        catalog_overlays=_catalog_overlays(root),
    )


def load_config(path: str | Path = "config.yml") -> CompassConfig:
    config_path = Path(path)
    try:
        return parse_config(yaml.safe_load(config_path.read_text(encoding="utf-8")))
    except OSError as error:
        raise ValueError(f"Unable to read config file {config_path}") from error
