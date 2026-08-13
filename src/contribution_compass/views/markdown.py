from __future__ import annotations

from pathlib import Path

from contribution_compass.domain.importance import rank_updates
from contribution_compass.domain.models import (
    CompassConfig,
    ContributionLead,
    ProjectNewsSnapshot,
    RepoGroup,
    Signal,
)


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


def render_project_news(date: str, name: str, snapshot: ProjectNewsSnapshot) -> str:
    lines = [
        f"# {name} Project News — {date}",
        "",
        "> Public GitHub release and roadmap evidence. Upcoming items are indications, not commitments.",
        "",
        f"Repository: [{snapshot.repository}](https://github.com/{snapshot.repository})",
        "",
    ]
    release = snapshot.latest_release
    if release:
        lines.extend(
            (
                f"## Latest stable: [{_safe(release.title)}]({release.url})",
                "",
                f"- Tag: `{_safe(release.tag)}`",
                f"- Published: {release.published_at}",
            )
        )
        lines.extend(f"- {_safe(item)}" for item in release.highlights)
    else:
        lines.append("No published stable GitHub release was found.")
    lines.extend(("", "## Publicly indicated upcoming work", ""))
    if snapshot.upcoming:
        for item in snapshot.upcoming:
            detail = f" — due {item.due_at}" if item.due_at else ""
            lines.append(f"- **{item.kind.title()}** [{_safe(item.title)}]({item.url}){detail}")
    else:
        lines.append("No public prerelease or open milestone was found.")
    lines.extend(("", "## Hacker News discussions", ""))
    if snapshot.community_discussions:
        for discussion in snapshot.community_discussions:
            lines.append(
                f"- [{_safe(discussion.title)}]({discussion.url}) — "
                f"[{discussion.score} points · {discussion.comments} comments]"
                f"({discussion.discussion_url})"
            )
        lines.append("")
        lines.append("Community discussion; not maintainer evidence.")
    else:
        lines.append("No matching current Hacker News discussion was found.")
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
        news: tuple[ProjectNewsSnapshot, ...],
    ) -> str:
        directory = self._root / date
        directory.mkdir(parents=True, exist_ok=True)
        summary = [
            f"# Contribution Compass — {date}",
            "",
            f"- {len(signals)} new or materially changed signals",
            f"- {len(leads)} evidence-qualified contribution leads",
            f"- {sum(item.latest_release is not None for item in news)} projects with release news",
            f"- {sum(bool(item.upcoming) for item in news)} projects with public upcoming items",
            f"- {sum(len(item.community_discussions) for item in news)} Hacker News discussions",
            "",
            "- [Project news](./news/index.md)",
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
        news_by_repo = {snapshot.repository: snapshot for snapshot in news}
        news_index = ["# Project News", ""]
        for group in config.repo_groups:
            for repo in group.repos:
                snapshot = news_by_repo.get(repo.repo)
                if snapshot is None:
                    continue
                relative = Path(group.id) / f"{repo.id}.md"
                destination = directory / "news" / relative
                destination.parent.mkdir(parents=True, exist_ok=True)
                destination.write_text(
                    render_project_news(date, repo.name, snapshot), encoding="utf-8"
                )
                news_index.append(f"- [{repo.name}](./{relative.as_posix()})")
        news_directory = directory / "news"
        news_directory.mkdir(parents=True, exist_ok=True)
        (news_directory / "index.md").write_text("\n".join(news_index) + "\n", encoding="utf-8")
        (directory / "summary.md").write_text("\n".join(summary) + "\n", encoding="utf-8")
        return str(directory)
