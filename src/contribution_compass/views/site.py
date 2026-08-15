from __future__ import annotations

import os
import shutil
from collections.abc import Callable
from dataclasses import dataclass
from math import ceil
from pathlib import Path
from typing import TypeVar
from xml.sax.saxutils import escape as xml_escape

from jinja2 import Environment

from contribution_compass.application.catalog import CatalogQueries
from contribution_compass.application.news import NewsQueries, ProjectNewsEntry
from contribution_compass.domain.importance import rank_updates
from contribution_compass.domain.models import ContributionLead, RepositoryDataset, Signal
from contribution_compass.domain.policies import (
    DEFAULT_CONTRIBUTION_POLICY,
    ContributionPolicy,
)
from contribution_compass.ports import Catalog
from contribution_compass.views.machine import MachineView, SiteContext, signal_anchor
from contribution_compass.views.templating import create_environment

T = TypeVar("T")


def page_count(total: int, page_size: int) -> int:
    return max(1, ceil(total / page_size))


@dataclass(frozen=True, slots=True)
class SiteBuild:
    output_root: str
    dates: int
    pages: int
    machine_files: int


@dataclass(frozen=True, slots=True)
class PageMetadata:
    title: str
    description: str
    api_url: str
    canonical_url: str
    scripts: tuple[str, ...] = ()


@dataclass(frozen=True, slots=True)
class Pagination:
    current: int
    total: int
    item_total: int
    previous_url: str | None
    next_url: str | None


@dataclass(frozen=True, slots=True)
class LeadCard:
    lead: ContributionLead
    collected_url: str
    search: str
    comments: int
    reactions: int


@dataclass(frozen=True, slots=True)
class NewsCard:
    entry: ProjectNewsEntry
    project_url: str


@dataclass(frozen=True, slots=True)
class GroupSummary:
    id: str
    name: str
    signal_count: int
    project_count: int
    lead_count: int
    activity_percent: int


