from __future__ import annotations

import argparse

from contribution_compass import __version__
from contribution_compass.views.site import StaticSitePublisher, default_site_urls


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(
        prog="contribution-compass",
        description="Personalized OSS investment recommender (v2 rewrite in progress)",
    )
    root.add_argument("--version", action="version", version=__version__)
    commands = root.add_subparsers(dest="command", required=True)
    site = commands.add_parser("site", help="Build the static v2 project-status page")
    site.add_argument("--output-root", default=".site")
    return root


def main() -> None:
    arguments = parser().parse_args()
    if arguments.command == "site":
        site_url, repository_url = default_site_urls()
        build = StaticSitePublisher(
            output_root=arguments.output_root,
            site_url=site_url,
            repository_url=repository_url,
        ).build()
        print(f"[site] generated {build.pages} page in {build.output_root}")


if __name__ == "__main__":
    main()
