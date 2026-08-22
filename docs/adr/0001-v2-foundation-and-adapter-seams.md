# ADR-0001: V2 keeps a Python core with real adapter seams

Status: Accepted

## Context

The v1 repository monitor encoded its fixed catalog throughout configuration, collection,
persistence, views, CLI, and MCP. The v2 product instead starts from a developer, discovers a
temporary candidate universe, evaluates project investments, and recommends a small portfolio.

## Decision

Keep Python 3.12 and separate domain, application, adapter, controller, and view modules. Domain
modules remain independent of HTTP, storage, Jinja2, CLI, and MCP. Application modules orchestrate
validated recommendation use cases. Introduce a port only when two real adapters require a stable
seam; avoid speculative pass-through interfaces.

Keep GitHub Actions, GitHub Pages, packaged Jinja2 templates, the CLI transport, and MCP transport.
During the reset they expose only honest rewrite status, not compatibility shims for v1 behavior.

## Consequences

The rewrite can reuse transport and publication mechanisms without preserving the old catalog
model. V1 commands and schemas intentionally break. Each future interface is shaped around the
developer’s question rather than internal storage.
