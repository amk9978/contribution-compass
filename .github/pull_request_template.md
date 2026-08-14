## Summary

Describe the focused change and the contributor problem it addresses.

## Evidence and design

Link the issue, source evidence, or architectural decision behind the change. Explain important
tradeoffs and why the selected scope is appropriate.

## Validation

- [ ] `uv run ruff check .`
- [ ] `uv run ruff format --check .`
- [ ] `uv run mypy src`
- [ ] `uv run pytest`
- [ ] `uv run contribution-compass site` when views or schemas change

## Project invariants

- [ ] New observations retain direct primary-evidence URLs.
- [ ] Empty configuration stays empty; no hidden defaults or repositories were introduced.
- [ ] Source, domain, application, and view responsibilities remain separated.
- [ ] Tests use fixtures or mocks rather than live network calls.
- [ ] No credentials, private data, or routine generated collection output are included.
- [ ] User-facing configuration or schema changes are documented.
