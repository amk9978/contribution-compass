# Observability & Reliability — 2026-08-13

> Factual GitHub evidence collected by Contribution Compass. No LLM analysis is performed.

## Contribution Leads

### [grafana-loki lacks basic feature of extracting nested json labels](https://github.com/grafana/loki/issues/6994)

- Project: `grafana/loki`
- Tier: `maintainer-invited`
- Evidence: Maintainers marked this as a good first issue; No assignee is listed
- Caveat: Confirm scope and availability with the maintainers before starting work.

### [Replace `go.uber.go/atomic` with Go standard library `sync/atomic`](https://github.com/grafana/loki/issues/20673)

- Project: `grafana/loki`
- Tier: `maintainer-invited`
- Evidence: Maintainers marked this as a good first issue; No assignee is listed
- Caveat: Confirm scope and availability with the maintainers before starting work.

### [Duplicate log lines can be introduced by automatic stream sharding](https://github.com/grafana/loki/issues/18760)

- Project: `grafana/loki`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

## Important Updates

### [OpenTelemetry Collector](https://github.com/open-telemetry/opentelemetry-collector)

- **Issue** [Dependency Dashboard](https://github.com/open-telemetry/opentelemetry-collector/issues/8903) — 0 comments · 0 reactions · open
- **Issue** [\[docs\] component status docs are out of date](https://github.com/open-telemetry/opentelemetry-collector/issues/15758) — 0 comments · 0 reactions · open
- **Pull Request** [fix(memorylimiter): report health status only on state changes](https://github.com/open-telemetry/opentelemetry-collector/pull/15756) — 2 comments · 0 reactions · open
- **Pull Request** [Update module github.com/pierrec/lz4/v4 to v4.1.28](https://github.com/open-telemetry/opentelemetry-collector/pull/15752) — 1 comments · 0 reactions · closed
- **Pull Request** [\[chore\]\[component/componentstatus\]: remove timestamp removal TODO](https://github.com/open-telemetry/opentelemetry-collector/pull/15757) — 0 comments · 0 reactions · open
- **Pull Request** [\[chore\] update component status docs to describe current behavior](https://github.com/open-telemetry/opentelemetry-collector/pull/15759) — 0 comments · 0 reactions · open

### [Datadog Agent](https://github.com/DataDog/datadog-agent)

- **Pull Request** [apm: use url.template for OTLP HTTP client resource names](https://github.com/DataDog/datadog-agent/pull/54496) — 8 comments · 2 reactions · open
- **Pull Request** [\[procmgr\] Windows spawn profiles foundation](https://github.com/DataDog/datadog-agent/pull/54731) — 30 comments · 1 reactions · open
- **Pull Request** [\[WP\] ICMPv4 packet flow classification](https://github.com/DataDog/datadog-agent/pull/54157) — 5 comments · 1 reactions · open
- **Pull Request** [ci: default GitLab jobs to shallow clones, keep full history where needed](https://github.com/DataDog/datadog-agent/pull/54834) — 4 comments · 1 reactions · open
- **Pull Request** [Split network-devices section in it's own file and fix ID links](https://github.com/DataDog/datadog-agent/pull/54769) — 3 comments · 1 reactions · open
- **Pull Request** [\[AAD-23\] Remove CUSUM detector](https://github.com/DataDog/datadog-agent/pull/54437) — 10 comments · 2 reactions · open
- **Pull Request** [Add source to distributions via checks.](https://github.com/DataDog/datadog-agent/pull/51295) — 8 comments · 2 reactions · open
- **Pull Request** [\[EBPF\] gpu: serialize NVML field value queries](https://github.com/DataDog/datadog-agent/pull/54821) — 6 comments · 2 reactions · open
- **Pull Request** [fix: avoid data race in grpclog.SetLogger on otelcol collector start](https://github.com/DataDog/datadog-agent/pull/54645) — 8 comments · 1 reactions · closed
- **Pull Request** [\[EBPF\] gpu: Support ARM64 NVML library discovery](https://github.com/DataDog/datadog-agent/pull/54720) — 9 comments · 2 reactions · closed
- **Pull Request** [Remove schemaBuilder and createschema command](https://github.com/DataDog/datadog-agent/pull/54793) — 5 comments · 2 reactions · open
- **Pull Request** [fix(installer): embed -nocap systemd unit templates](https://github.com/DataDog/datadog-agent/pull/54804) — 4 comments · 2 reactions · open
- **Pull Request** [\[AGENTRUN-1446\] Skip nss failover e2e test it if the fakeintakes are still in use](https://github.com/DataDog/datadog-agent/pull/54814) — 4 comments · 2 reactions · closed
- **Pull Request** [\[DSEC\] Move dd-sds dependency to shared workspace](https://github.com/DataDog/datadog-agent/pull/54815) — 5 comments · 2 reactions · closed
- **Pull Request** [fix(aix): discover Python checks via integrations-core AIX manifest tag](https://github.com/DataDog/datadog-agent/pull/54823) — 4 comments · 2 reactions · closed
- **Pull Request** [\[release\] Update release.json for 7.83.0-rc.3](https://github.com/DataDog/datadog-agent/pull/54845) — 4 comments · 2 reactions · open
- **Pull Request** [optimize the complexity of the trace_contention_begin](https://github.com/DataDog/datadog-agent/pull/54634) — 7 comments · 1 reactions · open
- **Pull Request** [\[EBPF\] gpu: add NVLink capability tag](https://github.com/DataDog/datadog-agent/pull/54828) — 6 comments · 1 reactions · open
- **Pull Request** [\[CONTP-2006\] feat(ddi): Add resolved target to workloadmeta](https://github.com/DataDog/datadog-agent/pull/54840) — 6 comments · 1 reactions · open
- **Pull Request** [\[CONTP-2006\] feat(ddi): Connect custom workload targets to DDI controller and streaming](https://github.com/DataDog/datadog-agent/pull/54843) — 6 comments · 1 reactions · open
- **Issue** [Dependency Dashboard](https://github.com/DataDog/datadog-agent/issues/33469) — 0 comments · 0 reactions · open
- **Pull Request** [feat(serverless-init): add shared infrastructure for AWS MicroVM cloud service](https://github.com/DataDog/datadog-agent/pull/53030) — 4 comments · 2 reactions · open
- **Pull Request** [feat(serverless-init): add MicroVM lifecycle HTTP forwarder](https://github.com/DataDog/datadog-agent/pull/53033) — 4 comments · 2 reactions · open
- **Pull Request** [\[CONTINT-5415\] Tag CronJob-owned Job events with kube_cronjob](https://github.com/DataDog/datadog-agent/pull/54362) — 5 comments · 1 reactions · closed
- **Pull Request** [\[ACTP\] package and activate par-control](https://github.com/DataDog/datadog-agent/pull/54529) — 5 comments · 1 reactions · open
- **Pull Request** [\[ACTP\] add par-control process lifecycle](https://github.com/DataDog/datadog-agent/pull/54589) — 4 comments · 1 reactions · open
- **Pull Request** [\[ACTP\] add par-control effective configuration](https://github.com/DataDog/datadog-agent/pull/54590) — 5 comments · 1 reactions · open
- **Pull Request** [\[ACTP\] add par-control executor channel](https://github.com/DataDog/datadog-agent/pull/54591) — 5 comments · 1 reactions · open
- **Pull Request** [\[ACTP\] add par-control OPMS client](https://github.com/DataDog/datadog-agent/pull/54592) — 5 comments · 1 reactions · open
- **Pull Request** [\[ACTP\] orchestrate par-control tasks](https://github.com/DataDog/datadog-agent/pull/54593) — 5 comments · 1 reactions · open

### [Prometheus](https://github.com/prometheus/prometheus)

- **Issue** [Dependency Dashboard](https://github.com/prometheus/prometheus/issues/17691) — 5 comments · 0 reactions · open
- **Pull Request** [Agent: replay WAL concurrently](https://github.com/prometheus/prometheus/pull/19414) — 0 comments · 0 reactions · open
- **Pull Request** [Enforce GitHub Action security across all repositories in the Prometheus org](https://github.com/prometheus/prometheus/pull/19415) — 1 comments · 0 reactions · open

### [Loki](https://github.com/grafana/loki)

- **Issue** [grafana-loki lacks basic feature of extracting nested json labels](https://github.com/grafana/loki/issues/6994) — 12 comments · 9 reactions · open
- **Issue** [Replace `go.uber.go/atomic` with Go standard library `sync/atomic`](https://github.com/grafana/loki/issues/20673) — 6 comments · 0 reactions · open
- **Pull Request** [fix(CI): release scripts add newline](https://github.com/grafana/loki/pull/19059) — 0 comments · 0 reactions · closed
