from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from datetime import UTC, datetime
from email.utils import format_datetime
from typing import Any
from xml.sax.saxutils import escape, quoteattr

from contribution_compass.application.catalog import CatalogQueries
from contribution_compass.application.news import NewsQueries, ProjectNewsEntry
from contribution_compass.domain.importance import importance_score
from contribution_compass.domain.models import ContributionLead, RepositoryDataset, Signal
from contribution_compass.ports import Catalog


@dataclass(frozen=True, slots=True)
class SiteContext:
    site_url: str
    repository_url: str


def signal_anchor(signal: Signal) -> str:
    digest = hashlib.sha1(signal.id.encode(), usedforsecurity=False).hexdigest()[:12]
    return f"signal-{digest}"


def json_text(value: Any) -> str:
    return json.dumps(value, indent=2, ensure_ascii=False) + "\n"


def signal_page_url(signal: Signal, dataset: RepositoryDataset, context: SiteContext) -> str:
    return (
        f"{context.site_url}/updates/{dataset.date}/{dataset.group_id}/"
        f"{dataset.repository_id}.html#{signal_anchor(signal)}"
    )


class MachineView:
    """Render stable machine interfaces without HTML knowledge."""

    def __init__(self, catalog: Catalog, context: SiteContext) -> None:
        self.catalog = catalog
        self.queries = CatalogQueries(catalog)
        self.news_queries = NewsQueries(catalog)
        self.context = context
        self.generated_at = datetime.now(UTC).isoformat().replace("+00:00", "Z")

    def index(self) -> str:
        dates = self.catalog.dates()
        return json_text(
            {
                "schemaVersion": 3,
                "name": "Contribution Compass",
                "generatedAt": self.generated_at,
                "description": (
                    "Factual project context, release and public-roadmap news, normalized GitHub "
                    "signals, append-only observation events, and evidence-backed contribution "
                    "leads."
                ),
                "latestDate": dates[0] if dates else None,
                "links": {
                    "website": f"{self.context.site_url}/",
                    "contributionLeads": f"{self.context.site_url}/api/v1/opportunities.json",
                    "projectNews": f"{self.context.site_url}/api/v1/news.json",
                    "newsJsonFeed": f"{self.context.site_url}/news/feed.json",
                    "newsRssFeed": f"{self.context.site_url}/news/feed.xml",
                    "schema": f"{self.context.site_url}/api/v1/schema.json",
                    "jsonFeed": f"{self.context.site_url}/feed.json",
                    "rssFeed": f"{self.context.site_url}/feed.xml",
                    "llmGuide": f"{self.context.site_url}/llms.txt",
                    "mcpGuide": f"{self.context.repository_url}/blob/main/docs/MCP.md",
                    "repository": self.context.repository_url,
                },
                "dates": [
                    {
                        "date": date,
                        "apiUrl": f"{self.context.site_url}/api/v1/dates/{date}/index.json",
                        "pageUrl": f"{self.context.site_url}/updates/{date}/",
                    }
                    for date in dates
                ],
            }
        )

    def schema(self) -> str:
        """Describe the stable envelopes and point to the navigable catalog."""
        return json_text(
            {
                "$schema": "https://json-schema.org/draft/2020-12/schema",
                "$id": f"{self.context.site_url}/api/v1/schema.json",
                "title": "Contribution Compass repository dataset",
                "description": (
                    "The complete repository payload is under the dataset property. Signal.url "
                    "and ContributionLead.evidenceUrl retain primary GitHub evidence."
                ),
                "type": "object",
                "required": ["schemaVersion", "dataset"],
                "properties": {
                    "schemaVersion": {"const": 3},
                    "dataset": {
                        "type": "object",
                        "required": [
                            "date",
                            "repository",
                            "group",
                            "signals",
                            "events",
                        ],
                        "properties": {
                            "date": {"type": "string", "format": "date"},
                            "group": {"type": "object"},
                            "repository": {"type": "object"},
                            "context": {"type": ["object", "null"]},
                            "news": {"type": ["object", "null"]},
                            "signals": {"type": "array", "items": {"type": "object"}},
                            "events": {"type": "array", "items": {"type": "object"}},
                        },
                    },
                },
            }
        )

    def date_index(self, date: str) -> str:
        datasets = self.catalog.repositories(date)
        groups: dict[str, dict[str, Any]] = {}
        for dataset in datasets:
            group = groups.setdefault(
                dataset.group_id,
                {
                    "id": dataset.group_id,
                    "name": dataset.group_name,
                    "repositoryCount": 0,
                    "signalCount": 0,
                    "eventCount": 0,
                },
            )
            group["repositoryCount"] += 1
            group["signalCount"] += len(dataset.signals)
            group["eventCount"] += len(dataset.events)
        for group in groups.values():
            group["apiUrl"] = (
                f"{self.context.site_url}/api/v1/dates/{date}/groups/{group['id']}/index.json"
            )
            group["pageUrl"] = f"{self.context.site_url}/updates/{date}/{group['id']}/"
        return json_text(
            {
                "schemaVersion": 3,
                "date": date,
                "signalCount": sum(len(dataset.signals) for dataset in datasets),
                "eventCount": sum(len(dataset.events) for dataset in datasets),
                "groups": list(groups.values()),
            }
        )

    def group_index(self, date: str, group_id: str) -> str:
        datasets = [
            dataset for dataset in self.catalog.repositories(date) if dataset.group_id == group_id
        ]
        return json_text(
            {
                "schemaVersion": 3,
                "date": date,
                "group": {
                    "id": group_id,
                    "name": datasets[0].group_name if datasets else group_id,
                },
                "repositories": [
                    {
                        "id": dataset.repository_id,
                        "repository": dataset.repository,
                        "name": dataset.repository_name,
                        "signalCount": len(dataset.signals),
                        "eventCount": len(dataset.events),
                        "apiUrl": (
                            f"{self.context.site_url}/api/v1/dates/{date}/groups/{group_id}/"
                            f"repositories/{dataset.repository_id}.json"
                        ),
                        "pageUrl": (
                            f"{self.context.site_url}/updates/{date}/{group_id}/"
                            f"{dataset.repository_id}.html"
                        ),
                    }
                    for dataset in datasets
                ],
            }
        )

    @staticmethod
    def repository(dataset: RepositoryDataset) -> str:
        return json_text({"schemaVersion": 3, "dataset": dataset.to_dict()})

    def news(self) -> str:
        entries = self.news_queries.list(limit=100)
        return json_text(
            {
                "schemaVersion": 3,
                "generatedAt": self.generated_at,
                "description": (
                    "Latest stable releases and publicly indicated upcoming work. Prereleases and "
                    "milestones are evidence, not delivery commitments."
                ),
                "count": len(entries),
                "projects": [self._news_entry(entry) for entry in entries],
            }
        )

    def _news_entry(self, entry: ProjectNewsEntry) -> dict[str, Any]:
        return {
            **entry.to_dict(),
            "pageUrl": (
                f"{self.context.site_url}/updates/{entry.date}/{entry.group_id}/"
                f"{entry.project_id}.html"
            ),
        }

    def opportunities(self) -> str:
        date = next(iter(self.catalog.dates()), None)
        datasets = self.catalog.repositories(date)
        dataset_by_repo = {dataset.repository: dataset for dataset in datasets}
        leads = self.queries.contribution_leads(limit=100)
        return json_text(
            {
                "schemaVersion": 3,
                "generatedAt": self.generated_at,
                "date": date,
                "description": "Evidence-backed leads from open, unassigned issues.",
                "methodology": {
                    "maintainerInvited": (
                        "Explicit invitation labels such as good first issue or help wanted."
                    ),
                    "triageLead": (
                        "Unassigned documentation work or engaged bugs/enhancements without an "
                        "explicit invitation."
                    ),
                    "warning": (
                        "Re-check live GitHub state and ask maintainers before substantial work."
                    ),
                },
                "count": len(leads),
                "leads": [self._lead(lead, dataset_by_repo) for lead in leads],
            }
        )

    def _lead(
        self, lead: ContributionLead, datasets: dict[str, RepositoryDataset]
    ) -> dict[str, Any]:
        dataset = datasets.get(lead.signal.project or "")
        return {
            **lead.to_dict(),
            "pageUrl": signal_page_url(lead.signal, dataset, self.context) if dataset else None,
        }

    def json_feed(self) -> str:
        datasets = [
            dataset for date in self.catalog.dates() for dataset in self.catalog.repositories(date)
        ]
        entries = sorted(
            ((signal, dataset) for dataset in datasets for signal in dataset.signals),
            key=lambda value: value[0].timestamp or value[1].date,
            reverse=True,
        )[:100]
        return json_text(
            {
                "version": "https://jsonfeed.org/version/1.1",
                "title": "Contribution Compass",
                "home_page_url": f"{self.context.site_url}/",
                "feed_url": f"{self.context.site_url}/feed.json",
                "description": "Important OSS updates and evidence-backed contribution leads.",
                "items": [
                    {
                        "id": f"{dataset.date}:{signal.id}",
                        "url": signal_page_url(signal, dataset, self.context),
                        "external_url": signal.url,
                        "title": f"[{dataset.repository_name}] {signal.title}",
                        "content_text": (signal.text or signal.kind)[:1200],
                        "date_published": signal.created_at,
                        "date_modified": signal.updated_at or signal.timestamp,
                        "tags": [signal.kind, *signal.labels],
                        "_contribution_compass": {
                            "project": signal.project,
                            "group": signal.group,
                            "state": signal.state,
                            "assignees": list(signal.assignees),
                            "change": signal.change,
                            "importanceScore": importance_score(signal),
                        },
                    }
                    for signal, dataset in entries
                ],
            }
        )

    def news_json_feed(self) -> str:
        items: list[dict[str, Any]] = []
        for entry in self.news_queries.list(limit=100):
            project_page = (
                f"{self.context.site_url}/updates/{entry.date}/{entry.group_id}/"
                f"{entry.project_id}.html"
            )
            release = entry.news.latest_release
            if release:
                items.append(
                    {
                        "id": f"release:{entry.repository}:{release.tag}",
                        "url": project_page,
                        "external_url": release.url,
                        "title": f"[{entry.project_name}] {release.title}",
                        "content_text": "\n".join(release.highlights)
                        or "Open the original release notes for details.",
                        "date_published": release.published_at,
                        "tags": ["release", entry.group_id, entry.repository],
                        "_contribution_compass": {
                            "kind": "latest_stable_release",
                            "project": entry.repository,
                            "evidenceUrl": release.url,
                        },
                    }
                )
            for upcoming in entry.news.upcoming:
                items.append(
                    {
                        "id": f"upcoming:{entry.repository}:{upcoming.kind}:{upcoming.url}",
                        "url": project_page,
                        "external_url": upcoming.url,
                        "title": f"[{entry.project_name}] Public {upcoming.kind}: {upcoming.title}",
                        "content_text": (
                            (upcoming.description or "Publicly indicated upcoming work.")
                            + " This is public evidence, not a delivery commitment."
                        )[:1200],
                        "date_published": upcoming.published_at or entry.news.collected_at,
                        "tags": ["upcoming", upcoming.kind, entry.group_id, entry.repository],
                        "_contribution_compass": {
                            "kind": upcoming.kind,
                            "project": entry.repository,
                            "dueAt": upcoming.due_at,
                            "progress": upcoming.progress,
                            "evidenceUrl": upcoming.url,
                        },
                    }
                )
        items.sort(key=lambda item: str(item.get("date_published", "")), reverse=True)
        return json_text(
            {
                "version": "https://jsonfeed.org/version/1.1",
                "title": "Contribution Compass Project News",
                "home_page_url": f"{self.context.site_url}/news/",
                "feed_url": f"{self.context.site_url}/news/feed.json",
                "description": "Latest stable releases and publicly indicated upcoming work.",
                "items": items[:100],
            }
        )

    def rss(self) -> str:
        return self._rss_document(
            json.loads(self.json_feed()),
            title="Contribution Compass",
            description="Important OSS updates and contribution leads.",
            feed_url=f"{self.context.site_url}/feed.xml",
        )

    def news_rss(self) -> str:
        return self._rss_document(
            json.loads(self.news_json_feed()),
            title="Contribution Compass Project News",
            description="Latest stable releases and publicly indicated upcoming work.",
            feed_url=f"{self.context.site_url}/news/feed.xml",
        )

    def _rss_document(
        self, feed: dict[str, Any], *, title: str, description: str, feed_url: str
    ) -> str:
        items = []
        for item in feed["items"]:
            published = item.get("date_modified") or item.get("date_published")
            published_rfc822 = None
            if published:
                try:
                    parsed = datetime.fromisoformat(str(published).replace("Z", "+00:00"))
                    published_rfc822 = format_datetime(parsed)
                except ValueError:
                    published_rfc822 = None
            items.append(
                "    <item>\n"
                f"      <title>{escape(item['title'])}</title>\n"
                f"      <link>{escape(item['url'])}</link>\n"
                f'      <guid isPermaLink="false">{escape(item["id"])}</guid>\n'
                + (
                    f"      <pubDate>{escape(published_rfc822)}</pubDate>\n"
                    if published_rfc822
                    else ""
                )
                + f"      <description>{escape(item['content_text'])}</description>\n"
                + f"      <source url={quoteattr(item['external_url'])}>GitHub evidence</source>\n"
                "    </item>"
            )
        return (
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">\n'
            "  <channel>\n"
            f"    <title>{escape(title)}</title>\n"
            f"    <link>{escape(self.context.site_url)}</link>\n"
            f"    <description>{escape(description)}</description>\n"
            f'    <atom:link href={quoteattr(feed_url)} rel="self" '
            'type="application/rss+xml"/>\n' + "\n".join(items) + "\n  </channel>\n</rss>\n"
        )

    def llms(self) -> str:
        return f"""# Contribution Compass

> Evidence-first project updates and contribution discovery. Collection performs no LLM inference.

## Start here

- [Contribution leads]({self.context.site_url}/api/v1/opportunities.json)
- [Project news]({self.context.site_url}/api/v1/news.json)
- [Project news JSON Feed]({self.context.site_url}/news/feed.json)
- [Project news RSS]({self.context.site_url}/news/feed.xml)
- [Versioned catalog]({self.context.site_url}/api/v1/index.json)
- [JSON Feed]({self.context.site_url}/feed.json)
- [RSS Feed]({self.context.site_url}/feed.xml)
- [MCP setup]({self.context.repository_url}/blob/main/docs/MCP.md)
- [Human contribution view]({self.context.site_url}/contribute/)

## Interpretation rules

- Signal URLs are primary GitHub evidence.
- Observation Events form the factual trail of discovered and changed Signals.
- Release highlights are extracted from original notes; public upcoming items are not commitments.
- Maintainer-Invited Leads have explicit invitation labels.
- Triage Leads are lower-confidence and are not maintainer-approved work.
- Re-check the live issue for state, assignment, scope, and contribution policy.
- Never invent maintainer intent, project importance, or contribution acceptance.
"""
