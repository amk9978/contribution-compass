# Contribution Compass

Contribution Compass keeps developers current on important activity in curated open-source projects
and finds evidence-backed sweet spots where a contribution may be useful.

It is a data gatherer first. GitHub evidence, separately labeled Hacker News discussions,
repository context, and observation history stay separate from interpretation. No OpenAI,
Anthropic, or other model credential is required.

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

## Why it exists

A list of repository activity is not enough. Contribution Compass helps answer:

- What important projects changed recently?
- What major developments shipped in their latest stable releases?
- What prereleases or milestones publicly indicate where a project is heading?
- Where are Hacker News readers discussing these configured projects?
- Which issues explicitly invite community help?
- Which unassigned issues may be worth discussing with maintainers?
- What context surrounds the project and issue?
- When was a Signal discovered, and what changed afterward?

Contribution Leads are conservative and transparent:

- **Maintainer-Invited:** an open, unassigned issue labeled `good first issue`, `help wanted`, or an
  equivalent explicit invitation.
- **Triage Lead:** unassigned documentation work or an engaged bug/enhancement without explicit
  maintainer invitation.

Closed, assigned, stale, duplicate, invalid, blocked, question, needs-info, and needs-reproduction
issues are excluded. A lead is not a guarantee of difficulty or acceptance; check the live issue and
talk to maintainers before substantial work.

## Evidence and history

Each repository dataset contains:

- Project Context: description, topics, language, license, default branch, stars, forks, and activity;
- normalized issue, pull-request, and release Signals;
- direct URLs to original GitHub evidence;
- append-only Observation Events containing discovered/changed snapshots and changed fields;
- collection-run metadata;
- a Project News Snapshot with its latest stable release and publicly visible upcoming items; and
- current matched Hacker News stories with article and discussion URLs, score, comments, and match
  reason.

Hacker News is shown as community discussion, never as maintainer evidence. The collector uses the
official `topstories` and `beststories` lists, applies the configured lookback and item cap, and does
not crawl the full comment tree.

```text
data/
  2026-08-13/
    manifest.json
    distributed-systems/
      foundationdb.json
      tigerbeetle.json
```

Data remains separated by date, group, and repository. Empty configuration groups stay empty; the
loader never inserts hidden defaults.

## Human and machine access

- Website: <https://amk9978.github.io/contribution-compass/>
- Contribution view: <https://amk9978.github.io/contribution-compass/contribute/>
- Project news: <https://amk9978.github.io/contribution-compass/news/>
- Machine catalog: <https://amk9978.github.io/contribution-compass/api/v1/index.json>
- Project news API: <https://amk9978.github.io/contribution-compass/api/v1/news.json>
- Project news JSON Feed: <https://amk9978.github.io/contribution-compass/news/feed.json>
- Project news RSS: <https://amk9978.github.io/contribution-compass/news/feed.xml>
- Contribution leads: <https://amk9978.github.io/contribution-compass/api/v1/opportunities.json>
- JSON Feed: <https://amk9978.github.io/contribution-compass/feed.json>
- RSS: <https://amk9978.github.io/contribution-compass/feed.xml>
- LLM guide: <https://amk9978.github.io/contribution-compass/llms.txt>
- MCP setup: [docs/MCP.md](docs/MCP.md)

LLM-backed tools should use MCP or the versioned JSON catalog instead of scraping visual HTML.

## Architecture

The Python core uses explicit module seams while avoiding pass-through abstraction:

```text
src/contribution_compass/
  domain/          models, invariants, importance, contribution rules
  application/     collection and catalog use cases
  ports.py         small interfaces implemented by real adapters
  adapters/        GitHub, local JSON, hosted JSON, state, persistence
  controllers/     CLI and MCP transports
  views/           Markdown, HTML, JSON, RSS, and LLM navigation
web/assets/        progressive browser CSS/JavaScript only
```

Domain modules know nothing about GitHub HTTP, files, HTML, or MCP. Controllers configure adapters
and invoke application modules. Local and hosted catalogs implement the same read interface. Views
render application results but do not classify opportunities.

See [CONTEXT.md](CONTEXT.md) for domain language and [docs/adr](docs/adr) for architectural decisions.

## Configure a fork

Edit `config.yml` with arbitrary project groups:

```yaml
lookback_hours: 24

hackernews:
  enabled: true
  story_limit: 200

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

Each repository ID must be globally unique. `repos: []` and `keywords: []` mean empty. Keywords are
persisted with repository data and participate in update, opportunity, and news searches. They are
also matched against Hacker News story titles, so choose specific phrases to avoid ambiguity. Exact
references to the configured GitHub repository are matched independently. Set
`hackernews.enabled: false` to disable that source while retaining keyword search metadata.

Human pages use static pagination: 20 contribution leads, 10 project-news cards, or 50 project
Signals per page. JSON, RSS, MCP, and direct GitHub/HN links remain available for deeper reading.

## Local use

Requirements: Python 3.12+ and [uv](https://docs.astral.sh/uv/).

```bash
uv sync --all-extras
export GITHUB_TOKEN="$(gh auth token)"
uv run contribution-compass collect
uv run contribution-compass site
```

Query without MCP:

```bash
uv run contribution-compass query opportunities --limit 10
uv run contribution-compass query news --query performance
uv run contribution-compass query updates --query cancellation
uv run contribution-compass query timeline 'github:owner/repo:issue:123'
```

Verification:

```bash
uv run ruff check .
uv run ruff format --check .
uv run mypy src
uv run pytest
uv run contribution-compass site
```

Tests use fixtures and mocks; they make no live GitHub requests.

## GitHub Actions

The scheduled `Contribution Compass` workflow uses GitHub's built-in `GITHUB_TOKEN`, collects data
from GitHub and the keyless official Hacker News interface, and commits `data/`, `reports/`, and
`.state/`. The Pages workflow publishes all human and machine
views after a successful collection. No extra secret is required.

For a fork:

1. Enable **Read and write permissions** in Settings → Actions → General.
2. Select **GitHub Actions** as the Pages source in Settings → Pages.
3. Edit `config.yml`.
4. Run the `Contribution Compass` workflow manually once.

URLs derive from the fork owner and repository name. Set the optional `SITE_URL` Actions variable
only for a custom domain.

## Optional inference extensions

The catalog and MCP interface are the intended seam for future LLM-backed inference. An extension
should write to a separate namespace, record its method/model/run, distinguish inference from direct
evidence, and cite immutable Signal or Observation Event IDs. It must not overwrite evidence.

## Difference from agents-radar

See [docs/COMPARISON.md](docs/COMPARISON.md) for the concise comparison. In short, agents-radar is a
broad AI-news digest with LLM synthesis; Contribution Compass is a Python, domain-agnostic evidence
catalog centered on contribution discovery, project context, and event trails.

## Attribution

Implementation patterns were selectively adapted from the MIT-licensed
[agents-radar](https://github.com/duanyytop/agents-radar). See [NOTICE.md](NOTICE.md) and
[LICENSE](LICENSE).
