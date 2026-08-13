# Engineering Radar

Engineering Radar is a scheduled, evidence-first contribution radar for a curated set of GitHub
repositories. It is designed primarily for machine readers and LLM-backed developer tools, while
remaining useful to humans looking for a concrete place to contribute.

It performs no LLM analysis, clustering, synthesis, or speculative opportunity generation. Its job is to gather
recent issues, pull requests, and releases, detect new or changed observations, and commit durable
data that another project can analyze later. A deterministic contribution classifier surfaces
maintainer-invited and lower-confidence triage leads without pretending to understand maintainer
intent.

```text
config.yml
    ↓
GitHub REST API
    ↓
normalized, deduplicated signals
    ↓
data/YYYY-MM-DD/<group>/<repository>.json
reports/YYYY-MM-DD/<group>.md
    ↓
static date/group/repository pages + RSS
    ↓
versioned JSON API + contribution leads + LLM guide
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
- open/closed state and current assignees;
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

## Static site and RSS

GitHub Pages publishes a visual explorer at
[amk9978.github.io/engineering-radar](https://amk9978.github.io/engineering-radar/). It is generated
entirely from the checked-in `data/` folders and provides:

- an activity overview for the newest collection;
- an evidence-backed contribution radar;
- an archive page for each date;
- a separate page for every group;
- a searchable, filterable page for every repository;
- direct links from every displayed item to its original GitHub evidence;
- light and dark themes;
- an [RSS 2.0 feed](https://amk9978.github.io/engineering-radar/feed.xml) containing the 100 most
  recent signals;
- a [JSON Feed](https://amk9978.github.io/engineering-radar/feed.json), versioned
  [machine API](https://amk9978.github.io/engineering-radar/api/v1/index.json), and
  [`llms.txt`](https://amk9978.github.io/engineering-radar/llms.txt).

This display layer does not perform semantic analysis or make cross-project claims. Its contribution
ranking is a transparent rules-based index over collected evidence. The generated `.site/` directory
is a build artifact and is not committed. Build it locally with:

```bash
pnpm site:build
```

For local browsing, serve `.site/` with any static file server. To override links for a custom Pages
domain, set `SITE_URL` before building.

## Contribution radar

The contribution view does not ask a model to brainstorm work. It deterministically evaluates the
latest normalized issues:

- **Maintainer-invited:** open, unassigned issues explicitly labeled `good first issue`,
  `help wanted`, `up for grabs`, or an equivalent invitation.
- **Triage lead:** open, unassigned documentation work or an engaged bug/enhancement without an
  explicit invitation.
- **Excluded:** closed, assigned, stale, duplicate, invalid, blocked, question, needs-info, and
  needs-reproduction issues.

Every lead contains its reasons, caveat, current collected state, and original evidence URL. A lead
is never a guarantee of difficulty, availability, suitability, or maintainer acceptance. Developers
and agents should check the live issue and communicate with maintainers before doing substantial
work.

## Machine and LLM access

Bots should start at `api/v1/index.json` or `llms.txt` rather than scraping visual HTML. The API is
folder-separated like the underlying storage:

```text
api/v1/index.json
api/v1/opportunities.json
api/v1/schema.json
api/v1/dates/<date>/index.json
api/v1/dates/<date>/groups/<group>/index.json
api/v1/dates/<date>/groups/<group>/repositories/<repository>.json
```

`api/v1/opportunities.json` documents the ranking method and distinguishes explicit maintainer
invitations from weaker triage leads. `feed.json` follows JSON Feed 1.1. `llms-full.txt` provides a
compact Markdown snapshot with direct links; it is navigation context, not synthesized analysis.

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
pnpm site:build
```

Tests use mocked API responses and do not depend on live GitHub calls.

## GitHub Actions

The workflow in `.github/workflows/radar.yml` runs daily and supports `workflow_dispatch`. It uses
GitHub Actions' built-in `GITHUB_TOKEN`, runs the collector, and commits `data/`, `reports/`, and
`.state/` back to the current repository. The separate `.github/workflows/pages.yml` workflow builds
and deploys the website and RSS after a successful radar run or a relevant push.

After pushing the project, enable Actions read/write permissions under:

```text
Repository Settings → Actions → General → Workflow permissions → Read and write permissions
```

Enable GitHub Pages with **GitHub Actions** as its source under:

```text
Repository Settings → Pages → Build and deployment → Source → GitHub Actions
```

Then trigger the first scan:

```bash
gh workflow run radar.yml
gh run watch
```

No additional Actions secrets or variables are required. The site URL is calculated from the fork's
owner and repository name, so changing `config.yml` and enabling the two workflows is sufficient for
a fork. If you use a custom domain, create an Actions variable named `SITE_URL` with its full origin.

## Consuming the data elsewhere

A separate analysis project should walk each date's `manifest.json` and read the referenced
repository files, using `Signal.id` for identity and `Signal.url` for primary evidence. The collector
deliberately does not make cross-project claims or transform observations into hypotheses.

See [examples/example-daily.md](examples/example-daily.md) for the human-readable format and
`src/signals/types.ts` for the data contract.

## Architecture

```text
src/config       YAML loading and strict validation
src/contributions deterministic, evidence-based contribution lead classification
src/sources      GitHub REST collection and bounded pagination
src/signals      normalized signal types and GitHub mapping
src/storage      fingerprints and daily JSON persistence
src/reports      deterministic Markdown update log
src/site         static HTML, split JSON API, feeds, LLM indexes, and sitemap generation
src/index.ts     collection orchestration
src/__tests__    mocked unit tests
```

## Attribution

Bounded GitHub pagination and workflow patterns were adapted from the MIT-licensed
[agents-radar](https://github.com/duanyytop/agents-radar). See [NOTICE.md](NOTICE.md) and
[LICENSE](LICENSE).
