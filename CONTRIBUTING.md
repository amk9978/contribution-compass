# Contributing to Contribution Compass

Thank you for helping make open-source project activity easier to follow and act on.

Contribution Compass is an evidence-first data gatherer. Contributions should preserve the direct
trail from every displayed claim to its GitHub or Hacker News source. Inference belongs in an
optional extension, not in the collection core.

## Good ways to contribute

- improve an existing source adapter or add a carefully scoped new one;
- improve configuration, dependency discovery, or fork onboarding;
- add a machine-readable or human-readable view over existing catalog data;
- improve accessibility, pagination, documentation, or test coverage;
- report a reproducible collection or rendering bug; or
- propose a curated source that directly serves open-source contributors.

Browse issues labeled [`good first issue`](https://github.com/amk9978/contribution-compass/labels/good%20first%20issue)
or [`help wanted`](https://github.com/amk9978/contribution-compass/labels/help%20wanted) for work the
maintainer has explicitly opened to contributors.

For substantial changes, open an issue before implementation so the scope and evidence model can
be agreed first.

## Project invariants

Please preserve these rules:

- repository groups and keywords come only from `config.yml`;
- an empty configured list remains empty—no hidden defaults;
- source observations retain their primary evidence URLs;
- Hacker News remains community discussion, never maintainer evidence;
- collection, domain rules, and presentation stay in separate modules;
- Contribution Measures remain deterministic and explainable;
- LLM credentials and generated interpretation are not required by the core;
- JSON schema changes are explicit and backward compatibility is considered; and
- credentials, tokens, private data, and local state never enter commits.

The domain language and boundaries are documented in [CONTEXT.md](CONTEXT.md). Architectural
decisions live in [docs/adr](docs/adr).

## Development setup

Requirements: Python 3.12+, [uv](https://docs.astral.sh/uv/), and Git.

```bash
git clone https://github.com/amk9978/contribution-compass.git
cd contribution-compass
uv sync --all-extras
```

Run the complete local verification suite:

```bash
uv run ruff check .
uv run ruff format --check .
uv run mypy src
uv run pytest
uv run contribution-compass site
```

Tests must use fixtures and mocks rather than live GitHub or Hacker News requests.

## Where changes belong

```text
src/contribution_compass/
  domain/          models, policies, and deterministic rules
  application/     collection and query use cases
  adapters/        GitHub, HN, persistence, and catalog implementations
  controllers/     CLI and MCP transports
  views/           Markdown, HTML, JSON, RSS, and llms.txt
web/assets/        progressive browser CSS and JavaScript
tests/             fixture-backed unit and integration tests
```

Avoid pass-through abstractions and large mixed-responsibility modules. A new source normally needs
an adapter implementing an existing port, normalization into the shared domain model, configuration
validation, and fixture-backed tests.

## Pull requests

- Keep one coherent change per pull request.
- Add or update tests for behavior changes.
- Update README, `CONTEXT.md`, or an ADR when public behavior or architecture changes.
- Do not include routine generated `data/`, `reports/`, `.state/`, or `.site/` output in a source PR.
- Explain the evidence and tradeoffs behind new collection or ranking behavior.
- Run the verification commands above before requesting review.

By participating, you agree to follow the [Code of Conduct](CODE_OF_CONDUCT.md). For usage
questions, see [SUPPORT.md](SUPPORT.md). Report security problems through [SECURITY.md](SECURITY.md),
not a public issue.
