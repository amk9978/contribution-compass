from __future__ import annotations

import argparse
import asyncio
import json
import logging
import os
import subprocess
from pathlib import Path

import httpx
import yaml

from contribution_compass.adapters.catalog import assemble_catalog
from contribution_compass.adapters.discovery import (
    GitHubRepositoryDiscovery,
    GitHubSetupInspector,
    RegistryRepositoryDiscovery,
)
from contribution_compass.adapters.github import GitHubCollector
from contribution_compass.adapters.hackernews import HackerNewsCollector
from contribution_compass.adapters.json_store import JsonDatasetWriter, JsonObservationStore
from contribution_compass.application.catalog import CatalogQueries
from contribution_compass.application.collect import CollectUpdates
from contribution_compass.application.news import NewsQueries
from contribution_compass.application.setup import SetupDoctor, infer_repository
from contribution_compass.config import load_config, parse_config
from contribution_compass.domain.bootstrap import (
    DependencyReference,
    ProjectCandidate,
    candidate,
    discover_manifest,
    initial_config_document,
    unique_candidates,
)
from contribution_compass.views.markdown import MarkdownReportWriter
from contribution_compass.views.site import StaticSitePublisher, default_site_urls


class _IndentedSafeDumper(yaml.SafeDumper):
    def increase_indent(self, flow: bool = False, indentless: bool = False) -> None:
        return super().increase_indent(flow, False)


def _positive_int(value: str) -> int:
    parsed = int(value)
    if parsed < 1:
        raise argparse.ArgumentTypeError("expected a positive integer")
    return parsed


async def collect(config_path: str) -> int:
    config = load_config(config_path)
    assembly = assemble_catalog(config)
    collection_config = assembly.collection_config
    token = os.getenv("GITHUB_TOKEN")
    if not token and any(group.repos for group in collection_config.repo_groups):
        raise RuntimeError("GITHUB_TOKEN is required to collect configured repositories reliably")
    use_case = CollectUpdates(
        GitHubCollector(token or ""),
        JsonObservationStore(),
        JsonDatasetWriter(),
        MarkdownReportWriter(),
        HackerNewsCollector(),
    )
    result = await use_case.execute(collection_config)
    configured_count = sum(len(group.repos) for group in config.repo_groups)
    delta_count = sum(len(group.repos) for group in collection_config.repo_groups)
    if assembly.active_overlays:
        print(
            f"[compass] reused {configured_count - delta_count} Project Sensors from overlays: "
            f"{', '.join(assembly.active_overlays)}"
        )
    for failure in assembly.failures:
        print(f"[compass] catalog overlay unavailable; collecting fallback: {failure}")
    print(
        f"[compass] {result.observed_count} observed; {result.changed_count} changed; "
        f"{result.event_count} events; {result.contribution_lead_count} contribution leads"
    )
    print(f"[compass] wrote {result.data_directory} and {result.report_directory}")
    for failure in result.failures:
        print(f"[compass] collection failure: {failure}")
    return 0


def initialize_config(arguments: argparse.Namespace) -> int:
    projects: list[ProjectCandidate] = [
        candidate(repository, source="command-line") for repository in arguments.repo
    ]
    dependencies: list[DependencyReference] = []
    for path in arguments.from_file:
        discovery = discover_manifest(path)
        projects.extend(discovery.repositories)
        dependencies.extend(discovery.dependencies)
    unresolved: list[DependencyReference] = []
    if dependencies:
        resolved, unresolved = RegistryRepositoryDiscovery().resolve(
            tuple(dependencies), limit=arguments.registry_limit
        )
        projects.extend(resolved)
    if arguments.from_starred:
        projects.extend(
            GitHubRepositoryDiscovery(os.getenv("GITHUB_TOKEN", "")).starred(
                arguments.starred_limit
            )
        )
    projects = unique_candidates(projects)
    if not projects:
        raise ValueError(
            "init found no GitHub repositories; pass --repo, --from-file, or --from-starred"
        )
    document = initial_config_document(
        projects,
        group_id=arguments.group_id,
        group_name=arguments.group_name,
    )
    parse_config(document)
    destination = Path(arguments.output)
    if destination.exists() and not arguments.force:
        raise ValueError(f"{destination} already exists; pass --force to replace it")
    destination.parent.mkdir(parents=True, exist_ok=True)
    temporary = destination.with_suffix(f"{destination.suffix}.tmp")
    temporary.write_text(
        yaml.dump(
            document,
            Dumper=_IndentedSafeDumper,
            sort_keys=False,
            allow_unicode=True,
        ),
        encoding="utf-8",
    )
    os.replace(temporary, destination)
    print(f"[compass] wrote {destination} with {len(projects)} Project Sensors")
    if unresolved:
        names = ", ".join(f"{item.ecosystem}:{item.name}" for item in unresolved[:10])
        suffix = "…" if len(unresolved) > 10 else ""
        print(
            f"[compass] {len(unresolved)} dependencies had no unambiguous GitHub repository: "
            f"{names}{suffix}"
        )
    print(f"[compass] review {destination}, then run contribution-compass doctor")
    return 0


