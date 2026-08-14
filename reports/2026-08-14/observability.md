# Observability & Reliability — 2026-08-14

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

### [Support Loading Collector Configuration Files from a Directory](https://github.com/open-telemetry/opentelemetry-collector/issues/9596)

- Project: `open-telemetry/opentelemetry-collector`
- Tier: `triage-lead`
- Evidence: Unassigned enhancement with community reactions
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [Duplicate log lines can be introduced by automatic stream sharding](https://github.com/grafana/loki/issues/18760)

- Project: `grafana/loki`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

## Important Updates

### [OpenTelemetry Collector](https://github.com/open-telemetry/opentelemetry-collector)

- **Issue** [Support Loading Collector Configuration Files from a Directory](https://github.com/open-telemetry/opentelemetry-collector/issues/9596) — 13 comments · 15 reactions · open
- **Issue** [Dependency Dashboard](https://github.com/open-telemetry/opentelemetry-collector/issues/8903) — 0 comments · 0 reactions · open
- **Issue** [Components using sharedcomponent may emit invalid status sequences](https://github.com/open-telemetry/opentelemetry-collector/issues/14692) — 2 comments · 0 reactions · open
- **Pull Request** [Update module github.com/golangci/golangci-lint/v2 to v2.12.2](https://github.com/open-telemetry/opentelemetry-collector/pull/14677) — 5 comments · 0 reactions · open
- **Pull Request** [Update module github.com/knadh/koanf/maps to v0.1.3](https://github.com/open-telemetry/opentelemetry-collector/pull/15750) — 2 comments · 0 reactions · closed
- **Pull Request** [fix(memorylimiter): report health status only on state changes](https://github.com/open-telemetry/opentelemetry-collector/pull/15756) — 2 comments · 0 reactions · open
- **Pull Request** [Update github-actions deps](https://github.com/open-telemetry/opentelemetry-collector/pull/15576) — 1 comments · 0 reactions · open
- **Pull Request** [Update module github.com/klauspost/compress to v1.19.2](https://github.com/open-telemetry/opentelemetry-collector/pull/15749) — 1 comments · 0 reactions · closed
- **Pull Request** [\[chore\] update component status docs to describe current behavior](https://github.com/open-telemetry/opentelemetry-collector/pull/15759) — 1 comments · 0 reactions · open
- **Pull Request** [\[confighttp\] Preserve IPv6 zone when parsing client address](https://github.com/open-telemetry/opentelemetry-collector/pull/15506) — 3 comments · 0 reactions · closed
- **Pull Request** [\[chore\]\[cmd/mdatagen\] fix confmap import in resource_test.go template](https://github.com/open-telemetry/opentelemetry-collector/pull/15760) — 0 comments · 0 reactions · open

### [Datadog Agent](https://github.com/DataDog/datadog-agent)

- **Pull Request** [Increase Quality Gate memory thresholds for ADP pre-flight mode](https://github.com/DataDog/datadog-agent/pull/54792) — 5 comments · 2 reactions · closed
- **Pull Request** [fix(data plane): run preflight mode for entire SMP experiment duration](https://github.com/DataDog/datadog-agent/pull/54794) — 7 comments · 2 reactions · open
- **Pull Request** [\[procmgr\] Windows spawn profiles foundation](https://github.com/DataDog/datadog-agent/pull/54731) — 31 comments · 1 reactions · open
- **Pull Request** [Build with race detector](https://github.com/DataDog/datadog-agent/pull/54333) — 5 comments · 1 reactions · open
- **Pull Request** [SMP experiment selection and codeowners v2](https://github.com/DataDog/datadog-agent/pull/54833) — 5 comments · 1 reactions · open
- **Pull Request** [ci: default GitLab jobs to shallow clones, keep full history where needed](https://github.com/DataDog/datadog-agent/pull/54834) — 5 comments · 1 reactions · closed
- **Pull Request** [\[CWS-6817\] Workload Protection on macOS: Endpoint Security proof of concept](https://github.com/DataDog/datadog-agent/pull/54854) — 5 comments · 1 reactions · open
- **Pull Request** [\[AAD-23\] Remove CUSUM detector](https://github.com/DataDog/datadog-agent/pull/54437) — 10 comments · 2 reactions · open
- **Pull Request** [Add source to distributions via checks.](https://github.com/DataDog/datadog-agent/pull/51295) — 8 comments · 2 reactions · closed
- **Pull Request** [Add macOS thermal check reading AppleSMC sensors and thermal pressure](https://github.com/DataDog/datadog-agent/pull/54504) — 6 comments · 2 reactions · open
- **Pull Request** [\[DOIO-171\] Add MySQL query action dispatch](https://github.com/DataDog/datadog-agent/pull/54556) — 7 comments · 2 reactions · open
- **Pull Request** [\[EBPF\] gpu: serialize NVML field value queries](https://github.com/DataDog/datadog-agent/pull/54821) — 7 comments · 2 reactions · closed
- **Pull Request** [feat(serverless-init): add shared infrastructure for AWS MicroVM cloud service](https://github.com/DataDog/datadog-agent/pull/53030) — 4 comments · 2 reactions · open
- **Pull Request** [feat(serverless-init): add MicroVM lifecycle HTTP forwarder](https://github.com/DataDog/datadog-agent/pull/53033) — 4 comments · 2 reactions · closed
- **Pull Request** [feat(serverless-init): add standalone MicroVM lifecycle HTTP server](https://github.com/DataDog/datadog-agent/pull/53085) — 5 comments · 2 reactions · open
- **Pull Request** [macos: notable-events collector health stats](https://github.com/DataDog/datadog-agent/pull/54547) — 4 comments · 2 reactions · open
- **Pull Request** [fix(logs): stop diluting leading timestamp matches](https://github.com/DataDog/datadog-agent/pull/54753) — 5 comments · 2 reactions · closed
- **Pull Request** [Remove schemaBuilder and createschema command](https://github.com/DataDog/datadog-agent/pull/54793) — 5 comments · 2 reactions · open
- **Pull Request** [\[APM\] Reduce allocations on the trace decode path](https://github.com/DataDog/datadog-agent/pull/54798) — 4 comments · 2 reactions · open
- **Pull Request** [\[AGENTRUN-1446\] Skip nss failover e2e test it if the fakeintakes are still in use](https://github.com/DataDog/datadog-agent/pull/54814) — 4 comments · 2 reactions · closed
- **Pull Request** [Deflake `TestKeepTryingLockingIfPermissionDenied` with `synctest`](https://github.com/DataDog/datadog-agent/pull/54830) — 4 comments · 2 reactions · closed
- **Pull Request** [\[release\] Update release.json for 7.83.0-rc.3](https://github.com/DataDog/datadog-agent/pull/54845) — 4 comments · 2 reactions · closed
- **Pull Request** [Bump internal agent image to tmpl-v26 (check_intake_queue 1.5.0)](https://github.com/DataDog/datadog-agent/pull/54851) — 4 comments · 2 reactions · open
- **Pull Request** [add support for CNM direct send to windows](https://github.com/DataDog/datadog-agent/pull/52410) — 7 comments · 2 reactions · open
- **Pull Request** [WIF-48: add delegated-auth dual-shipping foundation](https://github.com/DataDog/datadog-agent/pull/53517) — 7 comments · 1 reactions · open
- **Pull Request** [\[WINA-2940\] Break Group Policy passes into timed CSE invocations](https://github.com/DataDog/datadog-agent/pull/54546) — 6 comments · 1 reactions · open
- **Pull Request** [optimize the complexity of the trace_contention_begin](https://github.com/DataDog/datadog-agent/pull/54634) — 7 comments · 1 reactions · open
- **Pull Request** [\[procmgr\] Extract shared Rust client](https://github.com/DataDog/datadog-agent/pull/54676) — 3 comments · 2 reactions · closed
- **Pull Request** [\[ABLD-419\]  Only install bazelisk with dda inv install-tools on macos](https://github.com/DataDog/datadog-agent/pull/54746) — 3 comments · 2 reactions · closed
- **Pull Request** [\[EBPF\] Disable parallel GPU collection by default](https://github.com/DataDog/datadog-agent/pull/54817) — 6 comments · 1 reactions · open

### [Prometheus](https://github.com/prometheus/prometheus)

- **Issue** [Dependency Dashboard](https://github.com/prometheus/prometheus/issues/17691) — 5 comments · 0 reactions · open
- **Issue** [scrape: optimize `convert_classic_histograms_to_nhcb` (moving the logic to each parser, ST improvement)](https://github.com/prometheus/prometheus/issues/18324) — 3 comments · 0 reactions · open
- **Pull Request** [model/textparse: implement OM2 scrape format](https://github.com/prometheus/prometheus/pull/18606) — 6 comments · 0 reactions · open
- **Issue** [discovery/ionos: panic on servers with null optional fields](https://github.com/prometheus/prometheus/issues/19417) — 0 comments · 0 reactions · open
- **Pull Request** [fix(deps): update kubernetes go dependencies to v0.36.3](https://github.com/prometheus/prometheus/pull/18757) — 1 comments · 0 reactions · open
- **Pull Request** [Agent: replay WAL concurrently](https://github.com/prometheus/prometheus/pull/19414) — 1 comments · 0 reactions · open
- **Pull Request** [prw2-receive: accept PRW2 series that carry only exemplars](https://github.com/prometheus/prometheus/pull/19416) — 0 comments · 0 reactions · open
- **Pull Request** [discovery/ionos: guard nil optional fields to avoid panic](https://github.com/prometheus/prometheus/pull/19418) — 0 comments · 0 reactions · open

### [Loki](https://github.com/grafana/loki)

- **Issue** [grafana-loki lacks basic feature of extracting nested json labels](https://github.com/grafana/loki/issues/6994) — 13 comments · 9 reactions · open
- **Issue** [Proposal: Add native OCI Object Storage support to the Thanos storage client](https://github.com/grafana/loki/issues/23687) — 1 comments · 5 reactions · open
- **Pull Request** [fix(security/UNKNOWN/operator): Update go toolchain directive to v1.26.6 \[SECURITY\] (main)](https://github.com/grafana/loki/pull/23128) — 2 comments · 0 reactions · open
- **Pull Request** [fix(security/UNKNOWN/pkg/push): Update module golang.org/x/net to v0.56.0 \[SECURITY\] (release-3.7.x)](https://github.com/grafana/loki/pull/23422) — 1 comments · 0 reactions · open
- **Pull Request** [fix(security/UNKNOWN/): Update module golang.org/x/mod to v0.40.0 \[SECURITY\] (main)](https://github.com/grafana/loki/pull/23959) — 1 comments · 0 reactions · closed
- **Pull Request** [fix(security/UNKNOWN/operator): Update module golang.org/x/mod to v0.40.0 \[SECURITY\] (main)](https://github.com/grafana/loki/pull/23960) — 1 comments · 0 reactions · open
- **Pull Request** [fix(security/UNKNOWN/): Update module golang.org/x/mod to v0.40.0 \[SECURITY\] (release-3.7.x)](https://github.com/grafana/loki/pull/23962) — 1 comments · 0 reactions · open
- **Pull Request** [fix(security/UNKNOWN/): Update module golang.org/x/mod to v0.40.0 \[SECURITY\] (release-3.6.x)](https://github.com/grafana/loki/pull/23963) — 1 comments · 0 reactions · open
- **Issue** [Dependency Dashboard](https://github.com/grafana/loki/issues/23439) — 0 comments · 0 reactions · open
- **Pull Request** [feat(storage): Add OCI Thanos object store backend](https://github.com/grafana/loki/pull/23710) — 8 comments · 0 reactions · open
- **Pull Request** [fix: deduplicate log lines split across stream shards](https://github.com/grafana/loki/pull/23907) — 8 comments · 0 reactions · open
- **Issue** [ingester logs "Ingester is shutting down" non-stop](https://github.com/grafana/loki/issues/23769) — 1 comments · 0 reactions · open
- **Pull Request** [feat: Add application credentials support to Swift client configuration](https://github.com/grafana/loki/pull/20976) — 2 comments · 1 reactions · closed
- **Pull Request** [fix: Recognise thanos/minio S3 throttling errors as retryable and add backoff](https://github.com/grafana/loki/pull/23454) — 2 comments · 0 reactions · open
- **Pull Request** [fix(deps): Update github.com/prometheus/prometheus digest to 3c82a95 (main)](https://github.com/grafana/loki/pull/23627) — 0 comments · 0 reactions · open
- **Pull Request** [fix(deps): Update aws-sdk-go-v2 (main)](https://github.com/grafana/loki/pull/23870) — 0 comments · 0 reactions · open
- **Pull Request** [chore(deps): Update github.com/go-openapi/analysis (main)](https://github.com/grafana/loki/pull/23916) — 0 comments · 0 reactions · closed
- **Pull Request** [fix: Add meaningful chunk fetch loss metrics](https://github.com/grafana/loki/pull/23925) — 1 comments · 0 reactions · open
- **Pull Request** [perf: Lazy instantiation of drains for pattern ingesters](https://github.com/grafana/loki/pull/23944) — 0 comments · 0 reactions · closed
- **Pull Request** [chore(deps): Update github.com/Microsoft/go-winio digest to 7561016 (main)](https://github.com/grafana/loki/pull/22789) — 1 comments · 0 reactions · open
- **Pull Request** [chore(deps): Update google.golang.org/genproto digest to ec0a776 (main)](https://github.com/grafana/loki/pull/22963) — 1 comments · 0 reactions · closed
- **Pull Request** [chore(deps): Update google.golang.org/genproto/googleapis/api digest to ec0a776 (main)](https://github.com/grafana/loki/pull/23804) — 1 comments · 0 reactions · closed
- **Pull Request** [fix(deps): Update google.golang.org/genproto/googleapis/rpc digest to ec0a776 (main)](https://github.com/grafana/loki/pull/23805) — 0 comments · 0 reactions · closed
- **Pull Request** [chore(deps): Update module go.opentelemetry.io/otel/exporters/otlp/otlplog/otlploggrpc to v0.21.0 (main)](https://github.com/grafana/loki/pull/23810) — 1 comments · 0 reactions · open
- **Pull Request** [chore(deps): Update module go.opentelemetry.io/otel/exporters/otlp/otlplog/otlploghttp to v0.21.0 (main)](https://github.com/grafana/loki/pull/23811) — 1 comments · 0 reactions · open
- **Pull Request** [chore(deps): Update module go.opentelemetry.io/otel/exporters/otlp/otlpmetric/otlpmetricgrpc to v1.45.0 (main)](https://github.com/grafana/loki/pull/23812) — 1 comments · 0 reactions · open
- **Pull Request** [chore(deps): Update module go.opentelemetry.io/otel/exporters/otlp/otlpmetric/otlpmetrichttp to v1.45.0 (main)](https://github.com/grafana/loki/pull/23814) — 1 comments · 0 reactions · open
- **Pull Request** [chore(deps): Update module go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc to v1.45.0 (main)](https://github.com/grafana/loki/pull/23816) — 1 comments · 0 reactions · open
- **Pull Request** [chore(deps): Update module go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracehttp to v1.45.0 (main)](https://github.com/grafana/loki/pull/23817) — 1 comments · 0 reactions · open
- **Pull Request** [chore(deps): Update module go.opentelemetry.io/contrib/exporters/autoexport to v0.70.0 (main)](https://github.com/grafana/loki/pull/23848) — 1 comments · 0 reactions · open
