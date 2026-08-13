from __future__ import annotations

import argparse
import asyncio
import json
import logging
import os

from contribution_compass.adapters.catalog import LocalJsonCatalog
from contribution_compass.adapters.github import GitHubCollector
from contribution_compass.adapters.hackernews import HackerNewsCollector
from contribution_compass.adapters.json_store import JsonDatasetWriter, JsonObservationStore
from contribution_compass.application.catalog import CatalogQueries
from contribution_compass.application.collect import CollectUpdates
from contribution_compass.application.news import NewsQueries
from contribution_compass.config import load_config
from contribution_compass.views.markdown import MarkdownReportWriter
from contribution_compass.views.site import StaticSitePublisher, default_site_urls


async def collect(config_path: str) -> int:
    config = load_config(config_path)
    token = os.getenv("GITHUB_TOKEN")
    if not token and any(group.repos for group in config.repo_groups):
        raise RuntimeError("GITHUB_TOKEN is required to collect configured repositories reliably")
    use_case = CollectUpdates(
        GitHubCollector(token or ""),
        JsonObservationStore(),
        JsonDatasetWriter(),
        MarkdownReportWriter(),
        HackerNewsCollector(),
    )
    result = await use_case.execute(config)
    print(
        f"[compass] {result.observed_count} observed; {result.changed_count} changed; "
        f"{result.event_count} events; {result.contribution_lead_count} contribution leads"
    )
    print(f"[compass] wrote {result.data_directory} and {result.report_directory}")
    for failure in result.failures:
        print(f"[compass] collection failure: {failure}")
    return 0


def build_site(data_root: str, output_root: str) -> int:
    site_url, repository_url = default_site_urls()
    build = StaticSitePublisher(
        LocalJsonCatalog(data_root),
        output_root=output_root,
        site_url=site_url,
        repository_url=repository_url,
    ).build()
    print(
        f"[site] generated {build.pages} pages and {build.machine_files} machine files "
        f"for {build.dates} dates in {build.output_root}"
    )
    return 0


def query_catalog(arguments: argparse.Namespace) -> int:
    queries = CatalogQueries(LocalJsonCatalog(arguments.data_root))
    if arguments.query_command == "news":
        value = [
            entry.to_dict()
            for entry in NewsQueries(LocalJsonCatalog(arguments.data_root)).list(
                query=arguments.query,
                project=arguments.project,
                group=arguments.group,
                limit=arguments.limit,
            )
        ]
    elif arguments.query_command == "opportunities":
        value = [
            lead.to_dict()
            for lead in queries.contribution_leads(
                query=arguments.query,
                project=arguments.project,
                group=arguments.group,
                tier=arguments.tier,
                limit=arguments.limit,
            )
        ]
    elif arguments.query_command == "timeline":
        value = [event.to_dict() for event in queries.signal_timeline(arguments.signal_id)]
    else:
        value = [
            queries.update_dict(signal)
            for signal in queries.search_updates(
                query=arguments.query,
                project=arguments.project,
                group=arguments.group,
                kind=arguments.kind,
                limit=arguments.limit,
            )
        ]
    print(json.dumps(value, indent=2, ensure_ascii=False))
    return 0


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(prog="contribution-compass")
    subcommands = root.add_subparsers(dest="command", required=True)
    collect_parser = subcommands.add_parser("collect", help="Collect project updates from GitHub")
    collect_parser.add_argument("--config", default=os.getenv("COMPASS_CONFIG", "config.yml"))
    site = subcommands.add_parser("site", help="Build static human and machine views")
    site.add_argument("--data-root", default="data")
    site.add_argument("--output-root", default=".site")
    query = subcommands.add_parser("query", help="Query the local evidence catalog")
    query.add_argument("--data-root", default="data")
    query_subcommands = query.add_subparsers(dest="query_command", required=True)
    for name in ("updates", "opportunities", "news"):
        command = query_subcommands.add_parser(name)
        command.add_argument("--query", default="")
        command.add_argument("--project")
        command.add_argument("--group")
        command.add_argument("--limit", type=int, default=20)
        if name == "updates":
            command.add_argument("--kind", choices=("issue", "pull_request", "release"))
        elif name == "opportunities":
            command.add_argument("--tier", choices=("maintainer-invited", "triage-lead"))
    timeline = query_subcommands.add_parser("timeline")
    timeline.add_argument("signal_id")
    return root


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    arguments = parser().parse_args()
    try:
        if arguments.command == "collect":
            result = asyncio.run(collect(arguments.config))
        elif arguments.command == "site":
            result = build_site(arguments.data_root, arguments.output_root)
        else:
            result = query_catalog(arguments)
    except (RuntimeError, ValueError, OSError) as error:
        raise SystemExit(f"[compass] {error}") from error
    raise SystemExit(result)


if __name__ == "__main__":
    main()
