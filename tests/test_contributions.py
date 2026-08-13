from __future__ import annotations

from conftest import make_signal

from contribution_compass.domain.contributions import classify_contribution, rank_contributions


def test_explicit_invitation_is_ranked_with_evidence() -> None:
    lead = classify_contribution(make_signal())
    assert lead is not None
    assert lead.tier == "maintainer-invited"
    assert "Maintainers marked this as a good first issue" in lead.reasons
    assert lead.signal.url.startswith("https://github.com/")


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
