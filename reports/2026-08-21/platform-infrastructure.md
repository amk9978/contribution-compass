# Platform / Networking / Runtime Infrastructure — 2026-08-21

> Factual GitHub evidence collected by Contribution Compass. No LLM analysis is performed.

## Contribution Leads

### [Compression and decompression of gRPC through envoy proxy](https://github.com/envoyproxy/envoy/issues/41893)

- Project: `envoyproxy/envoy`
- Tier: `maintainer-invited`
- Evidence: Maintainer invitation label: help wanted; No assignee is listed
- Caveat: Confirm scope and availability with the maintainers before starting work.

### [values.schema.json contain duplicate data](https://github.com/cilium/cilium/issues/41099)

- Project: `cilium/cilium`
- Tier: `maintainer-invited`
- Evidence: Maintainer invitation label: help wanted; No assignee is listed
- Caveat: Confirm scope and availability with the maintainers before starting work.

### [admin: making a streaming version of /config_dump](https://github.com/envoyproxy/envoy/issues/32054)

- Project: `envoyproxy/envoy`
- Tier: `maintainer-invited`
- Evidence: Maintainer invitation label: help wanted; No assignee is listed
- Caveat: Confirm scope and availability with the maintainers before starting work.

### [Manifest Priority when pulling windows images with Windows Server 2025](https://github.com/containerd/containerd/issues/11366)

