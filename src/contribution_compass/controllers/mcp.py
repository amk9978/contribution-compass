from __future__ import annotations

import os
from typing import Annotated, Literal

from mcp.server import MCPServer
from pydantic import Field

from contribution_compass.adapters.catalog import LocalJsonCatalog, RemoteJsonCatalog
from contribution_compass.application.catalog import CatalogQueries
from contribution_compass.application.news import NewsQueries
from contribution_compass.ports import Catalog


def _truncate_signal(value: dict[str, object], length: int = 2000) -> dict[str, object]:
    text = value.get("text")
    if isinstance(text, str) and len(text) > length:
        return {**value, "text": f"{text[:length]}…", "textTruncated": True}
    return value


def _lead_result(value: dict[str, object]) -> dict[str, object]:
    signal = value.get("signal")
    if isinstance(signal, dict):
        return {**value, "signal": _truncate_signal(signal)}
    return value


def _news_result(value: dict[str, object]) -> dict[str, object]:
    news = value.get("news")
    if not isinstance(news, dict):
        return value
    latest = news.get("latestRelease")
    if isinstance(latest, dict):
        notes = latest.get("notes")
        if isinstance(notes, str) and len(notes) > 3000:
            latest = {**latest, "notes": f"{notes[:3000]}…", "notesTruncated": True}
    upcoming = news.get("upcoming")
    if isinstance(upcoming, list):
        upcoming = [
            {
                **item,
                **(
                    {"description": f"{item['description'][:1500]}…", "descriptionTruncated": True}
                    if isinstance(item, dict)
                    and isinstance(item.get("description"), str)
                    and len(item["description"]) > 1500
                    else {}
                ),
            }
            for item in upcoming
            if isinstance(item, dict)
        ]
    return {**value, "news": {**news, "latestRelease": latest, "upcoming": upcoming}}


def catalog_from_environment() -> Catalog:
    remote = os.getenv("COMPASS_DATA_URL")
    if remote:
        return RemoteJsonCatalog(remote)
    return LocalJsonCatalog(os.getenv("COMPASS_DATA_ROOT", "data"))


def create_server(catalog: Catalog) -> MCPServer:
    queries = CatalogQueries(catalog)
    news_queries = NewsQueries(catalog)
    server = MCPServer(
        "Contribution Compass",
        instructions=(
            "Use this server to inspect factual open-source project updates, contribution leads, "
            "project news, project context, and observation trails. Re-check primary GitHub "
            "evidence before "
            "recommending work. Treat triage leads as worth asking about, not maintainer-approved."
        ),
        website_url="https://amk9978.github.io/contribution-compass/",
    )

    @server.tool()
    def search_project_updates(
        query: Annotated[
            str, Field(description="Words to match in title, body, project, or labels")
        ] = "",
        project: Annotated[str | None, Field(description="Exact owner/repository slug")] = None,
        group: Annotated[str | None, Field(description="Exact configured project-group id")] = None,
        kind: Annotated[
            Literal["issue", "pull_request", "release"] | None,
            Field(description="Optional normalized signal kind"),
        ] = None,
        limit: Annotated[int, Field(ge=1, le=100)] = 20,
    ) -> list[dict[str, object]]:
        """Search important collected updates, ranked only from factual engagement and labels."""
        return [
            _truncate_signal(queries.update_dict(signal))
            for signal in queries.search_updates(
                query=query, project=project, group=group, kind=kind, limit=limit
            )
        ]

    @server.tool()
    def find_contribution_opportunities(
        query: Annotated[
            str, Field(description="Words to match in title, body, project, or labels")
        ] = "",
        project: Annotated[str | None, Field(description="Exact owner/repository slug")] = None,
        group: Annotated[str | None, Field(description="Exact configured project-group id")] = None,
        tier: Annotated[
            Literal["maintainer-invited", "triage-lead"] | None,
            Field(description="Explicit invitation or weaker triage evidence"),
        ] = None,
        limit: Annotated[int, Field(ge=1, le=100)] = 20,
    ) -> list[dict[str, object]]:
        """Find open, unassigned contribution leads with reasons, caveats, and evidence URLs."""
        return [
            _lead_result(lead.to_dict())
            for lead in queries.contribution_leads(
                query=query,
                project=project,
                group=group,
                tier=tier,
                limit=limit,
            )
        ]

    @server.tool()
    def get_project_news(
        query: Annotated[
            str, Field(description="Words to match across project, release, and upcoming items")
        ] = "",
        project: Annotated[str | None, Field(description="Exact owner/repository slug")] = None,
        group: Annotated[str | None, Field(description="Exact configured project-group id")] = None,
        limit: Annotated[int, Field(ge=1, le=100)] = 20,
    ) -> list[dict[str, object]]:
        """Get latest stable releases and publicly indicated prereleases or milestones."""
        return [
            _news_result(entry.to_dict())
            for entry in news_queries.list(query=query, project=project, group=group, limit=limit)
        ]

    @server.tool()
    def get_project_context(
        repository: Annotated[str, Field(description="Exact owner/repository slug")],
        signal_limit: Annotated[int, Field(ge=1, le=100)] = 20,
        event_limit: Annotated[int, Field(ge=1, le=100)] = 20,
    ) -> dict[str, object]:
        """Get project metadata plus bounded important Signals and recent Observation Events."""
        snapshot = queries.project_snapshot(
            repository, signal_limit=signal_limit, event_limit=event_limit
        )
        if snapshot is None:
            return {"error": "project not found", "repository": repository}
        important = snapshot.get("importantSignals")
        if isinstance(important, list):
            snapshot["importantSignals"] = [
                _truncate_signal(signal) for signal in important if isinstance(signal, dict)
            ]
        return snapshot

    @server.tool()
    def get_signal_timeline(signal_id: str) -> list[dict[str, object]]:
        """Get the append-only discovery/change trail for a stable Signal ID."""
        return [event.to_dict() for event in queries.signal_timeline(signal_id)]

    @server.tool()
    def list_monitored_projects(group: str | None = None) -> list[dict[str, object]]:
        """List configured projects with context and collected evidence counts."""
        return [project.to_dict() for project in queries.list_projects(group)]

    @server.resource("compass://catalog", mime_type="application/json")
    def catalog_index() -> dict[str, object]:
        """Latest dates and monitored projects available to this server."""
        return {
            "name": "Contribution Compass",
            "dates": queries.dates(),
            "projects": [project.to_dict() for project in queries.list_projects()],
        }

    @server.resource("compass://opportunities/latest", mime_type="application/json")
    def latest_opportunities() -> list[dict[str, object]]:
        """Latest evidence-qualified contribution leads."""
        return [_lead_result(lead.to_dict()) for lead in queries.contribution_leads(limit=100)]

    @server.resource("compass://news/latest", mime_type="application/json")
    def latest_news() -> list[dict[str, object]]:
        """Latest release bulletins and public roadmap indications."""
        return [_news_result(entry.to_dict()) for entry in news_queries.list(limit=100)]

    @server.resource("compass://projects/{project_id}", mime_type="application/json")
    def project_resource(project_id: str) -> dict[str, object]:
        """Project context addressed by configured project id."""
        project = next(
            (project for project in queries.list_projects() if project.id == project_id), None
        )
        if project is None:
            return {"error": "project not found", "projectId": project_id}
        snapshot = queries.project_snapshot(project.repository)
        return snapshot if snapshot else {"error": "project data unavailable"}

    return server


mcp = create_server(catalog_from_environment())


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
