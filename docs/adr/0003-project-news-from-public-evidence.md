# ADR-0003: Project news distinguishes maintainer evidence from community discussion

Status: Accepted

## Context

Contribution Compass should keep contributors current on major released developments and publicly
visible upcoming work without becoming a speculative news or LLM-summary pipeline.

## Decision

Collect a Project News Snapshot for each Project Sensor. Select the latest published stable GitHub
release as the Release Bulletin. Treat published prereleases and open GitHub milestones as Upcoming
Items. Extract a small set of headings and bullets from release notes deterministically for scanning,
while retaining the original notes and evidence URL.

Also collect current Hacker News stories matched to configured projects by explicit per-project
`keywords` or exact repository references. Keywords match story titles. Store the article URL, HN discussion URL, score,
comment count, timestamp, and match reason. Present these as Community Discussions in a separate
labeled section; never treat them as maintainer roadmap or release evidence. Do not crawl the
comment tree.

The GitHub and Hacker News adapters own source normalization. The domain news module owns evidence
selection and highlight extraction. HTML, JSON, Markdown, CLI, and MCP views consume the same model.

## Consequences

News remains reproducible and requires no model credential. Projects without public releases,
prereleases, or milestones clearly report that no supported public roadmap evidence was found.
Milestones and prereleases are indications, not delivery commitments. Broader editorial analysis can
still be added later as an Inference Extension that cites this evidence.

Hacker News matching may miss stories or produce an occasional false-positive keyword match. The
stored match reason makes this visible, and maintainers can tune or empty each repository's `keywords`
list in `config.yml`.
