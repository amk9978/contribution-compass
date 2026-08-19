# Platform / Networking / Runtime Infrastructure — 2026-08-19

> Factual GitHub evidence collected by Contribution Compass. No LLM analysis is performed.

## Contribution Leads

### [ACME support](https://github.com/envoyproxy/envoy/issues/96)

- Project: `envoyproxy/envoy`
- Tier: `maintainer-invited`
- Evidence: Maintainer invitation label: help wanted; No assignee is listed
- Caveat: Confirm scope and availability with the maintainers before starting work.

### [Cilium Gateway with Envoy rejects IPv6 PROXY headers from LB while IPv4 works](https://github.com/cilium/cilium/issues/42950)

- Project: `cilium/cilium`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [Gateway API L7LB north-south traffic still dropped on 1.19.4 when LB VIP is announced on a VLAN subinterface (not a bridge)](https://github.com/cilium/cilium/issues/46260)

- Project: `cilium/cilium`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [Pre-flight ahead of 1.20 upgrade doesn't drop CiliumNodeConfig v2alpha1 CRD](https://github.com/cilium/cilium/issues/47774)

- Project: `cilium/cilium`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [Cilium fails to properly write eBPF maps in some circumstances](https://github.com/cilium/cilium/issues/45196)

- Project: `cilium/cilium`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [v1.19.3: WireGuard handshakes never complete on any node pair (tunnel/geneve + DSR), all cross-node pod traffic dead, on Oracle Linux only.](https://github.com/cilium/cilium/issues/47565)

- Project: `cilium/cilium`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [There is no way to enable envoy-metrics service monitor for embedded envoy](https://github.com/cilium/cilium/issues/47825)

- Project: `cilium/cilium`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [http1: unsafe ctype usage and size_t to int narrowing in the HTTP/1 parser](https://github.com/envoyproxy/envoy/issues/46505)

- Project: `envoyproxy/envoy`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

## Important Updates

### [Cilium](https://github.com/cilium/cilium)

- **Issue** [Cilium Gateway with Envoy rejects IPv6 PROXY headers from LB while IPv4 works](https://github.com/cilium/cilium/issues/42950) — 10 comments · 12 reactions · open
- **Issue** [cilium-agent <-> cilium-envoy livelock on cilium.NetworkPolicy xDS after upgrading to 1.20.0 — sustained 85-100% CPU on every node, no CiliumNetworkPolicy/CiliumEnvoyConfig present](https://github.com/cilium/cilium/issues/47624) — 16 comments · 3 reactions · closed
- **Pull Request** [loadbalancer: Fix dropping traffic L2Announcement with externalTrafficPolicy: Local](https://github.com/cilium/cilium/pull/46399) — 19 comments · 11 reactions · open
- **Release** [1.18.13](https://github.com/cilium/cilium/releases/tag/v1.18.13) — 
- **Release** [1.20.1](https://github.com/cilium/cilium/releases/tag/v1.20.1) — 
- **Release** [1.19.7](https://github.com/cilium/cilium/releases/tag/v1.19.7) — 
- **Issue** [CiliumClusterwideNetworkPolicy does not allow us to define policy to lockdown traffic within each of the namespaces](https://github.com/cilium/cilium/issues/24731) — 15 comments · 8 reactions · closed
- **Issue** [loader: investigate lost BPF complexity coverage](https://github.com/cilium/cilium/issues/47647) — 6 comments · 3 reactions · closed
- **Issue** [Envoy NPDS not updated when new identities are added for GatewayAPI ingress endpoints doing hairpin traffic for (at least) wildcard matching policies](https://github.com/cilium/cilium/issues/43519) — 12 comments · 5 reactions · open
- **Issue** [v1.19.3: WireGuard handshakes never complete on any node pair (tunnel/geneve + DSR), all cross-node pod traffic dead, on Oracle Linux only.](https://github.com/cilium/cilium/issues/47565) — 4 comments · 1 reactions · open
- **Pull Request** [ipam: Accept native routing CIDR overlapping a secondary VPC CIDR](https://github.com/cilium/cilium/pull/47874) — 7 comments · 1 reactions · closed
- **Pull Request** [Add per-flow CT packet/byte counters to Hubble trace notifications](https://github.com/cilium/cilium/pull/45250) — 16 comments · 5 reactions · open
- **Pull Request** [renovate: Fix primary GID of the ubuntu user and restore builder.sh root check](https://github.com/cilium/cilium/pull/46652) — 26 comments · 2 reactions · closed
- **Issue** [CFP: Adding RISC-V as a supported architecture in Cilium's build system](https://github.com/cilium/cilium/issues/39977) — 5 comments · 5 reactions · open
- **Issue** [Gateway API L7LB north-south traffic still dropped on 1.19.4 when LB VIP is announced on a VLAN subinterface (not a bridge)](https://github.com/cilium/cilium/issues/46260) — 21 comments · 1 reactions · open
- **Issue** [Pre-flight ahead of 1.20 upgrade doesn't drop CiliumNodeConfig v2alpha1 CRD](https://github.com/cilium/cilium/issues/47774) — 3 comments · 5 reactions · open
- **Pull Request** [*: make dumps retry in netlink library, remove safenetlink package](https://github.com/cilium/cilium/pull/44315) — 22 comments · 2 reactions · open
- **Pull Request** [fix: Print port numbers correctly for map cilium_lb*_reverse_sk](https://github.com/cilium/cilium/pull/47134) — 19 comments · 2 reactions · open
- **Pull Request** [\[envoy\] Add HTTP CONNECT support](https://github.com/cilium/cilium/pull/45051) — 11 comments · 3 reactions · open
- **Pull Request** [Fix multiple regressions in Cilium LocalRedirectPolicy](https://github.com/cilium/cilium/pull/46638) — 15 comments · 2 reactions · open
- **Pull Request** [Proposing Flow IR implementation to improve hubble performance](https://github.com/cilium/cilium/pull/46896) — 19 comments · 2 reactions · open
- **Pull Request** [chore(deps): update all-dependencies (main)](https://github.com/cilium/cilium/pull/47859) — 15 comments · 2 reactions · closed
- **Pull Request** [\[41867\]\[Part6\] Hybrid Routing Route Installation](https://github.com/cilium/cilium/pull/45579) — 12 comments · 2 reactions · open
- **Pull Request** [node/manager: Populate node table from manager](https://github.com/cilium/cilium/pull/45953) — 13 comments · 2 reactions · closed
- **Issue** [Cilium fails to properly write eBPF maps in some circumstances](https://github.com/cilium/cilium/issues/45196) — 7 comments · 2 reactions · open
- **Issue** [node-init startup script fails on GKE >= 1.36.2-gke.2064000: GKE-containerd probe no longer matches node image](https://github.com/cilium/cilium/issues/47884) — 2 comments · 3 reactions · closed
- **Pull Request** [bpf, datapath: move the CT_* params to runtime config](https://github.com/cilium/cilium/pull/47537) — 11 comments · 2 reactions · open
- **Pull Request** [bgp: gate BGP announcements on host datapath init](https://github.com/cilium/cilium/pull/46948) — 12 comments · 2 reactions · open
- **Pull Request** [feat(bgp): support BGP unnumbered peering (RFC 5549 / ENHE)](https://github.com/cilium/cilium/pull/47394) — 9 comments · 2 reactions · open
- **Pull Request** [gateway-api: nodeSelector with hostNetwork enabled](https://github.com/cilium/cilium/pull/47463) — 9 comments · 2 reactions · open

### [Envoy](https://github.com/envoyproxy/envoy)

- **Issue** [ACME support](https://github.com/envoyproxy/envoy/issues/96) — 31 comments · 173 reactions · open
- **Pull Request** [\[WIP\] dns: add support for clusters based on SRV DNS record](https://github.com/envoyproxy/envoy/pull/35160) — 31 comments · 1 reactions · open
- **Pull Request** [network: fix stream leak when a user-space peer fully closes under half-close](https://github.com/envoyproxy/envoy/pull/45198) — 14 comments · 2 reactions · open
- **Issue** [Eager Upstream Connections: per_upstream_min_connections and Connection-Aware Load Balancing](https://github.com/envoyproxy/envoy/issues/45319) — 17 comments · 0 reactions · open
- **Pull Request** [Queue policy extension](https://github.com/envoyproxy/envoy/pull/43355) — 20 comments · 0 reactions · open
- **Issue** [UDP proxy for upstream health monitoring](https://github.com/envoyproxy/envoy/issues/37824) — 11 comments · 0 reactions · open
- **Issue** [Support sending access logs to syslog](https://github.com/envoyproxy/envoy/issues/45523) — 6 comments · 1 reactions · open
- **Issue** [match_delegate: let's lazy initialize the nested filter instance till after matcher eval](https://github.com/envoyproxy/envoy/issues/44825) — 13 comments · 0 reactions · closed
- **Pull Request** [add ratelimit descriptor extension to use jwt claims as descriptors](https://github.com/envoyproxy/envoy/pull/46138) — 12 comments · 1 reactions · closed
- **Issue** [\[ext_proc\] add a control message directs modes overrides before request header response](https://github.com/envoyproxy/envoy/issues/46125) — 6 comments · 0 reactions · open
- **Pull Request** [redis filter: support `CLUSTER SHARDS`](https://github.com/envoyproxy/envoy/pull/46480) — 6 comments · 2 reactions · closed
- **Issue** [http1: unsafe ctype usage and size_t to int narrowing in the HTTP/1 parser](https://github.com/envoyproxy/envoy/issues/46505) — 4 comments · 0 reactions · open
- **Pull Request** [Support subset lb using dynamically-set metadata for shadow HTTP traffic](https://github.com/envoyproxy/envoy/pull/46161) — 12 comments · 0 reactions · closed
- **Pull Request** [ext_proc: adding direct mode_override support](https://github.com/envoyproxy/envoy/pull/46318) — 12 comments · 0 reactions · open
- **Issue** [Make header forwarding configurable via proto config](https://github.com/envoyproxy/envoy/issues/46525) — 4 comments · 0 reactions · open
- **Pull Request** [fix: duplicate request body when when using FULL_DUPLEX_STREAMED ext_proc body mode with retries enabled](https://github.com/envoyproxy/envoy/pull/46095) — 13 comments · 0 reactions · open
- **Pull Request** [jwt_authn: sanitize payload and claim headers filter-wide](https://github.com/envoyproxy/envoy/pull/46586) — 8 comments · 0 reactions · open
- **Issue** [postgres_proxy: partial initial message bytes forwarded to upstream before fully decoded](https://github.com/envoyproxy/envoy/issues/46774) — 2 comments · 0 reactions · open
- **Pull Request** [xDS: change ext_proc drain process to work directionally](https://github.com/envoyproxy/envoy/pull/45901) — 7 comments · 0 reactions · open
- **Pull Request** [geoip: support additional maxmind database fields](https://github.com/envoyproxy/envoy/pull/46074) — 7 comments · 0 reactions · open
- **Pull Request** [tls: allow multiple TLS certificates in the upstream when using a custom TLS certificate selector](https://github.com/envoyproxy/envoy/pull/46479) — 6 comments · 0 reactions · open
- **Pull Request** [router: support building an SRDS scope key from filter state](https://github.com/envoyproxy/envoy/pull/46526) — 6 comments · 0 reactions · open
- **Pull Request** [mcp_router: add optional HMAC-SHA256 integrity for session IDs](https://github.com/envoyproxy/envoy/pull/46581) — 7 comments · 0 reactions · open
- **Pull Request** [rds: make the init manager for rds works for filter_chain and oauth2](https://github.com/envoyproxy/envoy/pull/46664) — 6 comments · 0 reactions · open
- **Pull Request** [fix: health check probes blocked indefinitely when EDS initialFetchTimeout is 0s](https://github.com/envoyproxy/envoy/pull/46667) — 7 comments · 0 reactions · open
- **Issue** [Newer release available `aws_c_auth_testdata`: v0.10.5 (current: v0.10.4)](https://github.com/envoyproxy/envoy/issues/46772) — 0 comments · 0 reactions · open
- **Issue** [deps: Enforce direct visibility of external deps by centralizing under bazel/deps](https://github.com/envoyproxy/envoy/issues/46786) — 1 comments · 0 reactions · open
- **Issue** [new filter to expose memory/cpu/rps to in the response](https://github.com/envoyproxy/envoy/issues/46796) — 1 comments · 0 reactions · open
- **Pull Request** [\[WIP\] bazel: Switch to bzlmod](https://github.com/envoyproxy/envoy/pull/42890) — 5 comments · 0 reactions · open
- **Pull Request** [fix: skip null pointer in EDS endpoints validation](https://github.com/envoyproxy/envoy/pull/45207) — 9 comments · 0 reactions · closed

### [Temporal](https://github.com/temporalio/temporal)

- **Issue** [DeleteWorkerDeploymentVersion fails permanently when a version summary outlives its version workflow](https://github.com/temporalio/temporal/issues/11539) — 2 comments · 0 reactions · open
- **Issue** [Persistence rate-limit ResourceExhausted is flattened to Unavailable in ProcessOutgoingSearchAttributes](https://github.com/temporalio/temporal/issues/11571) — 1 comments · 0 reactions · open
- **Pull Request** [Improve flaky report presentation](https://github.com/temporalio/temporal/pull/11528) — 2 comments · 1 reactions · closed
- **Issue** [Add a built-in Kubernetes service account ClaimMapper selectable via `authorization.claimMapper`](https://github.com/temporalio/temporal/issues/11607) — 0 comments · 0 reactions · open
- **Issue** [yuandrew test issue](https://github.com/temporalio/temporal/issues/11625) — 0 comments · 0 reactions · closed
- **Pull Request** [Adaptive test timeouts via Await](https://github.com/temporalio/temporal/pull/10417) — 2 comments · 0 reactions · open
- **Pull Request** [Fix approximateSize undercounting on activity start and heartbeat paths](https://github.com/temporalio/temporal/pull/11486) — 2 comments · 0 reactions · closed
- **Pull Request** [Release gRPC resolver registrations on shutdown](https://github.com/temporalio/temporal/pull/11543) — 2 comments · 0 reactions · open
- **Pull Request** [Trace inbound Nexus HTTP requests](https://github.com/temporalio/temporal/pull/11560) — 2 comments · 0 reactions · open
- **Pull Request** [Make supported callback kinds configurable](https://github.com/temporalio/temporal/pull/11566) — 2 comments · 0 reactions · open
- **Pull Request** [Await 2.0](https://github.com/temporalio/temporal/pull/10377) — 0 comments · 0 reactions · open
- **Pull Request** [Annotate worker task spans](https://github.com/temporalio/temporal/pull/10739) — 0 comments · 0 reactions · open
- **Pull Request** [Richer await timeout diagnostics](https://github.com/temporalio/temporal/pull/10781) — 0 comments · 0 reactions · open
- **Pull Request** [Add Worker Deployment and BuildID labels to (workflow,activity) task completion metrics](https://github.com/temporalio/temporal/pull/11348) — 0 comments · 0 reactions · open
- **Pull Request** [Preserve logger tags across Skip()](https://github.com/temporalio/temporal/pull/11355) — 0 comments · 0 reactions · open
- **Pull Request** [Fix constant/error-dependent retry jitter being truncated to a no-op](https://github.com/temporalio/temporal/pull/11397) — 0 comments · 0 reactions · open
- **Pull Request** [improvements on time-skipping task regeneration](https://github.com/temporalio/temporal/pull/11404) — 0 comments · 0 reactions · open
- **Pull Request** [Reorganize CHASM activity codebase](https://github.com/temporalio/temporal/pull/11446) — 1 comments · 0 reactions · open
- **Pull Request** [fix: \[Scheduler\] V1->V2 migration-eligibility fix and migrated-start ID](https://github.com/temporalio/temporal/pull/11462) — 0 comments · 0 reactions · open
- **Pull Request** [Add isolated functional test clusters](https://github.com/temporalio/temporal/pull/11465) — 0 comments · 0 reactions · open
- **Pull Request** [Split Versioning3 query tests](https://github.com/temporalio/temporal/pull/11472) — 0 comments · 0 reactions · closed
- **Pull Request** [Split Versioning3 independent activity tests](https://github.com/temporalio/temporal/pull/11477) — 0 comments · 0 reactions · open
- **Pull Request** [Gradual connect shedding tasks](https://github.com/temporalio/temporal/pull/11492) — 0 comments · 0 reactions · open
- **Pull Request** [admin-batch-1: run admin batch in temporal-system](https://github.com/temporalio/temporal/pull/11509) — 0 comments · 0 reactions · open
- **Pull Request** [Release OTEL logger registrations on shutdown](https://github.com/temporalio/temporal/pull/11551) — 1 comments · 0 reactions · open
- **Pull Request** [Only count reader reads that left tasks behind as stuck attempts](https://github.com/temporalio/temporal/pull/11554) — 0 comments · 0 reactions · closed
- **Pull Request** [Fix deferred BUFFER_ONE overlap processing](https://github.com/temporalio/temporal/pull/11555) — 0 comments · 0 reactions · closed
- **Pull Request** [Isolate ALLOW_ALL schedule completion state](https://github.com/temporalio/temporal/pull/11556) — 0 comments · 0 reactions · open
- **Pull Request** [Add OpenTelemetry HTTP instrumentation](https://github.com/temporalio/temporal/pull/11558) — 1 comments · 0 reactions · closed
- **Pull Request** [Trace outbound Nexus HTTP requests](https://github.com/temporalio/temporal/pull/11559) — 1 comments · 0 reactions · open

### [containerd](https://github.com/containerd/containerd)

- **Issue** [Mount OCI Artifacts](https://github.com/containerd/containerd/issues/11381) — 14 comments · 10 reactions · open
- **Issue** [Export image config through GRPC service](https://github.com/containerd/containerd/issues/10780) — 4 comments · 5 reactions · closed
- **Issue** [OAuth2 token fetch fails with "invalid character '<'" when auth service returns HTML for POST](https://github.com/containerd/containerd/issues/12822) — 4 comments · 5 reactions · closed
- **Issue** [Support for separating read only layers from writeable layers](https://github.com/containerd/containerd/issues/10517) — 11 comments · 3 reactions · open
- **Issue** [\[SIG-Node\]: <KEP-5607 - Allow HostNetwork Pods to Use User Namespaces>](https://github.com/containerd/containerd/issues/12489) — 11 comments · 0 reactions · open
- **Issue** [Zombie containers persist in metadata after reboot despite RemoveContainer success (containerd 1.7.29)](https://github.com/containerd/containerd/issues/12511) — 15 comments · 0 reactions · closed
- **Issue** [cgroups.procs file of sandbox container is empty. Causing pod deletion to hang since runc can't find the child processes](https://github.com/containerd/containerd/issues/11984) — 12 comments · 0 reactions · closed
- **Pull Request** [cri: enable mount manager for image mounts](https://github.com/containerd/containerd/pull/13542) — 12 comments · 1 reactions · open
- **Issue** [LLM/GenAI guidelines, policies, discussion](https://github.com/containerd/containerd/issues/12892) — 7 comments · 1 reactions · open
- **Issue** [containerd memory does not decrease after pods complete — retained per-container overhead for stopped containers](https://github.com/containerd/containerd/issues/13037) — 6 comments · 1 reactions · closed
- **Issue** [critest sometimes failed when run oom test case.](https://github.com/containerd/containerd/issues/12260) — 8 comments · 0 reactions · closed
- **Issue** [\[SIG-Node\]: KEP-5474 - Enable Writable cgroups for unprivileged containers](https://github.com/containerd/containerd/issues/12252) — 2 comments · 1 reactions · open
- **Issue** [New k8s CRI API: image_id in PullImageResponse](https://github.com/containerd/containerd/issues/12997) — 7 comments · 0 reactions · open
- **Issue** [Proposal: Support Pod-level checkpoint and restore](https://github.com/containerd/containerd/issues/13970) — 3 comments · 0 reactions · open
- **Issue** [Validate runc 1.4 pids.limit breaking change does not affect default spec generation in containerd](https://github.com/containerd/containerd/issues/12607) — 5 comments · 0 reactions · closed
- **Issue** [\[SIG-Node\]: KEP-6061 - OCI Artifact-Based Security Profile Distribution](https://github.com/containerd/containerd/issues/13546) — 0 comments · 1 reactions · open
- **Issue** [\[SIG-Node\]: 5758 - Per-container ulimits configuration](https://github.com/containerd/containerd/issues/13572) — 0 comments · 1 reactions · open
- **Issue** [\[SIG-Node\]: KEP-4191: Separate Read and write only layers](https://github.com/containerd/containerd/issues/13978) — 1 comments · 1 reactions · open
- **Pull Request** [shim: send event to a queue to prevent event to be dropped](https://github.com/containerd/containerd/pull/13653) — 5 comments · 1 reactions · open
- **Issue** [\[SIG-Node\]: Decoupling from k8s projects](https://github.com/containerd/containerd/issues/11822) — 2 comments · 0 reactions · closed
- **Pull Request** [oom: avoid per-wakeup allocations in cgroup v2 OOM watcher (#13558)](https://github.com/containerd/containerd/pull/13635) — 6 comments · 0 reactions · open
- **Issue** [runtime/v2: shim delete can fail before exec when the bundle directory has been removed](https://github.com/containerd/containerd/issues/13977) — 0 comments · 0 reactions · open
- **Issue** [\[SIG-Node\]: KEP-5823: Pod-Level Checkpoint/Restore](https://github.com/containerd/containerd/issues/13979) — 0 comments · 0 reactions · open
- **Pull Request** [warning if notfound on containerStatus api](https://github.com/containerd/containerd/pull/11613) — 4 comments · 0 reactions · open
- **Pull Request** [metadata: bound snapshotter Remove during garbage collection](https://github.com/containerd/containerd/pull/13799) — 5 comments · 0 reactions · open
- **Pull Request** [Support Pod-level checkpoint and restore](https://github.com/containerd/containerd/pull/13971) — 2 comments · 0 reactions · open
- **Pull Request** [Bump cri-api and rename signal enum keys](https://github.com/containerd/containerd/pull/13603) — 4 comments · 0 reactions · open
- **Pull Request** [Export config in CRI plugin](https://github.com/containerd/containerd/pull/13940) — 0 comments · 0 reactions · closed
- **Pull Request** [erofs: instrument warm up cache](https://github.com/containerd/containerd/pull/13941) — 0 comments · 0 reactions · open
- **Pull Request** [treat missing runtime state as container already dead during kill](https://github.com/containerd/containerd/pull/13951) — 0 comments · 0 reactions · open
