from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any, cast

DEFAULT_INVITATION_LABELS = (
    "good first issue",
    "help wanted",
    "up for grabs",
    "first timers only",
    "beginner friendly",
    "contributions welcome",
)

DEFAULT_BEGINNER_LABELS = (
    "good first issue",
    "first timers only",
    "beginner friendly",
)

DEFAULT_EXCLUDED_LABELS = (
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
)


@dataclass(frozen=True, slots=True)
class ContributionWeights:
    maintainer_invitation: int = 60
    beginner_friendly: int = 15
    documentation: int = 24
    engaged_bug: int = 18
    reacted_enhancement: int = 14
    reaction: int = 1
    comment_block: int = 1
    recent_activity: int = 5

    def to_dict(self) -> dict[str, int]:
        return cast(dict[str, int], asdict(self))


@dataclass(frozen=True, slots=True)
class ContributionThresholds:
    bug_engagement: int = 4
    enhancement_reactions: int = 3
    comments_per_point: int = 4
    max_reaction_count: int = 15
    max_comment_blocks: int = 10
    recent_days: int = 14

    def to_dict(self) -> dict[str, int]:
        return cast(dict[str, int], asdict(self))


@dataclass(frozen=True, slots=True)
class ContributionPolicy:
    """Deterministic, curator-controlled policy for qualifying and ranking leads."""

    version: int = 1
    invitation_labels: tuple[str, ...] = DEFAULT_INVITATION_LABELS
    beginner_labels: tuple[str, ...] = DEFAULT_BEGINNER_LABELS
    excluded_labels: tuple[str, ...] = DEFAULT_EXCLUDED_LABELS
    weights: ContributionWeights = field(default_factory=ContributionWeights)
    thresholds: ContributionThresholds = field(default_factory=ContributionThresholds)

    def to_dict(self) -> dict[str, Any]:
        return {
            "version": self.version,
            "invitationLabels": list(self.invitation_labels),
            "beginnerLabels": list(self.beginner_labels),
            "excludedLabels": list(self.excluded_labels),
            "weights": self.weights.to_dict(),
            "thresholds": self.thresholds.to_dict(),
        }


DEFAULT_CONTRIBUTION_POLICY = ContributionPolicy()
