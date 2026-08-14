from __future__ import annotations

import re
from datetime import UTC, datetime, timedelta

from contribution_compass.domain.models import (
    ContributionLead,
    ContributionMeasure,
    LeadTier,
    Signal,
)
from contribution_compass.domain.policies import (
    DEFAULT_CONTRIBUTION_POLICY,
    ContributionPolicy,
)


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


def _measure(id: str, label: str, points: int, evidence: str) -> ContributionMeasure:
    return ContributionMeasure(id=id, label=label, points=points, evidence=evidence)


def _parse_timestamp(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    return parsed if parsed.tzinfo else parsed.replace(tzinfo=UTC)


def _recent_measure(
    signal: Signal, policy: ContributionPolicy, as_of: datetime | None
) -> ContributionMeasure | None:
    updated = _parse_timestamp(signal.updated_at or signal.timestamp)
    if as_of is None or updated is None:
        return None
    reference = as_of if as_of.tzinfo else as_of.replace(tzinfo=UTC)
    if updated > reference or reference - updated > timedelta(days=policy.thresholds.recent_days):
        return None
    return _measure(
        "recent_activity",
        "Recent activity",
        policy.weights.recent_activity,
        f"Updated within {policy.thresholds.recent_days} days of this snapshot",
    )


def classify_contribution(
    signal: Signal,
    policy: ContributionPolicy = DEFAULT_CONTRIBUTION_POLICY,
    *,
    as_of: datetime | None = None,
) -> ContributionLead | None:
    """Return an evidence-qualified lead or None; never infer maintainer intent."""
    if signal.kind != "issue" or signal.state != "open" or signal.assignees:
        return None

    labels = tuple(normalize_label(label) for label in signal.labels)
    excluded = {normalize_label(label) for label in policy.excluded_labels}
    if any(label in excluded for label in labels):
        return None

    invitation_labels = {normalize_label(label) for label in policy.invitation_labels}
    beginner_labels = {normalize_label(label) for label in policy.beginner_labels}
    invitations = tuple(dict.fromkeys(label for label in labels if label in invitation_labels))
    comments = signal.metrics.comments if signal.metrics else 0
    reactions = signal.metrics.reactions if signal.metrics else 0
    measures = [
        _measure("open_issue", "Open issue", 0, "GitHub reports the issue as open"),
        _measure("unassigned", "Unassigned", 0, "No assignee is listed"),
    ]
    reasons: tuple[str, ...]
    tier: LeadTier

    if invitations:
        measures.append(
            _measure(
                "maintainer_invitation",
                "Maintainer invitation",
                policy.weights.maintainer_invitation,
                f"Invitation label: {', '.join(invitations)}",
            )
        )
        beginner_matches = tuple(
            dict.fromkeys(label for label in labels if label in beginner_labels)
        )
        if beginner_matches:
            measures.append(
                _measure(
                    "beginner_friendly",
                    "Beginner-friendly invitation",
                    policy.weights.beginner_friendly,
                    f"Beginner label: {', '.join(beginner_matches)}",
                )
            )
        tier = "maintainer-invited"
        reasons = (
            f"Maintainer invitation label: {', '.join(invitations)}",
            "No assignee is listed",
        )
    else:
        if _has_category(labels, "documentation"):
            category = _measure(
                "documentation",
                "Documentation scope",
                policy.weights.documentation,
                "Documentation-related label is present",
            )
            reason = "Documentation-related issue with no assignee listed"
        elif (
            _has_category(labels, "bug")
            and comments + reactions >= policy.thresholds.bug_engagement
        ):
            category = _measure(
                "engaged_bug",
                "Engaged bug",
                policy.weights.engaged_bug,
                f"Bug has {comments + reactions} visible comments and reactions",
            )
            reason = "Unassigned bug with visible community engagement"
        elif (
            _has_category(labels, "enhancement")
            and reactions >= policy.thresholds.enhancement_reactions
        ):
            category = _measure(
                "reacted_enhancement",
                "Reacted enhancement",
                policy.weights.reacted_enhancement,
                f"Enhancement has {reactions} reactions",
            )
            reason = "Unassigned enhancement with community reactions"
        else:
            return None
        measures.append(category)
        tier = "triage-lead"
        reasons = (reason,)

    reaction_count = min(reactions, policy.thresholds.max_reaction_count)
    if reaction_count and policy.weights.reaction:
        measures.append(
            _measure(
                "reactions",
                "Community reactions",
                reaction_count * policy.weights.reaction,
                f"{reactions} reactions; capped at {policy.thresholds.max_reaction_count}",
            )
        )
    comment_blocks = min(
        comments // policy.thresholds.comments_per_point,
        policy.thresholds.max_comment_blocks,
    )
    if comment_blocks and policy.weights.comment_block:
        measures.append(
            _measure(
                "comments",
                "Discussion activity",
                comment_blocks * policy.weights.comment_block,
                (
                    f"{comments} comments; one point block per "
                    f"{policy.thresholds.comments_per_point} comments"
                ),
            )
        )
    recent = _recent_measure(signal, policy, as_of)
    if recent and recent.points:
        measures.append(recent)

    return ContributionLead(
        signal=signal,
        tier=tier,
        score=sum(measure.points for measure in measures),
        reasons=reasons,
        caveat=(
            "Confirm scope and availability with the maintainers before starting work."
            if tier == "maintainer-invited"
            else "No explicit contribution invitation was found; ask maintainers whether a "
            "contribution is wanted."
        ),
        measures=tuple(measures),
        policy_version=policy.version,
    )


def rank_contributions(
    signals: list[Signal] | tuple[Signal, ...],
    limit: int = 100,
    *,
    policy: ContributionPolicy = DEFAULT_CONTRIBUTION_POLICY,
    as_of: datetime | None = None,
) -> list[ContributionLead]:
    leads = [
        lead
        for signal in signals
        if (lead := classify_contribution(signal, policy, as_of=as_of)) is not None
    ]
    return sorted(leads, key=lambda lead: (-lead.score, lead.signal.id))[:limit]
