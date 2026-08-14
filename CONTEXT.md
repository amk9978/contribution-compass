# Contribution Compass Domain Context

## Mission

Contribution Compass keeps the developer community current on important activity in curated
open-source projects and helps opportunistic contributors find evidence-backed places where their
work may be useful.

## Domain language

### Project Sensor

A configured GitHub repository monitored deeply over time. A Project Sensor belongs to an arbitrary
Project Group and may carry maintainer-curated Keywords for search and Hacker News matching. Avoid
“built-in repository” or domain-specific repository taxonomies.

### Keyword

A maintainer-curated phrase attached to a Project Sensor in `config.yml`. Keywords are persisted as
project metadata and included in factual catalog searches. They may guide discovery but are not
evidence that an individual Signal is about that phrase.

### Signal

A normalized issue, pull request, or release backed by a direct URL to its GitHub evidence. A Signal
is factual collected data, not an interpretation.

### Observation Event

An append-only record that a Signal was first discovered or materially changed at a particular
collection time. It contains the collected Signal snapshot and changed fields so consumers can
reconstruct a factual trail.

### Project Context

Collected repository metadata that helps a developer or model interpret Signals: description,
topics, primary language, license, default branch, activity counts, and repository URL.

### Project News Snapshot

Factual public release and roadmap information plus separately labeled Community Discussions for a
Project Sensor at collection time. It contains the latest stable Release Bulletin and any publicly
visible Upcoming Items. It is evidence, not a prediction that maintainers will deliver a plan on
time.

### Community Discussion

A current Hacker News story matched to a configured Project Sensor by explicit title keywords or an
exact repository reference. It retains both article and discussion URLs, score, comment count,
author, and match reason. It is community evidence, not maintainer evidence or endorsement. Avoid
“project announcement” unless the source itself establishes that fact.

### Release Bulletin

A published GitHub release with its original release notes and a direct evidence URL. Release-note
highlights are deterministically extracted headings and bullets, not an inferred summary.

### Upcoming Item

A public prerelease or open GitHub milestone that may indicate upcoming work. Its wording must say
“publicly indicated” rather than claiming a release commitment. Absence means no supported public
evidence was found, not that the project has no private roadmap.

### Contribution Lead

An open, unassigned issue surfaced by transparent deterministic rules. A Lead always contains its
evidence, reasons, and caveat.

### Contribution Measure

A named, factual scoring input attached to a Contribution Lead. It contains its point contribution
and the collected evidence that activated it. A Lead's score is exactly the sum of its Measures;
zero-point eligibility Measures may be retained for explanation. Avoid “quality score” or
“recommended task.”

### Contribution Policy

Curator-controlled label sets, weights, and thresholds used to qualify and rank Contribution Leads.
It is configuration, not collected evidence. Empty configured label sets stay empty, and a zero
weight disables that Measure's scoring effect.

### Maintainer-Invited Lead

A Contribution Lead with an explicit invitation label such as `good first issue` or `help wanted`.
It is still not a guarantee of acceptance or difficulty.

### Triage Lead

A lower-confidence Contribution Lead based on factual signals such as documentation labeling and
visible engagement. It must never be represented as maintainer-approved work.

### Inference Extension

An optional consumer of Signals, Observation Events, Project Context, and Contribution Leads. It may
produce hypotheses, but its output remains separate from collected evidence and must cite the
evidence it used.

### Personal Profile

A browser-local selection of Project Sensors used to filter the public catalog into a contributor's
own table. It is stored in `localStorage` or a shareable URL and never sent to a Contribution Compass
backend.

### Catalog Overlay

An optional, versioned Contribution Compass catalog reused by another installation. Only Project
Sensors already named in the consumer's `config.yml` may flow through an Overlay. Equally current
local data wins; stale or unavailable Overlays fall back to direct collection.

### Catalog Provenance

Metadata recording whether a repository snapshot came from local collection or a Catalog Overlay,
including the source snapshot date and, for an Overlay, its configured identity, URL, and generation
time.

## Invariants

- Every Signal and Contribution Lead retains a primary evidence URL.
- Every Release Bulletin and Upcoming Item retains a primary evidence URL.
- Every Community Discussion retains its article and Hacker News discussion URLs.
- Collection does not require or invoke an LLM.
- Observation Events are append-only; newer observations do not erase their trail.
- Empty configured groups stay empty and no hidden Project Sensors appear.
- Empty configured keyword lists stay empty and stored Keywords mirror `config.yml`.
- Empty Contribution Policy label sets and empty Catalog Overlay lists stay empty.
- A Contribution Lead score equals the sum of its named Contribution Measures.
- Catalog Overlays cannot introduce Project Sensors absent from the consumer's `config.yml`.
- Reused repository snapshots expose Catalog Provenance.
- MCP, CLI, static HTML, and JSON are adapters over the same application interface.
- Inference output, when added, is distinguishable from direct evidence.
