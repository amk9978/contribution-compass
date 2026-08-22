## Summary

Describe the focused change and the OSS investment decision it improves.

## Evidence and design

Link the issue, product-spec section, fixture, evidence, or architectural decision behind the
change. Explain important tradeoffs and why the selected scope is appropriate.

## Validation

- [ ] `uv run ruff check .`
- [ ] `uv run ruff format --check .`
- [ ] `uv run mypy src`
- [ ] `uv run pytest`
- [ ] `uv run contribution-compass site` when views or schemas change

## Project invariants

- [ ] Project evaluation happens before issue selection.
- [ ] Evidence, Measurements, Taste Policy, and Recommendations remain distinguishable.
- [ ] Missing evidence remains unknown rather than being silently imputed.
- [ ] Domain, application, adapter, controller, and view responsibilities remain separated.
- [ ] Tests use fixtures or mocks rather than live network calls.
- [ ] No credentials, private profile data, or unnecessary raw source snapshots are included.
- [ ] User-facing configuration or schema changes are documented.
