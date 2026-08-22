from __future__ import annotations

import json
import os
import shutil
from dataclasses import dataclass
from pathlib import Path

from jinja2 import Environment, PackageLoader, StrictUndefined, select_autoescape


@dataclass(frozen=True, slots=True)
class SiteBuild:
    output_root: str
    pages: int
    machine_files: int


def template_environment() -> Environment:
    return Environment(
        loader=PackageLoader("contribution_compass.views", "templates"),
        autoescape=select_autoescape(("html", "xml"), default=True),
        undefined=StrictUndefined,
        auto_reload=False,
        keep_trailing_newline=True,
    )


class StaticSitePublisher:
    def __init__(
        self,
        *,
        output_root: str | Path = ".site",
        site_url: str,
        repository_url: str,
    ) -> None:
        self.output_root = Path(output_root).resolve()
        self.site_url = site_url.rstrip("/")
        self.repository_url = repository_url.rstrip("/")

    def build(self) -> SiteBuild:
        if self.output_root in {Path.cwd().resolve(), Path(self.output_root.anchor)}:
            raise ValueError(f"Unsafe site output directory: {self.output_root}")
        shutil.rmtree(self.output_root, ignore_errors=True)
        self.output_root.mkdir(parents=True)
        page = (
            template_environment()
            .get_template("index.html")
            .render(
                site_url=self.site_url,
                repository_url=self.repository_url,
            )
        )
        (self.output_root / "index.html").write_text(page, encoding="utf-8")
        (self.output_root / "status.json").write_text(
            json.dumps(
                {
                    "name": "Contribution Compass",
                    "phase": "v2-rewrite",
                    "product": "personalized OSS investment recommender",
                    "specification": (f"{self.repository_url}/blob/main/docs/product-spec-v2.md"),
                },
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
        (self.output_root / ".nojekyll").write_text("", encoding="utf-8")
        return SiteBuild(str(self.output_root), pages=1, machine_files=1)


def default_site_urls() -> tuple[str, str]:
    repository = os.getenv("GITHUB_REPOSITORY", "amk9978/contribution-compass")
    owner, name = repository.split("/", 1)
    return (
        os.getenv("SITE_URL", f"https://{owner}.github.io/{name}"),
        os.getenv("REPOSITORY_URL", f"https://github.com/{repository}"),
    )
