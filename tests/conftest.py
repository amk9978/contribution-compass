from __future__ import annotations

from contribution_compass.domain.models import (
    CrawlRun,
    ObservationEvent,
    ProjectContext,
    RepositoryDataset,
    Signal,
)


def make_signal(**overrides: object) -> Signal:
    values: dict[str, object] = {
        "id": "github:acme/widget:issue:42",
        "source": "github",
        "group": "runtime-tools",
        "project": "acme/widget",
        "kind": "issue",
        "title": "Resources remain open after cancellation",
        "text": "A minimal reproduction and workaround are included.",
        "url": "https://github.com/acme/widget/issues/42",
        "createdAt": "2026-08-12T09:00:00Z",
        "updatedAt": "2026-08-13T09:30:00Z",
        "timestamp": "2026-08-13T09:30:00Z",
        "metrics": {"comments": 7, "reactions": 3},
        "labels": ["good first issue", "bug"],
        "author": "octocat",
        "state": "open",
        "assignees": [],
        "change": "new",
    }
    values.update(overrides)
    return Signal.from_dict(values)


def make_dataset(signal: Signal | None = None) -> RepositoryDataset:
    selected = signal or make_signal()
    event = ObservationEvent(
        id="event:one",
        signal_id=selected.id,
        event="discovered",
        observed_at="2026-08-13T10:00:00Z",
        changed_fields=(),
        signal=selected,
    )
    return RepositoryDataset(
        date="2026-08-13",
        group_id="runtime-tools",
        group_name="Runtime Tools",
        repository_id="widget",
        repository="acme/widget",
        repository_name="Widget",
        runs=[CrawlRun("2026-08-13T10:00:00Z", "2026-08-12T10:00:00Z", 1, 1)],
        signals=[selected],
        events=[event],
        context=ProjectContext(
            repository="acme/widget",
            url="https://github.com/acme/widget",
            description="A runtime widget",
            language="Python",
            topics=("runtime", "testing"),
            license="MIT",
            default_branch="main",
            stars=120,
            forks=12,
            open_issues=8,
            collected_at="2026-08-13T10:00:00Z",
        ),
    )
