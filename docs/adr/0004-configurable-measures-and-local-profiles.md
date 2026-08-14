# ADR-0004: Contribution ranking uses configurable measures and profiles stay local

Status: Accepted

## Context

The contribution page must help humans choose where to investigate without turning a deterministic
heuristic into an opaque recommendation. Maintainers also need to tune project-label conventions
without editing Python. Visitors should be able to personalize the hosted publication without an
account or backend.

## Decision

Qualify and rank Contribution Leads through a versioned Contribution Policy in `config.yml`. Emit a
named Contribution Measure for every activated eligibility, maintainer-intent, engagement, scope,
or recency fact. Define the score as the sum of Measure points and expose the complete breakdown in
HTML, JSON, CLI, and MCP.

Keep browser Personal Profiles in `localStorage` and shareable query parameters. Browser code may
filter published evidence and paginate presentation, but it does not classify Leads or write
evidence.

## Consequences

Curators can change weights, thresholds, invitation labels, beginner labels, and exclusions without
changing the domain implementation. Consumers can reproduce every score and ignore or replace the
policy. Hosted personalization requires no identity, cookies, server, or private dependency data.
The browser can only personalize projects already present in the published catalog.
