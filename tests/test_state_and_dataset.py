from __future__ import annotations

import json
from datetime import UTC, datetime
from pathlib import Path

from conftest import make_signal

from contribution_compass.adapters.catalog import LocalJsonCatalog
from contribution_compass.adapters.json_store import JsonDatasetWriter, JsonObservationStore
from contribution_compass.config import parse_config
from contribution_compass.domain.models import ProjectContext


def test_observation_events_form_an_append_only_change_trail(tmp_path: Path) -> None:
    root = tmp_path
    store = JsonObservationStore(root)
    first = make_signal(change=None)
    discovered = store.detect_changes((first,), datetime(2026, 8, 13, 10, tzinfo=UTC))
    unchanged = store.detect_changes((first,), datetime(2026, 8, 13, 11, tzinfo=UTC))
    updated_signal = make_signal(change=None, title="Resources leak after timeout")
    changed = store.detect_changes((updated_signal,), datetime(2026, 8, 13, 12, tzinfo=UTC))

    assert discovered.events[0].event == "discovered"
    assert unchanged.events == ()
    assert changed.events[0].event == "changed"
    assert "title" in changed.events[0].changed_fields


def test_dataset_persists_context_events_and_folder_separation(tmp_path: Path) -> None:
    root = tmp_path
    config = parse_config(
        {
            "repo_groups": {
                "runtime-tools": {
                    "name": "Runtime Tools",
                    "repos": [{"id": "widget", "repo": "acme/widget", "name": "Widget"}],
                }
            }
        }
    )
    signal = make_signal(change=None)
    changes = JsonObservationStore(root / "state").detect_changes(
        (signal,), datetime(2026, 8, 13, 10, tzinfo=UTC)
    )
    writer = JsonDatasetWriter(root / "data")
    context = ProjectContext("acme/widget", "https://github.com/acme/widget", stars=10)
    writer.persist(
        date="2026-08-13",
        collected_at=datetime(2026, 8, 13, 10, tzinfo=UTC),
        since=datetime(2026, 8, 12, 10, tzinfo=UTC),
        config=config,
        observed=(signal,),
        changes=changes,
        contexts=(context,),
        news=(),
    )

    path = root / "data/2026-08-13/runtime-tools/widget.json"
    raw = json.loads(path.read_text())
    assert raw["version"] == 3
    assert raw["context"]["stars"] == 10
    assert raw["events"][0]["signalId"] == signal.id
    catalog = LocalJsonCatalog(root / "data")
    assert catalog.events(signal.id)[0].event == "discovered"
