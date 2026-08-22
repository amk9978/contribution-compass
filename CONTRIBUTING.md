# Contributing to Contribution Compass

Contribution Compass is undergoing a validation-first v2 rewrite. The product is a personalized
OSS investment recommender, not an issue feed, activity dashboard, or generic repository search
engine.

Before substantial implementation, read [the v2 specification](docs/product-spec-v2.md),
[CONTEXT.md](CONTEXT.md), and the relevant [architectural decisions](docs/adr). Open or claim a
focused issue before starting broad work.

## Product invariants

- Project first, issue second.
- Missing or low-coverage evidence remains unknown.
- Hard Taste Policy floors run before comparative ranking.
- Project evaluation has exactly three axes: Fit, Absorption, and Upside.
- Evidence, Measurements, Taste Policy, and Recommendations remain distinguishable.
- Recommendation output retains provenance and direct primary evidence.
- Collection and deterministic recommendation do not require an LLM.
- Tests never depend on live GitHub or registry requests.

## Development

```bash
uv sync --all-extras
uv run ruff check .
uv run ruff format --check .
uv run mypy src
uv run pytest
uv run contribution-compass site
```

Keep one coherent change per pull request. Add fixture-backed tests for behavior changes and update
the specification, context, or an ADR when a public contract or architectural decision changes.
