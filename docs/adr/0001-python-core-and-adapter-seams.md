# ADR-0001: Python core with adapter seams

Status: Accepted

## Context

The maintainer is more familiar with Python than TypeScript. Contribution Compass must support a
scheduled collector, static publication, local and remote machine consumption, and MCP without
duplicating domain rules in each entry point.

## Decision

Use Python 3.12 for domain models, application use cases, collection, persistence, static
publication, and MCP. Keep browser JavaScript and CSS limited to progressive presentation behavior.

Organize modules into:

- `domain`: models, invariants, ranking, and contribution classification;
- `application`: collection and catalog use cases;
- `ports`: small interfaces at real seams;
- `adapters`: GitHub, local JSON, and hosted HTTP implementations;
- `controllers`: CLI and MCP entry points;
- `views`: Markdown and static-site rendering.

The catalog seam has two adapters: local checked-in data and the GitHub Pages JSON interface. Tests
use in-memory adapters through the same interface.

## Consequences

Domain rules are independent of transport and presentation. MCP handlers remain thin controllers.
The frontend may use JavaScript, but it cannot own collection or opportunity logic. Python replaces
the TypeScript toolchain and backend.
