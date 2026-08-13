from __future__ import annotations

import asyncio

from conftest import make_dataset
from mcp import Client

from contribution_compass.controllers.mcp import create_server
from contribution_compass.domain.models import ObservationEvent, RepositoryDataset, Signal


class MemoryCatalog:
    def __init__(self) -> None:
        self.dataset = make_dataset()

    def dates(self) -> list[str]:
        return ["2026-08-13"]

    def repositories(self, date: str | None = None) -> list[RepositoryDataset]:
        return [self.dataset]

    def project(self, repository: str, date: str | None = None) -> RepositoryDataset | None:
        return self.dataset if repository == self.dataset.repository else None

    def signals(self, date: str | None = None) -> list[Signal]:
        return self.dataset.signals

    def events(self, signal_id: str) -> list[ObservationEvent]:
        return [event for event in self.dataset.events if event.signal_id == signal_id]


def test_mcp_exposes_typed_tools_and_resources_in_memory() -> None:
    async def exercise() -> None:
        async with Client(create_server(MemoryCatalog())) as client:
            tools = await client.list_tools()
            names = {tool.name for tool in tools.tools}
            assert "find_contribution_opportunities" in names
            assert "get_signal_timeline" in names
            result = await client.call_tool(
                "find_contribution_opportunities", {"project": "acme/widget"}
            )
            assert result.structured_content is not None
            assert result.structured_content["result"][0]["evidenceUrl"].endswith("/issues/42")
            context = await client.call_tool(
                "get_project_context", {"repository": "acme/widget", "signal_limit": 1}
            )
            assert context.structured_content is not None
            assert len(context.structured_content["importantSignals"]) == 1
            assert context.structured_content["signalCount"] == 1
            resource = await client.read_resource("compass://opportunities/latest")
            assert "good first issue" in resource.contents[0].text

    asyncio.run(exercise())
