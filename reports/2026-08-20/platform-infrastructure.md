# Platform / Networking / Runtime Infrastructure — 2026-08-20

> Factual GitHub evidence collected by Contribution Compass. No LLM analysis is performed.

## Contribution Leads

### [Pre-flight ahead of 1.20 upgrade doesn't drop CiliumNodeConfig v2alpha1 CRD](https://github.com/cilium/cilium/issues/47774)

- Project: `cilium/cilium`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [Gateway API L7LB north-south traffic still dropped on 1.19.4 when LB VIP is announced on a VLAN subinterface (not a bridge)](https://github.com/cilium/cilium/issues/46260)

- Project: `cilium/cilium`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [WireGuard node-to-node encryption: oversized packets cause fragmentation, and BPF fragment tracking drops most second fragments](https://github.com/cilium/cilium/issues/46100)

- Project: `cilium/cilium`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [containerd crash with program exceeds 10000-thread limit - container-log FIFO open leaks an OS thread per failed CreateContainer](https://github.com/containerd/containerd/issues/13952)

- Project: `containerd/containerd`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [Gateway API: 503 connection timeout for same-node backends with L2 announcements and VXLAN tunnel mode](https://github.com/cilium/cilium/issues/48045)

- Project: `cilium/cilium`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [Floating-point numbers in filter configuration does not get read correctly for dynamic modules and Go filters](https://github.com/envoyproxy/envoy/issues/45678)

- Project: `envoyproxy/envoy`
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

- **Pull Request** [loadbalancer: Fix dropping traffic L2Announcement with externalTrafficPolicy: Local](https://github.com/cilium/cilium/pull/46399) — 26 comments · 11 reactions · open
- **Issue** [Pre-flight ahead of 1.20 upgrade doesn't drop CiliumNodeConfig v2alpha1 CRD](https://github.com/cilium/cilium/issues/47774) — 5 comments · 6 reactions · open
- **Pull Request** [renovate: Fix primary GID of the ubuntu user and restore builder.sh root check](https://github.com/cilium/cilium/pull/46652) — 28 comments · 2 reactions · closed
- **Issue** [Gateway API L7LB north-south traffic still dropped on 1.19.4 when LB VIP is announced on a VLAN subinterface (not a bridge)](https://github.com/cilium/cilium/issues/46260) — 22 comments · 1 reactions · open
- **Pull Request** [Documentation: document mesh security model](https://github.com/cilium/cilium/pull/47912) — 5 comments · 6 reactions · closed
- **Pull Request** [Proposing Flow IR implementation to improve hubble performance](https://github.com/cilium/cilium/pull/46896) — 19 comments · 2 reactions · open
- **Pull Request** [fix: Print port numbers correctly for map cilium_lb*_reverse_sk](https://github.com/cilium/cilium/pull/47134) — 19 comments · 2 reactions · open
- **Pull Request** [\[envoy\] Add HTTP CONNECT support](https://github.com/cilium/cilium/pull/45051) — 11 comments · 3 reactions · open
- **Pull Request** [bpf: Enable extended masquerade port range for BPF masquerade](https://github.com/cilium/cilium/pull/47301) — 14 comments · 2 reactions · open
- **Pull Request** [network driver: add sriov device manager](https://github.com/cilium/cilium/pull/47387) — 14 comments · 2 reactions · open
- **Pull Request** [L7 conformance CI fixes](https://github.com/cilium/cilium/pull/47517) — 19 comments · 2 reactions · open
- **Issue** [Improve Conntrack garbage collection](https://github.com/cilium/cilium/issues/5048) — 17 comments · 0 reactions · open
- **Pull Request** [gateway-api: add support for ExtensionRef using Envoy ext_proc filter](https://github.com/cilium/cilium/pull/46479) — 9 comments · 3 reactions · open
- **Pull Request** [bgp: gate BGP announcements on host datapath init](https://github.com/cilium/cilium/pull/46948) — 12 comments · 2 reactions · open
- **Pull Request** [bpf, datapath: move the CT_* params to runtime config](https://github.com/cilium/cilium/pull/47537) — 12 comments · 2 reactions · closed
- **Pull Request** [gateway-api: nodeSelector with hostNetwork enabled](https://github.com/cilium/cilium/pull/47463) — 10 comments · 2 reactions · open
- **Issue** [WireGuard node-to-node encryption: oversized packets cause fragmentation, and BPF fragment tracking drops most second fragments](https://github.com/cilium/cilium/issues/46100) — 9 comments · 1 reactions · open
- **Pull Request** [feat(bgp): support BGP unnumbered peering (RFC 5549 / ENHE)](https://github.com/cilium/cilium/pull/47394) — 9 comments · 2 reactions · open
- **Issue** [Gateway API: 503 connection timeout for same-node backends with L2 announcements and VXLAN tunnel mode](https://github.com/cilium/cilium/issues/48045) — 6 comments · 0 reactions · open
- **Pull Request** [bpf: ICMP checksum handling in SNAT RevNAT](https://github.com/cilium/cilium/pull/43196) — 15 comments · 1 reactions · closed
- **Pull Request** [bpf: simplify E/W L7LB handling with per-EP routes](https://github.com/cilium/cilium/pull/46548) — 6 comments · 2 reactions · open
- **Pull Request** [sysdump: contain WithFileSink output to the sysdump directory](https://github.com/cilium/cilium/pull/46609) — 6 comments · 2 reactions · closed
- **Pull Request** [loader: prune global functions unreachable from live code](https://github.com/cilium/cilium/pull/46731) — 3 comments · 4 reactions · open
- **Pull Request** [Policy: fix overselection for NotIn namespace labels](https://github.com/cilium/cilium/pull/46996) — 10 comments · 2 reactions · open
- **Pull Request** [Add various routing fixes for ENI IPv6 support](https://github.com/cilium/cilium/pull/47034) — 7 comments · 2 reactions · open
- **Pull Request** [Simplify cilium policy API types validation and parsing](https://github.com/cilium/cilium/pull/47154) — 10 comments · 2 reactions · open
- **Pull Request** [install: detect GKE from kubelet path](https://github.com/cilium/cilium/pull/47945) — 10 comments · 1 reactions · closed
- **Pull Request** [Pr/gwapi session persistence](https://github.com/cilium/cilium/pull/48029) — 6 comments · 2 reactions · open
- **Issue** [MTU issue for large UDP packets with native routing and DSR](https://github.com/cilium/cilium/issues/39690) — 5 comments · 1 reactions · closed
- **Issue** [Hubble Relay does not terminate, gRPC health server remains running](https://github.com/cilium/cilium/issues/47941) — 0 comments · 1 reactions · open

### [Envoy](https://github.com/envoyproxy/envoy)

- **Pull Request** [\[WIP\] dns: add support for clusters based on SRV DNS record](https://github.com/envoyproxy/envoy/pull/35160) — 31 comments · 1 reactions · open
- **Pull Request** [internal_upstream: reverse-propagate filter state across the internal listener boundary at close](https://github.com/envoyproxy/envoy/pull/45237) — 25 comments · 0 reactions · open
- **Pull Request** [xDS: add flow control fields to ext_proc protocol](https://github.com/envoyproxy/envoy/pull/45509) — 19 comments · 0 reactions · closed
- **Pull Request** [add ratelimit descriptor extension to use jwt claims as descriptors](https://github.com/envoyproxy/envoy/pull/46138) — 12 comments · 1 reactions · closed
- **Pull Request** [fix: duplicate request body when when using FULL_DUPLEX_STREAMED ext_proc body mode with retries enabled](https://github.com/envoyproxy/envoy/pull/46095) — 14 comments · 0 reactions · open
- **Issue** [http1: unsafe ctype usage and size_t to int narrowing in the HTTP/1 parser](https://github.com/envoyproxy/envoy/issues/46505) — 5 comments · 0 reactions · open
- **Pull Request** [fix: skip null pointer in EDS endpoints validation](https://github.com/envoyproxy/envoy/pull/45207) — 10 comments · 0 reactions · closed
- **Pull Request** [composite: fail over to the next sub-cluster when a sub-cluster has no hosts](https://github.com/envoyproxy/envoy/pull/46308) — 10 comments · 0 reactions · open
- **Pull Request** [Support hot restart handoff for connectionless UDP flows](https://github.com/envoyproxy/envoy/pull/46502) — 10 comments · 0 reactions · open
- **Issue** [Floating-point numbers in filter configuration does not get read correctly for dynamic modules and Go filters](https://github.com/envoyproxy/envoy/issues/45678) — 5 comments · 0 reactions · open
- **Pull Request** [xDS: change ext_proc drain process to work directionally](https://github.com/envoyproxy/envoy/pull/45901) — 8 comments · 0 reactions · open
- **Pull Request** [stream_info: use ArenaWrappedProto for dynamic metadata](https://github.com/envoyproxy/envoy/pull/46450) — 8 comments · 0 reactions · open
- **Issue** [Newer release available `simdutf`: v9.0.0 (current: v8.1.0)](https://github.com/envoyproxy/envoy/issues/45308) — 2 comments · 0 reactions · closed
- **Pull Request** [fix(listener): filter chain gradually drains connections with drain manager](https://github.com/envoyproxy/envoy/pull/45985) — 7 comments · 0 reactions · open
- **Pull Request** [upstream: optimize LRS locality stats allocation](https://github.com/envoyproxy/envoy/pull/46449) — 7 comments · 0 reactions · closed
- **Pull Request** [tls: allow multiple TLS certificates in the upstream when using a custom TLS certificate selector](https://github.com/envoyproxy/envoy/pull/46479) — 6 comments · 0 reactions · open
- **Pull Request** [mcp_transcoder: Fix Unbounded Recursion DoS](https://github.com/envoyproxy/envoy/pull/46543) — 6 comments · 0 reactions · closed
- **Pull Request** [rds: make the init manager for rds works for filter_chain and oauth2](https://github.com/envoyproxy/envoy/pull/46664) — 6 comments · 0 reactions · closed
- **Issue** [Newer release available `abseil_cpp`: 20260526.0 (current: 20260107.1)](https://github.com/envoyproxy/envoy/issues/45430) — 1 comments · 0 reactions · closed
- **Issue** [Newer release available `bazel_gazelle`: v0.52.2 (current: v0.47.0)](https://github.com/envoyproxy/envoy/issues/46364) — 0 comments · 0 reactions · closed
- **Issue** [Panic mode routes traffic to hosts that were excluded from the panic calculation (EDS `DRAINING`)](https://github.com/envoyproxy/envoy/issues/46800) — 1 comments · 0 reactions · open
- **Issue** [Newer release available `abseil_cpp`: 20260817.0 (current: 20260107.1)](https://github.com/envoyproxy/envoy/issues/46806) — 0 comments · 0 reactions · open
- **Issue** [Newer release available `gazelle`: v2.0.0-3 (current: v0.47.0)](https://github.com/envoyproxy/envoy/issues/46807) — 0 comments · 0 reactions · open
- **Issue** [Newer release available `simdutf`: v9.1.0 (current: v8.1.0)](https://github.com/envoyproxy/envoy/issues/46808) — 0 comments · 0 reactions · open
- **Issue** [Resurrect Envoy on Windows](https://github.com/envoyproxy/envoy/issues/46812) — 1 comments · 0 reactions · open
- **Pull Request** [\[WIP\] bazel: Switch to bzlmod](https://github.com/envoyproxy/envoy/pull/42890) — 5 comments · 0 reactions · open
- **Pull Request** [bazel: Add compatibility stubs for bzlmod](https://github.com/envoyproxy/envoy/pull/43255) — 4 comments · 0 reactions · closed
- **Pull Request** [router: add auto_host_rewrite support to RequestMirrorPolicy](https://github.com/envoyproxy/envoy/pull/44450) — 9 comments · 0 reactions · open
- **Pull Request** [lua: add downstreamRequestHeaders() accessor for response path](https://github.com/envoyproxy/envoy/pull/44594) — 8 comments · 0 reactions · open
- **Pull Request** [stats: migrate rds/scope rds to use new stats API](https://github.com/envoyproxy/envoy/pull/45914) — 5 comments · 0 reactions · closed

### [Temporal](https://github.com/temporalio/temporal)

- **Issue** [Replace LeveledCompactionStrategy (LCS) with Cassandra 5.x default UnifiedCompactionStrategy (UCS) in schema.cql](https://github.com/temporalio/temporal/issues/11314) — 2 comments · 0 reactions · open
- **Issue** [Fairsim partial counter configuration resets unspecified defaults](https://github.com/temporalio/temporal/issues/11534) — 2 comments · 0 reactions · open
- **Issue** [DeleteWorkerDeploymentVersion fails permanently when a version summary outlives its version workflow](https://github.com/temporalio/temporal/issues/11539) — 3 comments · 0 reactions · open
- **Issue** [Nexus: server may send malformed `request-timeout` header (negative values and units outside the Nexus grammar)](https://github.com/temporalio/temporal/issues/11569) — 2 comments · 0 reactions · open
- **Issue** [Persistence rate-limit ResourceExhausted is flattened to Unavailable in ProcessOutgoingSearchAttributes](https://github.com/temporalio/temporal/issues/11571) — 2 comments · 0 reactions · open
- **Issue** [PostgreSQL visibility v1.14 schema upgrade misses the v1.10–v1.13 rewrite optimization](https://github.com/temporalio/temporal/issues/11594) — 2 comments · 0 reactions · open
- **Issue** [Request Patch Release - For High & Critical Vulnerabilities in latest images - AWS Inspector Report](https://github.com/temporalio/temporal/issues/11497) — 1 comments · 0 reactions · open
- **Issue** [A brief `Unavailable` blip resets History queue backoff, causing a sustained retry storm](https://github.com/temporalio/temporal/issues/11547) — 1 comments · 0 reactions · open
- **Issue** [tdbg dlq commands reject the archival task category (5)](https://github.com/temporalio/temporal/issues/11586) — 0 comments · 0 reactions · closed
- **Issue** [Data race in UpdateWithStart: ExecutionState.Status read after workflow lock release](https://github.com/temporalio/temporal/issues/11600) — 0 comments · 0 reactions · closed
- **Issue** [Add a built-in Kubernetes service account ClaimMapper selectable via `authorization.claimMapper`](https://github.com/temporalio/temporal/issues/11607) — 1 comments · 0 reactions · open
- **Issue** [yuandrew test issue](https://github.com/temporalio/temporal/issues/11625) — 0 comments · 0 reactions · open
- **Issue** [MySQL persistence: support multi-host connectAddr and/or SRV-based endpoint discovery (no LB/VIP environments)](https://github.com/temporalio/temporal/issues/10171) — 2 comments · 0 reactions · open
- **Issue** [Membership: provide an operator-facing way to evict a "gray-failed" host (SWIM-reachable but unable to serve) from the ring](https://github.com/temporalio/temporal/issues/11108) — 2 comments · 0 reactions · open
- **Issue** [Membership: emit per-service reachable/available/draining member gauges](https://github.com/temporalio/temporal/issues/11146) — 3 comments · 0 reactions · open
- **Pull Request** [\[Scheduler\] Exclude retained completion history from Generator buffer capacity](https://github.com/temporalio/temporal/pull/11621) — 3 comments · 1 reactions · open
- **Issue** [Migrate Cassandra driver from legacy gocql v1.7.0 to apache/cassandra-gocql-driver/v2](https://github.com/temporalio/temporal/issues/11124) — 1 comments · 0 reactions · open
- **Issue** [Race Condition in Queue Pending Task Mitigation](https://github.com/temporalio/temporal/issues/11188) — 1 comments · 0 reactions · open
- **Issue** [Client TLS configs do not pick up refreshed root CAs](https://github.com/temporalio/temporal/issues/11230) — 1 comments · 0 reactions · open
- **Issue** [Nexus reapply cannot distinguish "CHASM owns this operation" from "no tree owns it"](https://github.com/temporalio/temporal/issues/11384) — 1 comments · 0 reactions · open
- **Issue** [A lost `RegisterWorkerInVersion` task permanently disables activity dispatch for a task queue](https://github.com/temporalio/temporal/issues/11402) — 1 comments · 0 reactions · open
- **Issue** [When temporal k8s pod restart, healer still probe the old pod ip ?](https://github.com/temporalio/temporal/issues/11429) — 1 comments · 0 reactions · open
- **Issue** [Bump Go toolchain to 1.26.4 to resolve net/textproto vuln (CVE-2026-42507 / GO-2026-5039)](https://github.com/temporalio/temporal/issues/11495) — 1 comments · 0 reactions · open
- **Issue** [ui-server: ListNamespaces/GetClusterInfo return 403 for namespace-scoped admin tokens (requires undocumented "temporal-system:" permission)](https://github.com/temporalio/temporal/issues/11639) — 0 comments · 0 reactions · open
- **Pull Request** [Make standalone activity completion callback attachment idempotent after closure](https://github.com/temporalio/temporal/pull/11612) — 1 comments · 1 reactions · closed
- **Pull Request** [Prevent malformed retry delays from poisoning Nexus completions](https://github.com/temporalio/temporal/pull/11617) — 1 comments · 1 reactions · closed
- **Pull Request** [Make standalone activity completion callback attachment idempotent after closure](https://github.com/temporalio/temporal/pull/11628) — 0 comments · 1 reactions · open
- **Pull Request** [Fix invoker action limit across phases](https://github.com/temporalio/temporal/pull/11630) — 0 comments · 1 reactions · open
- **Pull Request** [Adaptive test timeouts via Await](https://github.com/temporalio/temporal/pull/10417) — 2 comments · 0 reactions · open
- **Pull Request** [Recognize the new `commonpb` Worker callback variant](https://github.com/temporalio/temporal/pull/11380) — 2 comments · 0 reactions · open

### [containerd](https://github.com/containerd/containerd)

- **Issue** [Memory and CPU usage growing constantly, only restart helps](https://github.com/containerd/containerd/issues/11950) — 12 comments · 0 reactions · closed
- **Pull Request** [Make stat cancellable in case of stuck paths](https://github.com/containerd/containerd/pull/12023) — 38 comments · 0 reactions · open
- **Issue** [\[Go 1.24\] version >=v2.2 fails to create containers from images having /etc symlinked to an absolute path](https://github.com/containerd/containerd/issues/13382) — 2 comments · 5 reactions · open
- **Issue** [containerd crash with program exceeds 10000-thread limit - container-log FIFO open leaks an OS thread per failed CreateContainer](https://github.com/containerd/containerd/issues/13952) — 9 comments · 0 reactions · open
- **Pull Request** [cri: enable mount manager for image mounts](https://github.com/containerd/containerd/pull/13542) — 12 comments · 1 reactions · open
- **Issue** [\[SIG-Node\]: KEP-4191: Separate Read and write only layers](https://github.com/containerd/containerd/issues/13978) — 2 comments · 1 reactions · open
- **Issue** [container list api should support ignore filed](https://github.com/containerd/containerd/issues/12882) — 6 comments · 0 reactions · closed
- **Issue** [CRI API: allow to specify a moby namespace as a read-only source of images for kubernetes](https://github.com/containerd/containerd/issues/12761) — 5 comments · 0 reactions · closed
- **Issue** [\[SIG-Node\]: KEP-5823: Pod-Level Checkpoint/Restore](https://github.com/containerd/containerd/issues/13979) — 0 comments · 0 reactions · open
- **Pull Request** [oom: avoid per-wakeup allocations in cgroup v2 OOM watcher (#13558)](https://github.com/containerd/containerd/pull/13635) — 8 comments · 0 reactions · open
- **Pull Request** [pkg/oci: resolve rootfs symlinks for user lookup](https://github.com/containerd/containerd/pull/13818) — 3 comments · 2 reactions · open
- **Issue** [Add Request Metadata to Image Verification Plugin](https://github.com/containerd/containerd/issues/12540) — 1 comments · 0 reactions · closed
- **Pull Request** [warning if notfound on containerStatus api](https://github.com/containerd/containerd/pull/11613) — 4 comments · 0 reactions · open
- **Pull Request** [metadata: bound snapshotter Remove during garbage collection](https://github.com/containerd/containerd/pull/13799) — 5 comments · 0 reactions · open
- **Pull Request** [fix(runtime): apply load timeout to load shim](https://github.com/containerd/containerd/pull/13954) — 2 comments · 0 reactions · closed
- **Pull Request** [build(deps): bump the otel group with 8 updates](https://github.com/containerd/containerd/pull/13961) — 2 comments · 0 reactions · closed
- **Pull Request** [Support Pod-level checkpoint and restore](https://github.com/containerd/containerd/pull/13971) — 3 comments · 0 reactions · open
- **Pull Request** [vendor: github.com/sirupsen/logrus v1.10.1](https://github.com/containerd/containerd/pull/13294) — 1 comments · 0 reactions · open
- **Pull Request** [cri: add timeout warning log when stat mount point exceeds threshold](https://github.com/containerd/containerd/pull/13866) — 5 comments · 0 reactions · open
- **Pull Request** [mounts: handle temporary activation without system mounts](https://github.com/containerd/containerd/pull/13918) — 4 comments · 0 reactions · open
- **Pull Request** [cri, nri: record resolved image name and digest in container metadata](https://github.com/containerd/containerd/pull/13960) — 1 comments · 0 reactions · closed
- **Pull Request** [build(deps): bump github.com/klauspost/compress from 1.19.1 to 1.19.2](https://github.com/containerd/containerd/pull/13962) — 0 comments · 0 reactions · closed
- **Pull Request** [core/unpack: fetch layers of every config-sharing manifest](https://github.com/containerd/containerd/pull/13966) — 0 comments · 0 reactions · open
- **Pull Request** [vendor: github.com/stretchr/testify v1.12.1](https://github.com/containerd/containerd/pull/13973) — 0 comments · 0 reactions · open
- **Pull Request** [remotes/docker: add tls_groups host configuration](https://github.com/containerd/containerd/pull/13976) — 0 comments · 0 reactions · open
- **Pull Request** [feat(shim): implement Go stack dump for Windows shims](https://github.com/containerd/containerd/pull/13981) — 1 comments · 0 reactions · open
- **Pull Request** [vendor: github.com/Microsoft/hcsshim v0.15.0-rc.1](https://github.com/containerd/containerd/pull/12902) — 3 comments · 0 reactions · closed
- **Pull Request** [build(deps): bump google.golang.org/grpc from 1.82.1 to 1.83.0](https://github.com/containerd/containerd/pull/13920) — 2 comments · 0 reactions · closed
- **Pull Request** [update runhcs to v0.15.0-rc.4](https://github.com/containerd/containerd/pull/13984) — 2 comments · 0 reactions · closed
- **Pull Request** [pkg/archive: reject out-of-range owner IDs in layer headers](https://github.com/containerd/containerd/pull/13796) — 0 comments · 0 reactions · open
