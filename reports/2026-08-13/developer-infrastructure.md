# Developer Infrastructure — 2026-08-13

> Factual GitHub evidence collected by Contribution Compass. No LLM analysis is performed.

## Contribution Leads

### [Add environment variable to always use `--active` flag](https://github.com/astral-sh/uv/issues/11273)

- Project: `astral-sh/uv`
- Tier: `triage-lead`
- Evidence: Unassigned enhancement with community reactions
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

## Important Updates

### [Dagger](https://github.com/dagger/dagger)

- **Issue** [Python SDK ready for 1.0](https://github.com/dagger/dagger/issues/13626) — 2 comments · 1 reactions · open
- **Issue** [Typescript SDK ready for 1.0](https://github.com/dagger/dagger/issues/13627) — 2 comments · 0 reactions · open
- **Issue** [Go SDK is ready for 1.0](https://github.com/dagger/dagger/issues/13628) — 3 comments · 0 reactions · open
- **Issue** [Dang SDK is ready for 1.0](https://github.com/dagger/dagger/issues/13629) — 2 comments · 0 reactions · open
- **Issue** [Elixir SDK is ready for 1.0](https://github.com/dagger/dagger/issues/13867) — 2 comments · 0 reactions · open
- **Issue** [Java SDK is ready for 1.0](https://github.com/dagger/dagger/issues/13630) — 1 comments · 0 reactions · open
- **Issue** [PHP SDK is ready for 1.0](https://github.com/dagger/dagger/issues/13631) — 1 comments · 0 reactions · open
- **Issue** [v0.x modules are given a v1.0 view](https://github.com/dagger/dagger/issues/13883) — 1 comments · 0 reactions · open
- **Issue** [🐞 dagger module init fails "outside changeset root" when dagger.toml is in a subdirectory (monorepo layout)](https://github.com/dagger/dagger/issues/13889) — 0 comments · 0 reactions · open
- **Pull Request** [feat(schema): require declared Workspace! args on module functions](https://github.com/dagger/dagger/pull/13850) — 1 comments · 0 reactions · open
- **Pull Request** [feat: add experimental detachable sessions with source callback lifecycle](https://github.com/dagger/dagger/pull/13851) — 0 comments · 0 reactions · open
- **Pull Request** [workspace: add native polyfill replacements](https://github.com/dagger/dagger/pull/13854) — 0 comments · 0 reactions · open
- **Pull Request** [workspace: make changes cwd-relative and isolate SDK generation](https://github.com/dagger/dagger/pull/13855) — 0 comments · 0 reactions · open
- **Pull Request** [\[backport-0.21\] fix(engine): decouple active-clients API from session lifecycle locks](https://github.com/dagger/dagger/pull/13865) — 0 comments · 0 reactions · open
- **Pull Request** [fix(elixir): update vulnerable runtime dependencies](https://github.com/dagger/dagger/pull/13872) — 0 comments · 0 reactions · open
- **Pull Request** [feat(workspace): import another workspace's dagger.toml](https://github.com/dagger/dagger/pull/13882) — 0 comments · 0 reactions · open
- **Pull Request** [\[backport-0.21\] fix(engine): take session teardown off the client shutdown path](https://github.com/dagger/dagger/pull/13884) — 0 comments · 0 reactions · closed
- **Pull Request** [\[backport-0.21\] fix: hide registry HTTP probe errors](https://github.com/dagger/dagger/pull/13885) — 0 comments · 0 reactions · closed
- **Pull Request** [\[backport-0.21\] engine: prune DAGQL cache by metadata size](https://github.com/dagger/dagger/pull/13886) — 0 comments · 0 reactions · closed
- **Pull Request** [engine: support manual metadata pruning](https://github.com/dagger/dagger/pull/13887) — 0 comments · 0 reactions · open
- **Pull Request** [dagql: reduce e-graph result-removal contention](https://github.com/dagger/dagger/pull/13888) — 0 comments · 0 reactions · open

### [uv](https://github.com/astral-sh/uv)

- **Issue** [Add environment variable to always use `--active` flag](https://github.com/astral-sh/uv/issues/11273) — 16 comments · 26 reactions · open
- **Issue** [Allow additional data to be incuded in the user-agent similar to PIP_USER_AGENT_USER_DATA](https://github.com/astral-sh/uv/issues/17839) — 5 comments · 5 reactions · open
- **Pull Request** [Content-address wheel archives with directory hashes](https://github.com/astral-sh/uv/pull/19693) — 6 comments · 0 reactions · open
- **Issue** [--find-links with a relative path in a requirements file fails with "relative URL without a base" (regression since 0.12.x)](https://github.com/astral-sh/uv/issues/21016) — 7 comments · 1 reactions · open
- **Issue** [PEP 723 inline metadata tag not found when there's trailing whitespace](https://github.com/astral-sh/uv/issues/10918) — 9 comments · 0 reactions · closed
- **Issue** [UV recreates the venv on every run.](https://github.com/astral-sh/uv/issues/21066) — 7 comments · 0 reactions · open
- **Issue** [uv-build: suppress "missing upper bound" warning via env var](https://github.com/astral-sh/uv/issues/21074) — 6 comments · 0 reactions · open
- **Issue** [No migration path for native-tls -> system-certs with pinned environments](https://github.com/astral-sh/uv/issues/21035) — 4 comments · 0 reactions · open
- **Issue** [pip-style extra index url retry limit](https://github.com/astral-sh/uv/issues/21037) — 5 comments · 0 reactions · open
- **Issue** [uv tree --group specific_group | not showing only specific_group](https://github.com/astral-sh/uv/issues/21064) — 4 comments · 0 reactions · closed
- **Issue** [`uv run` uses wrong python interpreter inside virtualenv with copied python](https://github.com/astral-sh/uv/issues/21077) — 5 comments · 0 reactions · open
- **Issue** [Relative `tool.uv.sources` paths written as absolute in uv.lock since 0.10.10](https://github.com/astral-sh/uv/issues/20477) — 6 comments · 0 reactions · closed
- **Issue** [uv run resolves a console-script to a different, already-deleted project's stale cached venv](https://github.com/astral-sh/uv/issues/21062) — 2 comments · 0 reactions · open
- **Issue** [`uv lock` errors if `.venv` is not valid](https://github.com/astral-sh/uv/issues/19832) — 1 comments · 0 reactions · closed
- **Issue** [Dependency Dashboard](https://github.com/astral-sh/uv/issues/2658) — 0 comments · 0 reactions · open
- **Pull Request** [Support referencing indexes by name via `--index` and `--default-index`](https://github.com/astral-sh/uv/pull/17455) — 11 comments · 0 reactions · open
- **Pull Request** [Remove lib64-lib symlink in virtualenv](https://github.com/astral-sh/uv/pull/21015) — 6 comments · 0 reactions · open
- **Issue** [uv check --no-install-project](https://github.com/astral-sh/uv/issues/21083) — 1 comments · 0 reactions · open
- **Pull Request** [Add code coverage + HTML report machinery](https://github.com/astral-sh/uv/pull/19692) — 5 comments · 0 reactions · open
- **Pull Request** [Give a specific error when a PEP 723 closing tag has trailing whitespace](https://github.com/astral-sh/uv/pull/20944) — 5 comments · 0 reactions · closed
- **Pull Request** [Allow locking with an invalid project environment](https://github.com/astral-sh/uv/pull/21068) — 4 comments · 0 reactions · closed
- **Pull Request** [Deduplicate binary payloads with archive manifests](https://github.com/astral-sh/uv/pull/19694) — 2 comments · 0 reactions · open
- **Pull Request** [Fix lookahead for transitive extras on path dependencies](https://github.com/astral-sh/uv/pull/20736) — 3 comments · 0 reactions · closed
- **Pull Request** [Reject conflicts between packages and their own extras](https://github.com/astral-sh/uv/pull/21038) — 2 comments · 0 reactions · open
- **Pull Request** [move dirhash test_vectors.json generation to uv-dev](https://github.com/astral-sh/uv/pull/21081) — 2 comments · 0 reactions · open
- **Pull Request** [Update Rust crate async-trait to v0.1.91](https://github.com/astral-sh/uv/pull/20703) — 1 comments · 0 reactions · closed
- **Pull Request** [Update actions/setup-python action to v7](https://github.com/astral-sh/uv/pull/20874) — 0 comments · 0 reactions · closed
- **Pull Request** [Enable PGO for Linux x86-64 uv releases](https://github.com/astral-sh/uv/pull/21001) — 1 comments · 0 reactions · open
- **Pull Request** [Enable PGO for macOS ARM64 uv releases](https://github.com/astral-sh/uv/pull/21002) — 1 comments · 0 reactions · open
- **Pull Request** [Enable PGO for Windows x86-64 uv releases](https://github.com/astral-sh/uv/pull/21003) — 1 comments · 0 reactions · open

### [Testcontainers for Go](https://github.com/testcontainers/testcontainers-go)

- **Issue** [\[Feature\]: Honor DOCKER_HOST scheme when launching Ryuk (TCP/TLS daemon support)](https://github.com/testcontainers/testcontainers-go/issues/3662) — 2 comments · 0 reactions · open

### [Buf](https://github.com/bufbuild/buf)

No new or materially changed signals.
