# Contribution Compass

[![CI](https://github.com/amk9978/contribution-compass/actions/workflows/ci.yml/badge.svg)](https://github.com/amk9978/contribution-compass/actions/workflows/ci.yml)
[![Pages](https://github.com/amk9978/contribution-compass/actions/workflows/pages.yml/badge.svg)](https://amk9978.github.io/contribution-compass/)
[![Release](https://img.shields.io/github/v/release/amk9978/contribution-compass)](https://github.com/amk9978/contribution-compass/releases)
[![License: MIT](https://img.shields.io/badge/license-MIT-4c9aff.svg)](LICENSE)

**Follow the open-source projects you depend on, and find evidence-backed places to help.**

Contribution Compass collects issues, pull requests, releases, milestones, and matched Hacker News
discussions for a curated set of projects, then publishes them as a website, a versioned JSON
catalog, RSS feeds, and an MCP server.

It runs entirely on GitHub Actions using the built-in token. No server, no account, and no OpenAI,
Anthropic, or other model credential.

[![My Compass showing a personalized contribution table](docs/assets/my-compass.png)](https://amk9978.github.io/contribution-compass/personalize/)

## Start in one of three ways

**Browse — no install, account, or fork.**
Open [My Compass](https://amk9978.github.io/contribution-compass/personalize/), choose your
projects, and bookmark it as a developer start page. Your selection is stored only in
`localStorage` and the page URL.

**Connect an LLM.**
Point any MCP client at the catalog and ask it directly — see [docs/MCP.md](docs/MCP.md). The
versioned JSON catalog and [`llms.txt`](https://amk9978.github.io/contribution-compass/llms.txt)
serve the same data. Prefer either over scraping the HTML.

**Run your own.**

1. [Create a repository from the template](https://github.com/new?template_name=contribution-compass&template_owner=amk9978).
2. Edit `config.yml`, or generate it with `contribution-compass init`.
3. Enable Actions and select **GitHub Actions** as the Pages source.
4. Run the **Contribution Compass** workflow once from the Actions tab.

## How it works

```text
config.yml Project Sensors
        ↓
GitHub issues, pull requests, releases, milestones, and project metadata
        + current Hacker News discussions matched to configured projects
        ↓
normalized Signals + append-only Observation Events
        ↓
folder-separated JSON catalog
        ↓
human pages · JSON/feeds · CLI · MCP
        ↓
optional evidence-citing Inference Extensions
```

Collection, normalization, and interpretation stay separate. GitHub evidence, Hacker News
discussion, repository context, and observation history are labeled distinctly and never merged
into generated prose. Judgement is meant to live above this line, not inside it.

## What it answers

- What important projects changed recently?
- What shipped in their latest stable releases?
- What prereleases or milestones publicly indicate where a project is heading?
- Where are Hacker News readers discussing these projects?
- Which issues explicitly invite community help?
- Which unassigned issues may be worth discussing with maintainers?
- What context surrounds the project and the issue?
- When was a Signal discovered, and what changed afterward?

## Contribution leads

Two kinds, kept deliberately separate:

- **Maintainer-Invited** — an open, unassigned issue labeled `good first issue`, `help wanted`, or
  an equivalent explicit invitation.
- **Triage Lead** — unassigned documentation work, or an engaged bug or enhancement with no explicit
  invitation.

Closed, assigned, stale, duplicate, invalid, blocked, question, needs-info, and needs-reproduction
issues are excluded.

Every lead carries an additive score breakdown. Named Contribution Measures show exactly which
label, activity, engagement, or eligibility fact contributed each point, and `rankScore` is defined
as their sum. The label sets, weights, thresholds, and recency window form a **Contribution Policy**
in `config.yml` — curator-controlled heuristics, not generated judgments. Setting a weight to zero
disables that effect; empty label arrays stay empty.

> A lead is not a guarantee of difficulty, availability, or acceptance. Triage Leads in particular
> are engagement heuristics: a busy issue on a large consumer-facing tracker can rank highly without
> being contributable at all. Check the live issue, confirm the repository accepts external pull
> requests, and talk to maintainers before substantial work.

## Evidence and history

Each repository dataset contains:

- Project Context — description, topics, language, license, default branch, stars, forks, activity
- normalized issue, pull-request, and release Signals
- direct URLs to the original GitHub evidence
- append-only Observation Events with discovered/changed snapshots and changed fields
- collection-run metadata
- a Project News Snapshot with the latest stable release and publicly visible upcoming items
- current matched Hacker News stories with article and discussion URLs, score, comments, match reason

Hacker News is shown as community discussion, never as maintainer evidence. The collector uses the
official `topstories` and `beststories` lists, applies the configured lookback and item cap, and
does not crawl the full comment tree.

```text
data/
  2026-08-13/
    manifest.json
    distributed-systems/
      foundationdb.json
      tigerbeetle.json
```

Data stays separated by date, group, and repository. Empty configuration groups stay empty; the
loader never inserts hidden defaults.

## Access

| | |
|---|---|
| Website | <https://amk9978.github.io/contribution-compass/> |
| My Compass | <https://amk9978.github.io/contribution-compass/personalize/> |
| Contribute | <https://amk9978.github.io/contribution-compass/contribute/> |
| Project news | <https://amk9978.github.io/contribution-compass/news/> |
| MCP | [docs/MCP.md](docs/MCP.md) |
| LLM guide | <https://amk9978.github.io/contribution-compass/llms.txt> |
| Catalog | <https://amk9978.github.io/contribution-compass/api/v1/index.json> |
| Contribution leads | <https://amk9978.github.io/contribution-compass/api/v1/opportunities.json> |
| Project news API | <https://amk9978.github.io/contribution-compass/api/v1/news.json> |
| RSS · JSON Feed | [feed.xml](https://amk9978.github.io/contribution-compass/feed.xml) · [feed.json](https://amk9978.github.io/contribution-compass/feed.json) |
| News RSS · JSON Feed | [news/feed.xml](https://amk9978.github.io/contribution-compass/news/feed.xml) · [news/feed.json](https://amk9978.github.io/contribution-compass/news/feed.json) |

Human pages use static pagination: 20 contribution leads, 10 project-news cards, or 50 project
Signals per page. JSON, RSS, MCP, and direct GitHub/HN links remain available for deeper reading.

## Configure

### Generate `config.yml`

Rather than editing YAML by hand:

```bash
uv sync --all-extras

# Explicit repositories
uv run contribution-compass init --repo apple/foundationdb --repo temporalio/temporal --force

# Repositories behind direct dependencies in a supported manifest
uv run contribution-compass init --from-file go.mod --force
uv run contribution-compass init --from-file package.json --force
uv run contribution-compass init --from-file requirements.txt --force

# Your GitHub stars
export GITHUB_TOKEN="$(gh auth token)"
uv run contribution-compass init --from-starred --starred-limit 100 --force
```

`init` resolves npm and PyPI packages through public registry metadata, recognizes GitHub-backed Go
modules and direct Git dependencies, and reports anything it cannot map unambiguously. It never
guesses a repository silently. Review the generated YAML before the first collection.

### Edit `config.yml`

```yaml
lookback_hours: 24

hackernews:
  enabled: true
  story_limit: 200

contributions:
  invitation_labels: [good first issue, help wanted]
  beginner_labels: [good first issue]
  excluded_labels: [blocked, duplicate, stale]
  weights:
    maintainer_invitation: 60
    recent_activity: 5
  thresholds:
    recent_days: 14

catalog_overlays: []

repo_groups:
  compilers:
    name: Compiler Engineering
    repos:
      - id: llvm
        repo: llvm/llvm-project
        name: LLVM
        paginated: true
        keywords: [LLVM, compiler infrastructure]
```

Each repository ID must be globally unique. `repos: []` and `keywords: []` mean empty.

Keywords are persisted with repository data and participate in update, opportunity, and news
searches. They are also matched against Hacker News story titles, so choose specific phrases to
avoid ambiguity — exact references to the configured GitHub repository are matched independently.
Set `hackernews.enabled: false` to disable that source while keeping keyword search metadata.

The checked-in `config.yml` shows the complete default Contribution Policy.

### Reuse the public catalog

A fork can avoid recollecting overlapping repositories:

```yaml
catalog_overlays:
  - id: community
    url: https://amk9978.github.io/contribution-compass
    max_age_hours: 48
```

Your `repo_groups` stay authoritative — an overlay cannot introduce unconfigured projects. Fresh
matching snapshots are reused and only the remaining delta is collected. Equally current local data
wins. Stale, incompatible, or unavailable overlays fall back to direct GitHub collection. JSON and
MCP expose Catalog Provenance; checked-in Markdown reports cover the locally collected delta.

## Running it yourself

The scheduled `Contribution Compass` workflow uses the built-in `GITHUB_TOKEN`, collects from GitHub
and the keyless official Hacker News interface, and commits `data/`, `reports/`, and `.state/`. The
Pages workflow publishes every human and machine view after a successful collection. No extra secret
is required.

After creating a repository from the template:

1. Settings → Actions → General: ensure Actions are enabled. Read/write default permission is
   convenient; the collection workflow also requests `contents: write` explicitly.
2. Settings → Pages: select **GitHub Actions** as the source.
3. Generate or edit `config.yml`.
4. Run `uv run contribution-compass doctor --repository owner/repository`.
5. Run the `Contribution Compass` workflow manually once.

GitHub templates copy files and branches, not every repository setting, so the first two checks
cannot be safely assumed. `doctor` verifies local workflow contents and, when the token has suitable
read permissions, inspects the live Actions and Pages settings without changing them.

URLs derive from the repository owner and name. Set the optional `SITE_URL` Actions variable only
for a custom domain.

## Local use

Requires Python 3.12+ and [uv](https://docs.astral.sh/uv/).

```bash
uv sync --all-extras
export GITHUB_TOKEN="$(gh auth token)"
uv run contribution-compass collect
uv run contribution-compass site
uv run contribution-compass doctor --repository owner/repository
```

Query without MCP:

```bash
uv run contribution-compass query opportunities --limit 10
uv run contribution-compass query news --query performance
uv run contribution-compass query updates --query cancellation
uv run contribution-compass query timeline 'github:owner/repo:issue:123'
```

Verify:

```bash
uv run ruff check .
uv run ruff format --check .
uv run mypy src
uv run pytest
uv run contribution-compass site
```

Tests use fixtures and mocks; they make no live GitHub requests.

## Architecture

The Python core uses explicit module seams while avoiding pass-through abstraction:

```text
src/contribution_compass/
  domain/          models, invariants, importance, contribution rules
  application/     collection, catalog-query, and setup use cases
  ports.py         small interfaces implemented by real adapters
  adapters/        GitHub, local/hosted/overlay catalogs, state, persistence
  controllers/     CLI and MCP transports
  views/           Markdown, HTML, JSON, RSS, and LLM navigation
web/assets/        progressive browser CSS/JavaScript only
```

Domain modules know nothing about GitHub HTTP, files, HTML, or MCP. Controllers configure adapters
and invoke application modules. Local and hosted catalogs implement the same read interface. Views
render application results but do not classify opportunities.

See [CONTEXT.md](CONTEXT.md) for domain language and [docs/adr](docs/adr) for architectural
decisions.

## Inference extensions

The catalog and MCP interface are the intended seam for LLM-backed inference. An extension should
write to a separate namespace, record its method, model, and run, distinguish inference from direct
evidence, and cite immutable Signal or Observation Event IDs. It must not overwrite evidence.

## Contributing

Contributions are welcome. Start with
[`good first issue`](https://github.com/amk9978/contribution-compass/labels/good%20first%20issue) or
[`help wanted`](https://github.com/amk9978/contribution-compass/labels/help%20wanted), then read
[CONTRIBUTING.md](CONTRIBUTING.md). Usage questions belong in
[Discussions](https://github.com/amk9978/contribution-compass/discussions); vulnerabilities should
follow [SECURITY.md](SECURITY.md).

## License and attribution

MIT — see [LICENSE](LICENSE). Implementation patterns were selectively adapted from the MIT-licensed
[agents-radar](https://github.com/duanyytop/agents-radar); see [NOTICE.md](NOTICE.md), and
[docs/COMPARISON.md](docs/COMPARISON.md) for how the two projects differ.
