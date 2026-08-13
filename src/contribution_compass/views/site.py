from __future__ import annotations

import html
import os
import shutil
from collections.abc import Callable
from dataclasses import dataclass
from math import ceil
from pathlib import Path
from typing import TypeVar
from urllib.parse import urlparse
from xml.sax.saxutils import escape as xml_escape

from contribution_compass.application.catalog import CatalogQueries
from contribution_compass.application.news import NewsQueries, ProjectNewsEntry
from contribution_compass.domain.importance import importance_score, rank_updates
from contribution_compass.domain.models import ContributionLead, RepositoryDataset, Signal
from contribution_compass.ports import Catalog
from contribution_compass.views.machine import MachineView, SiteContext, signal_anchor

T = TypeVar("T")


def h(value: object) -> str:
    return html.escape(str(value), quote=True)


def safe_url(value: str) -> str:
    parsed = urlparse(value)
    return h(value) if parsed.scheme in {"http", "https"} else "#"


def compact(value: int) -> str:
    if value >= 1_000_000:
        return f"{value / 1_000_000:.1f}M"
    if value >= 1_000:
        return f"{value / 1_000:.1f}K"
    return str(value)


def short_date(value: str | None) -> str:
    return value[:10] if value else "date unavailable"


def page_count(total: int, page_size: int) -> int:
    return max(1, ceil(total / page_size))


@dataclass(frozen=True, slots=True)
class SiteBuild:
    output_root: str
    dates: int
    pages: int
    machine_files: int


