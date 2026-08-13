# Observability & Reliability — 2026-08-13

> Factual GitHub evidence collected by Contribution Compass. No LLM analysis is performed.

## Contribution Leads

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

- **Pull Request** [exporterhelper: record queue batch send size after batching](https://github.com/open-telemetry/opentelemetry-collector/pull/15510) — 8 comments · 1 reactions · open
- **Issue** [AIX support for tier 2](https://github.com/open-telemetry/opentelemetry-collector/issues/15704) — 0 comments · 0 reactions · open
- **Issue** [Dependency Dashboard](https://github.com/open-telemetry/opentelemetry-collector/issues/8903) — 0 comments · 0 reactions · open
- **Pull Request** [\[pdata/pprofile\] MergeTo: reserve index 0 of empty destination dictionary tables](https://github.com/open-telemetry/opentelemetry-collector/pull/15662) — 7 comments · 0 reactions · open
- **Pull Request** [Update module github.com/golangci/golangci-lint/v2 to v2.12.2](https://github.com/open-telemetry/opentelemetry-collector/pull/14677) — 5 comments · 0 reactions · open
- **Pull Request** [Drop only oversized items instead of the full batch](https://github.com/open-telemetry/opentelemetry-collector/pull/15267) — 4 comments · 0 reactions · open
- **Pull Request** [Fix grammatical errors and remove duplicate code in logs_router](https://github.com/open-telemetry/opentelemetry-collector/pull/15655) — 2 comments · 0 reactions · open
- **Pull Request** [feat: add support for identity compression algorithm in confighttp](https://github.com/open-telemetry/opentelemetry-collector/pull/15656) — 3 comments · 0 reactions · open
- **Pull Request** [\[pdata\] move useProtoPooling to beta](https://github.com/open-telemetry/opentelemetry-collector/pull/15684) — 3 comments · 0 reactions · open
- **Pull Request** [Add Certificate Revocation List (CRL) support](https://github.com/open-telemetry/opentelemetry-collector/pull/15685) — 2 comments · 0 reactions · open
- **Pull Request** [Update github-actions deps](https://github.com/open-telemetry/opentelemetry-collector/pull/15576) — 1 comments · 0 reactions · open
- **Pull Request** [feat(confignet): add Unix domain socket lifecycle management](https://github.com/open-telemetry/opentelemetry-collector/pull/15667) — 1 comments · 0 reactions · open
- **Pull Request** [scraperhelper: clarify collection_interval documentation](https://github.com/open-telemetry/opentelemetry-collector/pull/15734) — 1 comments · 0 reactions · open
- **Pull Request** [\[extension/memorylimiterextension\] Add otelcol_memorylimiter_refused_requests metric](https://github.com/open-telemetry/opentelemetry-collector/pull/15738) — 1 comments · 0 reactions · open
- **Pull Request** [Update module github.com/santhosh-tekuri/jsonschema/v6 to v6.0.3](https://github.com/open-telemetry/opentelemetry-collector/pull/15753) — 1 comments · 0 reactions · closed
- **Pull Request** [fix(memorylimiter): report health status only on state changes](https://github.com/open-telemetry/opentelemetry-collector/pull/15756) — 0 comments · 0 reactions · open
- **Pull Request** [\[chore\]\[component/componentstatus\]: remove timestamp removal TODO](https://github.com/open-telemetry/opentelemetry-collector/pull/15757) — 0 comments · 0 reactions · open

### [Datadog Agent](https://github.com/DataDog/datadog-agent)

- **Pull Request** [Increase Quality Gate memory thresholds for ADP pre-flight mode](https://github.com/DataDog/datadog-agent/pull/54792) — 5 comments · 2 reactions · open
- **Pull Request** [\[ABLD-536\] Bazelify `gotestsum` usage across the repo](https://github.com/DataDog/datadog-agent/pull/54107) — 7 comments · 3 reactions · closed
- **Pull Request** [\[CWS\] Fix glob bypass](https://github.com/DataDog/datadog-agent/pull/54159) — 7 comments · 2 reactions · open
- **Pull Request** [apm: use url.template for OTLP HTTP client resource names](https://github.com/DataDog/datadog-agent/pull/54496) — 7 comments · 2 reactions · open
- **Pull Request** [fix(data plane): run preflight mode for entire SMP experiment duration](https://github.com/DataDog/datadog-agent/pull/54794) — 6 comments · 2 reactions · open
- **Pull Request** [\[CWS\] Fix: handle activity dump endpoint host that already embeds a port](https://github.com/DataDog/datadog-agent/pull/54774) — 4 comments · 2 reactions · closed
- **Pull Request** [\[WP\] ICMPv4 packet flow classification](https://github.com/DataDog/datadog-agent/pull/54157) — 6 comments · 1 reactions · open
- **Pull Request** [\[WP\] Fix isolation re-apply mechanism](https://github.com/DataDog/datadog-agent/pull/54056) — 4 comments · 1 reactions · open
- **Pull Request** [\[WP\] Ignore unsupported socket types in flow_pid map during snapshot](https://github.com/DataDog/datadog-agent/pull/54166) — 5 comments · 1 reactions · closed
- **Pull Request** [\[CWS\] Kill container and cgroup scopes with cgroup v2 cgroup.kill](https://github.com/DataDog/datadog-agent/pull/54225) — 4 comments · 1 reactions · open
- **Pull Request** [Build with race detector](https://github.com/DataDog/datadog-agent/pull/54333) — 4 comments · 1 reactions · open
- **Pull Request** [fix(cws): register connected sockets in the `flow_pid` map](https://github.com/DataDog/datadog-agent/pull/54691) — 5 comments · 1 reactions · closed
- **Pull Request** [\[SBOM\] Refresh every image when spreading the refresh](https://github.com/DataDog/datadog-agent/pull/54715) — 4 comments · 2 reactions · open
- **Pull Request** [Revert "SBOM e2e: scan host and container images across runtimes"](https://github.com/DataDog/datadog-agent/pull/52200) — 6 comments · 0 reactions · closed
- **Pull Request** [\[procmgr\] Show profile and user in list and describe](https://github.com/DataDog/datadog-agent/pull/53568) — 26 comments · 1 reactions · open
- **Pull Request** [\[CWS\] Persist profile when cgroup is deleted / agent shutdown](https://github.com/DataDog/datadog-agent/pull/54138) — 3 comments · 1 reactions · open
- **Pull Request** [\[SBOM\] Derive image inUse from workloadmeta](https://github.com/DataDog/datadog-agent/pull/54713) — 7 comments · 0 reactions · closed
- **Pull Request** [DELA-251 - Initial implementation of cloud auth proof for an API key](https://github.com/DataDog/datadog-agent/pull/43554) — 4 comments · 0 reactions · closed
- **Pull Request** [sbom: remove the Trivy on-disk cache](https://github.com/DataDog/datadog-agent/pull/53411) — 5 comments · 0 reactions · open
- **Pull Request** [\[CWS-6177\] Use dynamic sampling](https://github.com/DataDog/datadog-agent/pull/54471) — 5 comments · 1 reactions · open
- **Pull Request** [\[procmgr\] Windows spawn profiles foundation](https://github.com/DataDog/datadog-agent/pull/54731) — 25 comments · 1 reactions · open
- **Pull Request** [Split network-devices section in it's own file and fix ID links](https://github.com/DataDog/datadog-agent/pull/54769) — 1 comments · 1 reactions · open
- **Pull Request** [Paulcacheux/unmarshal binary opt](https://github.com/DataDog/datadog-agent/pull/45964) — 2 comments · 0 reactions · closed
- **Pull Request** [Update dependency DataDog/dd-apm-library-python to v4.13.0](https://github.com/DataDog/datadog-agent/pull/54444) — 17 comments · 2 reactions · closed
- **Pull Request** [\[EBPF\] gpu: Skip unsupported vGPU max-clock queries](https://github.com/DataDog/datadog-agent/pull/54729) — 11 comments · 3 reactions · closed
- **Pull Request** [HA(e2e): Move tests to RC fakeintake to fix flakiness](https://github.com/DataDog/datadog-agent/pull/53246) — 13 comments · 2 reactions · closed
- **Pull Request** [feat(autodiscovery): tag configuration-discovery instances to mitigate duplicate metrics risk](https://github.com/DataDog/datadog-agent/pull/54660) — 8 comments · 3 reactions · closed
- **Pull Request** [Improve support for Windows across Invoke tasks](https://github.com/DataDog/datadog-agent/pull/54762) — 11 comments · 2 reactions · closed
- **Pull Request** [Add source to distributions via checks.](https://github.com/DataDog/datadog-agent/pull/51295) — 8 comments · 2 reactions · open
- **Pull Request** [feat(otel-logs): map instrumentation scope name to otel.scope.name](https://github.com/DataDog/datadog-agent/pull/52945) — 4 comments · 3 reactions · closed

### [Prometheus](https://github.com/prometheus/prometheus)

- **Issue** [__meta_kubernetes_service_loadbalancer_ip not working as expected](https://github.com/prometheus/prometheus/issues/14398) — 23 comments · 0 reactions · open
- **Issue** [alerting: expose activeAt for alert templating](https://github.com/prometheus/prometheus/issues/17273) — 7 comments · 0 reactions · open
- **Issue** [__address__ label from pod discovered through kubernetes discovery does not include port when relabelling](https://github.com/prometheus/prometheus/issues/11678) — 4 comments · 0 reactions · closed
- **Issue** [Dependency Dashboard](https://github.com/prometheus/prometheus/issues/17691) — 5 comments · 0 reactions · open
- **Issue** [discovery/file: Flaky `TestInvalidFileUpdate`  and `TestUpdateFileWithPartialWrites` tests](https://github.com/prometheus/prometheus/issues/18269) — 4 comments · 0 reactions · open
- **Issue** [promql/parser: parentheses around a plain duration literal are lost on round-trip](https://github.com/prometheus/prometheus/issues/18770) — 2 comments · 0 reactions · open
- **Pull Request** [TSDB: improve isolation performance](https://github.com/prometheus/prometheus/pull/19286) — 10 comments · 0 reactions · open
- **Issue** [Incorrect Markdown link formatting due to space between \[\] and ()](https://github.com/prometheus/prometheus/issues/18044) — 0 comments · 0 reactions · closed
- **Pull Request** [Populate __meta_kubernetes_service_loadbalancer_ip from status.loadBalancer.ingress with fallback to spec.loadBalancerIP](https://github.com/prometheus/prometheus/pull/17136) — 9 comments · 0 reactions · open
- **Pull Request** [\[BugFix\]promql: Reject offset/@ modifiers immediately before subquery range](https://github.com/prometheus/prometheus/pull/17852) — 6 comments · 0 reactions · open
- **Pull Request** [promql/parser: fix error position for duration division by zero](https://github.com/prometheus/prometheus/pull/19211) — 6 comments · 0 reactions · open
- **Pull Request** [docs: document NaN behaviour of clamp_max() and clamp_min()](https://github.com/prometheus/prometheus/pull/19274) — 7 comments · 0 reactions · open
- **Pull Request** [config: promote retry_on_http_429 to GA](https://github.com/prometheus/prometheus/pull/19390) — 4 comments · 0 reactions · open
- **Pull Request** [storage: add OriginalLabelsHash() method to SeriesSet](https://github.com/prometheus/prometheus/pull/19200) — 2 comments · 0 reactions · open
- **Pull Request** [cmd/prometheus: OS agnostic tests](https://github.com/prometheus/prometheus/pull/19340) — 2 comments · 0 reactions · closed
- **Pull Request** [cmd/prometheus: fix flaky TestRuntimeGOGCConfig](https://github.com/prometheus/prometheus/pull/19341) — 2 comments · 0 reactions · closed
- **Pull Request** [docker SD: add Image + ImageID to labels](https://github.com/prometheus/prometheus/pull/19386) — 2 comments · 0 reactions · open
- **Pull Request** [discovery/stackit: add support for postgres targets discovery](https://github.com/prometheus/prometheus/pull/19400) — 2 comments · 0 reactions · open
- **Pull Request** [fix(deps): update kubernetes go dependencies to v0.36.3](https://github.com/prometheus/prometheus/pull/18757) — 1 comments · 0 reactions · open
- **Pull Request** [discovery/aws: paginate Lightsail GetInstances so all instances are discovered](https://github.com/prometheus/prometheus/pull/19180) — 1 comments · 0 reactions · open
- **Pull Request** [tsdb: make panic lock-release test OS agnostic](https://github.com/prometheus/prometheus/pull/19339) — 0 comments · 0 reactions · closed
- **Pull Request** [config: fix windows config tests](https://github.com/prometheus/prometheus/pull/19370) — 0 comments · 0 reactions · closed
- **Pull Request** [docs: Add troubleshooting section with common issues and solutions](https://github.com/prometheus/prometheus/pull/19373) — 1 comments · 0 reactions · closed
- **Pull Request** [fix(discovery/aws): guard nil Placement and ImageId in EC2 discovery](https://github.com/prometheus/prometheus/pull/19375) — 1 comments · 0 reactions · open
- **Pull Request** [feat: add metric analyzer utilities for Prometheus metrics analysis](https://github.com/prometheus/prometheus/pull/19377) — 1 comments · 0 reactions · open
- **Pull Request** [promql: safely derive info series evaluation time](https://github.com/prometheus/prometheus/pull/19387) — 0 comments · 0 reactions · open
- **Pull Request** [discovery/aws: don't panic on ECS tasks with absent optional fields](https://github.com/prometheus/prometheus/pull/19396) — 1 comments · 0 reactions · closed
- **Pull Request** [scrape: use a dedicated HTTP client per unix socket target](https://github.com/prometheus/prometheus/pull/19399) — 1 comments · 0 reactions · open
- **Pull Request** [tsdb: document that OOO chunk IDs are no longer monotonically increasing](https://github.com/prometheus/prometheus/pull/19401) — 1 comments · 0 reactions · closed
- **Pull Request** [\[PREVIEW\] storage/remote: combine exemplars and samples in same PRW v2 request](https://github.com/prometheus/prometheus/pull/19402) — 1 comments · 0 reactions · closed

### [Loki](https://github.com/grafana/loki)

- **Issue** [Duplicate log lines can be introduced by automatic stream sharding](https://github.com/grafana/loki/issues/18760) — 3 comments · 13 reactions · open
- **Issue** [\[Bug\] PutObject fails with 400 InvalidArgument on non-AWS S3 (NetApp ONTAP, others) after PR #21848/#21849  -  x-amz-content-sha256 PAYLOAD-TRAILER not supported](https://github.com/grafana/loki/issues/21926) — 9 comments · 0 reactions · open
- **Issue** [Replace `go.uber.go/atomic` with Go standard library `sync/atomic`](https://github.com/grafana/loki/issues/20673) — 5 comments · 0 reactions · open
- **Issue** [Dependency Dashboard](https://github.com/grafana/loki/issues/23439) — 0 comments · 0 reactions · open
- **Issue** [Sharded avg_over_time(... | unwrap ...) with grouping under-reports the average](https://github.com/grafana/loki/issues/23890) — 0 comments · 0 reactions · closed
- **Pull Request** [feat(storage): Add OCI Thanos object store backend](https://github.com/grafana/loki/pull/23710) — 8 comments · 0 reactions · open
- **Pull Request** [fix: deduplicate log lines split across stream shards](https://github.com/grafana/loki/pull/23907) — 7 comments · 0 reactions · open
- **Pull Request** [feat(kafka): support configurable SASL mechanism (PLAIN, SCRAM-SHA-256, SCRAM-SHA-512)](https://github.com/grafana/loki/pull/21719) — 0 comments · 1 reactions · open
- **Pull Request** [fix(querier): Prevent sample query plan marshal race 🤖🤖🤖](https://github.com/grafana/loki/pull/23349) — 4 comments · 0 reactions · open
- **Pull Request** [\[DO NOT MERGE\] LogQL metric queries with stream-first iteration (prototype)](https://github.com/grafana/loki/pull/23641) — 5 comments · 0 reactions · open
- **Pull Request** [feat(distributor): add -distributor.extend-writes to keep write quorum during ingester scale-down](https://github.com/grafana/loki/pull/23908) — 5 comments · 0 reactions · open
- **Pull Request** [chore(deps): Update module go.etcd.io/etcd/client/v3 to v3.7.1 (main)](https://github.com/grafana/loki/pull/23000) — 2 comments · 0 reactions · open
- **Pull Request** [fix: Recognise thanos/minio S3 throttling errors as retryable and add backoff](https://github.com/grafana/loki/pull/23454) — 2 comments · 0 reactions · open
- **Pull Request** [feat: Introduce tsdb.shipper.index-reader-mode feature flag](https://github.com/grafana/loki/pull/23663) — 3 comments · 0 reactions · closed
- **Pull Request** [chore: Implement streaming reading of symbols section](https://github.com/grafana/loki/pull/23730) — 2 comments · 0 reactions · open
- **Pull Request** [docs: Add Thanos storage examples  🤖🤖🤖](https://github.com/grafana/loki/pull/23777) — 3 comments · 0 reactions · closed
- **Pull Request** [chore: Implement streaming reading of series](https://github.com/grafana/loki/pull/23790) — 2 comments · 0 reactions · open
- **Pull Request** [fix(logql): Count unwrapped samples in the sharded avg_over_time denominator](https://github.com/grafana/loki/pull/23906) — 2 comments · 0 reactions · closed
- **Pull Request** [fix(docs): correct broken 'pipeline errors' link in log queries](https://github.com/grafana/loki/pull/23927) — 2 comments · 0 reactions · closed
- **Pull Request** [feat(indexgateway): Add admission control to bound concurrent requests](https://github.com/grafana/loki/pull/23932) — 2 comments · 0 reactions · open
- **Pull Request** [feat(operator): Watch object storage Services for NetworkPolicy updates and surface ports in status](https://github.com/grafana/loki/pull/22436) — 0 comments · 0 reactions · open
- **Pull Request** [chore(deps): Update module go.etcd.io/etcd/api/v3 to v3.7.1 (main)](https://github.com/grafana/loki/pull/22574) — 1 comments · 0 reactions · open
- **Pull Request** [chore(deps): Update module go.etcd.io/etcd/client/pkg/v3 to v3.7.1 (main)](https://github.com/grafana/loki/pull/22575) — 1 comments · 0 reactions · open
- **Pull Request** [chore(deps): Update Terraform google to v7.43.0 (main)](https://github.com/grafana/loki/pull/22967) — 1 comments · 0 reactions · open
- **Pull Request** [fix(querier): Prevent log query plan marshal race 🤖🤖🤖](https://github.com/grafana/loki/pull/23357) — 1 comments · 0 reactions · open
- **Pull Request** [fix(deps): Update module github.com/tjhop/slog-gokit to v0.2.2 (main)](https://github.com/grafana/loki/pull/23397) — 1 comments · 0 reactions · open
- **Pull Request** [fix(deps): Update github.com/prometheus/prometheus digest to 762bc8a (main)](https://github.com/grafana/loki/pull/23627) — 1 comments · 0 reactions · open
- **Pull Request** [chore: Implement streaming reading of header and TOC](https://github.com/grafana/loki/pull/23696) — 0 comments · 0 reactions · closed
- **Pull Request** [refactor(chunks-inspect): Report block parse errors and drop the duplicate time.go](https://github.com/grafana/loki/pull/23721) — 0 comments · 0 reactions · closed
- **Pull Request** [chore(deps): Update github.com/grafana/objstore digest to ec72e5a (main)](https://github.com/grafana/loki/pull/23741) — 0 comments · 0 reactions · open
