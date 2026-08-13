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

- **Issue** [Replace stdlib net.Interface* with vishvananda/netlink to avoid blocked forever goroutines](https://github.com/cilium/cilium/issues/15051) — 10 comments · 5 reactions · closed
- **Pull Request** [Documentation: document mesh security model](https://github.com/cilium/cilium/pull/47912) — 1 comments · 5 reactions · open
- **Pull Request** [golangci-lint: Forbid stdlib `net.Interface*` functions](https://github.com/cilium/cilium/pull/47902) — 1 comments · 4 reactions · closed
- **Pull Request** [BPF Runtime Stats CLI](https://github.com/cilium/cilium/pull/47186) — 5 comments · 2 reactions · open
- **Pull Request** [gateway-api: log the right route kind when listing TLSRoutes fails](https://github.com/cilium/cilium/pull/47826) — 4 comments · 2 reactions · closed
- **Issue** [Dependency Dashboard](https://github.com/cilium/cilium/issues/33550) — 2 comments · 0 reactions · open
- **Issue** [Potential issue with usePrimaryAddress on a t3.small](https://github.com/cilium/cilium/issues/47930) — 3 comments · 0 reactions · open
- **Pull Request** [clustermesh/endpointslices: explicitly limit maximum decoder memory](https://github.com/cilium/cilium/pull/47932) — 2 comments · 2 reactions · closed
- **Pull Request** [operator/ipam: Remove the per-node pool-maintainer retry trigger](https://github.com/cilium/cilium/pull/47939) — 2 comments · 2 reactions · open
- **Pull Request** [contrib: Don't descend into ~/.cache subdirs when chowning in builder.sh](https://github.com/cilium/cilium/pull/45656) — 9 comments · 0 reactions · open
- **Pull Request** [DONOTMERGE : test commit](https://github.com/cilium/cilium/pull/47933) — 0 comments · 2 reactions · open
- **Pull Request** [\[WIP\] Runtime cloud-IPAM routing rules reconciliation](https://github.com/cilium/cilium/pull/47938) — 1 comments · 2 reactions · open
- **Pull Request** [hubble: add optional protocol and port labels to policy metrics](https://github.com/cilium/cilium/pull/47944) — 1 comments · 1 reactions · open
- **Pull Request** [install: detect containerd from GKE kubelet config](https://github.com/cilium/cilium/pull/47945) — 0 comments · 1 reactions · open

### [Envoy](https://github.com/envoyproxy/envoy)

- **Pull Request** [ext_proc: adding direct mode_override support](https://github.com/envoyproxy/envoy/pull/46318) — 11 comments · 0 reactions · open
- **Pull Request** [Support hot restart handoff for connectionless UDP flows](https://github.com/envoyproxy/envoy/pull/46502) — 7 comments · 0 reactions · open
- **Pull Request** [mcp_transcoder: Fix Unbounded Recursion DoS](https://github.com/envoyproxy/envoy/pull/46543) — 6 comments · 0 reactions · open
- **Pull Request** [Order dependent bug](https://github.com/envoyproxy/envoy/pull/46673) — 4 comments · 0 reactions · open
- **Pull Request** [Add extension point to OpenTelemetry tracer for custom exporters.](https://github.com/envoyproxy/envoy/pull/46679) — 2 comments · 0 reactions · open
- **Pull Request** [router: support building an SRDS scope key from filter state](https://github.com/envoyproxy/envoy/pull/46526) — 5 comments · 0 reactions · open
- **Pull Request** [Add support for `serverNameOverride` in ALTS and create `ServerNameDecoratorTransportSocketOptions`](https://github.com/envoyproxy/envoy/pull/46686) — 1 comments · 0 reactions · open

### [Temporal](https://github.com/temporalio/temporal)

- **Pull Request** [fix(batcher): scope deterministic request IDs to the batch job ID](https://github.com/temporalio/temporal/pull/11546) — 2 comments · 0 reactions · closed
- **Pull Request** [Return test runner orchestration outcomes](https://github.com/temporalio/temporal/pull/11033) — 0 comments · 0 reactions · open
- **Pull Request** [Add replication stream lane wire protocol and receiver-side lane routing](https://github.com/temporalio/temporal/pull/11303) — 0 comments · 0 reactions · open
- **Pull Request** [Skip worker commands task queues in missing TQ check](https://github.com/temporalio/temporal/pull/11481) — 0 comments · 0 reactions · open
- **Pull Request** [Separate test diagnostics and timeout parsing](https://github.com/temporalio/temporal/pull/11487) — 0 comments · 0 reactions · open
- **Pull Request** [Scope test diagnostics to canonical results](https://github.com/temporalio/temporal/pull/11488) — 0 comments · 0 reactions · open
- **Pull Request** [Use generic JUnit documents at runner boundaries](https://github.com/temporalio/temporal/pull/11512) — 0 comments · 0 reactions · open
- **Pull Request** [Harden shared JUnit report IO](https://github.com/temporalio/temporal/pull/11513) — 0 comments · 0 reactions · open
- **Pull Request** [Define canonical Go test attempt results](https://github.com/temporalio/temporal/pull/11514) — 0 comments · 0 reactions · open
- **Pull Request** [Record canonical Go test attempt results](https://github.com/temporalio/temporal/pull/11515) — 0 comments · 0 reactions · open
- **Pull Request** [Plan test retries from canonical results](https://github.com/temporalio/temporal/pull/11516) — 0 comments · 0 reactions · open
- **Pull Request** [Render JUnit from canonical attempt results](https://github.com/temporalio/temporal/pull/11517) — 0 comments · 0 reactions · open
- **Pull Request** [Adopt canonical test reporting pipeline](https://github.com/temporalio/temporal/pull/11518) — 0 comments · 0 reactions · open
- **Pull Request** [Fix sticky queue stats zeroed out](https://github.com/temporalio/temporal/pull/11527) — 0 comments · 0 reactions · open
- **Pull Request** [Update Selected API list.](https://github.com/temporalio/temporal/pull/11535) — 0 comments · 0 reactions · open
- **Pull Request** [Attribute queue reader stuck attempts to a slice](https://github.com/temporalio/temporal/pull/11541) — 0 comments · 0 reactions · open
- **Pull Request** [Release process-global lifecycle registrations](https://github.com/temporalio/temporal/pull/11543) — 0 comments · 0 reactions · open
- **Pull Request** [Enforce zero expected object leaks](https://github.com/temporalio/temporal/pull/11544) — 1 comments · 0 reactions · closed
- **Pull Request** [Add isolation manager for per-namespace replication lanes](https://github.com/temporalio/temporal/pull/11304) — 0 comments · 0 reactions · open
- **Pull Request** [fix time-skipping flaky tests](https://github.com/temporalio/temporal/pull/11548) — 0 comments · 0 reactions · open

### [containerd](https://github.com/containerd/containerd)

- **Issue** [TaskOOM event lost](https://github.com/containerd/containerd/issues/8893) — 17 comments · 0 reactions · open
- **Pull Request** [ci: add lima image list for fedora images](https://github.com/containerd/containerd/pull/13955) — 1 comments · 0 reactions · open
