# Prometheus Project News — 2026-08-20

> Public GitHub release and roadmap evidence. Upcoming items are indications, not commitments.

Repository: [prometheus/prometheus](https://github.com/prometheus/prometheus)

## Latest stable: [3.14.0 / 2026-08-17](https://github.com/prometheus/prometheus/releases/tag/v3.14.0)

- Tag: `v3.14.0`
- Published: 2026-08-18T08:49:40Z
- \[CHANGE\] API: Deprecate the stats query parameter of /api/v1/query and /api/v1/queryrange for values other than true and all. Other values still enable basic statistics but now return a deprecation warning; they will be rejected in the next
- \[CHANGE\] API: /api/v1/status/config now correctly shows separator: "" and replacement: "" in relabel configs when explicitly set to empty, instead of omitting them. #18653
- \[CHANGE\] Discovery/Hetzner: Drop the metahetznerdatacenter label for hcloud targets, following its removal from the Hetzner Cloud API. #19269
- \[CHANGE\] PromQL: Enable duration expressions by default. The promql-duration-expr feature flag is now a no-op. #19033
- \[CHANGE\] PromQL: Promote firstovertime to stable. It no longer requires the promql-experimental-functions feature flag. #19093
- \[FEATURE\] Discovery: Add Oracle Cloud Infrastructure compute service discovery (ocisdconfigs). #18919

## Publicly indicated upcoming work

- **Milestone** [Native Histograms](https://github.com/prometheus/prometheus/milestone/10)
- **Milestone** [OTEL Support](https://github.com/prometheus/prometheus/milestone/12)

## Hacker News discussions

No matching current Hacker News discussion was found.
