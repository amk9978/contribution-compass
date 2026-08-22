from __future__ import annotations

from collections.abc import Mapping
from typing import Any

import httpx

API_VERSION = "2022-11-28"
type QueryValue = str | int | float | bool | None


class GitHubClient:
    """Small GitHub transport shared by future profile, discovery, and evidence adapters."""

    def __init__(self, token: str = "", *, client: httpx.Client | None = None) -> None:
        headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": API_VERSION,
            "User-Agent": "contribution-compass",
        }
        if token:
            headers["Authorization"] = f"Bearer {token}"
        self._client = client or httpx.Client(
            base_url="https://api.github.com",
            timeout=20,
            follow_redirects=True,
            headers=headers,
        )

    def get(self, path: str, *, params: Mapping[str, QueryValue] | None = None) -> Any:
        response = self._client.get(path, params=params)
        response.raise_for_status()
        return response.json()

    def paginate(
        self,
        path: str,
        *,
        params: Mapping[str, QueryValue] | None = None,
        limit: int = 100,
    ) -> list[dict[str, Any]]:
        if limit < 1:
            return []
        results: list[dict[str, Any]] = []
        page = 1
        while len(results) < limit:
            page_size = min(100, limit - len(results))
            payload = self.get(
                path,
                params={**(params or {}), "per_page": page_size, "page": page},
            )
            if not isinstance(payload, list):
                raise ValueError(f"GitHub response for {path} was not an array")
            results.extend(item for item in payload if isinstance(item, dict))
            if len(payload) < page_size:
                break
            page += 1
        return results[:limit]
