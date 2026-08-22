from __future__ import annotations

import httpx

from contribution_compass.adapters.github import GitHubClient


def test_github_pagination_has_a_hard_limit() -> None:
    requests: list[httpx.Request] = []

    def respond(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        page = int(request.url.params["page"])
        return httpx.Response(200, json=[{"id": page * 100 + index} for index in range(100)])

    client = GitHubClient(
        "token",
        client=httpx.Client(
            base_url="https://api.github.test",
            transport=httpx.MockTransport(respond),
        ),
    )

    assert len(client.paginate("/items", limit=125)) == 125
    assert len(requests) == 2
    assert requests[0].url.params["per_page"] == "100"
    assert requests[1].url.params["per_page"] == "25"
