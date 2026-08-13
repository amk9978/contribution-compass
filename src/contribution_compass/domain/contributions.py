from __future__ import annotations

import re

from contribution_compass.domain.models import ContributionLead, Signal

INVITATION_LABELS = {
    "good first issue": "Maintainers marked this as a good first issue",
    "help wanted": "Maintainers explicitly requested help",
    "up for grabs": "Maintainers marked this as available",
    "first timers only": "Maintainers reserved this for a first-time contributor",
    "beginner friendly": "Maintainers marked this as beginner-friendly",
    "contributions welcome": "Maintainers explicitly welcome contributions",
}

DISQUALIFYING_LABELS = {
    "blocked",
    "duplicate",
    "invalid",
    "needs info",
    "needs repro",
    "question",
    "stale",
    "waiting for author",
    "waiting for response",
    "wontfix",
    "won't fix",
}


def normalize_label(value: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"[_-]+", " ", value.lower())).strip()


def _has_category(labels: tuple[str, ...], category: str) -> bool:
    if category == "documentation":
        return any(
            label in {"docs", "documentation"} or label.endswith((" docs", ":docs", "/docs"))
            for label in labels
        )
    return any(
        label == category or label.endswith(f"/{category}") or label.startswith(f"{category}:")
        for label in labels
    )


def classify_contribution(signal: Signal) -> ContributionLead | None:
    """Return an evidence-qualified lead or None; never infer maintainer intent."""
    if signal.kind != "issue" or signal.state != "open" or signal.assignees:
        return None

    labels = tuple(normalize_label(label) for label in signal.labels)
    if any(label in DISQUALIFYING_LABELS for label in labels):
        return None

    invitations = tuple(
        reason for label in labels if (reason := INVITATION_LABELS.get(label)) is not None
    )
    comments = signal.metrics.comments if signal.metrics else 0
    reactions = signal.metrics.reactions if signal.metrics else 0
    engagement = min(reactions, 15) + min(comments // 4, 10)

    if invitations:
        starter_bonus = 15 if {"good first issue", "first timers only"} & set(labels) else 0
        return ContributionLead(
            signal=signal,
            tier="maintainer-invited",
            score=60 + starter_bonus + engagement,
            reasons=tuple(dict.fromkeys((*invitations, "No assignee is listed"))),
            caveat="Confirm scope and availability with the maintainers before starting work.",
        )

    if _has_category(labels, "documentation"):
        reason = "Documentation-related issue with no assignee listed"
        category_score = 24
    elif _has_category(labels, "bug") and comments + reactions >= 4:
        reason = "Unassigned bug with visible community engagement"
        category_score = 18
    elif _has_category(labels, "enhancement") and reactions >= 3:
        reason = "Unassigned enhancement with community reactions"
        category_score = 14
    else:
        return None

    return ContributionLead(
        signal=signal,
        tier="triage-lead",
        score=category_score + engagement,
        reasons=(reason,),
        caveat=(
            "No explicit contribution invitation was found; ask maintainers whether a "
            "contribution is wanted."
        ),
    )


def rank_contributions(
    signals: list[Signal] | tuple[Signal, ...], limit: int = 100
) -> list[ContributionLead]:
    leads = [lead for signal in signals if (lead := classify_contribution(signal)) is not None]
    return sorted(leads, key=lambda lead: (-lead.score, lead.signal.id))[:limit]
