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

- **Pull Request** [datapath/linux: return orphaned node ID to pool on partial remap](https://github.com/cilium/cilium/pull/47568) — 21 comments · 2 reactions · closed
- **Pull Request** [Documentation: document mesh security model](https://github.com/cilium/cilium/pull/47912) — 1 comments · 5 reactions · open
- **Issue** [CI: firewall-egress-to-fqdns fails 6% of the time: command terminated with exit code 28](https://github.com/cilium/cilium/issues/47921) — 9 comments · 0 reactions · open
- **Pull Request** [node/manager: Populate node table from manager](https://github.com/cilium/cilium/pull/45953) — 8 comments · 2 reactions · open
- **Pull Request** [operator/ipam: recover nodes dropped from the instance cache during resync](https://github.com/cilium/cilium/pull/46839) — 9 comments · 2 reactions · closed
- **Pull Request** [egressgateway: react to local device/address changes](https://github.com/cilium/cilium/pull/47763) — 7 comments · 2 reactions · open
- **Issue** [Label Filters don't treat prefix as a regex when loaded from file](https://github.com/cilium/cilium/issues/47918) — 4 comments · 0 reactions · open
- **Pull Request** [feat(bgp): support BGP unnumbered peering (RFC 5549 / ENHE)](https://github.com/cilium/cilium/pull/47394) — 8 comments · 2 reactions · open
- **Pull Request** [ci: replace unsupported LLVM installation action](https://github.com/cilium/cilium/pull/47776) — 4 comments · 2 reactions · open
- **Pull Request** [gateway-api: log the right route kind when listing TLSRoutes fails](https://github.com/cilium/cilium/pull/47826) — 4 comments · 2 reactions · closed
- **Pull Request** [operator: prevent CNPs with nodeSelector from silently enforcing nothing](https://github.com/cilium/cilium/pull/47882) — 4 comments · 2 reactions · open
- **Pull Request** [golangci-lint: Forbid stdlib `net.Interface*` functions](https://github.com/cilium/cilium/pull/47902) — 1 comments · 3 reactions · open
- **Pull Request** [images: update cilium-envoy](https://github.com/cilium/cilium/pull/47895) — 3 comments · 3 reactions · open
- **Pull Request** [cilium-cli: Skip HostToWorld if no external IPv6](https://github.com/cilium/cilium/pull/47931) — 2 comments · 2 reactions · closed
- **Pull Request** [clustermesh/endpointslices: explicitly limit maximum decoder memory](https://github.com/cilium/cilium/pull/47932) — 2 comments · 2 reactions · open
- **Pull Request** [fix(deps): update all go dependencies main](https://github.com/cilium/cilium/pull/47937) — 2 comments · 2 reactions · open
- **Issue** [Operator/IPAM: recover nodes dropped from the instance cache by the full ENI resync](https://github.com/cilium/cilium/issues/46513) — 1 comments · 0 reactions · closed
- **Issue** [Potential issue with usePrimaryAddress on a t3.small](https://github.com/cilium/cilium/issues/47930) — 1 comments · 0 reactions · open
- **Pull Request** [ipam: Added ReservedRange To CiliumPodIPPool](https://github.com/cilium/cilium/pull/46880) — 5 comments · 2 reactions · open
- **Pull Request** [docs: add OpenChoreo to USERS.md](https://github.com/cilium/cilium/pull/47924) — 4 comments · 1 reactions · open
- **Pull Request** [bpf: preserve original source in NodePort tunnel traces](https://github.com/cilium/cilium/pull/47936) — 0 comments · 2 reactions · open
- **Pull Request** [Fix 5-tuple collision in conformance kind proxy embedded](https://github.com/cilium/cilium/pull/47277) — 3 comments · 2 reactions · open
- **Pull Request** [cilium-cli/connectivity: detect Cilium version in connectivity perf setup](https://github.com/cilium/cilium/pull/47927) — 2 comments · 1 reactions · open
- **Pull Request** [operator/ipam: Remove the per-node pool-maintainer retry trigger](https://github.com/cilium/cilium/pull/47939) — 2 comments · 2 reactions · open
- **Issue** [Gateway API: Envoy upstream replies from same-node backends lost (RST), nondeterministic across restarts — k3s/Ubuntu-raspi, not reproducible on kind](https://github.com/cilium/cilium/issues/47940) — 0 comments · 0 reactions · open
- **Issue** [Hubble Relay does not terminate, gRPC health server remains running](https://github.com/cilium/cilium/issues/47941) — 0 comments · 0 reactions · open
- **Pull Request** [fix(gateway): fail closed on invalid ExternalAuth](https://github.com/cilium/cilium/pull/47929) — 0 comments · 1 reactions · open
- **Pull Request** [\[WIP\] Runtime cloud-IPAM routing rules reconciliation](https://github.com/cilium/cilium/pull/47938) — 0 comments · 2 reactions · open
- **Pull Request** [hubble/relay: stop gRPC health server on shutdown](https://github.com/cilium/cilium/pull/47942) — 2 comments · 1 reactions · open
- **Pull Request** [gateway-api: compare static Gateway addresses as parsed IPs](https://github.com/cilium/cilium/pull/47943) — 1 comments · 1 reactions · open

### [Envoy](https://github.com/envoyproxy/envoy)

- **Pull Request** [hot restart: propagate programmatic stat tags across restart](https://github.com/envoyproxy/envoy/pull/45674) — 14 comments · 0 reactions · open
- **Pull Request** [c-ares: make qcache_max_ttl configurable](https://github.com/envoyproxy/envoy/pull/45073) — 15 comments · 0 reactions · closed
- **Pull Request** [composite: fail over to the next sub-cluster when a sub-cluster has no hosts](https://github.com/envoyproxy/envoy/pull/46308) — 9 comments · 0 reactions · open
- **Pull Request** [ext_proc: adding direct mode_override support](https://github.com/envoyproxy/envoy/pull/46318) — 10 comments · 0 reactions · open
- **Pull Request** [Support hot restart handoff for connectionless UDP flows](https://github.com/envoyproxy/envoy/pull/46502) — 7 comments · 0 reactions · open
- **Pull Request** [Disable fmtlib Unicode support on Windows](https://github.com/envoyproxy/envoy/pull/46601) — 5 comments · 0 reactions · open
- **Pull Request** [\[WIP\] bazel: Add compatibility stubs for bzlmod](https://github.com/envoyproxy/envoy/pull/43255) — 3 comments · 0 reactions · open
- **Pull Request** [network: send zero-length UDP datagrams](https://github.com/envoyproxy/envoy/pull/46613) — 2 comments · 0 reactions · open
- **Pull Request** [c-ares: disable shared resolver by default](https://github.com/envoyproxy/envoy/pull/46622) — 6 comments · 0 reactions · closed
- **Pull Request** [Order dependent bug](https://github.com/envoyproxy/envoy/pull/46673) — 2 comments · 0 reactions · open
- **Pull Request** [Allow connection teardown even when cert selection is not yet complete](https://github.com/envoyproxy/envoy/pull/46676) — 2 comments · 0 reactions · open
- **Pull Request** [Restrict local reply streaming integration tests](https://github.com/envoyproxy/envoy/pull/46682) — 2 comments · 0 reactions · open
- **Pull Request** [Ensure upstream hosts have rebalanced utilization](https://github.com/envoyproxy/envoy/pull/46683) — 2 comments · 0 reactions · open
- **Pull Request** [Avoid excessive hashing for well-known header lookups](https://github.com/envoyproxy/envoy/pull/46560) — 1 comments · 0 reactions · open
- **Pull Request** [Rescope Logger::Levels enum so it can be moved to envoy/ directory](https://github.com/envoyproxy/envoy/pull/46668) — 1 comments · 0 reactions · closed
- **Pull Request** [\[draft\] dym: go sdk for udp listener filter](https://github.com/envoyproxy/envoy/pull/46672) — 1 comments · 0 reactions · open
- **Pull Request** [quic: promote HTTP/3 API status from alpha to stable](https://github.com/envoyproxy/envoy/pull/46621) — 3 comments · 0 reactions · closed
- **Pull Request** [Create Snapshot of runtime stats before incrementing counter](https://github.com/envoyproxy/envoy/pull/46685) — 2 comments · 0 reactions · open
- **Pull Request** [coroutine: add ASSIGN_OR_CO_RETURN and CO_RETURN_IF_ERROR macros](https://github.com/envoyproxy/envoy/pull/46684) — 1 comments · 0 reactions · closed

### [Temporal](https://github.com/temporalio/temporal)

- **Issue** [A brief `Unavailable` blip resets History queue backoff, causing a sustained retry storm](https://github.com/temporalio/temporal/issues/11547) — 0 comments · 0 reactions · open
- **Pull Request** [Fix approximateSize undercounting on activity start and heartbeat paths](https://github.com/temporalio/temporal/pull/11486) — 2 comments · 0 reactions · open
- **Pull Request** [Validator generator \[WiP\]](https://github.com/temporalio/temporal/pull/10200) — 0 comments · 0 reactions · open
- **Pull Request** [Downscale test runner size, increase shards](https://github.com/temporalio/temporal/pull/10643) — 1 comments · 0 reactions · closed
- **Pull Request** [Return test runner orchestration outcomes](https://github.com/temporalio/temporal/pull/11033) — 0 comments · 0 reactions · open
- **Pull Request** [\[CHASM\] Support WithRequestID on UpdateComponent](https://github.com/temporalio/temporal/pull/11169) — 0 comments · 0 reactions · open
- **Pull Request** [Add replication stream lane wire protocol and receiver-side lane routing](https://github.com/temporalio/temporal/pull/11303) — 0 comments · 0 reactions · open
- **Pull Request** [Skip unbuildable replication tasks on stream sender instead of blocking](https://github.com/temporalio/temporal/pull/11422) — 0 comments · 0 reactions · open
- **Pull Request** [Standardize Claude review comments](https://github.com/temporalio/temporal/pull/11461) — 1 comments · 0 reactions · closed
- **Pull Request** [Add isolated functional test clusters](https://github.com/temporalio/temporal/pull/11465) — 0 comments · 0 reactions · open
- **Pull Request** [Extract shared JUnit XML handling](https://github.com/temporalio/temporal/pull/11480) — 1 comments · 0 reactions · closed
- **Pull Request** [Record canonical Go test attempt results](https://github.com/temporalio/temporal/pull/11487) — 0 comments · 0 reactions · open
- **Pull Request** [Drive test retries from attempt results](https://github.com/temporalio/temporal/pull/11488) — 0 comments · 0 reactions · open
- **Pull Request** [Track process-lifetime object leak baselines](https://github.com/temporalio/temporal/pull/11505) — 1 comments · 0 reactions · open
- **Pull Request** [Eliminate expected object leak suppressions](https://github.com/temporalio/temporal/pull/11508) — 0 comments · 0 reactions · closed
- **Pull Request** [Use generic JUnit documents at runner boundaries](https://github.com/temporalio/temporal/pull/11512) — 0 comments · 0 reactions · open
- **Pull Request** [Harden shared JUnit report IO](https://github.com/temporalio/temporal/pull/11513) — 0 comments · 0 reactions · open
- **Pull Request** [Render crash reports canonically](https://github.com/temporalio/temporal/pull/11514) — 0 comments · 0 reactions · open
- **Pull Request** [Persist canonical test attempt history](https://github.com/temporalio/temporal/pull/11515) — 0 comments · 0 reactions · open
- **Pull Request** [Remove legacy JUnit report merger](https://github.com/temporalio/temporal/pull/11516) — 0 comments · 0 reactions · open
- **Pull Request** [Simplify test runner attempt state](https://github.com/temporalio/temporal/pull/11517) — 0 comments · 0 reactions · open
- **Pull Request** [Return report persistence errors](https://github.com/temporalio/temporal/pull/11518) — 0 comments · 0 reactions · open
- **Pull Request** [Fix flakereport incomplete JUnit failures](https://github.com/temporalio/temporal/pull/11526) — 0 comments · 0 reactions · closed
- **Pull Request** [Update test shard salt](https://github.com/temporalio/temporal/pull/11533) — 0 comments · 0 reactions · closed
- **Pull Request** [Release removed shared cluster test references](https://github.com/temporalio/temporal/pull/11542) — 2 comments · 0 reactions · open
- **Pull Request** [Attribute queue reader stuck attempts to a slice](https://github.com/temporalio/temporal/pull/11541) — 0 comments · 0 reactions · open
- **Pull Request** [Release process-global lifecycle registrations](https://github.com/temporalio/temporal/pull/11543) — 0 comments · 0 reactions · open
- **Pull Request** [Enforce zero expected object leaks](https://github.com/temporalio/temporal/pull/11544) — 0 comments · 0 reactions · open
- **Pull Request** [fix(batcher): scope deterministic request IDs to the batch job ID](https://github.com/temporalio/temporal/pull/11546) — 1 comments · 0 reactions · open

### [containerd](https://github.com/containerd/containerd)

- **Issue** [Support container checkpoint/restore for gVisor runtime](https://github.com/containerd/containerd/issues/12280) — 7 comments · 1 reactions · open
- **Issue** [Cannot run OPA image in user namespace on GKE](https://github.com/containerd/containerd/issues/13129) — 5 comments · 0 reactions · open
- **Pull Request** [vendor: github.com/sirupsen/logrus v1.10.0](https://github.com/containerd/containerd/pull/13294) — 1 comments · 0 reactions · open
- **Pull Request** [\[release/2.2\] snapshots/erofs: protect snapshot staging from cleanup](https://github.com/containerd/containerd/pull/13950) — 0 comments · 0 reactions · closed
- **Pull Request** [erofs: instrument warm up cache](https://github.com/containerd/containerd/pull/13941) — 0 comments · 0 reactions · open
