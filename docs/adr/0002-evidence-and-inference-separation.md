# ADR-0002: Evidence and inference remain separate

Status: Accepted

## Context

The project should eventually support LLM-backed inference, while remaining a trustworthy factual
data gathering place for developers and automated consumers.

## Decision

Persist normalized Signal snapshots, Project Context, and append-only Observation Events as direct
evidence. Produce Contribution Leads only through documented deterministic rules. Expose these
records through the same catalog interface to static views and MCP.

Any future Inference Extension must write to a separate namespace, identify its method/model/run,
and cite immutable Signal or Observation Event IDs. Inference must never overwrite collected data.

## Consequences

Consumers can reconstruct what was observed and when. They can choose whether to trust or replace
an inference implementation without replacing collection. The MVP requires no model credentials.
