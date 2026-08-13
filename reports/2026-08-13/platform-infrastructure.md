# Platform / Networking / Runtime Infrastructure — 2026-08-13

> Factual GitHub evidence collected by Contribution Compass. No LLM analysis is performed.

## Contribution Leads

### [Continuous memory growth in containerd v2.1.4](https://github.com/containerd/containerd/issues/12738)

- Project: `containerd/containerd`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

## Important Updates

### [Cilium](https://github.com/cilium/cilium)

- **Issue** [CFP: OpenTelemetry tracing support for Gateway API-managed Envoy listeners](https://github.com/cilium/cilium/issues/44850) — 8 comments · 23 reactions · open
- **Issue** [ENI IPAM: agent fatals when ipv4NativeRoutingCIDR is a secondary VPC CIDR association](https://github.com/cilium/cilium/issues/47811) — 2 comments · 1 reactions · closed
- **Issue** [Envoy NPDS not updated when new identities are added for GatewayAPI ingress endpoints doing hairpin traffic for (at least) wildcard matching policies](https://github.com/cilium/cilium/issues/43519) — 9 comments · 5 reactions · open
- **Issue** [policy-cidr-match-mode=nodes does not work for wildcard CIDR matches](https://github.com/cilium/cilium/issues/47827) — 1 comments · 1 reactions · open
- **Pull Request** [bpf: use bpf_redirect_peer() for local pod-to-pod delivery on veth](https://github.com/cilium/cilium/pull/46227) — 12 comments · 0 reactions · open
- **Pull Request** [ipam: Accept native routing CIDR overlapping a secondary VPC CIDR](https://github.com/cilium/cilium/pull/47874) — 6 comments · 1 reactions · closed
- **Pull Request** [fix: Print port numbers correctly for map cilium_lb*_reverse_sk](https://github.com/cilium/cilium/pull/47134) — 18 comments · 2 reactions · open
- **Pull Request** [chore(deps): update all-dependencies (v1.20)](https://github.com/cilium/cilium/pull/47678) — 18 comments · 2 reactions · closed
- **Pull Request** [bpf: dsr: also send DSR info on first non-SYN packet towards new backend](https://github.com/cilium/cilium/pull/47529) — 12 comments · 3 reactions · closed
- **Issue** [Issue with backend remove in json state](https://github.com/cilium/cilium/issues/46493) — 14 comments · 0 reactions · closed
- **Pull Request** [bpf: populate fib lookup L4 tuple for ECMP path selection](https://github.com/cilium/cilium/pull/45608) — 7 comments · 4 reactions · open
- **Pull Request** [bpf: sockLB: allow translation for L2-announced ExternalIPs](https://github.com/cilium/cilium/pull/45672) — 11 comments · 3 reactions · open
- **Pull Request** [dnsproxy: use portReleased channel to prevent EADDRINUSE on transparent mode](https://github.com/cilium/cilium/pull/46736) — 14 comments · 2 reactions · open
- **Pull Request** [\[envoy\] Add HTTP CONNECT support](https://github.com/cilium/cilium/pull/45051) — 9 comments · 3 reactions · open
- **Pull Request** [\[41867\]\[Part6\] Hybrid Routing Route Installation](https://github.com/cilium/cilium/pull/45579) — 12 comments · 2 reactions · open
- **Pull Request** [Configurable FQDN DNS Proxy Redirection](https://github.com/cilium/cilium/pull/46824) — 13 comments · 2 reactions · open
- **Pull Request** [network driver: use statedb to manage agent devices](https://github.com/cilium/cilium/pull/47558) — 13 comments · 2 reactions · open
- **Pull Request** [Documentation: document mesh security model](https://github.com/cilium/cilium/pull/47912) — 1 comments · 5 reactions · open
- **Issue** [Improve BPF test speed](https://github.com/cilium/cilium/issues/45133) — 10 comments · 0 reactions · open
- **Pull Request** [bpf: host: pass IPv6 to the stack when the IPv6 datapath is disabled](https://github.com/cilium/cilium/pull/46473) — 6 comments · 3 reactions · closed
- **Pull Request** [bpf: Enable extended masquerade port range for BPF masquerade](https://github.com/cilium/cilium/pull/47301) — 10 comments · 2 reactions · open
- **Pull Request** [address httpUpstreamLingerTimeout chart templating issues](https://github.com/cilium/cilium/pull/47741) — 6 comments · 3 reactions · closed
- **Pull Request** [fix(docs): make render-docs target work on macOS](https://github.com/cilium/cilium/pull/47820) — 11 comments · 2 reactions · closed
- **Pull Request** [Fix endpoint panic when verbose policy logging is enabled](https://github.com/cilium/cilium/pull/47844) — 3 comments · 4 reactions · closed
- **Issue** [ExternalAuth filter fails unsafely if backendRef is missing a ReferenceGrant](https://github.com/cilium/cilium/issues/47877) — 1 comments · 2 reactions · open
- **Pull Request** [scaletozero: add datapath demand signalling for service scale-to-zero](https://github.com/cilium/cilium/pull/46641) — 5 comments · 3 reactions · open
- **Pull Request** [operator/ipam: recover nodes dropped from the instance cache during resync](https://github.com/cilium/cilium/pull/46839) — 9 comments · 2 reactions · open
- **Pull Request** [ipcache: fix CIDR reference counter to use canonical prefixes](https://github.com/cilium/cilium/pull/47208) — 4 comments · 3 reactions · closed
- **Pull Request** [bpf: Add is_subnet_same_id helper](https://github.com/cilium/cilium/pull/47403) — 1 comments · 4 reactions · closed
- **Pull Request** [chore(deps): update all-dependencies (v1.19)](https://github.com/cilium/cilium/pull/47679) — 9 comments · 2 reactions · closed

### [Envoy](https://github.com/envoyproxy/envoy)

- **Issue** [Open Request Cost Aggregation (ORCA)](https://github.com/envoyproxy/envoy/issues/6614) — 47 comments · 13 reactions · open
- **Issue** [Shift `clang-tidy` to github action](https://github.com/envoyproxy/envoy/issues/28566) — 48 comments · 0 reactions · open
- **Issue** [Add Support for JA4Latency FingerPrint Hash](https://github.com/envoyproxy/envoy/issues/41065) — 10 comments · 1 reactions · closed
- **Issue** [Hot restart lead to the abnormal exit of the new process](https://github.com/envoyproxy/envoy/issues/7468) — 4 comments · 2 reactions · closed
- **Pull Request** [Queue policy extension](https://github.com/envoyproxy/envoy/pull/43355) — 19 comments · 0 reactions · open
- **Issue** [Guidance on RPM packaging of official release binaries for RHEL/Rocky Linux](https://github.com/envoyproxy/envoy/issues/45866) — 6 comments · 0 reactions · closed
- **Pull Request** [add ratelimit descriptor extension to use jwt claims as descriptors](https://github.com/envoyproxy/envoy/pull/46138) — 11 comments · 1 reactions · open
- **Issue** [GeoIP LookupResult is always const, inhibiting move semantics](https://github.com/envoyproxy/envoy/issues/46531) — 5 comments · 0 reactions · open
- **Pull Request** [Manage on-call rotation and ical generation in code](https://github.com/envoyproxy/envoy/pull/43771) — 13 comments · 0 reactions · open
- **Issue** [http2: allow configuring upstream headers as HPACK never indexed](https://github.com/envoyproxy/envoy/issues/46584) — 3 comments · 0 reactions · open
- **Pull Request** [hot restart: propagate programmatic stat tags across restart](https://github.com/envoyproxy/envoy/pull/45674) — 14 comments · 0 reactions · open
- **Issue** [openssl compat: implement CNSA1_202603 compliance policy](https://github.com/envoyproxy/envoy/issues/46104) — 1 comments · 0 reactions · open
- **Issue** [tls: share parsed CA trust store (X509_STORE) across contexts built from identical CA material](https://github.com/envoyproxy/envoy/issues/46114) — 1 comments · 0 reactions · open
- **Issue** [http1: unsafe ctype usage and size_t to int narrowing in the HTTP/1 parser](https://github.com/envoyproxy/envoy/issues/46505) — 1 comments · 0 reactions · open
- **Issue** [cluster upstream_rq_timeout increments on requests that also complete successfully (rq_success == rq_total, rq_timeout independently non-zero)](https://github.com/envoyproxy/envoy/issues/46665) — 1 comments · 0 reactions · open
- **Issue** [health check probes blocked indefinitely when EDS initialFetchTimeout is 0s](https://github.com/envoyproxy/envoy/issues/46666) — 0 comments · 0 reactions · open
- **Issue** [reverse_tunnel: Implement proactive pings from the downstream_socket_interface](https://github.com/envoyproxy/envoy/issues/46677) — 1 comments · 0 reactions · open
- **Issue** [quic Support With OpenSSL](https://github.com/envoyproxy/envoy/issues/46678) — 0 comments · 0 reactions · open
- **Issue** [Newer release available `dd_trace_cpp`: v2.2.0 (current: v2.1.1)](https://github.com/envoyproxy/envoy/issues/46680) — 0 comments · 0 reactions · open
- **Issue** [Newer release available `rules_shell`: v0.9.0 (current: v0.8.0)](https://github.com/envoyproxy/envoy/issues/46681) — 0 comments · 0 reactions · open
- **Pull Request** [tls: allow multiple TLS certificates in the upstream when using a custom TLS certificate selector](https://github.com/envoyproxy/envoy/pull/46479) — 6 comments · 0 reactions · open
- **Pull Request** [Support hot restart handoff for connectionless UDP flows](https://github.com/envoyproxy/envoy/pull/46502) — 7 comments · 0 reactions · open
- **Pull Request** [ext_proc: document session affinity configuration](https://github.com/envoyproxy/envoy/pull/46558) — 6 comments · 0 reactions · closed
- **Pull Request** [\[WIP\] bazel: Switch to bzlmod](https://github.com/envoyproxy/envoy/pull/42890) — 5 comments · 0 reactions · open
- **Pull Request** [hot_restart: fix integer overflow in IPC message length handling](https://github.com/envoyproxy/envoy/pull/45882) — 5 comments · 0 reactions · closed
- **Pull Request** [stats: migrate rds/scope rds to use new stats API](https://github.com/envoyproxy/envoy/pull/45914) — 4 comments · 0 reactions · open
- **Pull Request** [stats: migrate almost all HTTP to new API](https://github.com/envoyproxy/envoy/pull/45983) — 4 comments · 0 reactions · closed
- **Pull Request** [composite: fail over to the next sub-cluster when a sub-cluster has no hosts](https://github.com/envoyproxy/envoy/pull/46308) — 9 comments · 0 reactions · open
- **Pull Request** [\[bp/v1.36\] dfp: fix a bug when cluster is removed before async lb be completed (#45064)](https://github.com/envoyproxy/envoy/pull/46460) — 4 comments · 0 reactions · closed
- **Pull Request** [http: add support for the QUERY method (RFC 10008)](https://github.com/envoyproxy/envoy/pull/46496) — 5 comments · 0 reactions · open

### [Temporal](https://github.com/temporalio/temporal)

- **Issue** [Scheduled Actions doesn't clear ContinuedFailure on null success payloads](https://github.com/temporalio/temporal/issues/8490) — 2 comments · 2 reactions · open
- **Issue** [config: strict mode for configuration parsing](https://github.com/temporalio/temporal/issues/2341) — 5 comments · 1 reactions · open
- **Issue** [Schedule "StartAt" not used when calculating intervals?](https://github.com/temporalio/temporal/issues/6173) — 0 comments · 1 reactions · open
- **Issue** [\[Scheduled Actions\] Skipped Action Metric](https://github.com/temporalio/temporal/issues/8087) — 1 comments · 1 reactions · open
- **Issue** [SignalWithStart hangs forever on an orphaned current-execution pointer](https://github.com/temporalio/temporal/issues/10841) — 2 comments · 0 reactions · open
- **Issue** [Schedule deadlocks after Workflow ID reuse when previous scheduled action has Workflow Retry chain](https://github.com/temporalio/temporal/issues/10579) — 0 comments · 0 reactions · open
- **Issue** [Replace LeveledCompactionStrategy (LCS) with Cassandra 5.x default UnifiedCompactionStrategy (UCS) in schema.cql](https://github.com/temporalio/temporal/issues/11314) — 1 comments · 0 reactions · open
- **Issue** [Fairsim partial counter configuration resets unspecified defaults](https://github.com/temporalio/temporal/issues/11534) — 1 comments · 0 reactions · open
- **Issue** [DeleteWorkerDeploymentVersion fails permanently when a version summary outlives its version workflow](https://github.com/temporalio/temporal/issues/11539) — 0 comments · 0 reactions · open
- **Issue** [Unable to create visibility database schema for MySQL](https://github.com/temporalio/temporal/issues/9522) — 1 comments · 0 reactions · open
- **Pull Request** [Persist Callback terminal failures](https://github.com/temporalio/temporal/pull/11413) — 9 comments · 0 reactions · closed
- **Pull Request** [VLN-1587: remediate claude-code-action-unhardened](https://github.com/temporalio/temporal/pull/11400) — 2 comments · 1 reactions · open
- **Pull Request** [Index GitHub Actions runs for flake bisecting](https://github.com/temporalio/temporal/pull/11524) — 1 comments · 1 reactions · open
- **Pull Request** [Add completion callbacks to SANOs](https://github.com/temporalio/temporal/pull/11415) — 2 comments · 0 reactions · closed
- **Pull Request** [Fix approximateSize undercounting on activity start and heartbeat paths](https://github.com/temporalio/temporal/pull/11486) — 2 comments · 0 reactions · open
- **Pull Request** [Improve flaky report presentation](https://github.com/temporalio/temporal/pull/11528) — 2 comments · 0 reactions · open
- **Pull Request** [Reduce test runner resources](https://github.com/temporalio/temporal/pull/10129) — 0 comments · 0 reactions · closed
- **Pull Request** [Validator generator \[WiP\]](https://github.com/temporalio/temporal/pull/10200) — 0 comments · 0 reactions · open
- **Pull Request** [Await 2.0](https://github.com/temporalio/temporal/pull/10377) — 0 comments · 0 reactions · open
- **Pull Request** [Adaptive test timeouts via Await](https://github.com/temporalio/temporal/pull/10417) — 0 comments · 0 reactions · open
- **Pull Request** [Downscale test runner size, increase shards](https://github.com/temporalio/temporal/pull/10643) — 1 comments · 0 reactions · open
- **Pull Request** [Richer await timeout diagnostics](https://github.com/temporalio/temporal/pull/10781) — 0 comments · 0 reactions · open
- **Pull Request** [Return test runner orchestration outcomes](https://github.com/temporalio/temporal/pull/11033) — 0 comments · 0 reactions · open
- **Pull Request** [\[CHASM\] Support WithRequestID on UpdateComponent](https://github.com/temporalio/temporal/pull/11169) — 0 comments · 0 reactions · open
- **Pull Request** [Stabilize mixed-brain server rolls](https://github.com/temporalio/temporal/pull/11204) — 0 comments · 0 reactions · closed
- **Pull Request** [Add data race summary to CI report](https://github.com/temporalio/temporal/pull/11211) — 0 comments · 0 reactions · open
- **Pull Request** [Track process-lifetime object leak baselines](https://github.com/temporalio/temporal/pull/11313) — 1 comments · 0 reactions · closed
- **Pull Request** [Preserve logger tags across Skip()](https://github.com/temporalio/temporal/pull/11355) — 0 comments · 0 reactions · open
- **Pull Request** [Recognize the new `commonpb` Worker callback variant](https://github.com/temporalio/temporal/pull/11380) — 1 comments · 0 reactions · open
- **Pull Request** [Fix constant/error-dependent retry jitter being truncated to a no-op](https://github.com/temporalio/temporal/pull/11397) — 0 comments · 0 reactions · open

### [containerd](https://github.com/containerd/containerd)

- **Release** [containerd 2.3.4](https://github.com/containerd/containerd/releases/tag/v2.3.4) — 
- **Release** [containerd 2.2.7](https://github.com/containerd/containerd/releases/tag/v2.2.7) — 
- **Issue** [containerd-shim process isn't reaped for some killed containers](https://github.com/containerd/containerd/issues/5708) — 18 comments · 5 reactions · closed
- **Issue** [Continuous memory growth in containerd v2.1.4](https://github.com/containerd/containerd/issues/12738) — 20 comments · 2 reactions · open
- **Issue** [Unpack failure when mixing remote and local snapshotters](https://github.com/containerd/containerd/issues/12752) — 3 comments · 3 reactions · closed
- **Issue** [containerd crash with program exceeds 10000-thread limit - container-log FIFO open leaks an OS thread per failed CreateContainer](https://github.com/containerd/containerd/issues/13952) — 7 comments · 0 reactions · open
- **Issue** [containerd on Windows 11 - cannot override root directory using --root parameter](https://github.com/containerd/containerd/issues/12131) — 4 comments · 0 reactions · closed
- **Issue** [Support for time namespaces](https://github.com/containerd/containerd/issues/12517) — 5 comments · 0 reactions · closed
- **Issue** [容器没有重启功能，是否可以出一个重启功能](https://github.com/containerd/containerd/issues/12728) — 5 comments · 0 reactions · closed
- **Issue** [CRI: tag+digest sandbox image breaks RunPodSandbox](https://github.com/containerd/containerd/issues/13529) — 1 comments · 1 reactions · closed
- **Issue** [CRI image pull is sometimes canceled by image_pull_progress_timeout during unpack](https://github.com/containerd/containerd/issues/13909) — 1 comments · 1 reactions · open
- **Issue** [Support env variable configuration for logging binary](https://github.com/containerd/containerd/issues/12760) — 2 comments · 0 reactions · closed
- **Issue** [make benchmark never work](https://github.com/containerd/containerd/issues/12973) — 2 comments · 0 reactions · open
- **Pull Request** [Allow hosts file configuration for proxies per registry](https://github.com/containerd/containerd/pull/13359) — 8 comments · 0 reactions · open
- **Pull Request** [shim: send event to a queue to prevent event to be dropped](https://github.com/containerd/containerd/pull/13653) — 4 comments · 1 reactions · open
- **Pull Request** [ignore update status file when no space](https://github.com/containerd/containerd/pull/11458) — 4 comments · 0 reactions · closed
- **Pull Request** [Draft: ctr support print plugin config](https://github.com/containerd/containerd/pull/11477) — 4 comments · 0 reactions · closed
- **Pull Request** [docker fetcher: strip sensitive headers on descriptor URLs](https://github.com/containerd/containerd/pull/12889) — 5 comments · 0 reactions · open
- **Pull Request** [oom: avoid per-wakeup allocations in cgroup v2 OOM watcher (#13558)](https://github.com/containerd/containerd/pull/13635) — 5 comments · 0 reactions · open
- **Pull Request** [tracing: align span attribute keys with OTel semantic conventions](https://github.com/containerd/containerd/pull/13928) — 5 comments · 0 reactions · open
- **Pull Request** [core/remotes/docker: only fetch descriptor urls for foreign layers](https://github.com/containerd/containerd/pull/13775) — 3 comments · 0 reactions · closed
- **Pull Request** [metadata: bound snapshotter Remove during garbage collection](https://github.com/containerd/containerd/pull/13799) — 3 comments · 0 reactions · open
- **Pull Request** [remotes/docker: retry blob fetch on connection reset by peer](https://github.com/containerd/containerd/pull/13915) — 2 comments · 0 reactions · open
- **Pull Request** [Ensure credentials are forwarded to configured mirrors](https://github.com/containerd/containerd/pull/13949) — 2 comments · 0 reactions · open
- **Pull Request** [vendor: github.com/sirupsen/logrus v1.10.0](https://github.com/containerd/containerd/pull/13294) — 1 comments · 0 reactions · open
- **Pull Request** [fix: prevent tar extraction data corruption by limiting reader size](https://github.com/containerd/containerd/pull/13705) — 0 comments · 0 reactions · open
- **Pull Request** [ctr: dedupe CRI image aliases in images list by default](https://github.com/containerd/containerd/pull/13830) — 1 comments · 0 reactions · open
- **Pull Request** [pkg/shim: Report bootstrap API mismatch on startup](https://github.com/containerd/containerd/pull/13910) — 0 comments · 0 reactions · open
- **Pull Request** [fix(cri): CRI image pull is sometimes canceled by image_pull_progress…](https://github.com/containerd/containerd/pull/13924) — 0 comments · 0 reactions · open
- **Pull Request** [Prepare release notes for v2.3.4](https://github.com/containerd/containerd/pull/13942) — 0 comments · 0 reactions · closed