- Project: `containerd/containerd`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [composite filter chain cannot handle stop correctly](https://github.com/envoyproxy/envoy/issues/42807)

- Project: `envoyproxy/envoy`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [Gateway API: 503 connection timeout for same-node backends with L2 announcements and VXLAN tunnel mode](https://github.com/cilium/cilium/issues/48045)

- Project: `cilium/cilium`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [containerd crash with program exceeds 10000-thread limit - container-log FIFO open leaks an OS thread per failed CreateContainer](https://github.com/containerd/containerd/issues/13952)

- Project: `containerd/containerd`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [host-firewall-egress-to-fqdns connectivity test fails on RHEL8.10](https://github.com/cilium/cilium/issues/47975)

- Project: `cilium/cilium`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [Kernel v7.2: FnSetRetval/CGroupSock call bpf_set_retval#187: R1 is not a scalar](https://github.com/cilium/cilium/issues/48016)

- Project: `cilium/cilium`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [Connected UDP sockets remain pinned to deleted CoreDNS backends after Pod IP changes](https://github.com/cilium/cilium/issues/48096)

- Project: `cilium/cilium`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

## Important Updates

### [Cilium](https://github.com/cilium/cilium)

- **Issue** [CFP: BFD(Bidirectional Forwarding Detection) support in BGP Control plane](https://github.com/cilium/cilium/issues/22394) — 16 comments · 42 reactions · open
- **Pull Request** [loadbalancer: Fix dropping traffic L2Announcement with externalTrafficPolicy: Local](https://github.com/cilium/cilium/pull/46399) — 28 comments · 11 reactions · open
- **Issue** [CFP: Network Quality of Service (QOS) API](https://github.com/cilium/cilium/issues/43150) — 12 comments · 8 reactions · open
- **Pull Request** [gateway-api: Implement FrontendTLSValidation for downstream mTLS](https://github.com/cilium/cilium/pull/43945) — 30 comments · 5 reactions · open
- **Issue** [Pre-flight ahead of 1.20 upgrade doesn't drop CiliumNodeConfig v2alpha1 CRD](https://github.com/cilium/cilium/issues/47774) — 7 comments · 6 reactions · open
- **Pull Request** [Test: do not merge](https://github.com/cilium/cilium/pull/41617) — 28 comments · 2 reactions · open
- **Pull Request** [L7 conformance CI fixes](https://github.com/cilium/cilium/pull/47517) — 21 comments · 2 reactions · open
- **Pull Request** [\[envoy\] Add HTTP CONNECT support](https://github.com/cilium/cilium/pull/45051) — 13 comments · 3 reactions · open
- **Pull Request** [bpf: Enable extended masquerade port range for BPF masquerade](https://github.com/cilium/cilium/pull/47301) — 14 comments · 2 reactions · open
- **Pull Request** [CLI: add toleration for a single etcd container restart](https://github.com/cilium/cilium/pull/48106) — 3 comments · 6 reactions · closed
- **Pull Request** [gateway-api: add support for ExtensionRef using Envoy ext_proc filter](https://github.com/cilium/cilium/pull/46479) — 9 comments · 3 reactions · open
- **Pull Request** [bgp: gate BGP announcements on host datapath init](https://github.com/cilium/cilium/pull/46948) — 13 comments · 2 reactions · open
- **Pull Request** [gateway-api: Reduce duplication + more test coverage](https://github.com/cilium/cilium/pull/46474) — 10 comments · 2 reactions · open
- **Pull Request** [lb (fix): require active state for backend when using topology hints](https://github.com/cilium/cilium/pull/47054) — 15 comments · 2 reactions · open
- **Pull Request** [Simplify cilium policy API types validation and parsing](https://github.com/cilium/cilium/pull/47154) — 10 comments · 2 reactions · open
- **Pull Request** [clustermesh: move cluster ID reservation logic into common and restart connection on config update](https://github.com/cilium/cilium/pull/47747) — 15 comments · 2 reactions · open
- **Pull Request** [Revert: re-create CiliumNodeConfig v2alpha1](https://github.com/cilium/cilium/pull/48087) — 3 comments · 4 reactions · closed
- **Pull Request** [mac: Make `mac.MAC` a `\[6\]byte`](https://github.com/cilium/cilium/pull/48089) — 3 comments · 4 reactions · open
- **Issue** [With Gateway API, the 3-way handshake fails when Envoy and the Backend Pod are running on the same Node.](https://github.com/cilium/cilium/issues/47591) — 8 comments · 0 reactions · open
- **Issue** [Gateway API: 503 connection timeout for same-node backends with L2 announcements and VXLAN tunnel mode](https://github.com/cilium/cilium/issues/48045) — 8 comments · 0 reactions · open
- **Pull Request** [Gateway-api: add support for session persistence](https://github.com/cilium/cilium/pull/48029) — 8 comments · 2 reactions · open
- **Pull Request** [envoy: Clarify legacy UpdateEnvoyResources](https://github.com/cilium/cilium/pull/48066) — 4 comments · 3 reactions · open
- **Pull Request** [datapath/l2responder: use l3 socket for v6 solicited node responder](https://github.com/cilium/cilium/pull/46332) — 10 comments · 2 reactions · closed
- **Pull Request** [allow cni channing generic veth to use bandwidth QoS](https://github.com/cilium/cilium/pull/46431) — 11 comments · 2 reactions · open
- **Pull Request** [bpf: simplify E/W L7LB handling with per-EP routes](https://github.com/cilium/cilium/pull/46548) — 7 comments · 2 reactions · open
- **Pull Request** [ipam: Added ReservedRange To CiliumPodIPPool](https://github.com/cilium/cilium/pull/46880) — 6 comments · 2 reactions · open
- **Pull Request** [.github: trigger workflow lint checks on merge_group](https://github.com/cilium/cilium/pull/47302) — 6 comments · 2 reactions · open
- **Pull Request** [linux/node: deallocate all IDs for deleted nodes](https://github.com/cilium/cilium/pull/47567) — 6 comments · 3 reactions · open
- **Pull Request** [ci: replace unsupported LLVM installation action](https://github.com/cilium/cilium/pull/47776) — 6 comments · 2 reactions · open
- **Pull Request** [install: detect GKE from kubelet path](https://github.com/cilium/cilium/pull/47945) — 11 comments · 1 reactions · closed

### [Envoy](https://github.com/envoyproxy/envoy)

- **Pull Request** [\[WIP\] dns: add support for clusters based on SRV DNS record](https://github.com/envoyproxy/envoy/pull/35160) — 31 comments · 1 reactions · open
- **Issue** [Support fallback to different backend cluster based on response status code from the primary cluster](https://github.com/envoyproxy/envoy/issues/38841) — 14 comments · 1 reactions · open
- **Issue** [Resurrect Envoy on Windows](https://github.com/envoyproxy/envoy/issues/46812) — 1 comments · 3 reactions · open
- **Pull Request** [Queue policy extension](https://github.com/envoyproxy/envoy/pull/43355) — 21 comments · 0 reactions · open
- **Issue** [admin: making a streaming version of /clusters](https://github.com/envoyproxy/envoy/issues/32055) — 11 comments · 1 reactions · open
- **Issue** [composite filter chain cannot handle stop correctly](https://github.com/envoyproxy/envoy/issues/42807) — 10 comments · 1 reactions · open
- **Pull Request** [quic: populate peer certificate details in QUIC connection info](https://github.com/envoyproxy/envoy/pull/45978) — 16 comments · 0 reactions · open
- **Issue** [Proposal: new LB extension envoy.load_balancing_policies.per_worker_subset (per-Envoy-worker subsetting, no upstream/xDS coordination)](https://github.com/envoyproxy/envoy/issues/45682) — 7 comments · 0 reactions · closed
- **Pull Request** [fix: duplicate request body when when using FULL_DUPLEX_STREAMED ext_proc body mode with retries enabled](https://github.com/envoyproxy/envoy/pull/46095) — 14 comments · 0 reactions · open
- **Pull Request** [ext_proc: adding direct mode_override support](https://github.com/envoyproxy/envoy/pull/46318) — 13 comments · 0 reactions · open
- **Issue** [openssl compat: implement CNSA1_202603 compliance policy](https://github.com/envoyproxy/envoy/issues/46104) — 2 comments · 0 reactions · closed
- **Issue** [tls: share parsed CA trust store (X509_STORE) across contexts built from identical CA material](https://github.com/envoyproxy/envoy/issues/46114) — 2 comments · 0 reactions · closed
- **Issue** [ext_proc FULL_DUPLEX_STREAMED: duplicate RequestBody chunk with EndOfStream=true on large bodies (1.35+)](https://github.com/envoyproxy/envoy/issues/46237) — 6 comments · 0 reactions · open
- **Pull Request** [mcp_transcoder: add header and cookie param transcoding.](https://github.com/envoyproxy/envoy/pull/45327) — 10 comments · 0 reactions · open
- **Pull Request** [metadata: supported to access specific item of ListValue by the MetadataKey](https://github.com/envoyproxy/envoy/pull/45948) — 10 comments · 0 reactions · open
- **Pull Request** [match_delegate: lazily create the delegated filter](https://github.com/envoyproxy/envoy/pull/46259) — 11 comments · 0 reactions · open
- **Pull Request** [\[fault filter\]: support custom error message for the aborted requests.](https://github.com/envoyproxy/envoy/pull/46814) — 10 comments · 0 reactions · open
- **Issue** [Compression and decompression of gRPC through envoy proxy](https://github.com/envoyproxy/envoy/issues/41893) — 4 comments · 0 reactions · open
- **Issue** [Panic mode routes traffic to hosts that were excluded from the panic calculation (EDS `DRAINING`)](https://github.com/envoyproxy/envoy/issues/46800) — 1 comments · 0 reactions · open
- **Issue** [Feature: Queue manager for circuit breaker queue](https://github.com/envoyproxy/envoy/issues/9606) — 5 comments · 0 reactions · open
- **Pull Request** [fix(filter): create filter chain before calling onLocalReply](https://github.com/envoyproxy/envoy/pull/45988) — 8 comments · 0 reactions · open
- **Issue** [admin: making a streaming version of /config_dump](https://github.com/envoyproxy/envoy/issues/32054) — 3 comments · 0 reactions · open
- **Pull Request** [upstream: add opt-in validation of bind config network namespaces](https://github.com/envoyproxy/envoy/pull/45976) — 7 comments · 0 reactions · open
- **Pull Request** [proto_message_extraction: use ArenaWrappedProto for extracted message](https://github.com/envoyproxy/envoy/pull/46453) — 6 comments · 0 reactions · closed
- **Pull Request** [http: add support for the QUERY method (RFC 10008)](https://github.com/envoyproxy/envoy/pull/46496) — 6 comments · 0 reactions · open
- **Pull Request** [network: send zero-length UDP datagrams](https://github.com/envoyproxy/envoy/pull/46613) — 6 comments · 0 reactions · open
- **Pull Request** [load_aware_locality: add out-of-band ORCA reporting](https://github.com/envoyproxy/envoy/pull/46670) — 6 comments · 0 reactions · open
- **Issue** [Newer release available `build_bazel_rules_apple`: 4.5.3 (current: 3.20.1)](https://github.com/envoyproxy/envoy/issues/45278) — 0 comments · 0 reactions · closed
- **Issue** [Newer release available `rules_apple`: 4.5.3 (current: 3.20.1)](https://github.com/envoyproxy/envoy/issues/46825) — 0 comments · 0 reactions · open
- **Issue** [Filter manager drops a body frame when a filter buffers it and returns Continue](https://github.com/envoyproxy/envoy/issues/46841) — 0 comments · 0 reactions · open

### [Temporal](https://github.com/temporalio/temporal)

- **Issue** [DeleteWorkerDeploymentVersion fails permanently when a version summary outlives its version workflow](https://github.com/temporalio/temporal/issues/11539) — 4 comments · 0 reactions · closed
- **Issue** [Replace LeveledCompactionStrategy (LCS) with Cassandra 5.x default UnifiedCompactionStrategy (UCS) in schema.cql](https://github.com/temporalio/temporal/issues/11314) — 3 comments · 0 reactions · open
- **Issue** [Worker Deployment version GC does not reclaim eligible drained versions at maxVersionsInDeployment, wedging rollouts](https://github.com/temporalio/temporal/issues/10737) — 5 comments · 0 reactions · open
- **Issue** [Batch Operations Can Hang Indefinitely on Visibility Query Timeouts](https://github.com/temporalio/temporal/issues/11683) — 0 comments · 0 reactions · open
- **Issue** [SQL session refresh can close the connection pool irrecoverably ("sql: database is closed"); membership heartbeat then fails silently forever, leaving a zombie cluster that reports SERVING](https://github.com/temporalio/temporal/issues/11691) — 0 comments · 0 reactions · open
- **Pull Request** [Make supported callback kinds configurable](https://github.com/temporalio/temporal/pull/11566) — 5 comments · 0 reactions · open
- **Pull Request** [Make standalone activity completion callback attachment idempotent after closure](https://github.com/temporalio/temporal/pull/11628) — 0 comments · 1 reactions · closed
- **Pull Request** [Configurable limit on activity info failure size](https://github.com/temporalio/temporal/pull/11644) — 0 comments · 1 reactions · open
- **Pull Request** [Preserve the original workflow start time on RebuildMutableState](https://github.com/temporalio/temporal/pull/11668) — 0 comments · 1 reactions · open
- **Pull Request** [Adaptive test timeouts via Await](https://github.com/temporalio/temporal/pull/10417) — 2 comments · 0 reactions · closed
- **Pull Request** [\[SDK Ergonomics\] NEXUS-519: Support Query-backed Nexus Operations](https://github.com/temporalio/temporal/pull/11274) — 3 comments · 0 reactions · closed
- **Pull Request** [Surface canceled CHASM Nexus operations as CanceledError](https://github.com/temporalio/temporal/pull/11312) — 7 comments · 0 reactions · open
- **Pull Request** [Populate CallbackInfo.outcome](https://github.com/temporalio/temporal/pull/11520) — 3 comments · 0 reactions · open
- **Pull Request** [Add helpers for testing exported spans](https://github.com/temporalio/temporal/pull/11655) — 2 comments · 0 reactions · open
- **Pull Request** [Emit namespace migration workflow lifecycle events](https://github.com/temporalio/temporal/pull/11658) — 2 comments · 0 reactions · closed
- **Pull Request** [Support MySQL multi-host and SRV connections](https://github.com/temporalio/temporal/pull/11659) — 2 comments · 0 reactions · open
- **Pull Request** [Fix activity timeout regeneration after unpause](https://github.com/temporalio/temporal/pull/11666) — 3 comments · 0 reactions · closed
- **Pull Request** [Fix 9436 describe task queue stats](https://github.com/temporalio/temporal/pull/9521) — 3 comments · 0 reactions · open
- **Pull Request** [Await 2.0](https://github.com/temporalio/temporal/pull/10377) — 0 comments · 0 reactions · open
- **Pull Request** [Annotate worker task spans](https://github.com/temporalio/temporal/pull/10739) — 1 comments · 0 reactions · open
- **Pull Request** [Richer await timeout diagnostics](https://github.com/temporalio/temporal/pull/10781) — 0 comments · 0 reactions · open
- **Pull Request** [Return early from CHASM PollComponent when shard moves off host](https://github.com/temporalio/temporal/pull/10878) — 0 comments · 0 reactions · closed
- **Pull Request** [Add Worker Deployment and BuildID labels to (workflow,activity) task completion metrics](https://github.com/temporalio/temporal/pull/11348) — 1 comments · 0 reactions · open
- **Pull Request** [Monitor child execution NotFound after ChildWorkflowExecutionStarted](https://github.com/temporalio/temporal/pull/11447) — 0 comments · 1 reactions · open
- **Pull Request** [fix: \[Scheduler\] V1->V2 migration-eligibility fix and migrated-start ID](https://github.com/temporalio/temporal/pull/11462) — 0 comments · 0 reactions · open
- **Pull Request** [NEXUS-504: Refactor Nexus frontend interceptors](https://github.com/temporalio/temporal/pull/11464) — 0 comments · 0 reactions · open
- **Pull Request** [admin-batch-1: run admin batch in temporal-system](https://github.com/temporalio/temporal/pull/11509) — 0 comments · 0 reactions · open
- **Pull Request** [Isolate ALLOW_ALL schedule completion state](https://github.com/temporalio/temporal/pull/11556) — 0 comments · 0 reactions · open
- **Pull Request** [Annotate Nexus spans](https://github.com/temporalio/temporal/pull/11561) — 1 comments · 0 reactions · closed
- **Pull Request** [Add completion callbacks to SANOs](https://github.com/temporalio/temporal/pull/11567) — 1 comments · 0 reactions · open

### [containerd](https://github.com/containerd/containerd)

- **Issue** [Manifest Priority when pulling windows images with Windows Server 2025](https://github.com/containerd/containerd/issues/11366) — 22 comments · 2 reactions · open
- **Issue** [\[Go 1.24\] version >=v2.2 fails to create containers from images having /etc symlinked to an absolute path](https://github.com/containerd/containerd/issues/13382) — 2 comments · 5 reactions · closed
- **Issue** [LLM/GenAI guidelines, policies, discussion](https://github.com/containerd/containerd/issues/12892) — 8 comments · 1 reactions · closed
- **Issue** [containerd crash with program exceeds 10000-thread limit - container-log FIFO open leaks an OS thread per failed CreateContainer](https://github.com/containerd/containerd/issues/13952) — 11 comments · 0 reactions · open
- **Issue** [32 bit arm image pull problems](https://github.com/containerd/containerd/issues/12838) — 13 comments · 0 reactions · closed
- **Issue** [\[SIG-Node\]: KEP-5474 - Enable Writable cgroups for unprivileged containers](https://github.com/containerd/containerd/issues/12252) — 2 comments · 1 reactions · open
- **Pull Request** [pkg/oci: resolve rootfs symlinks for user lookup](https://github.com/containerd/containerd/pull/13818) — 7 comments · 2 reactions · closed
- **Issue** [Proposal: Support Pod-level checkpoint and restore](https://github.com/containerd/containerd/issues/13970) — 4 comments · 0 reactions · closed
- **Issue** [2.2.0 config_path seems to have broken mirroring in config.toml](https://github.com/containerd/containerd/issues/12636) — 4 comments · 0 reactions · closed
- **Issue** [Add tls_groups configuration for Post-Quantum TLS in registry host config](https://github.com/containerd/containerd/issues/13663) — 5 comments · 0 reactions · open
- **Issue** [\[SIG-Node\]: KEP-5823: Pod-Level Checkpoint/Restore](https://github.com/containerd/containerd/issues/13979) — 1 comments · 0 reactions · open
- **Issue** [containerd 2.2 cannot parse the bootstrap response from a 2.3 runc shim](https://github.com/containerd/containerd/issues/13763) — 0 comments · 0 reactions · closed
- **Issue** [update kubernetes to release v1.37 when the GA becomes available ~wed August 26 eom](https://github.com/containerd/containerd/issues/13994) — 0 comments · 0 reactions · open
- **Issue** [Layers of config-sharing manifests are missing from the content store after pull](https://github.com/containerd/containerd/issues/14000) — 0 comments · 0 reactions · open
- **Pull Request** [metadata: bound snapshotter Remove during garbage collection](https://github.com/containerd/containerd/pull/13799) — 5 comments · 0 reactions · open
- **Pull Request** [mounts: handle temporary activation without system mounts](https://github.com/containerd/containerd/pull/13918) — 5 comments · 0 reactions · open
- **Pull Request** [pkg/shim: Return JSON bootstrap results to legacy callers](https://github.com/containerd/containerd/pull/13764) — 7 comments · 0 reactions · closed
- **Pull Request** [remotes/docker: retry blob fetch on connection reset by peer](https://github.com/containerd/containerd/pull/13915) — 3 comments · 0 reactions · open
- **Pull Request** [vendor: github.com/sirupsen/logrus v1.10.1](https://github.com/containerd/containerd/pull/13294) — 1 comments · 0 reactions · open
- **Pull Request** [minimal in-memory sandbox shim](https://github.com/containerd/containerd/pull/13300) — 1 comments · 1 reactions · open
- **Pull Request** [reference: reject `..` path components that rewrite the host](https://github.com/containerd/containerd/pull/13781) — 4 comments · 0 reactions · open
- **Pull Request** [cri: report swap and pod-level IO PSI in CRI stats](https://github.com/containerd/containerd/pull/13825) — 0 comments · 0 reactions · open
- **Pull Request** [build(deps): bump github.com/prometheus/client_golang from 1.24.0 to 1.24.1](https://github.com/containerd/containerd/pull/13883) — 0 comments · 0 reactions · open
- **Pull Request** [pkg/shim: Report bootstrap API mismatch on startup](https://github.com/containerd/containerd/pull/13910) — 0 comments · 0 reactions · closed
- **Pull Request** [cri, nri: record resolved image name and digest in container metadata](https://github.com/containerd/containerd/pull/13960) — 1 comments · 0 reactions · closed
- **Pull Request** [core/unpack: fetch layers of every config-sharing manifest](https://github.com/containerd/containerd/pull/13966) — 0 comments · 0 reactions · open
- **Pull Request** [internal/cri/server: avoid debug log formatting for container spec](https://github.com/containerd/containerd/pull/13972) — 0 comments · 0 reactions · open
- **Pull Request** [vendor: github.com/stretchr/testify v1.12.1](https://github.com/containerd/containerd/pull/13973) — 0 comments · 0 reactions · closed
- **Pull Request** [Add AGENTS.md guidance for AI coding agents](https://github.com/containerd/containerd/pull/13980) — 0 comments · 0 reactions · open
- **Pull Request** [cri: support to specify snapshot rwlayer path for overlayfs](https://github.com/containerd/containerd/pull/13986) — 0 comments · 0 reactions · open
