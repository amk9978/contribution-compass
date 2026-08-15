# ADR-0006: Jinja templates render static HTML

Status: Accepted

## Context

The static HTML adapter grew large enough that Python control flow, escaping, shared page chrome,
and markup had poor locality. Contribution Compass still needs crawlable pages that work without
JavaScript, while browser features and machine consumers use the versioned JSON interface.

## Decision

Render HTML with packaged Jinja2 templates. Configure one environment with automatic HTML/XML
escaping and strict undefined values. Python prepares presentation projections, navigation URLs,
and pagination; templates own markup and simple presentation conditions. Templates must not
collect data, classify Contribution Leads, or duplicate domain rules.

Keep static HTML and versioned JSON as sibling adapters over the application interface. Browser
JavaScript may read published JSON for interactive behavior, but ordinary pages retain meaningful
pre-rendered content.

## Consequences

Page layout and reusable cards have a dedicated presentation seam, and escaping policy has one
implementation. Missing template data fails the site build instead of silently producing partial
markup. The installed Python package includes Jinja2 and its templates, while GitHub Pages remains
fully static and no runtime backend is introduced.
