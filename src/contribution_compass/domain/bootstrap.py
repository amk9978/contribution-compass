from __future__ import annotations

import json
import re
import tomllib
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from contribution_compass.domain.policies import DEFAULT_CONTRIBUTION_POLICY

GITHUB_REFERENCE = re.compile(
    r"(?:git\+https?://|https?://|ssh://git@|git@)?github\.com[/:]"
    r"(?P<owner>[A-Za-z0-9_.-]+)/(?P<repo>[A-Za-z0-9_.-]+)",
    re.IGNORECASE,
)
REPOSITORY_SLUG = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")
PYTHON_REQUIREMENT = re.compile(r"^([A-Za-z0-9][A-Za-z0-9_.-]*)(?:\[[^]]+\])?")


@dataclass(frozen=True, slots=True)
class DependencyReference:
    ecosystem: str
    name: str


@dataclass(frozen=True, slots=True)
class ProjectCandidate:
    repository: str
    name: str
    keywords: tuple[str, ...]
    source: str


@dataclass(frozen=True, slots=True)
class ManifestDiscovery:
    repositories: tuple[ProjectCandidate, ...]
    dependencies: tuple[DependencyReference, ...]


def github_repository(value: str) -> str | None:
    stripped = value.strip().removesuffix(".git")
    if REPOSITORY_SLUG.fullmatch(stripped):
        return stripped
    match = GITHUB_REFERENCE.search(value)
    if not match:
        return None
    return f"{match.group('owner')}/{match.group('repo').removesuffix('.git')}"


def candidate(repository: str, *, name: str | None = None, source: str) -> ProjectCandidate:
    slug = github_repository(repository)
    if slug is None:
        raise ValueError(f"Expected a GitHub owner/repository reference, got {repository!r}")
    project_name = name or slug.split("/", 1)[1]
    return ProjectCandidate(
        repository=slug,
        name=project_name,
        keywords=(project_name,),
        source=source,
    )


def _package_json(path: Path, value: dict[str, Any]) -> ManifestDiscovery:
    repositories: list[ProjectCandidate] = []
    dependencies: list[DependencyReference] = []
    for section in ("dependencies", "devDependencies", "optionalDependencies"):
        raw = value.get(section, {})
        if not isinstance(raw, dict):
            continue
        for name, specification in raw.items():
            if not isinstance(name, str):
                continue
            slug = github_repository(str(specification))
            if slug:
                repositories.append(candidate(slug, name=name, source=str(path)))
            else:
                dependencies.append(DependencyReference("npm", name))
    return ManifestDiscovery(tuple(repositories), tuple(dependencies))


def _requirements(path: Path, text: str) -> ManifestDiscovery:
    repositories: list[ProjectCandidate] = []
    dependencies: list[DependencyReference] = []
    for raw_line in text.splitlines():
        line = raw_line.split(" #", 1)[0].strip()
        if not line or line.startswith(("#", "-r", "--requirement", "-c", "--constraint")):
            continue
        slug = github_repository(line)
        if slug:
            repositories.append(candidate(slug, source=str(path)))
            continue
        match = PYTHON_REQUIREMENT.match(line)
        if match:
            dependencies.append(DependencyReference("pypi", match.group(1)))
    return ManifestDiscovery(tuple(repositories), tuple(dependencies))


def _go_mod(path: Path, text: str) -> ManifestDiscovery:
    repositories: list[ProjectCandidate] = []
    in_require = False
    for raw_line in text.splitlines():
        line = raw_line.split("//", 1)[0].strip()
        if line == "require (":
            in_require = True
            continue
        if in_require and line == ")":
            in_require = False
            continue
        if line.startswith("require "):
            line = line.removeprefix("require ").strip()
        elif not in_require:
            continue
        module = line.split(maxsplit=1)[0] if line else ""
        slug = github_repository(module)
        if slug:
            repositories.append(candidate(slug, source=str(path)))
    return ManifestDiscovery(tuple(repositories), ())


def _pyproject(path: Path, value: dict[str, Any]) -> ManifestDiscovery:
    names: list[str] = []
    project = value.get("project")
    if isinstance(project, dict):
        dependencies = project.get("dependencies", [])
        if isinstance(dependencies, list):
            names.extend(str(item) for item in dependencies)
        optional = project.get("optional-dependencies", {})
        if isinstance(optional, dict):
            names.extend(
                str(item)
                for group in optional.values()
                if isinstance(group, list)
                for item in group
            )
    poetry = value.get("tool", {})
    if isinstance(poetry, dict):
        poetry = poetry.get("poetry", {})
        if isinstance(poetry, dict):
            dependencies = poetry.get("dependencies", {})
            if isinstance(dependencies, dict):
                names.extend(str(name) for name in dependencies if str(name).casefold() != "python")
    return _requirements(path, "\n".join(names))


def discover_manifest(path: str | Path) -> ManifestDiscovery:
    manifest = Path(path)
    try:
        text = manifest.read_text(encoding="utf-8")
    except OSError as error:
        raise ValueError(f"Unable to read dependency file {manifest}") from error
    name = manifest.name.casefold()
    try:
        if name == "package.json":
            value = json.loads(text)
            if not isinstance(value, dict):
                raise ValueError("expected a JSON object")
            return _package_json(manifest, value)
        if name == "go.mod":
            return _go_mod(manifest, text)
        if name == "pyproject.toml":
            return _pyproject(manifest, tomllib.loads(text))
        return _requirements(manifest, text)
    except (json.JSONDecodeError, tomllib.TOMLDecodeError, ValueError) as error:
        raise ValueError(f"Unable to parse dependency file {manifest}: {error}") from error


def unique_candidates(values: list[ProjectCandidate]) -> list[ProjectCandidate]:
    by_repository: dict[str, ProjectCandidate] = {}
    for value in values:
        by_repository.setdefault(value.repository.casefold(), value)
    return list(by_repository.values())


def safe_project_ids(values: list[ProjectCandidate]) -> dict[str, str]:
    base_ids = [
        re.sub(r"[^a-z0-9._-]+", "-", value.repository.split("/", 1)[1].casefold()).strip("-")
        for value in values
    ]
    duplicates = {value for value in base_ids if base_ids.count(value) > 1}
    result: dict[str, str] = {}
    for value, base in zip(values, base_ids, strict=True):
        selected = (
            re.sub(r"[^a-z0-9._-]+", "-", value.repository.casefold()).strip("-")
            if base in duplicates
            else base
        )
        result[value.repository] = selected
    return result


def initial_config_document(
    values: list[ProjectCandidate], *, group_id: str, group_name: str
) -> dict[str, Any]:
    projects = unique_candidates(values)
    ids = safe_project_ids(projects)
    policy = DEFAULT_CONTRIBUTION_POLICY
    return {
        "lookback_hours": 24,
        "hackernews": {"enabled": True, "story_limit": 200},
        "contributions": {
            "invitation_labels": list(policy.invitation_labels),
            "beginner_labels": list(policy.beginner_labels),
            "excluded_labels": list(policy.excluded_labels),
            "weights": policy.weights.to_dict(),
            "thresholds": policy.thresholds.to_dict(),
        },
        "catalog_overlays": [],
        "repo_groups": {
            group_id: {
                "name": group_name,
                "repos": [
                    {
                        "id": ids[value.repository],
                        "repo": value.repository,
                        "name": value.name,
                        "keywords": list(value.keywords),
                    }
                    for value in projects
                ],
            }
        },
    }