def _git_repository() -> str | None:
    result = subprocess.run(
        ["git", "config", "--get", "remote.origin.url"],
        check=False,
        capture_output=True,
        text=True,
    )
    return infer_repository(result.stdout) if result.returncode == 0 else None


def doctor(arguments: argparse.Namespace) -> int:
    config = load_config(arguments.config)
    token = os.getenv("GITHUB_TOKEN", "")
    repository = arguments.repository or os.getenv("GITHUB_REPOSITORY") or _git_repository()
    remote = None if arguments.offline or not repository else GitHubSetupInspector(token)
    report = SetupDoctor(remote).inspect(
        config,
        root=Path(arguments.root).resolve(),
        token_present=bool(token),
        repository=repository,
    )
    markers = {"pass": "PASS", "warning": "WARN", "fail": "FAIL"}
    for check in report.checks:
        print(f"[{markers[check.status]}] {check.message}")
        if check.remediation:
            print(f"       {check.remediation}")
    return 0 if report.ok else 1


def build_site(data_root: str, output_root: str, config_path: str) -> int:
    config = load_config(config_path)
    assembly = assemble_catalog(config, local_root=data_root)
    for failure in assembly.failures:
        logging.warning("[compass] catalog overlay unavailable: %s", failure)
    site_url, repository_url = default_site_urls()
    build = StaticSitePublisher(
        assembly.catalog,
        output_root=output_root,
        site_url=site_url,
        repository_url=repository_url,
        contribution_policy=config.contribution_policy,
    ).build()
    print(
        f"[site] generated {build.pages} pages and {build.machine_files} machine files "
        f"for {build.dates} dates in {build.output_root}"
    )
    return 0


def query_catalog(arguments: argparse.Namespace) -> int:
    config = load_config(arguments.config)
    assembly = assemble_catalog(config, local_root=arguments.data_root)
    for failure in assembly.failures:
        logging.warning("[compass] catalog overlay unavailable: %s", failure)
    queries = CatalogQueries(assembly.catalog, config.contribution_policy)
    if arguments.query_command == "news":
        value = [
            entry.to_dict()
            for entry in NewsQueries(assembly.catalog).list(
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
    initialize = subcommands.add_parser(
        "init", help="Generate config.yml from repositories, manifests, or GitHub stars"
    )
    initialize.add_argument("--repo", action="append", default=[], metavar="OWNER/REPOSITORY")
    initialize.add_argument("--from-file", action="append", default=[], metavar="PATH")
    initialize.add_argument("--from-starred", action="store_true")
    initialize.add_argument("--starred-limit", type=_positive_int, default=100)
    initialize.add_argument("--registry-limit", type=_positive_int, default=50)
    initialize.add_argument("--group-id", default="my-projects")
    initialize.add_argument("--group-name", default="My Projects")
    initialize.add_argument("--output", default="config.yml")
    initialize.add_argument("--force", action="store_true")
    diagnose = subcommands.add_parser(
        "doctor", help="Check local configuration and GitHub deployment readiness"
    )
    diagnose.add_argument("--config", default=os.getenv("COMPASS_CONFIG", "config.yml"))
    diagnose.add_argument("--root", default=".")
    diagnose.add_argument("--repository", metavar="OWNER/REPOSITORY")
    diagnose.add_argument("--offline", action="store_true")
    site = subcommands.add_parser("site", help="Build static human and machine views")
    site.add_argument("--data-root", default="data")
    site.add_argument("--output-root", default=".site")
    site.add_argument("--config", default=os.getenv("COMPASS_CONFIG", "config.yml"))
    query = subcommands.add_parser("query", help="Query the local evidence catalog")
    query.add_argument("--data-root", default="data")
    query.add_argument("--config", default=os.getenv("COMPASS_CONFIG", "config.yml"))
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
    logging.getLogger("httpx").setLevel(logging.WARNING)
    arguments = parser().parse_args()
    try:
        if arguments.command == "collect":
            result = asyncio.run(collect(arguments.config))
        elif arguments.command == "init":
            result = initialize_config(arguments)
        elif arguments.command == "doctor":
            result = doctor(arguments)
        elif arguments.command == "site":
            result = build_site(arguments.data_root, arguments.output_root, arguments.config)
        else:
            result = query_catalog(arguments)
    except (RuntimeError, ValueError, OSError, httpx.HTTPError) as error:
        raise SystemExit(f"[compass] {error}") from error
    raise SystemExit(result)


if __name__ == "__main__":
    main()
