from __future__ import annotations

import re
from typing import Any

from contribution_compass.domain.models import (
    ProjectNewsSnapshot,
    ReleaseBulletin,
    UpcomingItem,
)

MARKDOWN_LINK = re.compile(r"\[([^\]]+)\]\([^)]+\)")
MARKDOWN_DECORATION = re.compile(r"[*_`]+")
NOISE = ("full changelog", "new contributors", "contributors")
VERSION = re.compile(r"(?<!\d)(\d+)\.(\d+)(?:\.(\d+))?")


def _plain_markdown(value: str) -> str:
    value = MARKDOWN_LINK.sub(r"\1", value)
    value = MARKDOWN_DECORATION.sub("", value)
    return " ".join(value.split()).strip(" -#")


def release_highlights(notes: str | None, limit: int = 6) -> tuple[str, ...]:
    """Extract factual headings/bullets without pretending to summarize importance."""
    if not notes:
        return ()
    candidates: list[str] = []
    skip_section = False
    for raw_line in notes.splitlines():
        line = raw_line.strip()
        if line.startswith("##"):
            candidate = _plain_markdown(line)
            skip_section = any(term in candidate.casefold() for term in NOISE)
        elif re.match(r"^[-*+]\s+\S", line):
            if skip_section:
                continue
            candidate = _plain_markdown(line[1:])
        else:
            continue
        lowered = candidate.casefold()
        if not candidate or any(term in lowered for term in NOISE):
            continue
        if candidate not in candidates:
            candidates.append(candidate[:240])
        if len(candidates) >= limit:
            break
    return tuple(candidates)


def _release(raw: dict[str, Any], repository: str) -> ReleaseBulletin:
    notes = raw.get("body")
    published = raw.get("published_at") or raw.get("created_at")
    return ReleaseBulletin(
        repository=repository,
        tag=str(raw["tag_name"]),
        title=str(raw.get("name") or raw["tag_name"]).strip(),
        url=str(raw["html_url"]),
        published_at=str(published),
        notes=notes if isinstance(notes, str) and notes.strip() else None,
        highlights=release_highlights(notes if isinstance(notes, str) else None),
        prerelease=bool(raw.get("prerelease", False)),
    )


def _version(value: str) -> tuple[int, int, int] | None:
    match = VERSION.search(value)
    if match is None:
        return None
    return (int(match[1]), int(match[2]), int(match[3] or 0))


def build_project_news(
    repository: str,
    releases: list[dict[str, Any]],
    milestones: list[dict[str, Any]],
    collected_at: str,
) -> ProjectNewsSnapshot:
    published = [
        item
        for item in releases
        if not item.get("draft") and (item.get("published_at") or item.get("created_at"))
    ]
    stable = next((item for item in published if not item.get("prerelease")), None)
    stable_published = str(
        (stable.get("published_at") or stable.get("created_at")) if stable is not None else ""
    )
    prereleases = [
        item
        for item in published
        if item.get("prerelease")
        and str(item.get("published_at") or item.get("created_at") or "") > stable_published
    ][:3]
    stable_version = _version(str(stable["tag_name"])) if stable is not None else None
    upcoming: list[UpcomingItem] = [
        UpcomingItem(
            repository=repository,
            kind="prerelease",
            title=str(item.get("name") or item["tag_name"]),
            url=str(item["html_url"]),
            description=(str(item["body"])[:1000] if isinstance(item.get("body"), str) else None),
            tag=str(item["tag_name"]),
            published_at=str(item.get("published_at") or item.get("created_at")),
        )
        for item in prereleases
    ]
    public_milestones = [
        item
        for item in milestones
        if stable_version is None
        or (milestone_version := _version(str(item["title"]))) is None
        or milestone_version > stable_version
    ]
    for item in public_milestones[:5]:
        opened = int(item.get("open_issues", 0))
        closed = int(item.get("closed_issues", 0))
        total = opened + closed
        upcoming.append(
            UpcomingItem(
                repository=repository,
                kind="milestone",
                title=str(item["title"]),
                url=str(item["html_url"]),
                description=(
                    str(item["description"])[:1000]
                    if isinstance(item.get("description"), str)
                    else None
                ),
                due_at=item.get("due_on"),
                progress=round(closed * 100 / total) if total else None,
                open_issues=opened,
                closed_issues=closed,
            )
        )
    return ProjectNewsSnapshot(
        repository=repository,
        collected_at=collected_at,
        latest_release=_release(stable, repository) if stable else None,
        upcoming=tuple(upcoming),
    )
