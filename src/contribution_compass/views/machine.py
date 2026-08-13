from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from datetime import UTC, datetime
from email.utils import format_datetime
from typing import Any
from xml.sax.saxutils import escape, quoteattr

from contribution_compass.application.catalog import CatalogQueries
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
        self.context = context
        self.generated_at = datetime.now(UTC).isoformat().replace("+00:00", "Z")

    def index(self) -> str:
        dates = self.catalog.dates()
        return json_text(
            {
                "schemaVersion": 2,
                "name": "Contribution Compass",
                "generatedAt": self.generated_at,
                "description": (
                    "Factual project context, normalized GitHub signals, append-only observation "
                    "events, and evidence-backed contribution leads."
                ),
                "latestDate": dates[0] if dates else None,
                "links": {
                    "website": f"{self.context.site_url}/",
                    "contributionLeads": f"{self.context.site_url}/api/v1/opportunities.json",
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
                    "schemaVersion": {"const": 2},
                    "dataset": {
                        "type": "object",
                        "required": [
                            "date",
                            "repository",
                            "groupId",
                            "signals",
                            "events",
                        ],
                        "properties": {
                            "date": {"type": "string", "format": "date"},
                            "repository": {"type": "string"},
                            "context": {"type": ["object", "null"]},
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
                "schemaVersion": 2,
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
                "schemaVersion": 2,
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
        return json_text({"schemaVersion": 2, "dataset": dataset.to_dict()})

    def opportunities(self) -> str:
        date = next(iter(self.catalog.dates()), None)
        datasets = self.catalog.repositories(date)
        dataset_by_repo = {dataset.repository: dataset for dataset in datasets}
        leads = self.queries.contribution_leads(limit=100)
        return json_text(
            {
                "schemaVersion": 2,
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

    def rss(self) -> str:
        feed = json.loads(self.json_feed())
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
            "    <title>Contribution Compass</title>\n"
            f"    <link>{escape(self.context.site_url)}</link>\n"
            "    <description>Important OSS updates and contribution leads.</description>\n"
            f'    <atom:link href={quoteattr(f"{self.context.site_url}/feed.xml")} rel="self" '
            'type="application/rss+xml"/>\n' + "\n".join(items) + "\n  </channel>\n</rss>\n"
        )

    def llms(self) -> str:
        return f"""# Contribution Compass

> Evidence-first project updates and contribution discovery. Collection performs no LLM inference.

## Start here

- [Contribution leads]({self.context.site_url}/api/v1/opportunities.json)
- [Versioned catalog]({self.context.site_url}/api/v1/index.json)
- [JSON Feed]({self.context.site_url}/feed.json)
- [RSS Feed]({self.context.site_url}/feed.xml)
- [MCP setup]({self.context.repository_url}/blob/main/docs/MCP.md)
- [Human contribution view]({self.context.site_url}/contribute/)

## Interpretation rules

- Signal URLs are primary GitHub evidence.
- Observation Events form the factual trail of discovered and changed Signals.
- Maintainer-Invited Leads have explicit invitation labels.
- Triage Leads are lower-confidence and are not maintainer-approved work.
- Re-check the live issue for state, assignment, scope, and contribution policy.
- Never invent maintainer intent, project importance, or contribution acceptance.
"""
