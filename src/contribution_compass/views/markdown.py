from __future__ import annotations

from pathlib import Path

from contribution_compass.domain.importance import rank_updates
from contribution_compass.domain.models import CompassConfig, ContributionLead, RepoGroup, Signal


def _safe(value: str) -> str:
    return value.replace("[", "\\[").replace("]", "\\]").replace("\n", " ").strip()


def _signal(signal: Signal) -> str:
    metrics = signal.metrics
    detail: list[str] = []
    if metrics:
        detail.extend((f"{metrics.comments} comments", f"{metrics.reactions} reactions"))
    if signal.state:
        detail.append(signal.state)
    return f"- **{signal.kind.replace('_', ' ').title()}** [{_safe(signal.title)}]({signal.url}) — {' · '.join(detail)}"


def render_group(
    date: str, group: RepoGroup, signals: tuple[Signal, ...], leads: tuple[ContributionLead, ...]
) -> str:
    group_signals = tuple(signal for signal in signals if signal.group == group.id)
    group_leads = tuple(lead for lead in leads if lead.signal.group == group.id)
    repositories = {repo.repo: repo for repo in group.repos}
    lines = [
        f"# {group.name} — {date}",
        "",
        "> Factual GitHub evidence collected by Contribution Compass. No LLM analysis is performed.",
        "",
        "## Contribution Leads",
        "",
    ]
    if not group_leads:
        lines.append("No evidence-qualified contribution leads changed in this collection.")
    for lead in group_leads:
        lines.extend(
            (
                f"### [{_safe(lead.signal.title)}]({lead.signal.url})",
                "",
                f"- Project: `{lead.signal.project}`",
                f"- Tier: `{lead.tier}`",
                f"- Evidence: {'; '.join(lead.reasons)}",
                f"- Caveat: {lead.caveat}",
                "",
            )
        )
    lines.extend(("## Important Updates", ""))
    for repo_slug, repo in repositories.items():
        repo_signals = tuple(signal for signal in group_signals if signal.project == repo_slug)
        lines.extend((f"### [{repo.name}](https://github.com/{repo.repo})", ""))
        if repo_signals:
            lines.extend(_signal(signal) for signal in rank_updates(repo_signals, 30))
        else:
            lines.append("No new or materially changed signals.")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


class MarkdownReportWriter:
    def __init__(self, root: str | Path = "reports") -> None:
        self._root = Path(root)

    def publish(
        self,
        *,
        date: str,
        config: CompassConfig,
        signals: tuple[Signal, ...],
        leads: tuple[ContributionLead, ...],
    ) -> str:
        directory = self._root / date
        directory.mkdir(parents=True, exist_ok=True)
        summary = [
            f"# Contribution Compass — {date}",
            "",
            f"- {len(signals)} new or materially changed signals",
            f"- {len(leads)} evidence-qualified contribution leads",
            "",
            "## Project Groups",
            "",
        ]
        for group in config.repo_groups:
            group_signals = sum(signal.group == group.id for signal in signals)
            group_leads = sum(lead.signal.group == group.id for lead in leads)
            (directory / f"{group.id}.md").write_text(
                render_group(date, group, signals, leads), encoding="utf-8"
            )
            summary.append(
                f"- [{group.name}](./{group.id}.md) — {group_signals} updates, {group_leads} leads"
            )
        (directory / "summary.md").write_text("\n".join(summary) + "\n", encoding="utf-8")
        return str(directory)
