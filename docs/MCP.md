# MCP access

Contribution Compass exposes the same read-only catalog used by its CLI and static site through the
official Python MCP SDK. The MCP adapter performs no inference and never writes to GitHub.

## Tools

| Tool | Purpose |
|---|---|
| `search_project_updates` | Search and rank factual issues, pull requests, and releases |
| `find_contribution_opportunities` | Find open, unassigned leads with reasons and caveats |
| `get_project_news` | Read releases, public upcoming work, and separately labeled HN discussions |
| `get_project_context` | Read repository metadata, Signals, and Observation Events |
| `get_signal_timeline` | Reconstruct the discovered/changed trail for a stable Signal ID |
| `list_monitored_projects` | List Project Sensors and available context |

Resources provide the catalog, latest contribution leads, latest project news, Hacker News
discussion links, and per-project context under `compass://...` URIs.

Configured project `keywords` are persisted as project metadata, returned by project-list/context
tools, and included when searching updates, contribution leads, or project news.

## Choose a data adapter

By default, the server reads the clone's local `data/` directory. To use the continuously updated
GitHub Pages catalog instead, set:

```bash
COMPASS_DATA_URL=https://amk9978.github.io/contribution-compass
```

The local and hosted adapters implement the same catalog interface.

## Verify with MCP Inspector

From the repository root:

```bash
uv sync --all-extras
uv run mcp dev src/contribution_compass/controllers/mcp.py:mcp
```

## Claude Code

Replace `/absolute/path/to/contribution-compass` with the clone's absolute path:

```bash
claude mcp add contribution-compass \
  -e COMPASS_DATA_URL=https://amk9978.github.io/contribution-compass \
  -- uv run --directory /absolute/path/to/contribution-compass contribution-compass-mcp
```

Run `/mcp` inside Claude Code to verify the tools and resources.

## Codex

```bash
codex mcp add contribution-compass \
  --env COMPASS_DATA_URL=https://amk9978.github.io/contribution-compass \
  -- uv run --directory /absolute/path/to/contribution-compass contribution-compass-mcp
```

Verify with:

```bash
codex mcp get contribution-compass
```

Both clients launch the server over stdio. Logging goes to stderr because stdout belongs to the MCP
protocol.
