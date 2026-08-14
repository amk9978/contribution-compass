# Developer Infrastructure — 2026-08-14

> Factual GitHub evidence collected by Contribution Compass. No LLM analysis is performed.

## Contribution Leads

### [Add environment variable to always use `--active` flag](https://github.com/astral-sh/uv/issues/11273)

- Project: `astral-sh/uv`
- Tier: `triage-lead`
- Evidence: Unassigned enhancement with community reactions
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [Have `uv sync` default to `--locked`](https://github.com/astral-sh/uv/issues/12372)

- Project: `astral-sh/uv`
- Tier: `triage-lead`
- Evidence: Unassigned enhancement with community reactions
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

## Important Updates

### [Dagger](https://github.com/dagger/dagger)

- **Issue** [v0.x modules are given a v1.0 view](https://github.com/dagger/dagger/issues/13883) — 1 comments · 0 reactions · closed
- **Pull Request** [workspace: add native polyfill replacements](https://github.com/dagger/dagger/pull/13854) — 0 comments · 0 reactions · open
- **Pull Request** [workspace: compare changes from an explicit baseline](https://github.com/dagger/dagger/pull/13855) — 0 comments · 0 reactions · open
- **Pull Request** [engine: support manual metadata pruning](https://github.com/dagger/dagger/pull/13887) — 0 comments · 0 reactions · closed
- **Pull Request** [dagql: reduce e-graph result-removal contention](https://github.com/dagger/dagger/pull/13888) — 0 comments · 0 reactions · open
- **Pull Request** [fix: handle function arg name collision with inherited persistent flags](https://github.com/dagger/dagger/pull/13711) — 2 comments · 0 reactions · closed
- **Pull Request** [Fix/13605 go sdk codegen bootstrap](https://github.com/dagger/dagger/pull/13713) — 2 comments · 0 reactions · closed
- **Pull Request** [feat: docker api compatibility](https://github.com/dagger/dagger/pull/13761) — 2 comments · 0 reactions · open
- **Pull Request** [dagger agent dev env: in-repo agent modules](https://github.com/dagger/dagger/pull/13838) — 0 comments · 0 reactions · open
- **Pull Request** [sdk(improvement): support nullable object returns](https://github.com/dagger/dagger/pull/13879) — 0 comments · 0 reactions · open
- **Pull Request** [Add missing view gates](https://github.com/dagger/dagger/pull/13894) — 0 comments · 0 reactions · closed
- **Pull Request** [docs: clarify engine memory pruning configuration](https://github.com/dagger/dagger/pull/13895) — 0 comments · 0 reactions · open
- **Pull Request** [fix: drop ReadHeaderTimeout on HTTP/2 servers](https://github.com/dagger/dagger/pull/13896) — 0 comments · 0 reactions · open

### [uv](https://github.com/astral-sh/uv)

- **Release** [0.12.4](https://github.com/astral-sh/uv/releases/tag/0.12.4) — 
- **Pull Request** [Isolate reproduction publishing credentials from agent execution](https://github.com/astral-sh/uv/pull/21106) — 0 comments · 0 reactions · closed
- **Issue** [`uv run` uses wrong python interpreter inside virtualenv with copied python](https://github.com/astral-sh/uv/issues/21077) — 8 comments · 0 reactions · open
- **Issue** [Relative `tool.uv.sources` paths written as absolute in uv.lock since 0.10.10](https://github.com/astral-sh/uv/issues/20477) — 6 comments · 0 reactions · open
- **Issue** [UV recreates the venv on every run.](https://github.com/astral-sh/uv/issues/21066) — 7 comments · 0 reactions · closed
- **Issue** [Relative indexes in PEP 723 scripts are resolved against the current working directory](https://github.com/astral-sh/uv/issues/21096) — 1 comments · 0 reactions · open
- **Issue** [Dependency Dashboard](https://github.com/astral-sh/uv/issues/2658) — 0 comments · 0 reactions · open
- **Issue** [`uv export --format cyclonedx1.5` omits component hashes that `uv.lock` already carries](https://github.com/astral-sh/uv/issues/21122) — 0 comments · 0 reactions · open
- **Pull Request** [Fix relative indexes in PEP 723 scripts](https://github.com/astral-sh/uv/pull/21097) — 5 comments · 0 reactions · open
- **Pull Request** [move dirhash test_vectors.json generation to uv-dev](https://github.com/astral-sh/uv/pull/21081) — 3 comments · 0 reactions · open
- **Pull Request** [Enable PGO for Linux x86-64 uv releases](https://github.com/astral-sh/uv/pull/21001) — 1 comments · 0 reactions · open
- **Pull Request** [Enable PGO for macOS ARM64 uv releases](https://github.com/astral-sh/uv/pull/21002) — 1 comments · 0 reactions · open
- **Pull Request** [Enable PGO for Windows x86-64 uv releases](https://github.com/astral-sh/uv/pull/21003) — 1 comments · 0 reactions · open
- **Pull Request** [Enable PGO for Linux ARM64 uv releases](https://github.com/astral-sh/uv/pull/21004) — 1 comments · 0 reactions · open
- **Pull Request** [Stabilize publish index readiness checks](https://github.com/astral-sh/uv/pull/21050) — 0 comments · 0 reactions · closed
- **Pull Request** [Heal interpreter metadata cache entries when creating a virtual environment indicates corruption](https://github.com/astral-sh/uv/pull/21073) — 1 comments · 0 reactions · closed
- **Pull Request** [Disable profiling for wall-time CodSpeed benchmarks](https://github.com/astral-sh/uv/pull/21049) — 1 comments · 0 reactions · closed
- **Pull Request** [Use shared helpers for cache filesystem tests](https://github.com/astral-sh/uv/pull/21099) — 0 comments · 0 reactions · closed
- **Pull Request** [improve fix-bug automations PR title/summary](https://github.com/astral-sh/uv/pull/21100) — 0 comments · 0 reactions · closed
- **Pull Request** [Improve regression coverage for related bug manifestations](https://github.com/astral-sh/uv/pull/21101) — 0 comments · 0 reactions · closed
- **Pull Request** [Improve automated fixes for related bug manifestations](https://github.com/astral-sh/uv/pull/21102) — 0 comments · 0 reactions · open
- **Pull Request** [Keep build snapshot filters on test contexts](https://github.com/astral-sh/uv/pull/21103) — 0 comments · 0 reactions · closed
- **Pull Request** [Use test contexts for cache file-count filters](https://github.com/astral-sh/uv/pull/21104) — 0 comments · 0 reactions · closed
- **Pull Request** [Bump version to 0.12.4](https://github.com/astral-sh/uv/pull/21105) — 0 comments · 0 reactions · closed
- **Pull Request** [Keep pip table snapshot filters on test contexts](https://github.com/astral-sh/uv/pull/21107) — 0 comments · 0 reactions · closed
- **Pull Request** [Isolate resource limit integration test commands](https://github.com/astral-sh/uv/pull/21108) — 0 comments · 0 reactions · closed
- **Pull Request** [Remove redundant test context working-directory overrides](https://github.com/astral-sh/uv/pull/21109) — 0 comments · 0 reactions · closed
- **Pull Request** [Use test contexts for tool directories](https://github.com/astral-sh/uv/pull/21110) — 0 comments · 0 reactions · closed
- **Pull Request** [Exercise invalid cache paths in version integration coverage](https://github.com/astral-sh/uv/pull/21111) — 0 comments · 0 reactions · closed
- **Pull Request** [Fix centralized environment cache pruning test coverage](https://github.com/astral-sh/uv/pull/21112) — 0 comments · 0 reactions · closed

### [Testcontainers for Go](https://github.com/testcontainers/testcontainers-go)

No new or materially changed signals.

### [Buf](https://github.com/bufbuild/buf)

No new or materially changed signals.