class HtmlView:
    """Render crawlable HTML from application projections through Jinja templates."""

    def __init__(
        self,
        catalog: Catalog,
        context: SiteContext,
        contribution_policy: ContributionPolicy = DEFAULT_CONTRIBUTION_POLICY,
        *,
        templates: Environment | None = None,
    ) -> None:
        self.catalog = catalog
        self.queries = CatalogQueries(catalog, contribution_policy)
        self.news_queries = NewsQueries(catalog)
        self.context = context
        self.templates = templates or create_environment()
        self._signal_page_cache: dict[tuple[str, str], dict[str, int]] = {}

    @staticmethod
    def _window(values: list[T], page: int, page_size: int) -> list[T]:
        start = (page - 1) * page_size
        return values[start : start + page_size]

    def _render(self, template: str, page: PageMetadata, **values: object) -> str:
        return self.templates.get_template(template).render(
            site=self.context,
            page=page,
            **values,
        )

    @staticmethod
    def _pagination(
        current: int,
        total: int,
        url_for_page: Callable[[int], str],
        *,
        item_total: int,
    ) -> Pagination | None:
        if total <= 1:
            return None
        return Pagination(
            current=current,
            total=total,
            item_total=item_total,
            previous_url=url_for_page(current - 1) if current > 1 else None,
            next_url=url_for_page(current + 1) if current < total else None,
        )

    def _section_page_url(self, section: str, page: int) -> str:
        if page == 1:
            return f"{self.context.site_url}/{section}/"
        return f"{self.context.site_url}/{section}/page/{page}/"

    def _repository_page_url(self, dataset: RepositoryDataset, page: int) -> str:
        base = f"{self.context.site_url}/updates/{dataset.date}/{dataset.group_id}"
        if page == 1:
            return f"{base}/{dataset.repository_id}.html"
        return f"{base}/{dataset.repository_id}/page/{page}/"

    def _signal_page(self, dataset: RepositoryDataset, signal: Signal) -> int:
        key = (dataset.date, dataset.repository)
        if key not in self._signal_page_cache:
            ranked = rank_updates(dataset.signals, len(dataset.signals))
            self._signal_page_cache[key] = {
                item.id: position // 50 + 1 for position, item in enumerate(ranked)
            }
        return self._signal_page_cache[key].get(signal.id, 1)

    def _lead_card(self, lead: ContributionLead, dataset: RepositoryDataset | None) -> LeadCard:
        collected_url = "#"
        if dataset:
            collected_url = (
                f"{self._repository_page_url(dataset, self._signal_page(dataset, lead.signal))}"
                f"#{signal_anchor(lead.signal)}"
            )
        metrics = lead.signal.metrics
        return LeadCard(
            lead=lead,
            collected_url=collected_url,
            search=" ".join(
                (lead.signal.title, lead.signal.project or "", *lead.signal.labels)
            ).casefold(),
            comments=metrics.comments if metrics else 0,
            reactions=metrics.reactions if metrics else 0,
        )

    def _news_card(self, entry: ProjectNewsEntry) -> NewsCard:
        return NewsCard(
            entry=entry,
            project_url=(
                f"{self.context.site_url}/updates/{entry.date}/{entry.group_id}/"
                f"{entry.project_id}.html"
            ),
        )

    @staticmethod
    def _metrics(datasets: list[RepositoryDataset]) -> dict[str, int]:
        signals = [signal for dataset in datasets for signal in dataset.signals]
        return {
            "signals": len(signals),
            "repositories": sum(bool(dataset.signals) for dataset in datasets),
            "events": sum(len(dataset.events) for dataset in datasets),
        }

    def home(self) -> str:
        metadata = PageMetadata(
            "Project updates and contribution leads",
            "Important open-source project updates and evidence-backed contribution leads",
            f"{self.context.site_url}/api/v1/index.json",
            f"{self.context.site_url}/",
        )
        dates = self.catalog.dates()
        if not dates:
            return self._render("pages/empty.html", metadata)
        date = dates[0]
        datasets = self.catalog.repositories(date)
        signals = [signal for dataset in datasets for signal in dataset.signals]
        leads = self.queries.contribution_leads(limit=1000)
        by_repo = {dataset.repository: dataset for dataset in datasets}
        grouped: dict[str, list[RepositoryDataset]] = {}
        for dataset in datasets:
            grouped.setdefault(dataset.group_id, []).append(dataset)
        groups = [
            GroupSummary(
                id=group_id,
                name=items[0].group_name,
                signal_count=sum(len(item.signals) for item in items),
                project_count=len(items),
                lead_count=sum(lead.signal.group == group_id for lead in leads),
                activity_percent=max(1, min(100, sum(len(item.signals) for item in items) // 10)),
            )
            for group_id, items in grouped.items()
        ]
        return self._render(
            "pages/home.html",
            metadata,
            date=date,
            dataset_count=len(datasets),
            metrics=self._metrics(datasets),
            lead_count=len(leads),
            invited_count=sum(lead.tier == "maintainer-invited" for lead in leads),
            groups=groups,
            lead_cards=[
                self._lead_card(lead, by_repo.get(lead.signal.project or "")) for lead in leads[:6]
            ],
            news_cards=[self._news_card(entry) for entry in self.news_queries.list(limit=6)],
            updates=rank_updates(signals, 12),
        )

    def contributions(self, page: int = 1, page_size: int = 20) -> str:
        date = next(iter(self.catalog.dates()), "none")
        datasets = self.catalog.repositories(None)
        by_repo = {dataset.repository: dataset for dataset in datasets}
        leads = self.queries.contribution_leads(limit=1000)
        pages = page_count(len(leads), page_size)
        page = min(max(page, 1), pages)
        visible = self._window(list(leads), page, page_size)
        invited = sum(lead.tier == "maintainer-invited" for lead in leads)
        return self._render(
            "pages/contributions.html",
            PageMetadata(
                f"Contribution opportunities — page {page}",
                "Evidence-backed open-source contribution leads",
                f"{self.context.site_url}/api/v1/opportunities.json",
                self._section_page_url("contribute", page),
            ),
            date=date,
            invited=invited,
            triage=len(leads) - invited,
            visible_count=len(visible),
            cards=[
                self._lead_card(lead, by_repo.get(lead.signal.project or "")) for lead in visible
            ],
            pagination=self._pagination(
                page,
                pages,
                lambda value: self._section_page_url("contribute", value),
                item_total=len(leads),
            ),
        )

    def projects(self) -> str:
        rows = self.queries.compare_projects()
        headers = (
            ("Project", "project", "text"),
            ("Group", "group", "text"),
            ("Language", "language", "text"),
            ("License", "license", "text"),
            ("Stars", "stars", "number"),
            ("Forks", "forks", "number"),
            ("Latest stable", "release", "date"),
            ("Recent Leads observed", "leads", "number"),
        )
        return self._render(
            "pages/projects.html",
            PageMetadata(
                "Compare projects",
                "Compare factual project context and recently observed contribution leads",
                f"{self.context.site_url}/api/v1/projects.json",
                f"{self.context.site_url}/projects/",
                ("comparison.js",),
            ),
            rows=rows,
            headers=headers,
            date=rows[0].snapshot_date if rows else "none",
        )

    def personalize(self) -> str:
        date = next(iter(self.catalog.dates()), "none")
        groups: dict[str, list[RepositoryDataset]] = {}
        for dataset in self.catalog.repositories(None):
            groups.setdefault(dataset.group_id, []).append(dataset)
        return self._render(
            "pages/personalize.html",
            PageMetadata(
                "My Compass — personalized contribution table",
                "A local, personalized view of covered open-source projects and contribution leads",
                f"{self.context.site_url}/api/v1/opportunities.json",
                f"{self.context.site_url}/personalize/",
                ("personalize.js",),
            ),
            date=date,
            groups=groups,
        )

    def news(self, page: int = 1, page_size: int = 10) -> str:
        date = next(iter(self.catalog.dates()), "none")
        entries = self.news_queries.list(limit=1000)
        pages = page_count(len(entries), page_size)
        page = min(max(page, 1), pages)
        visible = self._window(list(entries), page, page_size)
        return self._render(
            "pages/news.html",
            PageMetadata(
                f"Project news — page {page}",
                "Latest releases and publicly indicated upcoming work across monitored projects",
                f"{self.context.site_url}/api/v1/news.json",
                self._section_page_url("news", page),
            ),
            date=date,
            with_upcoming=sum(bool(entry.news.upcoming) for entry in entries),
            with_release=sum(entry.news.latest_release is not None for entry in entries),
            discussion_count=sum(len(entry.news.community_discussions) for entry in entries),
            cards=[self._news_card(entry) for entry in visible],
            pagination=self._pagination(
                page,
                pages,
                lambda value: self._section_page_url("news", value),
                item_total=len(entries),
            ),
        )

    def date(self, date: str, datasets: list[RepositoryDataset]) -> str:
        groups: dict[str, list[RepositoryDataset]] = {}
        for dataset in datasets:
            groups.setdefault(dataset.group_id, []).append(dataset)
        summaries = [
            GroupSummary(
                id=group_id,
                name=items[0].group_name,
                signal_count=sum(len(item.signals) for item in items),
                project_count=len(items),
                lead_count=0,
                activity_percent=0,
            )
            for group_id, items in groups.items()
        ]
        return self._render(
            "pages/date.html",
            PageMetadata(
                date,
                f"Contribution Compass collection for {date}",
                f"{self.context.site_url}/api/v1/dates/{date}/index.json",
                f"{self.context.site_url}/updates/{date}/",
            ),
            date=date,
            groups=summaries,
        )

    def group(self, date: str, group_id: str, datasets: list[RepositoryDataset]) -> str:
        name = datasets[0].group_name if datasets else group_id
        return self._render(
            "pages/group.html",
            PageMetadata(
                name,
                f"{name} project updates",
                f"{self.context.site_url}/api/v1/dates/{date}/groups/{group_id}/index.json",
                f"{self.context.site_url}/updates/{date}/{group_id}/",
            ),
            date=date,
            group_id=group_id,
            name=name,
            datasets=datasets,
        )

    def repository(self, dataset: RepositoryDataset, page: int = 1, page_size: int = 50) -> str:
        ranked = rank_updates(dataset.signals, len(dataset.signals))
        pages = page_count(len(ranked), page_size)
        page = min(max(page, 1), pages)
        visible = self._window(list(ranked), page, page_size)
        news_entry = (
            ProjectNewsEntry(
                dataset.date,
                dataset.repository_id,
                dataset.repository,
                dataset.repository_name,
                dataset.group_id,
                dataset.group_name,
                dataset.news,
            )
            if dataset.news
            else None
        )
        return self._render(
            "pages/repository.html",
            PageMetadata(
                f"{dataset.repository_name} — page {page}",
                f"Context and observation trail for {dataset.repository}",
                (
                    f"{self.context.site_url}/api/v1/dates/{dataset.date}/groups/"
                    f"{dataset.group_id}/repositories/{dataset.repository_id}.json"
                ),
                self._repository_page_url(dataset, page),
            ),
            dataset=dataset,
            visible=visible,
            news_card=self._news_card(news_entry) if news_entry else None,
            trail=list(reversed(dataset.events[-30:])),
            pagination=self._pagination(
                page,
                pages,
                lambda value: self._repository_page_url(dataset, value),
                item_total=len(ranked),
            ),
        )


class StaticSitePublisher:
    def __init__(
        self,
        catalog: Catalog,
        *,
        output_root: str | Path = ".site",
        site_url: str,
        repository_url: str,
        assets_root: str | Path = "web/assets",
        contribution_policy: ContributionPolicy = DEFAULT_CONTRIBUTION_POLICY,
    ) -> None:
        self.catalog = catalog
        self.output_root = Path(output_root).resolve()
        self.context = SiteContext(site_url.rstrip("/"), repository_url.rstrip("/"))
        self.assets_root = Path(assets_root)
        self.contribution_policy = contribution_policy

    def _write(self, relative: str, content: str) -> None:
        destination = self.output_root / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(content, encoding="utf-8")

    def build(self) -> SiteBuild:
        if self.output_root in {Path.cwd().resolve(), Path(self.output_root.anchor)}:
            raise ValueError(f"Unsafe site output directory: {self.output_root}")
        shutil.rmtree(self.output_root, ignore_errors=True)
        self.output_root.mkdir(parents=True)
        shutil.copytree(self.assets_root, self.output_root / "assets")
        html_view = HtmlView(self.catalog, self.context, self.contribution_policy)
        machine = MachineView(self.catalog, self.context, self.contribution_policy)
        self._write("index.html", html_view.home())
        self._write("projects/index.html", html_view.projects())
        self._write("contribute/index.html", html_view.contributions())
        self._write("news/index.html", html_view.news())
        self._write("personalize/index.html", html_view.personalize())
        self._write("api/v1/index.json", machine.index())
        self._write("api/v1/schema.json", machine.schema())
        self._write("api/v1/opportunities.json", machine.opportunities())
        self._write("api/v1/news.json", machine.news())
        self._write("api/v1/projects.json", machine.project_comparison())
        self._write("feed.json", machine.json_feed())
        self._write("feed.xml", machine.rss())
        self._write("news/feed.json", machine.news_json_feed())
        self._write("news/feed.xml", machine.news_rss())
        self._write("llms.txt", machine.llms())
        self._write(".nojekyll", "")
        page_urls = [
            f"{self.context.site_url}/",
            f"{self.context.site_url}/projects/",
            f"{self.context.site_url}/contribute/",
            f"{self.context.site_url}/news/",
            f"{self.context.site_url}/personalize/",
        ]
        pages = 5
        machine_files = 8
        contribution_pages = page_count(len(html_view.queries.contribution_leads(limit=1000)), 20)
        for page in range(2, contribution_pages + 1):
            self._write(f"contribute/page/{page}/index.html", html_view.contributions(page))
            page_urls.append(f"{self.context.site_url}/contribute/page/{page}/")
            pages += 1
        news_pages = page_count(len(html_view.news_queries.list(limit=1000)), 10)
        for page in range(2, news_pages + 1):
            self._write(f"news/page/{page}/index.html", html_view.news(page))
            page_urls.append(f"{self.context.site_url}/news/page/{page}/")
            pages += 1
        for date in self.catalog.dates():
            datasets = self.catalog.repositories(date)
            self._write(f"updates/{date}/index.html", html_view.date(date, datasets))
            self._write(f"api/v1/dates/{date}/index.json", machine.date_index(date))
            page_urls.append(f"{self.context.site_url}/updates/{date}/")
            pages += 1
            machine_files += 1
            groups = sorted({dataset.group_id for dataset in datasets})
            for group_id in groups:
                group_datasets = [dataset for dataset in datasets if dataset.group_id == group_id]
                self._write(
                    f"updates/{date}/{group_id}/index.html",
                    html_view.group(date, group_id, group_datasets),
                )
                self._write(
                    f"api/v1/dates/{date}/groups/{group_id}/index.json",
                    machine.group_index(date, group_id),
                )
                page_urls.append(f"{self.context.site_url}/updates/{date}/{group_id}/")
                pages += 1
                machine_files += 1
                for dataset in group_datasets:
                    self._write(
                        f"updates/{date}/{group_id}/{dataset.repository_id}.html",
                        html_view.repository(dataset),
                    )
                    self._write(
                        f"api/v1/dates/{date}/groups/{group_id}/repositories/"
                        f"{dataset.repository_id}.json",
                        machine.repository(dataset),
                    )
                    page_urls.append(
                        f"{self.context.site_url}/updates/{date}/{group_id}/"
                        f"{dataset.repository_id}.html"
                    )
                    pages += 1
                    machine_files += 1
                    repository_pages = page_count(len(dataset.signals), 50)
                    for page in range(2, repository_pages + 1):
                        self._write(
                            f"updates/{date}/{group_id}/{dataset.repository_id}/page/"
                            f"{page}/index.html",
                            html_view.repository(dataset, page),
                        )
                        page_urls.append(
                            f"{self.context.site_url}/updates/{date}/{group_id}/"
                            f"{dataset.repository_id}/page/{page}/"
                        )
                        pages += 1
        self._write(
            "sitemap.xml",
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            + "".join(f"  <url><loc>{xml_escape(url)}</loc></url>\n" for url in page_urls)
            + "</urlset>\n",
        )
        self._write(
            "robots.txt",
            f"User-agent: *\nAllow: /\n\nSitemap: {self.context.site_url}/sitemap.xml\n"
            f"# Machine catalog: {self.context.site_url}/api/v1/index.json\n"
            f"# LLM guide: {self.context.site_url}/llms.txt\n",
        )
        return SiteBuild(str(self.output_root), len(self.catalog.dates()), pages, machine_files)


def default_site_urls() -> tuple[str, str]:
    repository = os.getenv("GITHUB_REPOSITORY", "amk9978/contribution-compass")
    owner, name = repository.split("/", 1)
    site_url = os.getenv("SITE_URL", f"https://{owner}.github.io/{name}")
    repository_url = os.getenv("REPOSITORY_URL", f"https://github.com/{repository}")
    return site_url, repository_url
