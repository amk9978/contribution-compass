from __future__ import annotations

from collections.abc import Iterable
from urllib.parse import quote

import httpx

from contribution_compass.domain.bootstrap import (
    DependencyReference,
    ProjectCandidate,
    candidate,
    github_repository,
    unique_candidates,
)

API_VERSION = "2026-03-10"


class GitHubRepositoryDiscovery:
    def __init__(self, token: str, *, client: httpx.Client | None = None) -> None:
        if not token:
            raise ValueError("GITHUB_TOKEN is required for --from-starred")
        self._client = client or httpx.Client(
            base_url="https://api.github.com",
            timeout=20,
            follow_redirects=True,
            headers={
                "Accept": "application/vnd.github+json",
                "Authorization": f"Bearer {token}",
                "X-GitHub-Api-Version": API_VERSION,
                "User-Agent": "contribution-compass",
            },
        )

    def starred(self, limit: int = 100) -> list[ProjectCandidate]:
        results: list[ProjectCandidate] = []
        page = 1
        while len(results) < limit:
            response = self._client.get(
                "/user/starred",
                params={"per_page": min(100, limit - len(results)), "page": page},
            )
            response.raise_for_status()
            payload = response.json()
            if not isinstance(payload, list):
                raise ValueError("GitHub starred-repositories response was not an array")
            for item in payload:
                if not isinstance(item, dict) or not isinstance(item.get("full_name"), str):
                    continue
                results.append(
                    candidate(
                        item["full_name"],
                        name=str(item.get("name") or item["full_name"].split("/", 1)[1]),
                        source="github-starred",
                    )
                )
            if len(payload) < min(100, limit - len(results) + len(payload)):
                break
            page += 1
        return results[:limit]


class RegistryRepositoryDiscovery:
    """Resolve direct package dependencies through public registry metadata."""

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

    def _npm(self, dependency: DependencyReference) -> ProjectCandidate | None:
        response = self._client.get(
            f"https://registry.npmjs.org/{quote(dependency.name, safe='@')}/latest"
        )
        response.raise_for_status()
        value = response.json()
        if not isinstance(value, dict):
            return None
        candidates = [value.get("repository"), value.get("homepage"), value.get("bugs")]
        for raw in candidates:
            for text in self._values(raw):
                slug = github_repository(text)
                if slug:
                    return candidate(slug, name=dependency.name, source=f"npm:{dependency.name}")
        return None

    def _pypi(self, dependency: DependencyReference) -> ProjectCandidate | None:
        response = self._client.get(f"https://pypi.org/pypi/{quote(dependency.name, safe='')}/json")
        response.raise_for_status()
        value = response.json()
        info = value.get("info") if isinstance(value, dict) else None
        if not isinstance(info, dict):
            return None
        candidates = [info.get("project_urls"), info.get("home_page"), info.get("package_url")]
        for raw in candidates:
            for text in self._values(raw):
                slug = github_repository(text)
                if slug:
                    return candidate(slug, name=dependency.name, source=f"pypi:{dependency.name}")
        return None

    def resolve(
        self, dependencies: tuple[DependencyReference, ...], *, limit: int = 50
    ) -> tuple[list[ProjectCandidate], list[DependencyReference]]:
        resolved: list[ProjectCandidate] = []
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
                found = (
                    self._npm(dependency)
                    if dependency.ecosystem == "npm"
                    else self._pypi(dependency)
                    if dependency.ecosystem == "pypi"
                    else None
                )
            except (httpx.HTTPError, ValueError):
                found = None
            if found:
                resolved.append(found)
            else:
                unresolved.append(dependency)
        return unique_candidates(resolved), unresolved


class GitHubSetupInspector:
    def __init__(self, token: str, *, client: httpx.Client | None = None) -> None:
        headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": API_VERSION,
            "User-Agent": "contribution-compass",
        }
        if token:
            headers["Authorization"] = f"Bearer {token}"
        self._client = client or httpx.Client(
            base_url="https://api.github.com",
            timeout=15,
            follow_redirects=True,
            headers=headers,
        )

    def get(self, repository: str, endpoint: str) -> tuple[int, dict[str, object] | None]:
        response = self._client.get(f"/repos/{repository}/{endpoint.lstrip('/')}")
        if response.status_code != 200:
            return response.status_code, None
        value = response.json()
        return (200, value if isinstance(value, dict) else None)
