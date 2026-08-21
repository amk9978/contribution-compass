# Observability & Reliability — 2026-08-21

> Factual GitHub evidence collected by Contribution Compass. No LLM analysis is performed.

## Contribution Leads

### [Deltas: add PromQL function to disable processing of start times](https://github.com/prometheus/prometheus/issues/19264)

- Project: `prometheus/prometheus`
- Tier: `maintainer-invited`
- Evidence: Maintainer invitation label: help wanted; No assignee is listed
- Caveat: Confirm scope and availability with the maintainers before starting work.

### [Volume API and index stats over-report after log deletion; log queries stay correct](https://github.com/grafana/loki/issues/23807)

- Project: `grafana/loki`
- Tier: `triage-lead`
- Evidence: Documentation-related issue with no assignee listed
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [ingester logs "Ingester is shutting down" non-stop](https://github.com/grafana/loki/issues/23769)

- Project: `grafana/loki`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

## Important Updates

### [OpenTelemetry Collector](https://github.com/open-telemetry/opentelemetry-collector)

- **Issue** [Add queue-oriented storage interface for persistent queues](https://github.com/open-telemetry/opentelemetry-collector/issues/15384) — 12 comments · 1 reactions · open
- **Pull Request** [\[confighttp\] Move keepalive config into a dedicated optional section](https://github.com/open-telemetry/opentelemetry-collector/pull/15308) — 12 comments · 2 reactions · open
- **Issue** [Dependency Dashboard](https://github.com/open-telemetry/opentelemetry-collector/issues/8903) — 0 comments · 0 reactions · open
- **Pull Request** [\[confignet\] Allow setting security descriptors for npipes](https://github.com/open-telemetry/opentelemetry-collector/pull/15212) — 7 comments · 0 reactions · open
- **Pull Request** [\[exporterhelper\] Cache request size per sizer type](https://github.com/open-telemetry/opentelemetry-collector/pull/15587) — 2 comments · 2 reactions · closed
- **Issue** [pprofileotlp.ExportRequest does not use the ProfilesDictionary for Resource attributes](https://github.com/open-telemetry/opentelemetry-collector/issues/15792) — 1 comments · 0 reactions · open
- **Issue** [Unset key_strindex is treated as a reference to string_table\[0\], erasing inline attribute keys](https://github.com/open-telemetry/opentelemetry-collector/issues/15793) — 1 comments · 0 reactions · open
- **Issue** [\[cmd/mdatagen\] Versioned Metrics migration improve documentation template](https://github.com/open-telemetry/opentelemetry-collector/issues/15795) — 1 comments · 0 reactions · open
- **Issue** [queuestorage: A storage extension optimized for queues based on bbolt.](https://github.com/open-telemetry/opentelemetry-collector/issues/15797) — 0 comments · 0 reactions · closed
- **Pull Request** [Update module github.com/golangci/golangci-lint/v2 to v2.13.1](https://github.com/open-telemetry/opentelemetry-collector/pull/14677) — 5 comments · 0 reactions · open
- **Pull Request** [Update module github.com/dkorunic/betteralign to v0.15.0](https://github.com/open-telemetry/opentelemetry-collector/pull/15113) — 4 comments · 0 reactions · open
- **Pull Request** [\[chore\] Fix inverted IsEmpty godoc for SpanID/TraceID/ProfileID](https://github.com/open-telemetry/opentelemetry-collector/pull/15519) — 4 comments · 0 reactions · open
- **Pull Request** [Update github-actions deps](https://github.com/open-telemetry/opentelemetry-collector/pull/15576) — 2 comments · 0 reactions · open
- **Pull Request** [Update github-actions deps (major)](https://github.com/open-telemetry/opentelemetry-collector/pull/15579) — 2 comments · 0 reactions · open
- **Pull Request** [\[cmd/mdatagen\] Allow underscores in feature gate names](https://github.com/open-telemetry/opentelemetry-collector/pull/15593) — 3 comments · 0 reactions · open
- **Pull Request** [Add recursion depth limit to JSON unmarshalling](https://github.com/open-telemetry/opentelemetry-collector/pull/15604) — 3 comments · 0 reactions · open
- **Pull Request** [\[pkg/pdata\] avoid allocations in WriteInt64 and WriteUint64](https://github.com/open-telemetry/opentelemetry-collector/pull/15629) — 2 comments · 0 reactions · open
- **Pull Request** [Fix null bodies in schema](https://github.com/open-telemetry/opentelemetry-collector/pull/15729) — 2 comments · 0 reactions · open
- **Pull Request** [\[exporterhelper\] Inject queue and batch metrics](https://github.com/open-telemetry/opentelemetry-collector/pull/15770) — 3 comments · 0 reactions · closed
- **Pull Request** [\[chore\]\[rfc/confmap\]: add two new approaches for merging lists across configurations](https://github.com/open-telemetry/opentelemetry-collector/pull/15107) — 5 comments · 0 reactions · open
- **Pull Request** [\[pdata/pprofile\] add bounds checks to FromLocationIndices and switchDictionary](https://github.com/open-telemetry/opentelemetry-collector/pull/15698) — 5 comments · 0 reactions · open
- **Pull Request** [\[exporterhelper\] Preserve pipeline ownership for persistent queue requests](https://github.com/open-telemetry/opentelemetry-collector/pull/15739) — 1 comments · 0 reactions · open
- **Pull Request** [\[chore\] \[internal/statusutil\] Turn into a submodule](https://github.com/open-telemetry/opentelemetry-collector/pull/15787) — 1 comments · 0 reactions · open
- **Pull Request** [\[chore\] \[cmd/mdatagen\] Assert logs builder content in TestRunContents](https://github.com/open-telemetry/opentelemetry-collector/pull/15791) — 1 comments · 0 reactions · open
- **Pull Request** [confighttp: accept identity content encoding](https://github.com/open-telemetry/opentelemetry-collector/pull/15585) — 3 comments · 0 reactions · closed
- **Pull Request** [\[chore\] Add tests for batch sizer defaulting behavior](https://github.com/open-telemetry/opentelemetry-collector/pull/15591) — 2 comments · 0 reactions · closed
- **Pull Request** [\[processor/batch\] Honor Shutdown context during final flush](https://github.com/open-telemetry/opentelemetry-collector/pull/15602) — 3 comments · 0 reactions · closed
- **Pull Request** [fix(configtls): use correct variable in invalid curve type error message](https://github.com/open-telemetry/opentelemetry-collector/pull/15605) — 3 comments · 0 reactions · closed
- **Pull Request** [fix: treat key_strindex==0 as not-set sentinel (inline key erase) \[fj4WqyCCw3C5ShR1RfB7MoBPTpkRrBFYP1uT35g3MvT\]](https://github.com/open-telemetry/opentelemetry-collector/pull/15796) — 3 comments · 0 reactions · closed
- **Pull Request** [fix: bound memory growth in queuebatch split path by flushing incrementally \[fj4WqyCCw3C5ShR1RfB7MoBPTpkRrBFYP1uT35g3MvT\]](https://github.com/open-telemetry/opentelemetry-collector/pull/15798) — 2 comments · 0 reactions · open

### [Datadog Agent](https://github.com/DataDog/datadog-agent)

- **Release** [7.82.2](https://github.com/DataDog/datadog-agent/releases/tag/7.82.2) — 
- **Pull Request** [\[procmgr\] Show profile and user in list and describe](https://github.com/DataDog/datadog-agent/pull/53568) — 45 comments · 2 reactions · closed
- **Pull Request** [Update module google.golang.org/protobuf to v1.36.12](https://github.com/DataDog/datadog-agent/pull/55142) — 24 comments · 1 reactions · closed
- **Pull Request** [\[procmgr\] Windows spawn profiles foundation](https://github.com/DataDog/datadog-agent/pull/54731) — 74 comments · 1 reactions · open
- **Pull Request** [\[NETPATH-1118\] Enable traceroute for CNM Dynamic Tests](https://github.com/DataDog/datadog-agent/pull/55161) — 24 comments · 0 reactions · open
- **Pull Request** [\[NETPATH-1118\] Add baseline dynamic tests for CNM](https://github.com/DataDog/datadog-agent/pull/55075) — 38 comments · 1 reactions · closed
- **Pull Request** [Convert linux_bpf to linux && bpf build tags](https://github.com/DataDog/datadog-agent/pull/55099) — 6 comments · 2 reactions · closed
- **Pull Request** [\[DO NOT MERGE\] One-off e2e run with ADP enabled by default](https://github.com/DataDog/datadog-agent/pull/53415) — 6 comments · 1 reactions · open
- **Pull Request** [\[ABLD-294\] Bump `rules_go` to embed `go.mod` data in Go binaries](https://github.com/DataDog/datadog-agent/pull/54995) — 6 comments · 1 reactions · closed
- **Pull Request** [Add support for renamed settings](https://github.com/DataDog/datadog-agent/pull/53496) — 5 comments · 1 reactions · open
- **Pull Request** [\[WP\] Fix ICMPv4 packet flow classification](https://github.com/DataDog/datadog-agent/pull/54157) — 5 comments · 1 reactions · open
- **Pull Request** [\[WP\] Add info in ptrace error log](https://github.com/DataDog/datadog-agent/pull/55061) — 4 comments · 1 reactions · closed
- **Pull Request** [\[SMP\] Update CLI to v0.28.0 and lading to 0.33.0](https://github.com/DataDog/datadog-agent/pull/55135) — 4 comments · 1 reactions · closed
- **Pull Request** [\[CWS\] Go pprof-label span-context reader + legacy TLS removal](https://github.com/DataDog/datadog-agent/pull/53988) — 7 comments · 0 reactions · open
- **Pull Request** [smp experiment selection](https://github.com/DataDog/datadog-agent/pull/54933) — 6 comments · 0 reactions · open
- **Pull Request** [\[CWS\] kmt: run x86 security-agent tests on z1d.metal](https://github.com/DataDog/datadog-agent/pull/55180) — 7 comments · 1 reactions · open
- **Pull Request** [\[WP\] Fix isolation re-apply mechanism](https://github.com/DataDog/datadog-agent/pull/54056) — 4 comments · 0 reactions · open
- **Pull Request** [\[CWS-6628\] Implement the unshare syscall event](https://github.com/DataDog/datadog-agent/pull/54609) — 5 comments · 0 reactions · open
- **Pull Request** [test(aix): skip unit tests unsupported on AIX](https://github.com/DataDog/datadog-agent/pull/54975) — 4 comments · 0 reactions · open
- **Pull Request** [compliance/k8sconfig: fix kubelet defaults when --config is used](https://github.com/DataDog/datadog-agent/pull/55127) — 4 comments · 0 reactions · open
- **Pull Request** [Add cws-btfhub-sync skill](https://github.com/DataDog/datadog-agent/pull/54297) — 2 comments · 0 reactions · open
- **Pull Request** [fix(cws): add the mnt_namespace.ns offset when reading a mount namespace ID](https://github.com/DataDog/datadog-agent/pull/55192) — 6 comments · 0 reactions · open
- **Pull Request** [flatten ActivityTreeNodeStats to reduce heap allocations](https://github.com/DataDog/datadog-agent/pull/46469) — 4 comments · 0 reactions · closed
- **Pull Request** [\[CWS\] Do not run test container with all privileges](https://github.com/DataDog/datadog-agent/pull/46544) — 4 comments · 0 reactions · closed
- **Pull Request** [\[CWS\] Host-wide capture window on the V2 security profile manager](https://github.com/DataDog/datadog-agent/pull/54453) — 5 comments · 0 reactions · open
- **Pull Request** [Group CWS functional tests by module config](https://github.com/DataDog/datadog-agent/pull/54544) — 4 comments · 0 reactions · open
- **Issue** [\[BUG\] Cluster Agent External Metrics Provider returns HTTP 500 for "no serie found" — should return 422 to enable downstream FillValue/fallback handling](https://github.com/DataDog/datadog-agent/issues/46843) — 3 comments · 4 reactions · open
- **Pull Request** [apm: use url.template for OTLP HTTP client resource names](https://github.com/DataDog/datadog-agent/pull/54496) — 12 comments · 2 reactions · open
- **Pull Request** [Add additional approvers to static quality gate EXCEPTION_APPROVERS](https://github.com/DataDog/datadog-agent/pull/54861) — 11 comments · 2 reactions · open
- **Pull Request** [\[procmgr\] Config gates for processes.d auto-start](https://github.com/DataDog/datadog-agent/pull/54732) — 12 comments · 1 reactions · open

### [Prometheus](https://github.com/prometheus/prometheus)

- **Issue** [otlp endpoint: No metric translation by default](https://github.com/prometheus/prometheus/issues/14990) — 5 comments · 3 reactions · open
- **Issue** [promql: Make `promql-delayed-name-removal` the default](https://github.com/prometheus/prometheus/issues/15855) — 11 comments · 0 reactions · open
- **Issue** [Remove support for TSDB V1 format (in Prometheus 4)](https://github.com/prometheus/prometheus/issues/17681) — 8 comments · 0 reactions · open
- **Issue** [PromQL: Consider requiring constant numeric parameters for aggregations](https://github.com/prometheus/prometheus/issues/16358) — 0 comments · 1 reactions · open
- **Issue** [config: Change default of scrape_native_histograms and send_native_histograms to true](https://github.com/prometheus/prometheus/issues/17396) — 1 comments · 1 reactions · open
- **Issue** [Proposal: combine 'promtool' and 'prometheus' binaries in Prometheus 4](https://github.com/prometheus/prometheus/issues/13571) — 3 comments · 0 reactions · open
- **Issue** [instrumentation: remove summaries that have been replaced by native histograms, reduce/remove classic buckets](https://github.com/prometheus/prometheus/issues/17333) — 3 comments · 0 reactions · open
- **Issue** [scrape: Have a static default for `scrape_protocols`](https://github.com/prometheus/prometheus/issues/17336) — 2 comments · 0 reactions · open
- **Issue** [Make metric metadata parameters more consistent](https://github.com/prometheus/prometheus/issues/12862) — 1 comments · 0 reactions · open
- **Issue** [Expand scrape_config_files in the /config web UI endpoint](https://github.com/prometheus/prometheus/issues/12591) — 6 comments · 4 reactions · closed
- **Pull Request** [chore(deps): update module golang.org/x/mod to v0.40.0 \[security\]](https://github.com/prometheus/prometheus/pull/19419) — 1 comments · 0 reactions · open
- **Pull Request** [chore(deps): update module github.com/google/cel-go to v0.30.0 \[security\]](https://github.com/prometheus/prometheus/pull/19451) — 0 comments · 0 reactions · open
- **Issue** [Dependency Dashboard](https://github.com/prometheus/prometheus/issues/17691) — 5 comments · 0 reactions · open
- **Issue** [Deltas: add PromQL function to disable processing of start times](https://github.com/prometheus/prometheus/issues/19264) — 3 comments · 0 reactions · open
- **Issue** [Make XOR2 the default Chunk Encoding](https://github.com/prometheus/prometheus/issues/19080) — 3 comments · 0 reactions · open
- **Pull Request** [ui: show effective scrape pool configuration](https://github.com/prometheus/prometheus/pull/19384) — 7 comments · 0 reactions · closed
- **Pull Request** [scrape: detect duplicate series after metric relabeling](https://github.com/prometheus/prometheus/pull/19305) — 9 comments · 0 reactions · open
- **Pull Request** [discovery/aws: paginate Lightsail GetInstances so all instances are discovered](https://github.com/prometheus/prometheus/pull/19180) — 2 comments · 0 reactions · open
- **Pull Request** [promtool: add rule test coverage reporting](https://github.com/prometheus/prometheus/pull/18432) — 1 comments · 0 reactions · open
- **Pull Request** [fix(deps): update kubernetes go dependencies to v0.36.3](https://github.com/prometheus/prometheus/pull/18757) — 1 comments · 0 reactions · open
- **Pull Request** [discovery/azure: run tests in parallel](https://github.com/prometheus/prometheus/pull/18940) — 0 comments · 0 reactions · open
- **Pull Request** [Avoid locking HEAD shards when running gc](https://github.com/prometheus/prometheus/pull/19421) — 1 comments · 0 reactions · open
- **Pull Request** [promql: fix panic in extendFloats on a series with an empty window](https://github.com/prometheus/prometheus/pull/19431) — 0 comments · 0 reactions · open
- **Pull Request** [tsdb: fix in-order chunk ID overflow via modular wrapping](https://github.com/prometheus/prometheus/pull/19450) — 1 comments · 0 reactions · open
- **Pull Request** [PromQL: Do not register start timestamp reset if ST hasn't changed](https://github.com/prometheus/prometheus/pull/19454) — 0 comments · 0 reactions · open
- **Pull Request** [tsdb: stabilize the XOR2 float chunk encoding](https://github.com/prometheus/prometheus/pull/19461) — 0 comments · 0 reactions · open
- **Pull Request** [promql: fix sort_by_label tie-break for natural-equal labels](https://github.com/prometheus/prometheus/pull/19466) — 0 comments · 0 reactions · open
- **Pull Request** [Scrape: Dropping metadata when label is dropped](https://github.com/prometheus/prometheus/pull/19467) — 1 comments · 0 reactions · open
- **Pull Request** [perf(scrape): optimize series cache lookups](https://github.com/prometheus/prometheus/pull/19468) — 0 comments · 0 reactions · open
- **Pull Request** [tsdb: retry appends when GC retires the resolved series](https://github.com/prometheus/prometheus/pull/19469) — 0 comments · 0 reactions · open

### [Loki](https://github.com/grafana/loki)

- **Issue** [Latest version missing .deb package(3.7.3)](https://github.com/grafana/loki/issues/22851) — 6 comments · 8 reactions · open
- **Issue** [Regression (3.6.0+): compactor retention fails on boltdb-shipper chunks spanning an index-period boundary ("could not find entry of chunk ... to remove it")](https://github.com/grafana/loki/issues/23358) — 1 comments · 2 reactions · open
- **Issue** [Tailing leaks BaseLabelsBuilder.resultCache — regression of #6152, reintroduced by #9949](https://github.com/grafana/loki/issues/24031) — 0 comments · 0 reactions · open
- **Issue** [Proposal: Add native OCI Object Storage support via Thanos objstore.](https://github.com/grafana/loki/issues/23687) — 1 comments · 5 reactions · open
- **Pull Request** [fix(security/UNKNOWN/): Update module golang.org/x/mod to v0.40.0 \[SECURITY\] (release-3.7.x)](https://github.com/grafana/loki/pull/23962) — 1 comments · 0 reactions · closed
- **Pull Request** [fix(security/UNKNOWN/): Update module go.etcd.io/etcd/client/pkg/v3 to v3.6.14 \[SECURITY\] (release-3.7.x)](https://github.com/grafana/loki/pull/24061) — 0 comments · 0 reactions · closed
- **Issue** [introduce columnar chunk format](https://github.com/grafana/loki/issues/5723) — 5 comments · 3 reactions · open
- **Pull Request** [fix(security/UNKNOWN/): Update module github.com/containerd/containerd/v2 to v2.2.5 \[SECURITY\] (release-3.7.x)](https://github.com/grafana/loki/pull/24097) — 0 comments · 0 reactions · closed
- **Issue** [ingester logs "Ingester is shutting down" non-stop](https://github.com/grafana/loki/issues/23769) — 6 comments · 0 reactions · open
- **Issue** [Logs disapear from querier every 3 days but re-appears when recreating the containers](https://github.com/grafana/loki/issues/22638) — 9 comments · 0 reactions · open
- **Issue** [approx_topk() fails with parse error when using operator's custom LogQL parser](https://github.com/grafana/loki/issues/23150) — 6 comments · 0 reactions · open
- **Issue** [\[helm\] Zone-aware ingester StatefulSets emit a duplicate `name` label and become invalid when `ingester.podLabels.name` is set](https://github.com/grafana/loki/issues/23919) — 2 comments · 0 reactions · closed
- **Issue** [Dependency Dashboard](https://github.com/grafana/loki/issues/23439) — 0 comments · 0 reactions · open
- **Issue** [\[helm\] - its very confusing to figure out the correct loki chart for oss users](https://github.com/grafana/loki/issues/23964) — 1 comments · 0 reactions · open
- **Issue** [indexgateway: Cap client-side in-flight requests to avoid retry amplification when all replicas shed](https://github.com/grafana/loki/issues/24051) — 1 comments · 0 reactions · open
- **Issue** [Metric queries and log queries cover different time ranges for the same request](https://github.com/grafana/loki/issues/24093) — 0 comments · 0 reactions · open
- **Pull Request** [\[DO NOT MERGE\] LogQL metric queries with stream-first iteration (prototype)](https://github.com/grafana/loki/pull/23641) — 8 comments · 0 reactions · open
- **Pull Request** [feat(storage): Add OCI Thanos object store backend](https://github.com/grafana/loki/pull/23710) — 9 comments · 0 reactions · open
- **Issue** [Loki query performance is slow](https://github.com/grafana/loki/issues/22572) — 2 comments · 0 reactions · open
- **Issue** [Azure backend config does not support http_config](https://github.com/grafana/loki/issues/22870) — 2 comments · 0 reactions · open
- **Issue** [Logcli: structured metadata is missing when using --tail after first batch of messages are shown](https://github.com/grafana/loki/issues/22928) — 3 comments · 0 reactions · open
- **Issue** [pattern tee: nil-pointer panic in distributor - TenantConfigs nil because PatternIngesterTee lacks TenantConfigs module dependency](https://github.com/grafana/loki/issues/23076) — 2 comments · 0 reactions · open
- **Issue** [panic: runtime error: index out of range \[-1\] github.com/grafana/loki/v3/pkg/logproto.encodeVarintLogproto](https://github.com/grafana/loki/issues/23376) — 2 comments · 0 reactions · open
- **Issue** [\[loki\] Document StatefulSet-immutable Helm values and upgrade/migration notes (Flux/SSA)](https://github.com/grafana/loki/issues/23912) — 2 comments · 0 reactions · closed
- **Issue** [Loki Label filter improve performance](https://github.com/grafana/loki/issues/6082) — 3 comments · 0 reactions · open
- **Pull Request** [docs: Note that index/stats and index/volume are not deletion-aware](https://github.com/grafana/loki/pull/23866) — 6 comments · 0 reactions · open
- **Issue** [Compactor delete-request-store initialization fails independently of the main S3 object-store client](https://github.com/grafana/loki/issues/22376) — 1 comments · 0 reactions · open
- **Issue** [\[Helm\] extraObjects: tpl re-evaluates user content, breaking Prometheus/Loki ruler templates ({{ $labels }}, {{ $value }})](https://github.com/grafana/loki/issues/22416) — 1 comments · 0 reactions · closed
- **Issue** [\u0022 unicode escaping in log messages on .NET 10](https://github.com/grafana/loki/issues/22481) — 1 comments · 0 reactions · open
- **Issue** [LogQL: Pretty printing json/logfmt logs](https://github.com/grafana/loki/issues/22511) — 1 comments · 0 reactions · open
