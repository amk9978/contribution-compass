# Platform / Networking / Runtime Infrastructure — 2026-08-22

> Factual GitHub evidence collected by Contribution Compass. No LLM analysis is performed.

## Contribution Leads

### [v1.19.3: WireGuard handshakes never complete on any node pair (tunnel/geneve + DSR), all cross-node pod traffic dead, on Oracle Linux only.](https://github.com/cilium/cilium/issues/47565)

- Project: `cilium/cilium`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [Kernel v7.2: FnSetRetval/CGroupSock call bpf_set_retval#187: R1 is not a scalar](https://github.com/cilium/cilium/issues/48016)

- Project: `cilium/cilium`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [There is no way to enable envoy-metrics service monitor for embedded envoy](https://github.com/cilium/cilium/issues/47825)

- Project: `cilium/cilium`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

## Important Updates

### [Cilium](https://github.com/cilium/cilium)

- **Issue** [v1.19.3: WireGuard handshakes never complete on any node pair (tunnel/geneve + DSR), all cross-node pod traffic dead, on Oracle Linux only.](https://github.com/cilium/cilium/issues/47565) — 5 comments · 1 reactions · open
- **Issue** [Cilium HTTP L7 policies break HTTP proxy (CONNECT) connections](https://github.com/cilium/cilium/issues/24276) — 10 comments · 6 reactions · closed
- **Issue** [BPF masquerading: Traffic to ExternalIP node addresses is masqueraded](https://github.com/cilium/cilium/issues/41462) — 2 comments · 1 reactions · open
- **Issue** [Cilium is not starting on the new EKS nodes after upgrade 1.16.7 -> 1.19.4](https://github.com/cilium/cilium/issues/46608) — 3 comments · 7 reactions · open
- **Pull Request** [ipam: Accept native routing CIDR overlapping a secondary VPC CIDR](https://github.com/cilium/cilium/pull/47874) — 7 comments · 1 reactions · closed
- **Pull Request** [L7 conformance CI fixes](https://github.com/cilium/cilium/pull/47517) — 24 comments · 2 reactions · open
- **Pull Request** [policy: Fix data race on the map state identity index](https://github.com/cilium/cilium/pull/48098) — 2 comments · 1 reactions · open
- **Pull Request** [Proposing Flow IR implementation to improve hubble performance](https://github.com/cilium/cilium/pull/46896) — 20 comments · 2 reactions · open
- **Pull Request** [fix: Print port numbers correctly for map cilium_lb*_reverse_sk](https://github.com/cilium/cilium/pull/47134) — 20 comments · 2 reactions · open
- **Pull Request** [ciliumidentity: include named-port labels in operator-managed identities](https://github.com/cilium/cilium/pull/48033) — 0 comments · 1 reactions · open
- **Pull Request** [\[envoy\] Add HTTP CONNECT support](https://github.com/cilium/cilium/pull/45051) — 15 comments · 3 reactions · closed
- **Pull Request** [bpf: Enable extended masquerade port range for BPF masquerade](https://github.com/cilium/cilium/pull/47301) — 18 comments · 2 reactions · open
- **Pull Request** [Gateway-api: add support for session persistence](https://github.com/cilium/cilium/pull/48029) — 16 comments · 2 reactions · open
- **Pull Request** [mac: Make `mac.MAC` a `\[6\]byte`](https://github.com/cilium/cilium/pull/48089) — 3 comments · 5 reactions · open
- **Pull Request** [k8s/testutils: Validate CRDs on k8s/add and k8s/update by default](https://github.com/cilium/cilium/pull/47469) — 12 comments · 2 reactions · open
- **Issue** [Kernel v7.2: FnSetRetval/CGroupSock call bpf_set_retval#187: R1 is not a scalar](https://github.com/cilium/cilium/issues/48016) — 6 comments · 1 reactions · open
- **Pull Request** [datapath/l2responder: use l3 socket for v6 solicited node responder](https://github.com/cilium/cilium/pull/46332) — 11 comments · 2 reactions · closed
- **Pull Request** [gateway-api: Reduce duplication + more test coverage](https://github.com/cilium/cilium/pull/46474) — 11 comments · 2 reactions · open
- **Pull Request** [BPF: Refactor nat tests to use scapy fixtures and add checksum coverage](https://github.com/cilium/cilium/pull/47222) — 11 comments · 2 reactions · closed
- **Pull Request** [linux/node: deallocate all IDs for deleted nodes](https://github.com/cilium/cilium/pull/47567) — 7 comments · 3 reactions · open
- **Issue** [Persistent traffic drops after 1.18.10 → 1.19.5 upgrade - warning log "Skipping named port" for all named-port ingress rules](https://github.com/cilium/cilium/issues/48110) — 0 comments · 2 reactions · open
- **Pull Request** [Policy & friends: Use labels.Labels rather than labels.LabelArray](https://github.com/cilium/cilium/pull/46231) — 4 comments · 4 reactions · open
- **Pull Request** [feat(bgp): support BGP unnumbered peering (RFC 5549 / ENHE)](https://github.com/cilium/cilium/pull/47394) — 9 comments · 2 reactions · open
- **Pull Request** [envoy: Clarify legacy UpdateEnvoyResources](https://github.com/cilium/cilium/pull/48066) — 4 comments · 3 reactions · open
- **Pull Request** [hubble: Observe node table for peer updates](https://github.com/cilium/cilium/pull/48076) — 8 comments · 2 reactions · closed
- **Pull Request** [Add zone locality info to envoy endpoints if service EndPointSlices have zone information.](https://github.com/cilium/cilium/pull/47335) — 6 comments · 2 reactions · open
- **Pull Request** [ci: replace unsupported LLVM installation action](https://github.com/cilium/cilium/pull/47776) — 7 comments · 2 reactions · open
- **Pull Request** [neighbordiscovery: Observe node table for neighbor discovery](https://github.com/cilium/cilium/pull/48080) — 6 comments · 2 reactions · closed
- **Issue** [\[renovate\] "update all go dependencies main (main)" encountered an error](https://github.com/cilium/cilium/issues/47377) — 5 comments · 0 reactions · closed
- **Issue** [There is no way to enable envoy-metrics service monitor for embedded envoy](https://github.com/cilium/cilium/issues/47825) — 4 comments · 0 reactions · open

### [Envoy](https://github.com/envoyproxy/envoy)

- **Pull Request** [oauth2: chunk large token cookies](https://github.com/envoyproxy/envoy/pull/43135) — 34 comments · 5 reactions · open
- **Pull Request** [dns: add support for clusters based on SRV DNS record](https://github.com/envoyproxy/envoy/pull/35160) — 32 comments · 1 reactions · open
- **Pull Request** [Ext authz caching](https://github.com/envoyproxy/envoy/pull/44874) — 32 comments · 0 reactions · open
- **Pull Request** [network: fix stream leak when a user-space peer fully closes under half-close](https://github.com/envoyproxy/envoy/pull/45198) — 23 comments · 2 reactions · open
- **Pull Request** [Queue policy extension](https://github.com/envoyproxy/envoy/pull/43355) — 21 comments · 0 reactions · closed
- **Pull Request** [hot restart: propagate programmatic stat tags across restart](https://github.com/envoyproxy/envoy/pull/45674) — 17 comments · 0 reactions · open
- **Pull Request** [upstream: add per-worker subset load balancer](https://github.com/envoyproxy/envoy/pull/45979) — 16 comments · 0 reactions · open
- **Issue** [ext_proc FULL_DUPLEX_STREAMED: duplicate RequestBody chunk with EndOfStream=true on large bodies (1.35+)](https://github.com/envoyproxy/envoy/issues/46237) — 7 comments · 0 reactions · open
- **Pull Request** [fix: duplicate request body when when using FULL_DUPLEX_STREAMED ext_proc body mode with retries enabled](https://github.com/envoyproxy/envoy/pull/46095) — 14 comments · 0 reactions · open
- **Pull Request** [QUIC eBPF hot restart part 0](https://github.com/envoyproxy/envoy/pull/45504) — 12 comments · 0 reactions · open
- **Issue** [oauth2: add RequestId (x-request-id) tag to OAuth2 filter application logs for correlation with access logs](https://github.com/envoyproxy/envoy/issues/46164) — 2 comments · 0 reactions · closed
- **Pull Request** [Optional tls_params in certificate to override TLS params in context](https://github.com/envoyproxy/envoy/pull/45680) — 10 comments · 0 reactions · open
- **Pull Request** [http: add support for the QUERY method (RFC 10008)](https://github.com/envoyproxy/envoy/pull/46496) — 6 comments · 1 reactions · open
- **Issue** [grpc access log: add negotiated TLS group ID to TLSProperties](https://github.com/envoyproxy/envoy/issues/46736) — 1 comments · 0 reactions · open
- **Pull Request** [geoip: support additional maxmind database fields](https://github.com/envoyproxy/envoy/pull/46074) — 8 comments · 0 reactions · open
- **Pull Request** [jwt_authn: sanitize payload and claim headers filter-wide](https://github.com/envoyproxy/envoy/pull/46586) — 9 comments · 0 reactions · open
- **Pull Request** [upstream: skip empty locality groups in LRS reporting](https://github.com/envoyproxy/envoy/pull/45992) — 7 comments · 0 reactions · open
- **Pull Request** [tls: allow multiple TLS certificates in the upstream when using a custom TLS certificate selector](https://github.com/envoyproxy/envoy/pull/46479) — 6 comments · 0 reactions · open
- **Pull Request** [udp_proxy: support formatter extensions in tunneling config headers](https://github.com/envoyproxy/envoy/pull/46509) — 7 comments · 0 reactions · open
- **Pull Request** [router: support building an SRDS scope key from filter state](https://github.com/envoyproxy/envoy/pull/46526) — 7 comments · 0 reactions · open
- **Pull Request** [network: send zero-length UDP datagrams](https://github.com/envoyproxy/envoy/pull/46613) — 6 comments · 0 reactions · open
- **Pull Request** [load_aware_locality: add out-of-band ORCA reporting](https://github.com/envoyproxy/envoy/pull/46670) — 7 comments · 0 reactions · open
- **Pull Request** [transport_socket(http_11_proxy): add Proxy-Authorization header support](https://github.com/envoyproxy/envoy/pull/46675) — 7 comments · 0 reactions · open
- **Pull Request** [Prep for cross platform support for dynamic modules](https://github.com/envoyproxy/envoy/pull/46763) — 6 comments · 0 reactions · open
- **Pull Request** [http: fix filter manager dropping a body frame on continue](https://github.com/envoyproxy/envoy/pull/46842) — 2 comments · 1 reactions · open
- **Issue** [dynamic_modules: add configurable shared stats scopes and cardinality limits](https://github.com/envoyproxy/envoy/issues/46425) — 1 comments · 0 reactions · open
- **Issue** [dynamic modules: add xDS config validator support](https://github.com/envoyproxy/envoy/issues/46470) — 0 comments · 0 reactions · open
- **Issue** [health check: use the ALPN-negotiated protocol for HTTP health checks](https://github.com/envoyproxy/envoy/issues/46848) — 1 comments · 0 reactions · open
- **Issue** [Newer release available `com_google_protobuf`: v36.0 (current: v35.1)](https://github.com/envoyproxy/envoy/issues/46849) — 0 comments · 0 reactions · open
- **Issue** [Newer release available `rules_pkg`: 1.3 (current: 1.2.0)](https://github.com/envoyproxy/envoy/issues/46850) — 0 comments · 0 reactions · open

### [Temporal](https://github.com/temporalio/temporal)

- **Issue** [DeleteWorkerDeploymentVersion fails permanently when a version summary outlives its version workflow](https://github.com/temporalio/temporal/issues/11539) — 5 comments · 0 reactions · closed
- **Pull Request** [Preserve the original workflow start time on RebuildMutableState](https://github.com/temporalio/temporal/pull/11668) — 2 comments · 1 reactions · open
- **Issue** [PostgreSQL history pagination rescans rows before composite cursors](https://github.com/temporalio/temporal/issues/11709) — 0 comments · 0 reactions · open
- **Issue** [SQL persistence rewrites unchanged current execution rows](https://github.com/temporalio/temporal/issues/11710) — 0 comments · 0 reactions · open
- **Issue** [SQL workflow mutations lock executions before an equivalent conditional update](https://github.com/temporalio/temporal/issues/11711) — 0 comments · 0 reactions · open
- **Issue** [Provide the temporal development cli in the release archive](https://github.com/temporalio/temporal/issues/11718) — 0 comments · 0 reactions · open
- **Issue** [\[Bug\] MaximumAttempts can't be set to 0 when history.defaultActivityRetryPolicy is set to an other value on temporal server](https://github.com/temporalio/temporal/issues/11721) — 1 comments · 0 reactions · open
- **Pull Request** [Fix invoker action limit across phases](https://github.com/temporalio/temporal/pull/11630) — 0 comments · 1 reactions · open
- **Pull Request** [Configurable limit on activity info failure size](https://github.com/temporalio/temporal/pull/11644) — 0 comments · 1 reactions · open
- **Pull Request** [Annotate worker task spans](https://github.com/temporalio/temporal/pull/10739) — 2 comments · 0 reactions · open
- **Pull Request** [Add helpers for testing exported spans](https://github.com/temporalio/temporal/pull/11655) — 2 comments · 0 reactions · closed
- **Pull Request** [Support MySQL multi-host and SRV connections](https://github.com/temporalio/temporal/pull/11659) — 2 comments · 0 reactions · open
- **Pull Request** [Tag Nexus completion request logs](https://github.com/temporalio/temporal/pull/11684) — 2 comments · 0 reactions · closed
- **Pull Request** [changes for returning previous transaction ID to OSS](https://github.com/temporalio/temporal/pull/11694) — 2 comments · 0 reactions · closed
- **Pull Request** [Add context-aware channel test helpers](https://github.com/temporalio/temporal/pull/11700) — 2 comments · 0 reactions · open
- **Pull Request** [Fix ListQueues: iterator leak, unbounded CQL round-trips, and PageState after Close](https://github.com/temporalio/temporal/pull/9523) — 6 comments · 0 reactions · open
- **Pull Request** [Add replication stream lane wire protocol and receiver-side lane routing](https://github.com/temporalio/temporal/pull/11303) — 0 comments · 0 reactions · open
- **Pull Request** [Add Worker Deployment and BuildID labels to (workflow,activity) task completion metrics](https://github.com/temporalio/temporal/pull/11348) — 1 comments · 0 reactions · open
- **Pull Request** [Add version to deletion workflow replication task](https://github.com/temporalio/temporal/pull/11411) — 0 comments · 0 reactions · open
- **Pull Request** [NEXUS-504: Refactor Nexus frontend interceptors](https://github.com/temporalio/temporal/pull/11464) — 0 comments · 0 reactions · open
- **Pull Request** [Gradual connect shedding tasks](https://github.com/temporalio/temporal/pull/11492) — 0 comments · 0 reactions · open
- **Pull Request** [admin-batch-1: run admin batch in temporal-system](https://github.com/temporalio/temporal/pull/11509) — 0 comments · 0 reactions · open
- **Pull Request** [Add completion callbacks to SANOs](https://github.com/temporalio/temporal/pull/11567) — 1 comments · 0 reactions · open
- **Pull Request** [Refactor NamespaceRateLimitInterceptor with functions to consume N tokens](https://github.com/temporalio/temporal/pull/11582) — 0 comments · 0 reactions · closed
- **Pull Request** [Reuse test context for namespace setup](https://github.com/temporalio/temporal/pull/11623) — 1 comments · 0 reactions · open
- **Pull Request** [Tag HSM outbound Nexus call failure logs](https://github.com/temporalio/temporal/pull/11662) — 1 comments · 0 reactions · open
- **Pull Request** [Replace errors.As with errors.AsType](https://github.com/temporalio/temporal/pull/11674) — 1 comments · 0 reactions · open
- **Pull Request** [Use slices.Backward for reverse iteration](https://github.com/temporalio/temporal/pull/11676) — 1 comments · 0 reactions · closed
- **Pull Request** [Use integer range loops](https://github.com/temporalio/temporal/pull/11677) — 1 comments · 0 reactions · open
- **Pull Request** [Make UnprocessableTaskError pointer-only](https://github.com/temporalio/temporal/pull/11678) — 1 comments · 0 reactions · closed

### [containerd](https://github.com/containerd/containerd)

- **Issue** [btrfs snapshotter: stats collection walks 1.5M inodes per pass on an idle node](https://github.com/containerd/containerd/issues/13967) — 1 comments · 2 reactions · open
- **Issue** [Failed to restore from checkpoint when imageRef not complete](https://github.com/containerd/containerd/issues/12876) — 14 comments · 0 reactions · closed
- **Pull Request** [pkg/oci: resolve rootfs symlinks for user lookup](https://github.com/containerd/containerd/pull/13818) — 7 comments · 2 reactions · closed
- **Issue** [\[SIG-Node\]: KEP-5823: Pod-Level Checkpoint/Restore](https://github.com/containerd/containerd/issues/13979) — 3 comments · 0 reactions · open
- **Pull Request** [internal/cri/server/events: use testing/synctest](https://github.com/containerd/containerd/pull/13997) — 4 comments · 0 reactions · closed
- **Pull Request** [Shim mount handler protocol](https://github.com/containerd/containerd/pull/14002) — 2 comments · 0 reactions · open
- **Pull Request** [vendor: github.com/sirupsen/logrus v1.10.1](https://github.com/containerd/containerd/pull/13294) — 1 comments · 0 reactions · closed
- **Pull Request** [build(deps): bump github.com/prometheus/client_golang from 1.24.0 to 1.24.1](https://github.com/containerd/containerd/pull/13883) — 0 comments · 0 reactions · open
- **Pull Request** [contrib/apparmor: allow signals/ptrace for stacked-label exec processes](https://github.com/containerd/containerd/pull/13905) — 1 comments · 0 reactions · open
- **Pull Request** [build(deps): bump the codeql-actions group across 1 directory with 3 updates](https://github.com/containerd/containerd/pull/13963) — 0 comments · 0 reactions · open
- **Pull Request** [build(deps): bump azure/login from 3.0.0 to 3.0.1](https://github.com/containerd/containerd/pull/13964) — 0 comments · 0 reactions · open
- **Pull Request** [build(deps): bump actions/attest-build-provenance from 4.1.1 to 4.2.2](https://github.com/containerd/containerd/pull/13965) — 0 comments · 0 reactions · closed
- **Pull Request** [core/unpack: fetch layers of every config-sharing manifest](https://github.com/containerd/containerd/pull/13966) — 0 comments · 0 reactions · open
- **Pull Request** [Update mount manager schema](https://github.com/containerd/containerd/pull/13975) — 0 comments · 0 reactions · open
- **Pull Request** [Add AGENTS.md guidance for AI coding agents](https://github.com/containerd/containerd/pull/13980) — 1 comments · 0 reactions · open
- **Pull Request** [cri: truncate the checkpoint archive when it already exists](https://github.com/containerd/containerd/pull/13988) — 0 comments · 0 reactions · open
- **Pull Request** [\[release/2.3\] update runhcs to v0.15.0-rc.4](https://github.com/containerd/containerd/pull/13990) — 1 comments · 0 reactions · closed
- **Pull Request** [Remove shim.Command form pkg](https://github.com/containerd/containerd/pull/13991) — 0 comments · 0 reactions · open
- **Pull Request** [fix: fix incorrect restart=always restart logic](https://github.com/containerd/containerd/pull/13993) — 0 comments · 0 reactions · open
- **Pull Request** [\[release/2.2\] pkg/oci: resolve rootfs symlinks for user lookup](https://github.com/containerd/containerd/pull/13998) — 0 comments · 0 reactions · closed
- **Pull Request** [internal/cri/server: remove remaining uses of k8s.io/utils](https://github.com/containerd/containerd/pull/14003) — 1 comments · 1 reactions · closed
- **Pull Request** [vendor: tags.cncf.io/container-device-interface 05ae4b5bb730](https://github.com/containerd/containerd/pull/14004) — 2 comments · 0 reactions · closed
- **Pull Request** [Add support for ExecRequest.envs environment injection](https://github.com/containerd/containerd/pull/13637) — 1 comments · 0 reactions · open
- **Pull Request** [\[release/2.2\] pkg/oci: resolve rootfs symlinks for user lookup](https://github.com/containerd/containerd/pull/14005) — 0 comments · 0 reactions · open
- **Pull Request** [Bump go-runc to 1.2.0](https://github.com/containerd/containerd/pull/14006) — 0 comments · 0 reactions · open
- **Pull Request** [build(deps): bump the k8s group across 1 directory with 2 updates](https://github.com/containerd/containerd/pull/14007) — 0 comments · 0 reactions · open
- **Pull Request** [build(deps): bump github.com/moby/sys/userns from 0.1.0 to 0.2.0 in the moby-sys group](https://github.com/containerd/containerd/pull/14008) — 0 comments · 0 reactions · open
- **Pull Request** [build(deps): bump github.com/checkpoint-restore/checkpointctl from 1.5.0 to 1.6.0](https://github.com/containerd/containerd/pull/14009) — 0 comments · 0 reactions · open
