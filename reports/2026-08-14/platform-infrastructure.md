# Platform / Networking / Runtime Infrastructure — 2026-08-14

> Factual GitHub evidence collected by Contribution Compass. No LLM analysis is performed.

## Contribution Leads

No evidence-qualified contribution leads changed in this collection.
## Important Updates

### [Cilium](https://github.com/cilium/cilium)

- **Issue** [cilium-agent <-> cilium-envoy livelock on cilium.NetworkPolicy xDS after upgrading to 1.20.0 — sustained 85-100% CPU on every node, no CiliumNetworkPolicy/CiliumEnvoyConfig present](https://github.com/cilium/cilium/issues/47624) — 14 comments · 2 reactions · open
- **Pull Request** [ipam: Accept native routing CIDR overlapping a secondary VPC CIDR](https://github.com/cilium/cilium/pull/47874) — 7 comments · 1 reactions · closed
- **Pull Request** [bpf: populate fib lookup L4 tuple for ECMP path selection](https://github.com/cilium/cilium/pull/45608) — 7 comments · 4 reactions · open
- **Pull Request** [bpf: Enable extended masquerade port range for BPF masquerade](https://github.com/cilium/cilium/pull/47301) — 12 comments · 2 reactions · open
- **Pull Request** [k8s: migrate from legacy config to ClusterInfo](https://github.com/cilium/cilium/pull/47854) — 13 comments · 2 reactions · open
- **Pull Request** [Documentation: document mesh security model](https://github.com/cilium/cilium/pull/47912) — 1 comments · 5 reactions · open
- **Issue** [CI: firewall-egress-to-fqdns fails 6% of the time: command terminated with exit code 28](https://github.com/cilium/cilium/issues/47921) — 10 comments · 0 reactions · open
- **Pull Request** [operator/ipam: recover nodes dropped from the instance cache during resync](https://github.com/cilium/cilium/pull/46839) — 11 comments · 2 reactions · closed
- **Pull Request** [TEST CI](https://github.com/cilium/cilium/pull/47184) — 13 comments · 2 reactions · open
- **Pull Request** [standalone-dns-proxy: return an error when no endpoint is found](https://github.com/cilium/cilium/pull/47791) — 8 comments · 2 reactions · closed
- **Pull Request** [golangci-lint: Forbid stdlib `net.Interface*` functions](https://github.com/cilium/cilium/pull/47902) — 1 comments · 4 reactions · closed
- **Pull Request** [Moved bgp config flags to bgp cell](https://github.com/cilium/cilium/pull/46748) — 3 comments · 3 reactions · open
- **Pull Request** [bpf: lb: reply to ICMP echo (ping) for service VIPs (opt-in)](https://github.com/cilium/cilium/pull/47130) — 3 comments · 4 reactions · open
- **Pull Request** [ces: fix shutdown deadlock](https://github.com/cilium/cilium/pull/47802) — 7 comments · 2 reactions · closed
- **Issue** [Label Filters don't treat prefix as a regex when loaded from file](https://github.com/cilium/cilium/issues/47918) — 5 comments · 0 reactions · open
- **Issue** [Hubble Relay does not terminate, gRPC health server remains running](https://github.com/cilium/cilium/issues/47941) — 0 comments · 1 reactions · open
- **Pull Request** [BPF Runtime Stats CLI](https://github.com/cilium/cilium/pull/47186) — 5 comments · 2 reactions · open
- **Pull Request** [test(bpf): parallelize eBPF test compilation](https://github.com/cilium/cilium/pull/47426) — 5 comments · 2 reactions · closed
- **Pull Request** [gateway-api: filter CEC controls from infrastructure metadata](https://github.com/cilium/cilium/pull/47732) — 4 comments · 2 reactions · open
- **Pull Request** [ci: use GitHub App client ID in v1.20 image workflow](https://github.com/cilium/cilium/pull/47787) — 4 comments · 2 reactions · open
- **Pull Request** [gateway-api: log the right route kind when listing TLSRoutes fails](https://github.com/cilium/cilium/pull/47826) — 4 comments · 2 reactions · closed
- **Pull Request** [chore(deps): update all github action dependencies (main)](https://github.com/cilium/cilium/pull/47861) — 4 comments · 2 reactions · closed
- **Issue** [Dependency Dashboard](https://github.com/cilium/cilium/issues/33550) — 2 comments · 0 reactions · open
- **Pull Request** [gateway-api/gamma: refresh CEC owner refs on route recreation](https://github.com/cilium/cilium/pull/47840) — 2 comments · 2 reactions · closed
- **Pull Request** [clustermesh/endpointslices: explicitly limit maximum decoder memory](https://github.com/cilium/cilium/pull/47932) — 3 comments · 2 reactions · closed
- **Pull Request** [fix(deps): update all go dependencies main](https://github.com/cilium/cilium/pull/47937) — 3 comments · 2 reactions · open
- **Issue** [pkg/idpool: use lazy map allocation in NewIDPool to reduce memory usage](https://github.com/cilium/cilium/issues/47925) — 0 comments · 0 reactions · open
- **Issue** [Gateway API: Envoy upstream replies from same-node backends lost (RST), nondeterministic across restarts — k3s/Ubuntu-raspi, not reproducible on kind](https://github.com/cilium/cilium/issues/47940) — 0 comments · 0 reactions · open
- **Pull Request** [socketlb: Clean up orphan bpf_links on restart](https://github.com/cilium/cilium/pull/46389) — 4 comments · 2 reactions · open
- **Pull Request** [install: detect containerd from GKE kubelet config](https://github.com/cilium/cilium/pull/47945) — 5 comments · 1 reactions · open

### [Envoy](https://github.com/envoyproxy/envoy)

- **Pull Request** [Queue policy extension](https://github.com/envoyproxy/envoy/pull/43355) — 19 comments · 0 reactions · open
- **Issue** [Proposal: new LB extension envoy.load_balancing_policies.per_worker_subset (per-Envoy-worker subsetting, no upstream/xDS coordination)](https://github.com/envoyproxy/envoy/issues/45682) — 6 comments · 0 reactions · open
- **Pull Request** [ext_proc: adding direct mode_override support](https://github.com/envoyproxy/envoy/pull/46318) — 11 comments · 0 reactions · open
- **Issue** [health check probes blocked indefinitely when EDS initialFetchTimeout is 0s](https://github.com/envoyproxy/envoy/issues/46666) — 1 comments · 0 reactions · open
- **Issue** [quic Support With OpenSSL](https://github.com/envoyproxy/envoy/issues/46678) — 1 comments · 0 reactions · open
- **Issue** [dynamic_modules: add metrics with labels ABI support for access logs](https://github.com/envoyproxy/envoy/issues/45765) — 3 comments · 0 reactions · closed
- **Issue** [proposal: add extension priority_load_shed HTTP filter for header-based priority shedding](https://github.com/envoyproxy/envoy/issues/45993) — 3 comments · 0 reactions · closed
- **Pull Request** [tls: allow multiple TLS certificates in the upstream when using a custom TLS certificate selector](https://github.com/envoyproxy/envoy/pull/46479) — 6 comments · 0 reactions · open
- **Issue** [Add platform constraints for extensions](https://github.com/envoyproxy/envoy/issues/46633) — 0 comments · 0 reactions · open
- **Issue** [vhds: support fully on-demand (non-wildcard) initial subscription](https://github.com/envoyproxy/envoy/issues/46641) — 0 comments · 0 reactions · open
- **Issue** [Uncaught exception in Redis proxy inline command parser](https://github.com/envoyproxy/envoy/issues/46642) — 0 comments · 0 reactions · open
- **Pull Request** [APM: add utilities to define and validate JSON schema. add the first schema - OpenAI chat completion schema](https://github.com/envoyproxy/envoy/pull/46645) — 4 comments · 0 reactions · closed
- **Pull Request** [Order dependent bug](https://github.com/envoyproxy/envoy/pull/46673) — 4 comments · 0 reactions · open
- **Pull Request** [Fix listFineGrainLoggers so that it lists loggers](https://github.com/envoyproxy/envoy/pull/46573) — 3 comments · 0 reactions · closed
- **Pull Request** [adaptive concurrency: add min concurrency limit knob](https://github.com/envoyproxy/envoy/pull/46602) — 6 comments · 0 reactions · open
- **Pull Request** [ai_protocol_manager: add response handling and extract response token usage oai, ahth, gemini](https://github.com/envoyproxy/envoy/pull/46603) — 2 comments · 0 reactions · open
- **Pull Request** [Avoid unnecesary renaming of watcher_target.yaml](https://github.com/envoyproxy/envoy/pull/46656) — 3 comments · 0 reactions · closed
- **Pull Request** [c-ares: move dns shared resolver logic to upstream cluster](https://github.com/envoyproxy/envoy/pull/46657) — 2 comments · 0 reactions · open
- **Pull Request** [fix: wasm remote code fetch race writing negative cache entry](https://github.com/envoyproxy/envoy/pull/46674) — 2 comments · 0 reactions · open
- **Pull Request** [transport_socket(http_11_proxy): add Proxy-Authorization header support](https://github.com/envoyproxy/envoy/pull/46675) — 2 comments · 0 reactions · open
- **Pull Request** [Add extension point to OpenTelemetry tracer for custom exporters.](https://github.com/envoyproxy/envoy/pull/46679) — 2 comments · 0 reactions · open
- **Pull Request** [mcp_transcoder: add sse server response support.](https://github.com/envoyproxy/envoy/pull/45374) — 5 comments · 0 reactions · open
- **Pull Request** [fix(listener): filter chain gradually drains connections with drain manager](https://github.com/envoyproxy/envoy/pull/45985) — 5 comments · 0 reactions · open
- **Pull Request** [mcp_router: add optional HMAC-SHA256 integrity for session IDs](https://github.com/envoyproxy/envoy/pull/46581) — 4 comments · 0 reactions · open
- **Pull Request** [tls_inspector: fix GREASE filtering in JA4_c signature algorithms](https://github.com/envoyproxy/envoy/pull/46658) — 1 comments · 0 reactions · open
- **Pull Request** [cleanup: replace erase-remove idiom with std::erase_if or absl::erase_if](https://github.com/envoyproxy/envoy/pull/46663) — 1 comments · 0 reactions · open
- **Pull Request** [fix: health check probes blocked indefinitely when EDS initialFetchTimeout is 0s](https://github.com/envoyproxy/envoy/pull/46667) — 1 comments · 0 reactions · open
- **Pull Request** [ext_proc: Adding support to send empty body buffer with EoS = true](https://github.com/envoyproxy/envoy/pull/46355) — 2 comments · 0 reactions · open
- **Pull Request** [bazel: support platform-based Darwin architecture selection](https://github.com/envoyproxy/envoy/pull/46637) — 2 comments · 0 reactions · open
- **Pull Request** [tls_inspector: add optional protocol parameter to JA4Fingerprinter::create](https://github.com/envoyproxy/envoy/pull/46659) — 2 comments · 0 reactions · open

### [Temporal](https://github.com/temporalio/temporal)

- **Pull Request** [Index GitHub Actions runs for flake bisecting](https://github.com/temporalio/temporal/pull/11524) — 1 comments · 1 reactions · open
- **Pull Request** [Recognize the new `commonpb` Worker callback variant](https://github.com/temporalio/temporal/pull/11380) — 2 comments · 0 reactions · open
- **Pull Request** [Populate CallbackInfo.outcome](https://github.com/temporalio/temporal/pull/11520) — 2 comments · 0 reactions · open
- **Pull Request** [Improve flaky report presentation](https://github.com/temporalio/temporal/pull/11528) — 2 comments · 0 reactions · open
- **Pull Request** [Release removed shared cluster test references](https://github.com/temporalio/temporal/pull/11542) — 2 comments · 0 reactions · open
- **Pull Request** [Await 2.0](https://github.com/temporalio/temporal/pull/10377) — 0 comments · 0 reactions · open
- **Pull Request** [Adaptive test timeouts via Await](https://github.com/temporalio/temporal/pull/10417) — 0 comments · 0 reactions · open
- **Pull Request** [Richer await timeout diagnostics](https://github.com/temporalio/temporal/pull/10781) — 0 comments · 0 reactions · open
- **Pull Request** [\[CHASM\] Support WithRequestID on UpdateComponent](https://github.com/temporalio/temporal/pull/11169) — 0 comments · 0 reactions · closed
- **Pull Request** [Emit handover watermark and shard readiness wide events](https://github.com/temporalio/temporal/pull/11401) — 0 comments · 0 reactions · closed
- **Pull Request** [Skip unbuildable replication tasks on stream sender instead of blocking](https://github.com/temporalio/temporal/pull/11422) — 0 comments · 0 reactions · open
- **Pull Request** [Record what a replication task carried on the sent lifecycle event](https://github.com/temporalio/temporal/pull/11459) — 0 comments · 0 reactions · closed
- **Pull Request** [Schedule v2 replay fidelity](https://github.com/temporalio/temporal/pull/11463) — 0 comments · 0 reactions · open
- **Pull Request** [NEXUS-504: Refactor Nexus frontend interceptors](https://github.com/temporalio/temporal/pull/11464) — 0 comments · 0 reactions · open
- **Pull Request** [replication: emit source_task_id and source_cluster on passive-side lifecycle events](https://github.com/temporalio/temporal/pull/11479) — 0 comments · 0 reactions · closed
- **Pull Request** [move admin batch jobs to sys ns](https://github.com/temporalio/temporal/pull/11494) — 0 comments · 0 reactions · open
- **Pull Request** [Track process-lifetime object leak baselines](https://github.com/temporalio/temporal/pull/11505) — 1 comments · 0 reactions · closed
- **Pull Request** [admin-batch-1: run admin batch in temporal-system](https://github.com/temporalio/temporal/pull/11509) — 0 comments · 0 reactions · open
- **Pull Request** [Use Go client for flaky report GitHub API calls](https://github.com/temporalio/temporal/pull/11523) — 1 comments · 0 reactions · open
- **Pull Request** [Fix Schedule V2 BUFFER_ONE with a deferred start](https://github.com/temporalio/temporal/pull/11530) — 1 comments · 0 reactions · closed
- **Pull Request** [Update Selected API list.](https://github.com/temporalio/temporal/pull/11535) — 0 comments · 0 reactions · open
- **Pull Request** [Attribute queue reader stuck attempts to a slice](https://github.com/temporalio/temporal/pull/11541) — 1 comments · 0 reactions · closed
- **Pull Request** [Release gRPC resolver registrations on shutdown](https://github.com/temporalio/temporal/pull/11543) — 0 comments · 0 reactions · open
- **Pull Request** [Release OTEL logger registrations on shutdown](https://github.com/temporalio/temporal/pull/11551) — 0 comments · 0 reactions · open
- **Pull Request** [Trim the Claude review comments](https://github.com/temporalio/temporal/pull/11553) — 5 comments · 0 reactions · open
- **Pull Request** [Annotate worker task spans](https://github.com/temporalio/temporal/pull/10739) — 0 comments · 0 reactions · open
- **Pull Request** [fix: \[Scheduler\] V1->V2 migration-eligibility fix and migrated-start ID](https://github.com/temporalio/temporal/pull/11462) — 0 comments · 0 reactions · open
- **Pull Request** [Limit flakereport size](https://github.com/temporalio/temporal/pull/11552) — 1 comments · 0 reactions · open
- **Pull Request** [Only count reader reads that left tasks behind as stuck attempts](https://github.com/temporalio/temporal/pull/11554) — 0 comments · 0 reactions · open
- **Pull Request** [Fix deferred BUFFER_ONE overlap processing](https://github.com/temporalio/temporal/pull/11555) — 0 comments · 0 reactions · open

### [containerd](https://github.com/containerd/containerd)

- **Issue** [TaskOOM event lost](https://github.com/containerd/containerd/issues/8893) — 17 comments · 0 reactions · open
- **Pull Request** [runc-shim: add TLA+ spec!](https://github.com/containerd/containerd/pull/11587) — 4 comments · 4 reactions · closed
- **Issue** [Add linux/riscv64 to CI test matrix](https://github.com/containerd/containerd/issues/13020) — 8 comments · 0 reactions · open
- **Issue** [Checkpoint restore on ubuntu with docker fails](https://github.com/containerd/containerd/issues/12141) — 7 comments · 0 reactions · closed
- **Issue** [Pass tracing context from containerd-shim to runc and OCI hooks](https://github.com/containerd/containerd/issues/12300) — 7 comments · 0 reactions · closed
- **Issue** [can shim exposse a standard API](https://github.com/containerd/containerd/issues/12794) — 4 comments · 0 reactions · closed
- **Issue** [Fuzz test FuzzArchiveExport fails intermittently with "context deadline exceeded"](https://github.com/containerd/containerd/issues/12991) — 2 comments · 0 reactions · closed
- **Pull Request** [Add optional Snapshot and Restore to snapshotters](https://github.com/containerd/containerd/pull/13111) — 4 comments · 0 reactions · closed
- **Pull Request** [pkg/shim: Report bootstrap API mismatch on startup](https://github.com/containerd/containerd/pull/13910) — 0 comments · 0 reactions · open
- **Pull Request** [fix(cri): CRI image pull is sometimes canceled by image_pull_progress…](https://github.com/containerd/containerd/pull/13924) — 0 comments · 0 reactions · open
- **Pull Request** [treat missing runtime state as container already dead during kill](https://github.com/containerd/containerd/pull/13951) — 0 comments · 0 reactions · open
- **Pull Request** [fix(runtime): apply load timeout to load shim](https://github.com/containerd/containerd/pull/13954) — 0 comments · 0 reactions · open
- **Pull Request** [config: add default RuntimePlatforms configuration support](https://github.com/containerd/containerd/pull/11601) — 3 comments · 0 reactions · closed
- **Pull Request** [pkg/oci: include same-name supplemental groups in AdditionalGIDs](https://github.com/containerd/containerd/pull/13587) — 0 comments · 0 reactions · open
- **Pull Request** [build(deps): bump lycheeverse/lychee-action from 2.7.0 to 2.9.0](https://github.com/containerd/containerd/pull/13773) — 0 comments · 0 reactions · open
- **Pull Request** [core/runtime/v2: add timeout to shim.delete during loadShims](https://github.com/containerd/containerd/pull/13852) — 1 comments · 0 reactions · open
- **Pull Request** [fix: retry task deletion on container removal to prevent orphaned bun…](https://github.com/containerd/containerd/pull/13925) — 0 comments · 0 reactions · open
- **Pull Request** [Export config in CRI plugin](https://github.com/containerd/containerd/pull/13940) — 0 comments · 0 reactions · open
- **Pull Request** [Update Go to 1.26.6](https://github.com/containerd/containerd/pull/13957) — 1 comments · 0 reactions · closed
- **Pull Request** [runtime: invoke Shutdown after every task deletion](https://github.com/containerd/containerd/pull/13958) — 1 comments · 0 reactions · open
