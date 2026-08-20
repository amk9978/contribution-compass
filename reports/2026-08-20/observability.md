# Observability & Reliability — 2026-08-20

> Factual GitHub evidence collected by Contribution Compass. No LLM analysis is performed.

## Contribution Leads

### [Replace `go.uber.go/atomic` with Go standard library `sync/atomic`](https://github.com/grafana/loki/issues/20673)

- Project: `grafana/loki`
- Tier: `maintainer-invited`
- Evidence: Maintainer invitation label: good first issue; No assignee is listed
- Caveat: Confirm scope and availability with the maintainers before starting work.

## Important Updates

### [OpenTelemetry Collector](https://github.com/open-telemetry/opentelemetry-collector)

- **Issue** [\[confmap\] is not preserving the original type when a slice of a map is unmarshalled](https://github.com/open-telemetry/opentelemetry-collector/issues/12793) — 13 comments · 0 reactions · closed
- **Pull Request** [\[confighttp\] Move keepalive config into a dedicated optional section](https://github.com/open-telemetry/opentelemetry-collector/pull/15308) — 12 comments · 2 reactions · open
- **Issue** [Components using sharedcomponent may emit invalid status sequences](https://github.com/open-telemetry/opentelemetry-collector/issues/14692) — 2 comments · 0 reactions · closed
- **Issue** [Add `freebsd/amd64` to platform tier-3](https://github.com/open-telemetry/opentelemetry-collector/issues/15781) — 3 comments · 0 reactions · open
- **Issue** [Add `solaris/amd64` to platform tier-3](https://github.com/open-telemetry/opentelemetry-collector/issues/15782) — 3 comments · 0 reactions · open
- **Issue** [\[cmd/mdatagen\] \[filter\] Allow wildcard patterns as a filtering option](https://github.com/open-telemetry/opentelemetry-collector/issues/15652) — 4 comments · 0 reactions · open
- **Issue** [Dependency Dashboard](https://github.com/open-telemetry/opentelemetry-collector/issues/8903) — 0 comments · 0 reactions · open
- **Pull Request** [\[exporter/exporterhelper\] Add cardinality_limit for the batch partitions](https://github.com/open-telemetry/opentelemetry-collector/pull/15225) — 13 comments · 0 reactions · open
- **Pull Request** [fix(service): prevent deadlock when reporting fatal errors during shutdown](https://github.com/open-telemetry/opentelemetry-collector/pull/15428) — 12 comments · 0 reactions · open
- **Issue** [Collector json log output is intermingled with non-json output](https://github.com/open-telemetry/opentelemetry-collector/issues/12378) — 1 comments · 0 reactions · closed
- **Issue** [\[processor/memorylimiter\] Only send component status events when status changed](https://github.com/open-telemetry/opentelemetry-collector/issues/15751) — 0 comments · 0 reactions · closed
- **Pull Request** [Update module github.com/golangci/golangci-lint/v2 to v2.13.0](https://github.com/open-telemetry/opentelemetry-collector/pull/14677) — 5 comments · 0 reactions · open
- **Pull Request** [\[confmap\] Remove dead isStringyStructure and add regression test](https://github.com/open-telemetry/opentelemetry-collector/pull/15746) — 4 comments · 0 reactions · closed
- **Pull Request** [fix(memorylimiter): report health status only on state changes](https://github.com/open-telemetry/opentelemetry-collector/pull/15756) — 5 comments · 0 reactions · closed
- **Pull Request** [Update module github.com/dkorunic/betteralign to v0.14.4](https://github.com/open-telemetry/opentelemetry-collector/pull/15113) — 2 comments · 0 reactions · open
- **Pull Request** [\[confignet\] Allow setting security descriptors for npipes](https://github.com/open-telemetry/opentelemetry-collector/pull/15212) — 7 comments · 0 reactions · open
- **Pull Request** [Update github-actions deps](https://github.com/open-telemetry/opentelemetry-collector/pull/15576) — 2 comments · 0 reactions · open
- **Pull Request** [Update github-actions deps (major)](https://github.com/open-telemetry/opentelemetry-collector/pull/15579) — 2 comments · 0 reactions · open
- **Pull Request** [feat: add support for identity compression algorithm in confighttp](https://github.com/open-telemetry/opentelemetry-collector/pull/15656) — 3 comments · 0 reactions · open
- **Pull Request** [\[memorylimiter\] Add disable_gc configuration option (rebased)](https://github.com/open-telemetry/opentelemetry-collector/pull/15666) — 3 comments · 1 reactions · open
- **Pull Request** [\[service/telemetry\] Route OTel SDK internal errors through the collec…](https://github.com/open-telemetry/opentelemetry-collector/pull/15695) — 3 comments · 0 reactions · closed
- **Pull Request** [\[chore\] Move axw to emeritus](https://github.com/open-telemetry/opentelemetry-collector/pull/15726) — 2 comments · 1 reactions · closed
- **Pull Request** [Implement DSCP (Differentiated Services Code Point)](https://github.com/open-telemetry/opentelemetry-collector/pull/15733) — 2 comments · 0 reactions · open
- **Pull Request** [\[extension/memorylimiterextension\] Add otelcol_memorylimiter_refused_requests metric](https://github.com/open-telemetry/opentelemetry-collector/pull/15738) — 2 comments · 0 reactions · open
- **Pull Request** [\[chore\]\[component/componentstatus\]: remove timestamp removal TODO](https://github.com/open-telemetry/opentelemetry-collector/pull/15757) — 3 comments · 0 reactions · closed
- **Pull Request** [\[chore\] \[exporterhelper\] Remove obsolete readIndex workaround in persistent queue test](https://github.com/open-telemetry/opentelemetry-collector/pull/15764) — 2 comments · 0 reactions · closed
- **Pull Request** [\[exporter/otlp_http\] Prevent retries when body parsing fails on successful HTTP exports](https://github.com/open-telemetry/opentelemetry-collector/pull/15389) — 5 comments · 0 reactions · closed
- **Pull Request** [\[chore\]\[cmd/mdatagen\] fix confmap import in resource test generation template](https://github.com/open-telemetry/opentelemetry-collector/pull/15760) — 0 comments · 0 reactions · open
- **Pull Request** [\[chore\]\[sharedcomponent\] Fix lifecycle status duplication and start-error propagation](https://github.com/open-telemetry/opentelemetry-collector/pull/15762) — 1 comments · 0 reactions · closed
- **Pull Request** [\[exporterhelper\] Inject queue and batch metrics](https://github.com/open-telemetry/opentelemetry-collector/pull/15770) — 1 comments · 0 reactions · open

### [Datadog Agent](https://github.com/DataDog/datadog-agent)

- **Pull Request** [\[procmgr\] Show profile and user in list and describe](https://github.com/DataDog/datadog-agent/pull/53568) — 43 comments · 2 reactions · open
- **Pull Request** [\[procmgr\] Windows spawn profiles foundation](https://github.com/DataDog/datadog-agent/pull/54731) — 62 comments · 1 reactions · open
- **Pull Request** [\[NETPATH-1122\] Add baseline Dynamic Tests for CNM (deprecated version)](https://github.com/DataDog/datadog-agent/pull/54938) — 51 comments · 1 reactions · closed
- **Pull Request** [\[SBOM\] Refresh every image when spreading the refresh](https://github.com/DataDog/datadog-agent/pull/54715) — 10 comments · 2 reactions · closed
- **Pull Request** [\[NETPATH-1118\] Add baseline dynamic tests for CNM](https://github.com/DataDog/datadog-agent/pull/55075) — 38 comments · 1 reactions · open
- **Pull Request** [test: speed up slow unit tests with testing/synctest](https://github.com/DataDog/datadog-agent/pull/54977) — 9 comments · 2 reactions · closed
- **Pull Request** [\[SBOM\] Skip images whose SBOM cannot be uncompressed](https://github.com/DataDog/datadog-agent/pull/54714) — 10 comments · 1 reactions · closed
- **Pull Request** [\[CWS\] Fix: handle activity dump endpoint host that already embeds a port](https://github.com/DataDog/datadog-agent/pull/54774) — 6 comments · 2 reactions · closed
- **Pull Request** [Convert linux_bpf to linux && bpf build tags](https://github.com/DataDog/datadog-agent/pull/55099) — 6 comments · 2 reactions · open
- **Pull Request** [Add support for renamed settings](https://github.com/DataDog/datadog-agent/pull/53496) — 5 comments · 1 reactions · open
- **Pull Request** [Remove unused ctx argument from bazel helper](https://github.com/DataDog/datadog-agent/pull/55038) — 4 comments · 1 reactions · closed
- **Pull Request** [\[WP\] Add info in ptrace error log](https://github.com/DataDog/datadog-agent/pull/55061) — 4 comments · 1 reactions · open
- **Pull Request** [\[CWS\] Go pprof-label span-context reader + legacy TLS removal](https://github.com/DataDog/datadog-agent/pull/53988) — 7 comments · 0 reactions · open
- **Pull Request** [\[Backport 7.83.x\] \[CWS\] Fix: handle activity dump endpoint host that already embeds a port](https://github.com/DataDog/datadog-agent/pull/55062) — 3 comments · 1 reactions · closed
- **Pull Request** [sbom: default runtime usage properties only on OS packages](https://github.com/DataDog/datadog-agent/pull/55110) — 7 comments · 1 reactions · open
- **Pull Request** [sbom: key the runtime enrichment dedup on bom-ref](https://github.com/DataDog/datadog-agent/pull/55111) — 7 comments · 1 reactions · open
- **Pull Request** [\[CWS\] fix matching sub-expression reporting in the And/Or operators](https://github.com/DataDog/datadog-agent/pull/54604) — 0 comments · 2 reactions · open
- **Pull Request** [\[CWS-6628\] Implement the unshare syscall event](https://github.com/DataDog/datadog-agent/pull/54609) — 5 comments · 0 reactions · open
- **Pull Request** [\[CWS\] Disable sysctl snapshots when required sysfs files are missing](https://github.com/DataDog/datadog-agent/pull/54898) — 4 comments · 0 reactions · closed
- **Pull Request** [test(aix): skip unit tests unsupported on AIX](https://github.com/DataDog/datadog-agent/pull/54975) — 5 comments · 0 reactions · open
- **Pull Request** [Userspace buffering of the ring buffer](https://github.com/DataDog/datadog-agent/pull/55003) — 5 comments · 0 reactions · open
- **Pull Request** [\[CWS-6779\] Implement the setns syscall](https://github.com/DataDog/datadog-agent/pull/55126) — 5 comments · 1 reactions · open
- **Pull Request** [\[SMP\] Update CLI to v0.28.0 and lading to 0.33.0](https://github.com/DataDog/datadog-agent/pull/55135) — 4 comments · 1 reactions · open
- **Pull Request** [feat(numa-monitoring): add experimental NUMA monitoring module and check](https://github.com/DataDog/datadog-agent/pull/54361) — 6 comments · 0 reactions · open
- **Pull Request** [\[Backport 7.83.x\]  \[CWS\] Fix: handle activity dump endpoint host that already embeds a port](https://github.com/DataDog/datadog-agent/pull/55092) — 3 comments · 1 reactions · closed
- **Pull Request** [\[CWS\] Buffer security profile v2 metrics in atomics](https://github.com/DataDog/datadog-agent/pull/55103) — 5 comments · 0 reactions · open
- **Pull Request** [sbom: warn when container image scanning has no container runtime](https://github.com/DataDog/datadog-agent/pull/55115) — 4 comments · 0 reactions · open
- **Pull Request** [compliance/k8sconfig: fix kubelet defaults when --config is used](https://github.com/DataDog/datadog-agent/pull/55127) — 4 comments · 0 reactions · open
- **Pull Request** [compliance/k8sconfig: do not report an unreadable file as empty](https://github.com/DataDog/datadog-agent/pull/55128) — 4 comments · 0 reactions · open
- **Pull Request** [apm: use url.template for OTLP HTTP client resource names](https://github.com/DataDog/datadog-agent/pull/54496) — 12 comments · 2 reactions · open

### [Prometheus](https://github.com/prometheus/prometheus)

- **Pull Request** [Update module golang.org/x/mod to v0.40.0 \[SECURITY\]](https://github.com/prometheus/prometheus/pull/19419) — 1 comments · 0 reactions · open
- **Pull Request** [Update module github.com/google/cel-go to v0.30.0 \[SECURITY\]](https://github.com/prometheus/prometheus/pull/19451) — 0 comments · 0 reactions · open
- **Issue** [Dependency Dashboard](https://github.com/prometheus/prometheus/issues/17691) — 5 comments · 0 reactions · open
- **Issue** [Remote-write should check that label names are valid](https://github.com/prometheus/prometheus/issues/11571) — 3 comments · 0 reactions · open
- **Pull Request** [model/textparse: implement OM2 scrape format](https://github.com/prometheus/prometheus/pull/18606) — 7 comments · 0 reactions · open
- **Pull Request** [ui: show effective scrape pool configuration](https://github.com/prometheus/prometheus/pull/19384) — 7 comments · 0 reactions · open
- **Pull Request** [web/api/v1: Fix tests that will always fail on windows - no guard/han…](https://github.com/prometheus/prometheus/pull/19369) — 4 comments · 0 reactions · closed
- **Pull Request** [discovery/stackit: add support for postgres targets discovery](https://github.com/prometheus/prometheus/pull/19400) — 4 comments · 0 reactions · open
- **Pull Request** [promql: test alignment of subquery end timestamp to parent's step grid](https://github.com/prometheus/prometheus/pull/18598) — 6 comments · 0 reactions · closed
- **Pull Request** [tsdb: fix ABBA lock-ordering deadlock in gc/gcSeries check callbacks](https://github.com/prometheus/prometheus/pull/19448) — 2 comments · 0 reactions · open
- **Pull Request** [promtool: add rule test coverage reporting](https://github.com/prometheus/prometheus/pull/18432) — 1 comments · 0 reactions · open
- **Pull Request** [config: support env var expansion in relabel_configs](https://github.com/prometheus/prometheus/pull/18457) — 4 comments · 0 reactions · open
- **Pull Request** [Update Kubernetes Go dependencies to v0.36.3](https://github.com/prometheus/prometheus/pull/18757) — 1 comments · 0 reactions · open
- **Pull Request** [tsdb: make panic lock-release test OS agnostic](https://github.com/prometheus/prometheus/pull/19339) — 0 comments · 0 reactions · closed
- **Pull Request** [discovery/aws: don't panic on ECS clusters configured by name](https://github.com/prometheus/prometheus/pull/19449) — 1 comments · 0 reactions · open
- **Pull Request** [tsdb: fix in-order chunk ID overflow via modular wrapping](https://github.com/prometheus/prometheus/pull/19450) — 0 comments · 0 reactions · open
- **Pull Request** [textparse: fix nil histogram when native and classic histograms are mixed in one metric family](https://github.com/prometheus/prometheus/pull/19452) — 0 comments · 0 reactions · open
- **Pull Request** [promql: fix typo in preprocessExprHelper comment](https://github.com/prometheus/prometheus/pull/19453) — 0 comments · 0 reactions · open
- **Pull Request** [PromQL: Do not register start timestamp reset if ST hasn't changed](https://github.com/prometheus/prometheus/pull/19454) — 0 comments · 0 reactions · open
- **Pull Request** [storage: make AppenderV2.AppendExemplars mandatory, drop it from Append](https://github.com/prometheus/prometheus/pull/19455) — 0 comments · 0 reactions · open
- **Pull Request** [docs: fix broken range vector selector link in query examples](https://github.com/prometheus/prometheus/pull/19456) — 0 comments · 0 reactions · open
- **Pull Request** [storage/remote: migrate Remote Write 1.0 receiver to AppenderV2](https://github.com/prometheus/prometheus/pull/19457) — 0 comments · 0 reactions · open
- **Pull Request** [Fix BenchmarkParsePromText for expfmt-promtext](https://github.com/prometheus/prometheus/pull/19458) — 0 comments · 0 reactions · closed
- **Pull Request** [storage/remote: migrate Remote Write 2.x receiver to AppenderV2](https://github.com/prometheus/prometheus/pull/19459) — 0 comments · 0 reactions · open
- **Pull Request** [tsdb: fix gcSeries and mmapHeadChunksInStripe deadlocking](https://github.com/prometheus/prometheus/pull/19460) — 0 comments · 0 reactions · open
- **Pull Request** [tsdb: stabilize the XOR2 float chunk encoding](https://github.com/prometheus/prometheus/pull/19461) — 0 comments · 0 reactions · open
- **Pull Request** [Reduce allocations when parsing labels](https://github.com/prometheus/prometheus/pull/19462) — 0 comments · 0 reactions · open
- **Pull Request** [web/api/v1: Enforce LF line endings via .gitattributes](https://github.com/prometheus/prometheus/pull/19463) — 0 comments · 0 reactions · open
- **Pull Request** [harden: this pnpm workspace configuration does not set ... in...](https://github.com/prometheus/prometheus/pull/19464) — 0 comments · 0 reactions · open
- **Pull Request** [ci: run the oldest Go tests on 1.26](https://github.com/prometheus/prometheus/pull/19465) — 0 comments · 0 reactions · open

### [Loki](https://github.com/grafana/loki)

- **Pull Request** [fix(security/UNKNOWN/): Update module golang.org/x/mod to v0.40.0 \[SECURITY\] (release-3.7.x)](https://github.com/grafana/loki/pull/23962) — 1 comments · 0 reactions · open
- **Pull Request** [fix(security/UNKNOWN/): Update module golang.org/x/mod to v0.40.0 \[SECURITY\] (release-3.6.x)](https://github.com/grafana/loki/pull/23963) — 1 comments · 0 reactions · open
- **Pull Request** [fix(security/UNKNOWN/): Update module go.etcd.io/etcd/client/pkg/v3 to v3.5.33 \[SECURITY\] (release-3.6.x)](https://github.com/grafana/loki/pull/24062) — 0 comments · 0 reactions · closed
- **Issue** [Replace `go.uber.go/atomic` with Go standard library `sync/atomic`](https://github.com/grafana/loki/issues/20673) — 7 comments · 0 reactions · open
- **Issue** [Dependency Dashboard](https://github.com/grafana/loki/issues/23439) — 0 comments · 0 reactions · open
- **Pull Request** [\[DO NOT MERGE\] LogQL metric queries with stream-first iteration (prototype)](https://github.com/grafana/loki/pull/23641) — 8 comments · 0 reactions · open
- **Pull Request** [feat(storage): Add OCI Thanos object store backend](https://github.com/grafana/loki/pull/23710) — 9 comments · 0 reactions · open
- **Pull Request** [fix: Recognise thanos/minio S3 throttling errors as retryable](https://github.com/grafana/loki/pull/23454) — 2 comments · 1 reactions · closed
- **Pull Request** [docs: Note that index/stats and index/volume are not deletion-aware](https://github.com/grafana/loki/pull/23866) — 6 comments · 0 reactions · open
- **Issue** [\[helm\] Zone-aware ingester StatefulSets emit a duplicate `name` label and become invalid when `ingester.podLabels.name` is set](https://github.com/grafana/loki/issues/23919) — 1 comments · 0 reactions · open
- **Issue** [Metric queries and log queries cover different time ranges for the same request](https://github.com/grafana/loki/issues/24093) — 0 comments · 0 reactions · open
- **Pull Request** [feat(kafka): support configurable SASL mechanism (PLAIN, SCRAM-SHA-256, SCRAM-SHA-512)](https://github.com/grafana/loki/pull/21719) — 0 comments · 1 reactions · open
- **Pull Request** [chore: Chunk fetch failure policy](https://github.com/grafana/loki/pull/23973) — 4 comments · 0 reactions · open
- **Pull Request** [chore(deps): Update module go.etcd.io/etcd/client/v3 to v3.7.1 (main)](https://github.com/grafana/loki/pull/23000) — 2 comments · 0 reactions · open
- **Pull Request** [feat(logql): Add approx_count_distinct aggregation](https://github.com/grafana/loki/pull/23782) — 2 comments · 0 reactions · open
- **Pull Request** [fix(operator): Validate passthrough gateway CA exists](https://github.com/grafana/loki/pull/23800) — 3 comments · 0 reactions · open
- **Pull Request** [fix: Add meaningful chunk fetch loss metrics](https://github.com/grafana/loki/pull/23925) — 2 comments · 0 reactions · open
- **Pull Request** [feat(indexgateway): Add admission control to bound concurrent requests](https://github.com/grafana/loki/pull/23932) — 3 comments · 0 reactions · open
- **Pull Request** [fix(indexgateway): Cap client-side in-flight requests to avoid retry amplification](https://github.com/grafana/loki/pull/24057) — 2 comments · 0 reactions · open
- **Pull Request** [docs: Check storage schema topic for accuracy 🤖🤖🤖](https://github.com/grafana/loki/pull/24065) — 3 comments · 0 reactions · closed
- **Pull Request** [fix(deps): Update github.com/twmb/franz-go/pkg/kfake digest to beb096a (main)](https://github.com/grafana/loki/pull/22534) — 1 comments · 0 reactions · open
- **Pull Request** [fix(deps): Update github.com/prometheus/prometheus digest to b2b7990 (main)](https://github.com/grafana/loki/pull/23627) — 0 comments · 0 reactions · open
- **Pull Request** [chore(deps): Update golang:1.26.5 Docker digest to 705e964 (main) - autoclosed](https://github.com/grafana/loki/pull/23762) — 0 comments · 0 reactions · closed
- **Pull Request** [chore: PushWithResolver can be package private, no need for it to be exported](https://github.com/grafana/loki/pull/23881) — 0 comments · 0 reactions · closed
- **Pull Request** [fix(operator): Remove BoltDB alerts, recording rules, and Grafana dashboards](https://github.com/grafana/loki/pull/23884) — 0 comments · 0 reactions · closed
- **Pull Request** [chore: Log usage of failed queries with failure cause](https://github.com/grafana/loki/pull/23886) — 0 comments · 0 reactions · closed
- **Pull Request** [docs: Check Authentication topic for accuracy  🤖🤖🤖](https://github.com/grafana/loki/pull/24017) — 1 comments · 0 reactions · closed
- **Pull Request** [chore: Add new code to decompress the request body](https://github.com/grafana/loki/pull/24025) — 0 comments · 0 reactions · open
- **Pull Request** [docs: Check scalability topic for accuracy 🤖🤖🤖](https://github.com/grafana/loki/pull/24028) — 1 comments · 0 reactions · closed
- **Pull Request** [chore: Pool file handles](https://github.com/grafana/loki/pull/24037) — 1 comments · 0 reactions · closed
