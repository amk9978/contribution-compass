# ADR-0005: Catalog overlays preserve local curation and provenance

Status: Accepted

## Context

Independent installations often monitor overlapping repositories. Re-collecting every shared
Project Sensor wastes GitHub quota and makes forks more expensive, but silently importing all
projects from a central catalog would violate configuration semantics and obscure evidence origin.

## Decision

Allow optional versioned Catalog Overlays configured by URL and maximum age. An Overlay may satisfy
only repositories explicitly present in the consumer's `config.yml`. A fresh matching Overlay
removes that repository from the direct collection delta. When composing a snapshot, newer source
dates win and equally current local data wins.

Attach Catalog Provenance to every composed repository dataset. Ignore stale, incompatible, or
unavailable Overlays and collect those Project Sensors directly instead.

## Consequences

Forks can reuse the public catalog while retaining their own groups, names, Keywords, and additional
Project Sensors. The hosted catalog remains an optimization, not a required central backend.
Checked-in Markdown reports describe the locally collected delta; composed HTML, JSON, CLI, and MCP
views include fresh reused data.