class HtmlView:
    """Human presentation only; domain decisions arrive through CatalogQueries."""

    def __init__(self, catalog: Catalog, context: SiteContext) -> None:
        self.catalog = catalog
        self.queries = CatalogQueries(catalog)
        self.news_queries = NewsQueries(catalog)
        self.context = context
        self._signal_page_cache: dict[tuple[str, str], dict[str, int]] = {}

    @staticmethod
    def _window(values: list[T], page: int, page_size: int) -> list[T]:
        start = (page - 1) * page_size
        return values[start : start + page_size]

    def _pagination(
        self,
        current: int,
        total: int,
        url_for_page: Callable[[int], str],
        *,
        item_total: int,
    ) -> str:
        if total <= 1:
            return ""
        url = url_for_page
        previous = (
            f'<a rel="prev" href="{h(url(current - 1))}">← Previous</a>'
            if current > 1
            else '<span class="disabled">← Previous</span>'
        )
        following = (
            f'<a rel="next" href="{h(url(current + 1))}">Next →</a>'
            if current < total
            else '<span class="disabled">Next →</span>'
        )
        return f'<nav class="pagination" aria-label="Pagination">{previous}<span>Page {current} of {total} · {item_total} items</span>{following}</nav>'

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

    def page(self, title: str, description: str, content: str, *, api_url: str) -> str:
        return f"""<!doctype html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{h(description)}">
  <meta name="color-scheme" content="dark light">
  <title>{h(title)} · Contribution Compass</title>
  <link rel="icon" href="{self.context.site_url}/assets/favicon.svg" type="image/svg+xml">
  <link rel="alternate" type="application/json" title="Machine data" href="{api_url}">
  <link rel="alternate" type="application/feed+json" title="JSON Feed" href="{self.context.site_url}/feed.json">
  <link rel="alternate" type="application/rss+xml" title="RSS" href="{self.context.site_url}/feed.xml">
  <link rel="stylesheet" href="{self.context.site_url}/assets/styles.css">
  <link rel="stylesheet" href="{self.context.site_url}/assets/contributions.css">
</head>
<body>
  <header class="topbar">
    <a class="brand" href="{self.context.site_url}/"><span class="brand-mark">⌖</span><span>contribution/<strong>compass</strong></span></a>
    <nav class="topnav"><a href="{self.context.site_url}/contribute/">Contribute</a><a href="{self.context.site_url}/news/">News</a><a href="{self.context.site_url}/api/v1/index.json">Data</a><a class="secondary-nav" href="{self.context.site_url}/feed.xml">RSS</a><a class="secondary-nav" href="{self.context.repository_url}">GitHub</a><button class="theme-toggle" type="button" aria-label="Toggle color theme">◐</button></nav>
  </header>
  {content}
  <footer class="footer"><span>Direct GitHub and Hacker News evidence · No generated analysis</span><span><a href="{self.context.site_url}/llms.txt">LLM guide</a> · <a href="{self.context.repository_url}/blob/main/docs/MCP.md">MCP</a></span></footer>
  <script src="{self.context.site_url}/assets/app.js" defer></script>
</body>
</html>"""

    @staticmethod
    def _metrics(datasets: list[RepositoryDataset]) -> dict[str, int]:
        signals = [signal for dataset in datasets for signal in dataset.signals]
        return {
            "signals": len(signals),
            "repositories": sum(bool(dataset.signals) for dataset in datasets),
            "issues": sum(signal.kind == "issue" for signal in signals),
            "pulls": sum(signal.kind == "pull_request" for signal in signals),
            "releases": sum(signal.kind == "release" for signal in signals),
            "events": sum(len(dataset.events) for dataset in datasets),
        }

    @staticmethod
    def _metric(label: str, value: str | int, detail: str) -> str:
        rendered = compact(value) if isinstance(value, int) else value
        return f'<div class="metric"><span>{h(label)}</span><strong>{h(rendered)}</strong><small>{h(detail)}</small></div>'

    def _lead_card(self, lead: ContributionLead, dataset: RepositoryDataset | None) -> str:
        labels = "".join(
            f'<span class="label">{h(label)}</span>' for label in lead.signal.labels[:5]
        )
        collected_url = "#"
        if dataset:
            signal_page = self._signal_page(dataset, lead.signal)
            collected_url = (
                f"{self._repository_page_url(dataset, signal_page)}#{signal_anchor(lead.signal)}"
            )
        search = " ".join(
            (lead.signal.title, lead.signal.project or "", *lead.signal.labels)
        ).casefold()
        return f"""<article class="contribution-card" data-tier="{lead.tier}" data-contribution-search="{h(search)}">
  <div class="contribution-head"><span class="lead-tier {lead.tier}">{"Maintainer invited" if lead.tier == "maintainer-invited" else "Triage lead"}</span><span>{h(lead.signal.project or "")}</span></div>
  <h3><a href="{safe_url(lead.signal.url)}">{h(lead.signal.title)}</a></h3>
  <div class="lead-reasons">{"".join(f"<span>{h(reason)}</span>" for reason in lead.reasons)}</div>
  <div class="signal-meta"><span>{lead.signal.metrics.comments if lead.signal.metrics else 0} comments</span><span>{lead.signal.metrics.reactions if lead.signal.metrics else 0} reactions</span>{labels}</div>
  <p class="lead-caveat">{h(lead.caveat)}</p>
  <div class="lead-actions"><a href="{safe_url(lead.signal.url)}">Check live issue ↗</a><a href="{collected_url}">Collected context →</a></div>
</article>"""

    def _signal_card(self, signal: Signal) -> str:
        body = (signal.text or "")[:360]
        search = " ".join((signal.title, signal.text or "", *signal.labels)).casefold()[:1000]
        labels = "".join(f'<span class="label">{h(label)}</span>' for label in signal.labels[:5])
        return f"""<article class="signal-card" id="{signal_anchor(signal)}" data-kind="{signal.kind}" data-search="{h(search)}">
  <div class="signal-head"><span class="kind {signal.kind}">{h(signal.kind.replace("_", " "))}</span><time>{h(signal.timestamp or "unknown")}</time></div>
  <h3><a href="{safe_url(signal.url)}">{h(signal.title)}</a></h3>
  {f"<p>{h(body)}</p>" if body else ""}
  <div class="signal-meta"><span>importance {importance_score(signal)}</span>{f"<span>@{h(signal.author)}</span>" if signal.author else ""}{f"<span>{h(signal.state)}</span>" if signal.state else ""}{labels}<a class="evidence" href="{safe_url(signal.url)}">Original evidence ↗</a></div>
</article>"""

    def _news_card(self, entry: ProjectNewsEntry) -> str:
        release = entry.news.latest_release
        highlights = (
            "".join(f"<li>{h(item)}</li>" for item in release.highlights[:5]) if release else ""
        )
        release_html = (
            f"""<div class="release-bulletin"><div class="news-meta"><span class="news-kind stable">Latest stable</span><time>{h(short_date(release.published_at))}</time></div><h3><a href="{safe_url(release.url)}">{h(release.title)}</a></h3><code>{h(release.tag)}</code>{f"<ul>{highlights}</ul>" if highlights else "<p>Open the original release notes for details.</p>"}<a class="evidence" href="{safe_url(release.url)}">Original release notes ↗</a></div>"""
            if release
            else '<div class="release-bulletin unavailable"><p>No published stable GitHub release was found.</p></div>'
        )
        upcoming = "".join(
            f"""<li><span class="news-kind {item.kind}">{h(item.kind)}</span><div><a href="{safe_url(item.url)}">{h(item.title)}</a><small>{h(f"Due {short_date(item.due_at)}" if item.due_at else f"Published {short_date(item.published_at)}" if item.published_at else "Publicly indicated")}</small>{f'<span class="progress-label">{item.progress}% complete · {item.open_issues} open</span>' if item.progress is not None else ""}</div></li>"""
            for item in entry.news.upcoming[:5]
        )
        discussions = "".join(
            f'<li><div><a href="{safe_url(item.url)}">{h(item.title)}</a><small>{item.score} points · {item.comments} comments · {h(short_date(item.published_at))}</small></div><a class="hn-link" href="{safe_url(item.discussion_url)}">HN discussion ↗</a></li>'
            for item in entry.news.community_discussions[:4]
        )
        community_html = (
            f'<div class="community-news"><h3>Hacker News discussions</h3><ul>{discussions}</ul><p class="news-caveat">Community discussion, matched to this configured project; not maintainer evidence.</p></div>'
            if discussions
            else ""
        )
        project_url = (
            f"{self.context.site_url}/updates/{entry.date}/{entry.group_id}/{entry.project_id}.html"
        )
        return f"""<article class="news-card"><header><div><span class="repo-slug">{h(entry.repository)}</span><h2><a href="{project_url}">{h(entry.project_name)}</a></h2></div><span>{h(entry.group_name)}</span></header>{release_html}<div class="upcoming-news"><h3>Publicly indicated next</h3><ul>{upcoming or '<li class="unavailable">No public prerelease or open milestone found.</li>'}</ul><p class="news-caveat">Prereleases and milestones indicate public plans; they are not delivery commitments.</p></div>{community_html}</article>"""

    def home(self) -> str:
        dates = self.catalog.dates()
        if not dates:
            content = '<main class="empty-state"><h1>Waiting for the first collection</h1></main>'
            return self.page(
                "Project updates and contribution leads",
                "Contribution Compass is waiting for data",
                content,
                api_url=f"{self.context.site_url}/api/v1/index.json",
            )
        date = dates[0]
        datasets = self.catalog.repositories(date)
        signals = [signal for dataset in datasets for signal in dataset.signals]
        leads = self.queries.contribution_leads(limit=1000)
        news = self.news_queries.list(limit=6)
        invited = [lead for lead in leads if lead.tier == "maintainer-invited"]
        by_repo = {dataset.repository: dataset for dataset in datasets}
        metrics = self._metrics(datasets)
        groups: dict[str, list[RepositoryDataset]] = {}
        for dataset in datasets:
            groups.setdefault(dataset.group_id, []).append(dataset)
        group_cards = "".join(
            f"""<a class="group-card" href="{self.context.site_url}/updates/{date}/{group_id}/"><div class="group-title"><h3>{h(items[0].group_name)}</h3><strong>{compact(sum(len(item.signals) for item in items))}</strong></div><div class="activity-bar"><span style="width:{max(1, min(100, sum(len(item.signals) for item in items) // 10))}%"></span></div><div class="group-meta"><span>{len(items)} projects</span><span>{sum(lead.signal.group == group_id for lead in leads)} contribution leads</span></div></a>"""
            for group_id, items in groups.items()
        )
        lead_cards = "".join(
            self._lead_card(lead, by_repo.get(lead.signal.project or "")) for lead in leads[:6]
        )
        updates = "".join(self._signal_card(signal) for signal in rank_updates(signals, 12))
        news_cards = "".join(self._news_card(entry) for entry in news)
        content = f"""<main>
<section class="hero shell"><div><span class="eyebrow">LATEST COLLECTION · {date}</span><h1>Follow important projects.<br><em>Find where to help.</em></h1><p>Factual updates, project context, and evidence-backed contribution leads from {len(datasets)} curated open-source projects.</p></div><a class="date-chip" href="{self.context.site_url}/updates/{date}/"><span>Browse snapshot</span><strong>{date}</strong></a></section>
<section class="metrics shell">{self._metric("Signals", metrics["signals"], "new or changed")}{self._metric("Contribution leads", len(leads), "evidence-qualified")}{self._metric("Maintainer invited", len(invited), "explicitly labeled")}{self._metric("Projects", metrics["repositories"], "with activity")}{self._metric("Trail events", metrics["events"], "append-only")}</section>
<section class="section shell"><div class="section-heading"><div><span class="eyebrow">PROJECT MAP</span><h2>Curated communities</h2></div><span>{len(groups)} groups</span></div><div class="group-grid">{group_cards}</div></section>
<section class="section shell"><div class="section-heading"><div><span class="eyebrow">CONTRIBUTION COMPASS</span><h2>Evidence-backed places to help</h2></div><a href="{self.context.site_url}/contribute/">View all →</a></div><p class="section-intro">Explicit invitations are separated from lower-confidence triage leads. Check the live issue before starting.</p><div class="contribution-grid">{lead_cards or '<div class="no-leads">The next collection will populate leads after state and assignee metadata is available.</div>'}</div></section>
<section class="section shell"><div class="section-heading"><div><span class="eyebrow">PROJECT NEWS</span><h2>What shipped—and what may be next</h2></div><a href="{self.context.site_url}/news/">All project news →</a></div><p class="section-intro">Maintainer release and roadmap evidence, plus relevant Hacker News discussions kept clearly separate.</p><div class="news-grid">{news_cards or '<div class="no-leads">Project news will appear after the next collection.</div>'}</div></section>
<section class="section shell archive"><div class="section-heading"><div><span class="eyebrow">IMPORTANT UPDATES</span><h2>What deserves attention</h2></div><a href="{self.context.site_url}/feed.json">JSON Feed →</a></div><div class="signal-list compact-list">{updates}</div></section>
</main>"""
        return self.page(
            "Project updates and contribution leads",
            "Important open-source project updates and evidence-backed contribution leads",
            content,
            api_url=f"{self.context.site_url}/api/v1/index.json",
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
        cards = "".join(
            self._lead_card(lead, by_repo.get(lead.signal.project or "")) for lead in visible
        )
        pagination = self._pagination(
            page,
            pages,
            lambda value: self._section_page_url("contribute", value),
            item_total=len(leads),
        )
        content = f"""<main class="shell detail-page"><nav class="breadcrumbs"><a href="{self.context.site_url}/">Compass</a><span>/</span><span>Contribute</span></nav>
<section class="detail-hero"><span class="eyebrow">CONTRIBUTION COMPASS · {date}</span><h1>Find a concrete place<br>to contribute.</h1><p>Discovery leads—not generated project ideas—with the evidence and caveat behind every result.</p></section>
<section class="lead-method"><div><strong>{invited}</strong><span>Maintainer-invited</span><p>Explicit contribution labels.</p></div><div><strong>{len(leads) - invited}</strong><span>Triage leads</span><p>Worth asking about; not pre-approved.</p></div><div><strong>Live check</strong><span>Required</span><p>Confirm state, assignment, and scope.</p></div></section>
<section class="filter-bar contribution-filter"><input id="contribution-search" type="search" placeholder="Search this page…"><div class="filter-buttons"><button class="active" data-contribution-filter="all">All</button><button data-contribution-filter="maintainer-invited">Maintainer invited</button><button data-contribution-filter="triage-lead">Triage leads</button></div><span id="contribution-count">{len(visible)} shown</span></section>
<section class="contribution-grid">{cards or '<div class="no-leads">No evidence-qualified leads are available in this snapshot.</div>'}</section>
{pagination}
</main>"""
        return self.page(
            f"Contribution opportunities — page {page}",
            "Evidence-backed open-source contribution leads",
            content,
            api_url=f"{self.context.site_url}/api/v1/opportunities.json",
        )

    def news(self, page: int = 1, page_size: int = 10) -> str:
        date = next(iter(self.catalog.dates()), "none")
        entries = self.news_queries.list(limit=1000)
        pages = page_count(len(entries), page_size)
        page = min(max(page, 1), pages)
        visible = self._window(list(entries), page, page_size)
        with_upcoming = sum(bool(entry.news.upcoming) for entry in entries)
        with_release = sum(entry.news.latest_release is not None for entry in entries)
        discussions = sum(len(entry.news.community_discussions) for entry in entries)
        cards = "".join(self._news_card(entry) for entry in visible)
        pagination = self._pagination(
            page,
            pages,
            lambda value: self._section_page_url("news", value),
            item_total=len(entries),
        )
        content = f"""<main class="shell detail-page"><nav class="breadcrumbs"><a href="{self.context.site_url}/">Compass</a><span>/</span><span>News</span></nav>
<section class="detail-hero"><span class="eyebrow">PROJECT NEWS · {date}</span><h1>See what shipped.<br>Follow where people are talking.</h1><p>Release developments, public roadmap evidence, and relevant Hacker News discussions for configured projects.</p></section>
<section class="lead-method"><div><strong>{with_release}</strong><span>Latest releases</span><p>Stable release notes from GitHub.</p></div><div><strong>{with_upcoming}</strong><span>Public roadmaps</span><p>Prereleases or open milestones.</p></div><div><strong>{discussions}</strong><span>HN discussions</span><p>Current community conversations.</p></div></section>
<section class="news-explainer"><strong>How to read this</strong><p>GitHub releases and roadmaps are maintainer evidence. Hacker News is community discussion and is labeled separately. No generated summaries are used. <a href="{self.context.site_url}/news/feed.xml">Subscribe to project-news RSS →</a></p></section>
<section class="news-grid news-grid-full">{cards or '<div class="no-leads">No project news has been collected yet.</div>'}</section>{pagination}</main>"""
        return self.page(
            f"Project news — page {page}",
            "Latest releases and publicly indicated upcoming work across monitored projects",
            content,
            api_url=f"{self.context.site_url}/api/v1/news.json",
        )

    def date(self, date: str, datasets: list[RepositoryDataset]) -> str:
        groups: dict[str, list[RepositoryDataset]] = {}
        for dataset in datasets:
            groups.setdefault(dataset.group_id, []).append(dataset)
        cards = "".join(
            f'<a class="group-card" href="{self.context.site_url}/updates/{date}/{group}/"><div class="group-title"><h3>{h(items[0].group_name)}</h3><strong>{sum(len(item.signals) for item in items)}</strong></div><div class="group-meta"><span>{len(items)} projects</span><span>Explore →</span></div></a>'
            for group, items in groups.items()
        )
        content = f'<main class="shell detail-page"><section class="detail-hero"><span class="eyebrow">COLLECTION SNAPSHOT</span><h1>{date}</h1><p>Browse factual updates by project group.</p></section><div class="group-grid">{cards}</div></main>'
        return self.page(
            date,
            f"Contribution Compass collection for {date}",
            content,
            api_url=f"{self.context.site_url}/api/v1/dates/{date}/index.json",
        )

    def group(self, date: str, group_id: str, datasets: list[RepositoryDataset]) -> str:
        cards = "".join(
            f'<a class="repository-card" href="{self.context.site_url}/updates/{date}/{group_id}/{dataset.repository_id}.html"><div><span class="repo-slug">{h(dataset.repository)}</span><h2>{h(dataset.repository_name)}</h2></div><strong>{len(dataset.signals)}</strong><span class="repo-link">{len(dataset.events)} trail events · View →</span></a>'
            for dataset in datasets
        )
        name = datasets[0].group_name if datasets else group_id
        content = f'<main class="shell detail-page"><section class="detail-hero"><span class="eyebrow">{date}</span><h1>{h(name)}</h1><p>{len(datasets)} curated projects.</p></section><section class="repository-grid">{cards}</section></main>'
        return self.page(
            name,
            f"{name} project updates",
            content,
            api_url=f"{self.context.site_url}/api/v1/dates/{date}/groups/{group_id}/index.json",
        )

    def repository(self, dataset: RepositoryDataset, page: int = 1, page_size: int = 50) -> str:
        context = dataset.context
        context_html = (
            f'<section class="project-context"><p>{h(context.description or "No repository description.")}</p><div class="signal-meta"><span>{compact(context.stars)} stars</span><span>{compact(context.forks)} forks</span><span>{h(context.language or "language unknown")}</span><span>{h(context.license or "license unknown")}</span>{"".join(f'<span class="label">{h(topic)}</span>' for topic in context.topics[:8])}</div></section>'
            if context
            else '<section class="project-context"><p>Project context will be collected on the next run.</p></section>'
        )
        ranked = rank_updates(dataset.signals, len(dataset.signals))
        pages = page_count(len(ranked), page_size)
        page = min(max(page, 1), pages)
        visible = self._window(list(ranked), page, page_size)
        signals = "".join(self._signal_card(signal) for signal in visible)
        pagination = self._pagination(
            page,
            pages,
            lambda value: self._repository_page_url(dataset, value),
            item_total=len(ranked),
        )
        trail = "".join(
            f"<li><time>{h(event.observed_at)}</time><strong>{h(event.event)}</strong><span>{h(', '.join(event.changed_fields) or 'initial snapshot')}</span></li>"
            for event in reversed(dataset.events[-30:])
        )
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
        news_html = (
            f'<section class="project-news"><div class="section-heading"><div><span class="eyebrow">PROJECT NEWS</span><h2>Release, roadmap, and discussion</h2></div><a href="{self.context.site_url}/news/">All news →</a></div>{self._news_card(news_entry)}</section>'
            if news_entry
            else '<section class="project-context"><p>Project news will be collected on the next run.</p></section>'
        )
        content = f"""<main class="shell detail-page"><section class="repo-hero"><div><span class="eyebrow">{h(dataset.repository)}</span><h1>{h(dataset.repository_name)}</h1><p>{len(dataset.signals)} signals · {len(dataset.events)} observation events</p></div><a class="primary-button" href="https://github.com/{h(dataset.repository)}">Open repository ↗</a></section>{context_html}{news_html}<section class="timeline"><h2>Observation trail</h2><ol>{trail or "<li>Trail events begin with the next collection.</li>"}</ol></section><section class="filter-bar"><input id="signal-search" type="search" placeholder="Search this page…"><div class="filter-buttons"><button class="active" data-filter="all">All</button><button data-filter="issue">Issues</button><button data-filter="pull_request">PRs</button><button data-filter="release">Releases</button></div><span id="filter-count">{len(visible)} shown</span></section><section class="signal-list">{signals or '<div class="no-signals">No changed signals.</div>'}</section>{pagination}</main>"""
        return self.page(
            f"{dataset.repository_name} — page {page}",
            f"Context and observation trail for {dataset.repository}",
            content,
            api_url=(
                f"{self.context.site_url}/api/v1/dates/{dataset.date}/groups/{dataset.group_id}/"
                f"repositories/{dataset.repository_id}.json"
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
    ) -> None:
        self.catalog = catalog
        self.output_root = Path(output_root).resolve()
        self.context = SiteContext(site_url.rstrip("/"), repository_url.rstrip("/"))
        self.assets_root = Path(assets_root)

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
        html_view = HtmlView(self.catalog, self.context)
        machine = MachineView(self.catalog, self.context)
        self._write("index.html", html_view.home())
        self._write("contribute/index.html", html_view.contributions())
        self._write("news/index.html", html_view.news())
        self._write("api/v1/index.json", machine.index())
        self._write("api/v1/schema.json", machine.schema())
        self._write("api/v1/opportunities.json", machine.opportunities())
        self._write("api/v1/news.json", machine.news())
        self._write("feed.json", machine.json_feed())
        self._write("feed.xml", machine.rss())
        self._write("news/feed.json", machine.news_json_feed())
        self._write("news/feed.xml", machine.news_rss())
        self._write("llms.txt", machine.llms())
        self._write(".nojekyll", "")
        page_urls = [
            f"{self.context.site_url}/",
            f"{self.context.site_url}/contribute/",
            f"{self.context.site_url}/news/",
        ]
        pages = 3
        machine_files = 7
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
