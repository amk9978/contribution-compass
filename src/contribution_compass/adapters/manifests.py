from __future__ import annotations

import json
import re
import tomllib
from pathlib import Path
from typing import Any

from contribution_compass.domain.candidates import CandidateRepository, DiscoveryEvidence
from contribution_compass.domain.dependencies import (
    DependencyReference,
    DependencyScope,
    ManifestDiscovery,
)

GITHUB_REFERENCE = re.compile(
    r"(?:git\+https?://|https?://|ssh://git@|git@)?github\.com[/:]"
    r"(?P<owner>[A-Za-z0-9_.-]+)/(?P<repo>[A-Za-z0-9_.-]+)",
    re.IGNORECASE,
)
REPOSITORY_SLUG = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")
PYTHON_REQUIREMENT = re.compile(r"^([A-Za-z0-9][A-Za-z0-9_.-]*)(?:\[[^]]+\])?")


def github_repository(value: str) -> str | None:
    stripped = value.strip()
    if stripped.startswith("github:"):
        stripped = stripped.removeprefix("github:")
    stripped = stripped.split("#", 1)[0].removesuffix(".git")
    if REPOSITORY_SLUG.fullmatch(stripped):
        return stripped
    match = GITHUB_REFERENCE.search(value)
    if not match:
        return None
    return f"{match.group('owner')}/{match.group('repo').removesuffix('.git')}"


def candidate(repository: str, *, name: str | None = None, source: str) -> CandidateRepository:
    slug = github_repository(repository)
    if slug is None:
        raise ValueError(f"Expected a GitHub owner/repository reference, got {repository!r}")
    return CandidateRepository(
        repository=slug,
        name=name or slug.split("/", 1)[1],
        evidence=(DiscoveryEvidence(source=source, detail=repository),),
    )


def _dependency(
    path: Path, ecosystem: str, name: str, scope: DependencyScope
) -> DependencyReference:
    return DependencyReference(ecosystem=ecosystem, name=name, scope=scope, manifest=str(path))


def _package_json(path: Path, value: dict[str, Any]) -> ManifestDiscovery:
    repositories: list[CandidateRepository] = []
    dependencies: list[DependencyReference] = []
    sections: tuple[tuple[str, DependencyScope], ...] = (
        ("dependencies", "runtime"),
        ("devDependencies", "development"),
        ("optionalDependencies", "optional"),
    )
    for section, scope in sections:
        raw = value.get(section, {})
        if not isinstance(raw, dict):
            continue
        for name, specification in raw.items():
            if not isinstance(name, str):
                continue
            slug = github_repository(str(specification))
            if slug:
                repositories.append(candidate(slug, name=name, source=f"manifest:{path}"))
            else:
                dependencies.append(_dependency(path, "npm", name, scope))
    return ManifestDiscovery(tuple(repositories), tuple(dependencies))


def _requirements(path: Path, text: str) -> ManifestDiscovery:
    repositories: list[CandidateRepository] = []
    dependencies: list[DependencyReference] = []
    for raw_line in text.splitlines():
        line = raw_line.split(" #", 1)[0].strip()
        if not line or line.startswith(("#", "-r", "--requirement", "-c", "--constraint")):
            continue
        slug = github_repository(line)
        if slug:
            repositories.append(candidate(slug, source=f"manifest:{path}"))
            continue
        match = PYTHON_REQUIREMENT.match(line)
        if match:
            dependencies.append(_dependency(path, "pypi", match.group(1), "runtime"))
    return ManifestDiscovery(tuple(repositories), tuple(dependencies))


def _go_mod(path: Path, text: str) -> ManifestDiscovery:
    repositories: list[CandidateRepository] = []
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
            repositories.append(candidate(slug, source=f"manifest:{path}"))
    return ManifestDiscovery(tuple(repositories), ())


def _pyproject(path: Path, value: dict[str, Any]) -> ManifestDiscovery:
    dependencies: list[DependencyReference] = []
    project = value.get("project")
    if isinstance(project, dict):
        direct = project.get("dependencies", [])
        if isinstance(direct, list):
            dependencies.extend(_python_dependencies(path, direct, "runtime"))
        optional = project.get("optional-dependencies", {})
        if isinstance(optional, dict):
            for group in optional.values():
                if isinstance(group, list):
                    dependencies.extend(_python_dependencies(path, group, "optional"))
    poetry = value.get("tool", {})
    if isinstance(poetry, dict):
        poetry = poetry.get("poetry", {})
        if isinstance(poetry, dict):
            raw = poetry.get("dependencies", {})
            if isinstance(raw, dict):
                dependencies.extend(
                    _dependency(path, "pypi", str(name), "runtime")
                    for name in raw
                    if str(name).casefold() != "python"
                )
    return ManifestDiscovery((), tuple(dependencies))


def _python_dependencies(
    path: Path, values: list[object], scope: DependencyScope
) -> list[DependencyReference]:
    result: list[DependencyReference] = []
    for value in values:
        match = PYTHON_REQUIREMENT.match(str(value))
        if match:
            result.append(_dependency(path, "pypi", match.group(1), scope))
    return result


def discover_manifest(path: str | Path) -> ManifestDiscovery:
    manifest = Path(path)
    try:
        text = manifest.read_text(encoding="utf-8")
    except OSError as error:
        raise ValueError(f"Unable to read dependency file {manifest}") from error
    try:
        name = manifest.name.casefold()
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


def unique_candidates(values: list[CandidateRepository]) -> list[CandidateRepository]:
    merged: dict[str, CandidateRepository] = {}
    for value in values:
        key = value.repository.casefold()
        previous = merged.get(key)
        if previous is None:
            merged[key] = value
            continue
        evidence = tuple(dict.fromkeys((*previous.evidence, *value.evidence)))
        merged[key] = CandidateRepository(previous.repository, previous.name, evidence)
    return list(merged.values())
