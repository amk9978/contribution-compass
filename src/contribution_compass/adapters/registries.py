from __future__ import annotations

from collections.abc import Iterable
from urllib.parse import quote

import httpx

from contribution_compass.adapters.manifests import candidate, github_repository, unique_candidates
from contribution_compass.domain.candidates import CandidateRepository
from contribution_compass.domain.dependencies import DependencyReference


class RegistryRepositoryDiscovery:
    """Resolve package identities to repositories without guessing ambiguous matches."""

    def __init__(self, *, client: httpx.Client | None = None) -> None:
        self._client = client or httpx.Client(timeout=12, follow_redirects=True)

    @staticmethod
    def _values(value: object) -> Iterable[str]:
        if isinstance(value, str):
            yield value
        elif isinstance(value, dict):
            for item in value.values():
                if isinstance(item, str):
                    yield item

    def _metadata(self, dependency: DependencyReference) -> dict[str, object] | None:
        if dependency.ecosystem == "npm":
            url = f"https://registry.npmjs.org/{quote(dependency.name, safe='@')}/latest"
        elif dependency.ecosystem == "pypi":
            url = f"https://pypi.org/pypi/{quote(dependency.name, safe='')}/json"
        else:
            return None
        response = self._client.get(url)
        response.raise_for_status()
        value = response.json()
        return value if isinstance(value, dict) else None

    def _resolve_one(self, dependency: DependencyReference) -> CandidateRepository | None:
        value = self._metadata(dependency)
        if value is None:
            return None
        info = value.get("info") if dependency.ecosystem == "pypi" else value
        if not isinstance(info, dict):
            return None
        fields = (
            (info.get("repository"), info.get("homepage"), info.get("bugs"))
            if dependency.ecosystem == "npm"
            else (info.get("project_urls"), info.get("home_page"), info.get("package_url"))
        )
        for raw in fields:
            for text in self._values(raw):
                slug = github_repository(text)
                if slug:
                    return candidate(
                        slug,
                        name=dependency.name,
                        source=f"registry:{dependency.ecosystem}:{dependency.name}",
                    )
        return None

    def resolve(
        self, dependencies: tuple[DependencyReference, ...], *, limit: int = 50
    ) -> tuple[list[CandidateRepository], list[DependencyReference]]:
        resolved: list[CandidateRepository] = []
        unresolved: list[DependencyReference] = []
        seen: set[tuple[str, str]] = set()
        for dependency in dependencies:
            key = (dependency.ecosystem, dependency.name.casefold())
            if key in seen:
                continue
            seen.add(key)
            if len(seen) > limit:
                unresolved.append(dependency)
                continue
            try:
                found = self._resolve_one(dependency)
            except (httpx.HTTPError, ValueError):
                found = None
            if found:
                resolved.append(found)
            else:
                unresolved.append(dependency)
        return unique_candidates(resolved), unresolved
