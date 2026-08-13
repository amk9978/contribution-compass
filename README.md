# Engineering Radar

Engineering Radar is a small scheduled collector for a curated set of GitHub repositories.

It performs no LLM analysis, clustering, synthesis, or opportunity generation. Its job is to gather
recent issues, pull requests, and releases, detect new or changed observations, and commit durable
data that another project can analyze later.

```text
config.yml
    ↓
GitHub REST API
    ↓
normalized, deduplicated signals
    ↓
data/YYYY-MM-DD/<group>/<repository>.json
reports/YYYY-MM-DD/<group>.md
```

## What it collects

For each repository configured in `config.yml`:

- issues;
- pull requests;
- releases;
- titles and bodies;
- timestamps;
- comments and reactions;
- labels and authors;
- direct URLs to the original GitHub evidence.

GitHub's Issues API includes pull requests, so the collector checks the `pull_request` marker and
classifies each observation exactly once. High-volume repositories can opt into bounded pagination.
A failure in one repository is logged and does not stop the remaining repositories.

## Outputs

The primary interface for downstream analysis is separated by date, group, and repository:

```text
data/
  2026-08-13/
    manifest.json
    distributed-systems/
      foundationdb.json
      tigerbeetle.json
    observability/
      prometheus.json
```

Each repository JSON file contains:

- collection-run metadata;
- normalized signals marked as `new` or `updated`;
- stable IDs and original evidence URLs;
- that repository's same-day updates, retained across repeated workflow runs.

The manifest contains only run counts and paths; it does not merge repository updates. Human-readable
logs follow the same date separation, with `reports/YYYY-MM-DD/summary.md` linking to one Markdown
file per configured group. They contain no generated interpretation.

`.state/github.json` contains fingerprints used to avoid emitting unchanged observations again.
The scheduled workflow commits all three locations.

## Configuration

Repository groups are arbitrary and data-driven:

```yaml
lookback_hours: 24

repo_groups:
  compilers:
    name: Compiler Engineering
    repos:
      - id: llvm
        repo: llvm/llvm-project
        name: LLVM
        paginated: true
```

Each repository needs a globally unique `id`, a GitHub `owner/repository` slug, and a display
`name`. An empty `repos: []` stays empty; no defaults or hidden repositories are restored. Set
`RADAR_CONFIG` to use a different configuration file.

The checked-in configuration contains the requested distributed systems, platform, observability,
data infrastructure, AI infrastructure, developer infrastructure, and small coding-agent
infrastructure groups.

## Local setup

Requirements: Node.js 22+ and pnpm.

```bash
pnpm install
export GITHUB_TOKEN="$(gh auth token)"
pnpm start
```

No OpenAI, Anthropic, or other model credentials are used.

Run the verification suite with:

```bash
pnpm lint
pnpm format:check
pnpm typecheck
pnpm test
```

Tests use mocked API responses and do not depend on live GitHub calls.

## GitHub Actions

The workflow in `.github/workflows/radar.yml` runs daily and supports `workflow_dispatch`. It uses
GitHub Actions' built-in `GITHUB_TOKEN`, runs the collector, and commits `data/`, `reports/`, and
`.state/` back to the current repository.

After pushing the project, enable Actions read/write permissions under:

```text
Repository Settings → Actions → General → Workflow permissions → Read and write permissions
```

Then trigger the first scan:

```bash
gh workflow run radar.yml
gh run watch
```

No additional Actions secrets or variables are required.

## Consuming the data elsewhere

A separate analysis project should walk each date's `manifest.json` and read the referenced
repository files, using `Signal.id` for identity and `Signal.url` for primary evidence. The collector
deliberately does not make cross-project claims or transform observations into hypotheses.

See [examples/example-daily.md](examples/example-daily.md) for the human-readable format and
`src/signals/types.ts` for the data contract.

## Architecture

```text
src/config       YAML loading and strict validation
src/sources      GitHub REST collection and bounded pagination
src/signals      normalized signal types and GitHub mapping
src/storage      fingerprints and daily JSON persistence
src/reports      deterministic Markdown update log
src/index.ts     collection orchestration
src/__tests__    mocked unit tests
```

## Attribution

Bounded GitHub pagination and workflow patterns were adapted from the MIT-licensed
[agents-radar](https://github.com/duanyytop/agents-radar). See [NOTICE.md](NOTICE.md) and
[LICENSE](LICENSE).
