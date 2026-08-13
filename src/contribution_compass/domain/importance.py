from __future__ import annotations

from contribution_compass.domain.models import Signal

IMPORTANT_LABEL_TERMS = (
    "breaking",
    "critical",
    "performance",
    "regression",
    "security",
)


def importance_score(signal: Signal) -> int:
    """Rank update visibility using only collected facts."""
    metrics = signal.metrics
    score = 30 if signal.kind == "release" else 0
    if signal.kind == "issue":
        score += 4
    if signal.change == "updated":
        score += 2
    if metrics:
        score += min(metrics.reactions, 20) * 2
        score += min(metrics.comments, 40) // 2
    normalized_labels = tuple(label.lower() for label in signal.labels)
    score += 12 * sum(
        any(term in label for label in normalized_labels) for term in IMPORTANT_LABEL_TERMS
    )
    return score


def rank_updates(signals: list[Signal] | tuple[Signal, ...], limit: int = 100) -> list[Signal]:
    return sorted(
        signals,
        key=lambda signal: (-(importance_score(signal)), signal.id),
    )[:limit]
