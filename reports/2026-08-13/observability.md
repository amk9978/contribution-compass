# Observability & Reliability — 2026-08-13

> Factual GitHub evidence collected by Contribution Compass. No LLM analysis is performed.

## Contribution Leads

### [Duplicate log lines can be introduced by automatic stream sharding](https://github.com/grafana/loki/issues/18760)

- Project: `grafana/loki`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

## Important Updates

### [OpenTelemetry Collector](https://github.com/open-telemetry/opentelemetry-collector)

- **Issue** [`otelcol_exporter_queue_batch_send_size_bytes` records size for batches coming to the queue](https://github.com/open-telemetry/opentelemetry-collector/issues/14674) — 10 comments · 1 reactions · closed
- **Pull Request** [exporterhelper: record queue batch send size after batching](https://github.com/open-telemetry/opentelemetry-collector/pull/15510) — 9 comments · 1 reactions · closed
- **Issue** [Dependency Dashboard](https://github.com/open-telemetry/opentelemetry-collector/issues/8903) — 0 comments · 0 reactions · open
- **Issue** [\[exporterhelper\] Unbounded memory growth in queuebatch split path when flush workers are starved by a slow-draining exporter (sizer: bytes)](https://github.com/open-telemetry/opentelemetry-collector/issues/15747) — 2 comments · 0 reactions · open
- **Pull Request** [fix(memorylimiter): report health status only on state changes](https://github.com/open-telemetry/opentelemetry-collector/pull/15756) — 2 comments · 0 reactions · open
- **Pull Request** [Update github-actions deps](https://github.com/open-telemetry/opentelemetry-collector/pull/15576) — 1 comments · 0 reactions · open
- **Pull Request** [\[chore\]\[component/componentstatus\]: remove timestamp removal TODO](https://github.com/open-telemetry/opentelemetry-collector/pull/15757) — 0 comments · 0 reactions · open
- **Pull Request** [\[chore\]\[cmd/mdatagen\] Handle subpackage metadata.yaml in config generator](https://github.com/open-telemetry/opentelemetry-collector/pull/15735) — 1 comments · 0 reactions · open
- **Pull Request** [Update module github.com/pierrec/lz4/v4 to v4.1.28](https://github.com/open-telemetry/opentelemetry-collector/pull/15752) — 1 comments · 0 reactions · open
- **Pull Request** [Update module golang.org/x/mod to v0.39.0](https://github.com/open-telemetry/opentelemetry-collector/pull/15755) — 1 comments · 0 reactions · closed

### [Datadog Agent](https://github.com/DataDog/datadog-agent)

- **Pull Request** [Increase Quality Gate memory thresholds for ADP pre-flight mode](https://github.com/DataDog/datadog-agent/pull/54792) — 5 comments · 2 reactions · open
- **Pull Request** [\[CWS\] Fix: handle activity dump endpoint host that already embeds a port](https://github.com/DataDog/datadog-agent/pull/54774) — 4 comments · 2 reactions · closed
- **Pull Request** [\[WP\] ICMPv4 packet flow classification](https://github.com/DataDog/datadog-agent/pull/54157) — 6 comments · 1 reactions · open
- **Pull Request** [\[CWS-6177\] Use dynamic sampling](https://github.com/DataDog/datadog-agent/pull/54471) — 5 comments · 1 reactions · open
- **Pull Request** [\[procmgr\] Windows spawn profiles foundation](https://github.com/DataDog/datadog-agent/pull/54731) — 29 comments · 1 reactions · open
- **Pull Request** [Split network-devices section in it's own file and fix ID links](https://github.com/DataDog/datadog-agent/pull/54769) — 1 comments · 1 reactions · open
- **Pull Request** [SMP experiment selection and codeowners v2](https://github.com/DataDog/datadog-agent/pull/54833) — 5 comments · 1 reactions · open
- **Pull Request** [ci: default GitLab jobs to shallow clones, keep full history where needed](https://github.com/DataDog/datadog-agent/pull/54834) — 4 comments · 1 reactions · open
- **Pull Request** [feat(autodiscovery): tag configuration-discovery instances to mitigate duplicate metrics risk](https://github.com/DataDog/datadog-agent/pull/54660) — 8 comments · 3 reactions · closed
- **Pull Request** [Add source to distributions via checks.](https://github.com/DataDog/datadog-agent/pull/51295) — 8 comments · 2 reactions · open
- **Pull Request** [packaging/aix: use rmssys only in unconfig, drop odmdelete](https://github.com/DataDog/datadog-agent/pull/51861) — 6 comments · 2 reactions · closed
- **Pull Request** [\[EBPF\] gpu: serialize NVML field value queries](https://github.com/DataDog/datadog-agent/pull/54821) — 6 comments · 2 reactions · open
- **Pull Request** [Unify converter features behavior](https://github.com/DataDog/datadog-agent/pull/52993) — 5 comments · 2 reactions · open
- **Pull Request** [fix(cluster-agent): gate pprof/expvar debug endpoints to loopback](https://github.com/DataDog/datadog-agent/pull/54508) — 8 comments · 1 reactions · closed
- **Pull Request** [Update ownership/notifications for delegatedauth component+code](https://github.com/DataDog/datadog-agent/pull/54539) — 4 comments · 3 reactions · open
- **Pull Request** [fix: avoid data race in grpclog.SetLogger on otelcol collector start](https://github.com/DataDog/datadog-agent/pull/54645) — 8 comments · 1 reactions · open
- **Pull Request** [Remove schemaBuilder and createschema command](https://github.com/DataDog/datadog-agent/pull/54793) — 5 comments · 2 reactions · open
- **Pull Request** [fix(installer): embed -nocap systemd unit templates](https://github.com/DataDog/datadog-agent/pull/54804) — 4 comments · 2 reactions · open
- **Pull Request** [Remove bazel strptime_cgo_testlib override](https://github.com/DataDog/datadog-agent/pull/54810) — 5 comments · 2 reactions · closed
- **Pull Request** [\[AGENTRUN-1446\] Skip nss failover e2e test it if the fakeintakes are still in use](https://github.com/DataDog/datadog-agent/pull/54814) — 4 comments · 2 reactions · open
- **Pull Request** [\[DSEC\] Move dd-sds dependency to shared workspace](https://github.com/DataDog/datadog-agent/pull/54815) — 5 comments · 2 reactions · open
- **Pull Request** [Copy python files to avoid junction issues](https://github.com/DataDog/datadog-agent/pull/54819) — 5 comments · 2 reactions · open
- **Pull Request** [Deflake `TestKeepTryingLockingIfPermissionDenied` with `synctest`](https://github.com/DataDog/datadog-agent/pull/54830) — 4 comments · 2 reactions · open
- **Pull Request** [WIF-48: add delegated-auth dual-shipping foundation](https://github.com/DataDog/datadog-agent/pull/53517) — 7 comments · 1 reactions · open
- **Pull Request** [\[WINA-2940\] Break Group Policy passes into timed CSE invocations](https://github.com/DataDog/datadog-agent/pull/54546) — 6 comments · 1 reactions · open
- **Pull Request** [optimize the complexity of the trace_contention_begin](https://github.com/DataDog/datadog-agent/pull/54634) — 7 comments · 1 reactions · open
- **Pull Request** [\[procmgr\] Extract shared Rust client](https://github.com/DataDog/datadog-agent/pull/54676) — 3 comments · 2 reactions · open
- **Pull Request** [test(ndm): add e2e coverage for Agent Workload Balancing](https://github.com/DataDog/datadog-agent/pull/54795) — 7 comments · 1 reactions · closed
- **Pull Request** [\[Backport 7.82.x\]  \[EBPF\] Gate NVML workloadmeta collector on GPU monitoring](https://github.com/DataDog/datadog-agent/pull/54805) — 3 comments · 2 reactions · closed
- **Pull Request** [Move tools/tar_checksums to bazel/tools](https://github.com/DataDog/datadog-agent/pull/54812) — 2 comments · 2 reactions · closed

### [Prometheus](https://github.com/prometheus/prometheus)

- **Pull Request** [model/textparse: implement OM2 scrape format](https://github.com/prometheus/prometheus/pull/18606) — 6 comments · 0 reactions · open
- **Pull Request** [promql/parser: preserve parentheses around duration literals](https://github.com/prometheus/prometheus/pull/19403) — 1 comments · 0 reactions · open
- **Pull Request** [discovery/kubernetes: populate loadbalancer IP from status.ingress](https://github.com/prometheus/prometheus/pull/19404) — 0 comments · 0 reactions · open
- **Pull Request** [discovery/aws: don't panic on ElastiCache caches with absent optional fields](https://github.com/prometheus/prometheus/pull/19405) — 0 comments · 0 reactions · open
- **Pull Request** [discovery/file: wait for a matching snapshot instead of failing on empty updates](https://github.com/prometheus/prometheus/pull/19407) — 1 comments · 0 reactions · open
- **Pull Request** [tsdb: release oversized head-chunk cache for single-chunk series](https://github.com/prometheus/prometheus/pull/19412) — 0 comments · 0 reactions · open
- **Pull Request** [scrape: keep staleness tracking in sync when the series ref changes](https://github.com/prometheus/prometheus/pull/19328) — 1 comments · 0 reactions · open
- **Pull Request** [promql: preserve name-dropping through the info function](https://github.com/prometheus/prometheus/pull/19413) — 0 comments · 0 reactions · open
- **Pull Request** [Agent wal](https://github.com/prometheus/prometheus/pull/19414) — 0 comments · 0 reactions · open

### [Loki](https://github.com/grafana/loki)

- **Issue** [Dependency Dashboard](https://github.com/grafana/loki/issues/23439) — 0 comments · 0 reactions · open
- **Pull Request** [feat(indexgateway): Add admission control to bound concurrent requests](https://github.com/grafana/loki/pull/23932) — 2 comments · 0 reactions · open
- **Pull Request** [fix(deps): Update github.com/prometheus/prometheus digest to 3c82a95 (main)](https://github.com/grafana/loki/pull/23627) — 1 comments · 0 reactions · open
- **Pull Request** [test(logql): Run logqltest scripts through query-frontend and query-scheduler](https://github.com/grafana/loki/pull/23909) — 0 comments · 0 reactions · open
- **Pull Request** [docs: Add Apache APISIX to third-party clients 🤖🤖🤖](https://github.com/grafana/loki/pull/23934) — 1 comments · 0 reactions · closed
- **Pull Request** [fix(deps): Update module github.com/redis/go-redis/v9 to v9.22.0 (main)](https://github.com/grafana/loki/pull/23806) — 0 comments · 0 reactions · open
- **Pull Request** [fix(logql): Fix ip() line filter matching inside "or" chains](https://github.com/grafana/loki/pull/23940) — 0 comments · 0 reactions · open
- **Pull Request** [fix(deps): Update module google.golang.org/protobuf to v1.36.12 (main)](https://github.com/grafana/loki/pull/23941) — 0 comments · 0 reactions · closed
- **Pull Request** [fix(logql): Avoid data race in sharded avg_over_time grouping](https://github.com/grafana/loki/pull/23942) — 0 comments · 0 reactions · open
- **Pull Request** [fix(chunkenc): Stop counting filtered-out lines in post_filter_lines](https://github.com/grafana/loki/pull/23943) — 0 comments · 0 reactions · open
