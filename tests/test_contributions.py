from __future__ import annotations

from datetime import UTC, datetime

from conftest import make_signal

from contribution_compass.domain.contributions import classify_contribution, rank_contributions
from contribution_compass.domain.policies import ContributionPolicy, ContributionWeights


def test_explicit_invitation_is_ranked_with_evidence() -> None:
    lead = classify_contribution(make_signal())
    assert lead is not None
    assert lead.tier == "maintainer-invited"
    assert "Maintainer invitation label: good first issue" in lead.reasons
    assert lead.signal.url.startswith("https://github.com/")
    assert lead.score == sum(measure.points for measure in lead.measures)
    assert {measure.id for measure in lead.measures} >= {
        "open_issue",
        "unassigned",
        "maintainer_invitation",
        "beginner_friendly",
        "reactions",
        "comments",
    }


def test_closed_assigned_stale_and_pull_request_are_excluded() -> None:
    assert classify_contribution(make_signal(state="closed")) is None
    assert classify_contribution(make_signal(assignees=["maintainer"])) is None
    assert classify_contribution(make_signal(labels=["good first issue", "stale"])) is None
    assert classify_contribution(make_signal(kind="pull_request")) is None


def test_triage_is_distinct_and_invitation_ranks_first() -> None:
    docs = make_signal(id="docs", labels=["area:docs"])
    lead = classify_contribution(docs)
    assert lead is not None and lead.tier == "triage-lead"
    assert rank_contributions([docs, make_signal()])[0].tier == "maintainer-invited"


def test_policy_weights_and_recency_are_explicit_measures() -> None:
    policy = ContributionPolicy(
        weights=ContributionWeights(
            maintainer_invitation=10,
            beginner_friendly=0,
            reaction=2,
            comment_block=0,
            recent_activity=7,
        )
    )
    lead = classify_contribution(
        make_signal(),
        policy,
        as_of=datetime(2026, 8, 14, tzinfo=UTC),
    )
    assert lead is not None
    points = {measure.id: measure.points for measure in lead.measures}
    assert points == {
        "open_issue": 0,
        "unassigned": 0,
        "maintainer_invitation": 10,
        "beginner_friendly": 0,
        "reactions": 6,
        "recent_activity": 7,
    }
    assert lead.score == 23


def test_empty_invitation_labels_do_not_restore_defaults() -> None:
    policy = ContributionPolicy(invitation_labels=(), beginner_labels=())
    assert classify_contribution(make_signal(labels=["good first issue"]), policy) is None
