# Platform / Networking / Runtime Infrastructure — 2026-08-14

> Factual GitHub evidence collected by Contribution Compass. No LLM analysis is performed.

## Contribution Leads

### [CI: Non-zero (3) restart count of cilium-* (config) must be investigated](https://github.com/cilium/cilium/issues/40492)

- Project: `cilium/cilium`
- Tier: `maintainer-invited`
- Evidence: Maintainer invitation label: help wanted; No assignee is listed
- Caveat: Confirm scope and availability with the maintainers before starting work.

### [Allow worker CPU affinity to be set](https://github.com/envoyproxy/envoy/issues/14619)

- Project: `envoyproxy/envoy`
- Tier: `maintainer-invited`
- Evidence: Maintainer invitation label: help wanted; No assignee is listed
- Caveat: Confirm scope and availability with the maintainers before starting work.

## Important Updates

### [Cilium](https://github.com/cilium/cilium)

- **Pull Request** [feat: implement BPF_MAP_TYPE_SK_STORAGE for IPv4/IPv6 socket revNAT](https://github.com/cilium/cilium/pull/44767) — 26 comments · 2 reactions · open
- **Pull Request** [\[CFP-39876\]: Add connectivity test for non-global namespace isolation](https://github.com/cilium/cilium/pull/46604) — 18 comments · 3 reactions · closed
- **Pull Request** [k8s: migrate from legacy config to ClusterInfo](https://github.com/cilium/cilium/pull/47854) — 15 comments · 2 reactions · open
- **Pull Request** [Documentation: document mesh security model](https://github.com/cilium/cilium/pull/47912) — 3 comments · 5 reactions · closed
- **Pull Request** [loadbalancer: skip Maintenance backends with no hint in topology safeguard scan](https://github.com/cilium/cilium/pull/47961) — 3 comments · 6 reactions · open
- **Pull Request** [network driver: use statedb to manage agent devices](https://github.com/cilium/cilium/pull/47558) — 13 comments · 2 reactions · open
- **Pull Request** [node/manager: Populate node table from manager](https://github.com/cilium/cilium/pull/45953) — 8 comments · 2 reactions · open
- **Pull Request** [avoid identity lookups for server-independent DNS rules](https://github.com/cilium/cilium/pull/46526) — 12 comments · 2 reactions · closed
- **Pull Request** [aws/ipam: retry prefix ENI in eligible sibling subnets before /32 fal…](https://github.com/cilium/cilium/pull/46746) — 8 comments · 2 reactions · open
- **Pull Request** [network driver: add sriov device manager](https://github.com/cilium/cilium/pull/47387) — 13 comments · 2 reactions · open
- **Pull Request** [standalone-dns-proxy: return an error when no endpoint is found](https://github.com/cilium/cilium/pull/47791) — 8 comments · 2 reactions · closed
- **Pull Request** [ces: fix shutdown deadlock](https://github.com/cilium/cilium/pull/47802) — 9 comments · 2 reactions · closed
- **Issue** [CFP: Cilium for s390x](https://github.com/cilium/cilium/issues/40493) — 10 comments · 0 reactions · open
- **Pull Request** [ci: use GitHub App client ID in v1.20 image workflow](https://github.com/cilium/cilium/pull/47787) — 6 comments · 2 reactions · open
- **Pull Request** [bpf: nat: extract inner IPv6 header from ICMP payload in-place](https://github.com/cilium/cilium/pull/47917) — 6 comments · 2 reactions · closed
- **Issue** [CI: Non-zero (3) restart count of cilium-* (config) must be investigated](https://github.com/cilium/cilium/issues/40492) — 9 comments · 0 reactions · open
- **Issue** [Potential issue with usePrimaryAddress on a t3.small](https://github.com/cilium/cilium/issues/47930) — 5 comments · 0 reactions · open
- **Pull Request** [BPF Runtime Stats CLI](https://github.com/cilium/cilium/pull/47186) — 5 comments · 2 reactions · closed
- **Pull Request** [BPF: Refactor nat tests to use scapy fixtures and add checksum coverage](https://github.com/cilium/cilium/pull/47222) — 9 comments · 2 reactions · open
- **Pull Request** [Add zone locality info to envoy endpoints if service EndPointSlices have zone information.](https://github.com/cilium/cilium/pull/47335) — 4 comments · 2 reactions · open
- **Pull Request** [test(bpf): parallelize eBPF test compilation](https://github.com/cilium/cilium/pull/47426) — 5 comments · 2 reactions · closed
- **Pull Request** [gateway-api: filter CEC controls from infrastructure metadata](https://github.com/cilium/cilium/pull/47732) — 5 comments · 2 reactions · closed
- **Pull Request** [gateway-api: log the right route kind when listing TLSRoutes fails](https://github.com/cilium/cilium/pull/47826) — 4 comments · 2 reactions · closed
- **Pull Request** [operator: prevent CNPs with nodeSelector from silently enforcing nothing](https://github.com/cilium/cilium/pull/47882) — 5 comments · 2 reactions · open
- **Pull Request** [clustermesh/endpointslices: explicitly limit maximum decoder memory](https://github.com/cilium/cilium/pull/47932) — 4 comments · 2 reactions · closed
- **Pull Request** [fix(deps): update all go dependencies main](https://github.com/cilium/cilium/pull/47937) — 4 comments · 2 reactions · closed
- **Pull Request** [clustermesh: transition service exports to observer](https://github.com/cilium/cilium/pull/47955) — 5 comments · 2 reactions · open
- **Issue** [Dependency Dashboard](https://github.com/cilium/cilium/issues/33550) — 2 comments · 0 reactions · open
- **Issue** [Host datapath BPF programs leak on every device change, exhausting kernel executable memory](https://github.com/cilium/cilium/issues/47730) — 3 comments · 0 reactions · open
- **Pull Request** [operator/endpointslice: Fix races on slim controller](https://github.com/cilium/cilium/pull/47228) — 7 comments · 2 reactions · closed

### [Envoy](https://github.com/envoyproxy/envoy)

- **Pull Request** [Queue policy extension](https://github.com/envoyproxy/envoy/pull/43355) — 19 comments · 0 reactions · open
- **Issue** [UDP proxy for upstream health monitoring](https://github.com/envoyproxy/envoy/issues/37824) — 10 comments · 0 reactions · open
- **Pull Request** [add ratelimit descriptor extension to use jwt claims as descriptors](https://github.com/envoyproxy/envoy/pull/46138) — 11 comments · 1 reactions · open
- **Issue** [Allow worker CPU affinity to be set](https://github.com/envoyproxy/envoy/issues/14619) — 8 comments · 0 reactions · open
- **Issue** [envoy_api in Bazel Registry outdated causing builds/validations to fail](https://github.com/envoyproxy/envoy/issues/44696) — 8 comments · 0 reactions · closed
- **Issue** [Newer release available `rules_shell`: v0.9.0 (current: v0.8.0)](https://github.com/envoyproxy/envoy/issues/46681) — 0 comments · 0 reactions · closed
- **Issue** [Summary lost during main publish](https://github.com/envoyproxy/envoy/issues/46147) — 2 comments · 0 reactions · open
- **Issue** [PLACEHOLDER still problematic on main (at least) for branch dev/reopen](https://github.com/envoyproxy/envoy/issues/46149) — 3 comments · 0 reactions · open
- **Issue** [Migrate darwin config_settings to constraint_values for --platforms compatibility](https://github.com/envoyproxy/envoy/issues/46572) — 3 comments · 0 reactions · closed
- **Pull Request** [ratelimit: add Retry-After header support](https://github.com/envoyproxy/envoy/pull/46289) — 10 comments · 0 reactions · open
- **Pull Request** [adaptive concurrency: add min concurrency limit knob](https://github.com/envoyproxy/envoy/pull/46602) — 6 comments · 0 reactions · closed
- **Issue** [Newer release available `dev_cel`: v0.25.2 (current: v0.25.1)](https://github.com/envoyproxy/envoy/issues/45283) — 1 comments · 0 reactions · closed
- **Issue** [Newer release available `cel_cpp`: v0.16.0 (current: v0.14.0)](https://github.com/envoyproxy/envoy/issues/46498) — 1 comments · 0 reactions · closed
- **Issue** [HTTP3/QUIC listeners do not support 384-bit EC certificates](https://github.com/envoyproxy/envoy/issues/46694) — 0 comments · 0 reactions · open
- **Issue** [Newer release available `cel_cpp`: v0.16.1 (current: v0.14.0)](https://github.com/envoyproxy/envoy/issues/46695) — 0 comments · 0 reactions · open
- **Issue** [Newer release available `cel_spec`: v0.25.3 (current: v0.25.2)](https://github.com/envoyproxy/envoy/issues/46696) — 0 comments · 0 reactions · open
- **Issue** [Newer release available `dev_cel`: v0.25.3 (current: v0.25.1)](https://github.com/envoyproxy/envoy/issues/46697) — 0 comments · 0 reactions · open
- **Issue** [Newer release available `rules_python`: 2.3.0 (current: 2.2.0)](https://github.com/envoyproxy/envoy/issues/46698) — 0 comments · 0 reactions · open
- **Issue** [http: propose exact request-target rewrite early-header-mutation extension](https://github.com/envoyproxy/envoy/issues/46700) — 0 comments · 0 reactions · open
- **Pull Request** [metadata: supported to access specific item of ListValue by the MetadataKey](https://github.com/envoyproxy/envoy/pull/45948) — 8 comments · 0 reactions · open
- **Pull Request** [mcp_router: add optional HMAC-SHA256 integrity for session IDs](https://github.com/envoyproxy/envoy/pull/46581) — 5 comments · 0 reactions · open
- **Pull Request** [formatter: add formatValueTo to reduce allocation of protobuf value](https://github.com/envoyproxy/envoy/pull/46607) — 4 comments · 0 reactions · closed
- **Pull Request** [Order dependent bug](https://github.com/envoyproxy/envoy/pull/46673) — 5 comments · 0 reactions · open
- **Pull Request** [xDS: change ext_proc drain process to work directionally](https://github.com/envoyproxy/envoy/pull/45901) — 6 comments · 0 reactions · open
- **Pull Request** [bazel: support platform-based Darwin architecture selection](https://github.com/envoyproxy/envoy/pull/46637) — 2 comments · 0 reactions · closed
- **Pull Request** [c-ares: move dns shared resolver logic to upstream cluster](https://github.com/envoyproxy/envoy/pull/46657) — 2 comments · 0 reactions · open
- **Pull Request** [cleanup: replace erase-remove idiom with std::erase_if or absl::erase_if](https://github.com/envoyproxy/envoy/pull/46663) — 2 comments · 0 reactions · closed
- **Pull Request** [transport_socket(http_11_proxy): add Proxy-Authorization header support](https://github.com/envoyproxy/envoy/pull/46675) — 3 comments · 0 reactions · open
- **Pull Request** [Ensure upstream hosts have rebalanced utilization](https://github.com/envoyproxy/envoy/pull/46683) — 2 comments · 0 reactions · open
- **Pull Request** [rds: clean up unnecessary publish status](https://github.com/envoyproxy/envoy/pull/46596) — 1 comments · 0 reactions · open

### [Temporal](https://github.com/temporalio/temporal)

- **Issue** [Nexus: server may send malformed `request-timeout` header (negative values and units outside the Nexus grammar)](https://github.com/temporalio/temporal/issues/11569) — 1 comments · 0 reactions · open
- **Issue** [Persistence rate-limit ResourceExhausted is flattened to Unavailable in ProcessOutgoingSearchAttributes](https://github.com/temporalio/temporal/issues/11571) — 0 comments · 0 reactions · open
- **Pull Request** [Trim the Claude review comments](https://github.com/temporalio/temporal/pull/11553) — 5 comments · 0 reactions · closed
- **Pull Request** [Recognize the new `commonpb` Worker callback variant](https://github.com/temporalio/temporal/pull/11380) — 2 comments · 0 reactions · open
- **Pull Request** [Populate CallbackInfo.outcome](https://github.com/temporalio/temporal/pull/11520) — 2 comments · 0 reactions · open
- **Pull Request** [Release removed shared cluster test references](https://github.com/temporalio/temporal/pull/11542) — 2 comments · 0 reactions · closed
- **Pull Request** [Add data race summary to CI report](https://github.com/temporalio/temporal/pull/11211) — 0 comments · 0 reactions · open
- **Pull Request** [Add replication stream lane wire protocol and receiver-side lane routing](https://github.com/temporalio/temporal/pull/11303) — 0 comments · 0 reactions · open
- **Pull Request** [Preserve logger tags across Skip()](https://github.com/temporalio/temporal/pull/11355) — 0 comments · 0 reactions · open
- **Pull Request** [Fix constant/error-dependent retry jitter being truncated to a no-op](https://github.com/temporalio/temporal/pull/11397) — 0 comments · 0 reactions · open
- **Pull Request** [Skip unbuildable replication tasks on stream sender instead of blocking](https://github.com/temporalio/temporal/pull/11422) — 0 comments · 0 reactions · closed
- **Pull Request** [fix: \[Scheduler\] V1->V2 migration-eligibility fix and migrated-start ID](https://github.com/temporalio/temporal/pull/11462) — 0 comments · 0 reactions · open
- **Pull Request** [Skip worker commands task queues in missing TQ check](https://github.com/temporalio/temporal/pull/11481) — 0 comments · 0 reactions · open
- **Pull Request** [Enable Claude reviews for OSS Matching](https://github.com/temporalio/temporal/pull/11500) — 0 comments · 0 reactions · closed
- **Pull Request** [Fix sticky queue stats zeroed out](https://github.com/temporalio/temporal/pull/11527) — 0 comments · 0 reactions · open
- **Pull Request** [Update Selected API list.](https://github.com/temporalio/temporal/pull/11535) — 0 comments · 0 reactions · closed
- **Pull Request** [Validate fairsim inputs and preserve counter defaults](https://github.com/temporalio/temporal/pull/11536) — 1 comments · 0 reactions · open
- **Pull Request** [Release gRPC resolver registrations on shutdown](https://github.com/temporalio/temporal/pull/11543) — 0 comments · 0 reactions · open
- **Pull Request** [fix time-skipping flaky tests](https://github.com/temporalio/temporal/pull/11548) — 0 comments · 0 reactions · closed
- **Pull Request** [Release OTEL logger registrations on shutdown](https://github.com/temporalio/temporal/pull/11551) — 0 comments · 0 reactions · open
- **Pull Request** [Limit flakereport size](https://github.com/temporalio/temporal/pull/11552) — 1 comments · 0 reactions · open
- **Pull Request** [Only count reader reads that left tasks behind as stuck attempts](https://github.com/temporalio/temporal/pull/11554) — 0 comments · 0 reactions · open
- **Pull Request** [Add OpenTelemetry HTTP instrumentation](https://github.com/temporalio/temporal/pull/11558) — 1 comments · 0 reactions · open
- **Pull Request** [Trace outbound Nexus HTTP requests](https://github.com/temporalio/temporal/pull/11559) — 0 comments · 0 reactions · open
- **Pull Request** [\[Visibility\]\[Elasticsearch\] Change datetime format to always include nanos component](https://github.com/temporalio/temporal/pull/11564) — 0 comments · 0 reactions · open
- **Pull Request** [Make supported callback kinds configurable](https://github.com/temporalio/temporal/pull/11566) — 1 comments · 0 reactions · open
- **Pull Request** [Add completion callbacks to SANOs](https://github.com/temporalio/temporal/pull/11567) — 0 comments · 0 reactions · open
- **Pull Request** [Fix 9436 describe task queue stats](https://github.com/temporalio/temporal/pull/9521) — 2 comments · 0 reactions · open
- **Pull Request** [Ownership linter \[wip\]](https://github.com/temporalio/temporal/pull/10734) — 0 comments · 0 reactions · open
- **Pull Request** [Split Versioning3 query tests](https://github.com/temporalio/temporal/pull/11472) — 0 comments · 0 reactions · open

### [containerd](https://github.com/containerd/containerd)

- **Issue** [Empty cache files causes "KillPodSandbox" errors when deleting pods](https://github.com/containerd/containerd/issues/8197) — 17 comments · 11 reactions · open
- **Pull Request** [cri: enable mount manager for image mounts](https://github.com/containerd/containerd/pull/13542) — 12 comments · 1 reactions · open
- **Pull Request** [metadata: bound snapshotter Remove during garbage collection](https://github.com/containerd/containerd/pull/13799) — 4 comments · 0 reactions · open
- **Pull Request** [pkg/shim: Report bootstrap API mismatch on startup](https://github.com/containerd/containerd/pull/13910) — 0 comments · 0 reactions · open
- **Pull Request** [fix(cri): CRI image pull is sometimes canceled by image_pull_progress…](https://github.com/containerd/containerd/pull/13924) — 0 comments · 0 reactions · open
- **Pull Request** [Export config in CRI plugin](https://github.com/containerd/containerd/pull/13940) — 0 comments · 0 reactions · open
- **Pull Request** [ci: add lima image list for fedora images](https://github.com/containerd/containerd/pull/13955) — 1 comments · 0 reactions · open
- **Pull Request** [runtime: invoke Shutdown after every task deletion](https://github.com/containerd/containerd/pull/13958) — 1 comments · 0 reactions · open
- **Pull Request** [apparmor: add signal and ptrace rules for stacked profiles](https://github.com/containerd/containerd/pull/12887) — 3 comments · 0 reactions · open
- **Pull Request** [Use toolchain directive to declare preferred Go version](https://github.com/containerd/containerd/pull/13657) — 3 comments · 0 reactions · open
- **Pull Request** [contrib/apparmor: allow signals/ptrace for stacked-label exec processes](https://github.com/containerd/containerd/pull/13905) — 1 comments · 0 reactions · open
- **Pull Request** [cri: trace image pull result attributes](https://github.com/containerd/containerd/pull/13959) — 1 comments · 0 reactions · open
- **Pull Request** [nri(wip): record resolved image name and digest in container metadata](https://github.com/containerd/containerd/pull/13960) — 0 comments · 0 reactions · open
