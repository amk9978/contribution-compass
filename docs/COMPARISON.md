# Contribution Compass vs. agents-radar

`agents-radar` inspired the original collector. Contribution Compass selectively retains useful
pagination, workflow, static browsing, and feed patterns, but serves a different mission.

| Dimension | Contribution Compass | agents-radar |
|---|---|---|
| Primary purpose | Important curated-project updates plus evidence-backed contribution discovery | Bilingual AI ecosystem news and synthesized daily digests |
| Domain | Arbitrary repository groups | AI tools, OpenClaw peers, skills, AI infrastructure, and AI news |
| Core language | Python | TypeScript, plus a separate TypeScript Cloudflare MCP worker |
| LLM dependency | None; inference is an optional extension | Providers and prompts are central to digest generation |
| Evidence model | Normalized Signals, Project Context, and append-only Observation Events | Generated Markdown reports and daily highlight artifacts |
| Contribution discovery | Configurable, additive Contribution Measures; explicit Maintainer-Invited vs. lower-confidence Triage Leads | Not the central data model |
| Project news | Stable releases, public prereleases/milestones, and separately labeled matching HN discussions | Broader editorial/news-source digest |
| Configuration | Arbitrary groups; empty means empty; no hidden defaults | Specialized categories and documented fallback defaults |
| MCP | Reads local or hosted structured evidence; includes context and timelines | Hosted report listing, retrieval, and text search |
| Personalization | Static browser-local profiles plus fork/template configuration and shared catalog overlays | Report-level browsing and filtering |
| Breadth | Configured GitHub projects plus matching Hacker News discussions | Ten broad AI/news sources |
| Inference separation | Future inference must cite evidence and live in a separate namespace | Collection and LLM synthesis share the digest pipeline |

See `NOTICE.md` for MIT attribution and the upstream copyright notice.
