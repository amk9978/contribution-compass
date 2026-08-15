# Platform / Networking / Runtime Infrastructure — 2026-08-15

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

- **Pull Request** [TEST CI](https://github.com/cilium/cilium/pull/47184) — 13 comments · 2 reactions · closed
- **Pull Request** [bpf: Enable extended masquerade port range for BPF masquerade](https://github.com/cilium/cilium/pull/47301) — 12 comments · 2 reactions · open
- **Issue** [CI: Non-zero (3) restart count of cilium-* (config) must be investigated](https://github.com/cilium/cilium/issues/40492) — 10 comments · 0 reactions · open
- **Issue** [CI: firewall-egress-to-fqdns fails 6% of the time: command terminated with exit code 28](https://github.com/cilium/cilium/issues/47921) — 11 comments · 0 reactions · closed
- **Pull Request** [BPF: Refactor nat tests to use scapy fixtures and add checksum coverage](https://github.com/cilium/cilium/pull/47222) — 11 comments · 2 reactions · closed
- **Pull Request** [feat(bgp): support BGP unnumbered peering (RFC 5549 / ENHE)](https://github.com/cilium/cilium/pull/47394) — 9 comments · 2 reactions · open
- **Pull Request** [cilium-cli: remove endpoint restore failed msg from ignored warnings](https://github.com/cilium/cilium/pull/46135) — 11 comments · 2 reactions · closed
- **Issue** [Dependency Dashboard](https://github.com/cilium/cilium/issues/33550) — 2 comments · 0 reactions · open
- **Pull Request** [golangci-lint: Migrate checks from bash scripts to forbidigo/depguard rules](https://github.com/cilium/cilium/pull/47946) — 2 comments · 2 reactions · closed
- **Pull Request** [.github: add ariane trigger phrase for e2e upgrade test](https://github.com/cilium/cilium/pull/47957) — 7 comments · 1 reactions · closed
- **Pull Request** [v1.20 Backports 2026-08-14](https://github.com/cilium/cilium/pull/47967) — 2 comments · 2 reactions · closed
- **Pull Request** [cilium-cli: disable host-firewall-egress-to-fqdns test on RHEL](https://github.com/cilium/cilium/pull/47970) — 3 comments · 2 reactions · closed
- **Issue** [Gateway API: Envoy upstream replies from same-node backends lost (RST), nondeterministic across restarts on ARM64](https://github.com/cilium/cilium/issues/47940) — 0 comments · 0 reactions · open
- **Issue** [clustermesh: security hardening](https://github.com/cilium/cilium/issues/47968) — 1 comments · 0 reactions · open
- **Pull Request** [ctmap: Use MapPair to store TCP and Any map](https://github.com/cilium/cilium/pull/46683) — 5 comments · 2 reactions · open
- **Pull Request** [pkg/datapath/sockets/probe: fix inet diag probing.](https://github.com/cilium/cilium/pull/47104) — 5 comments · 2 reactions · open
- **Pull Request** [install: detect GKE from kubelet path](https://github.com/cilium/cilium/pull/47945) — 5 comments · 1 reactions · open
- **Pull Request** [Fix operator.unmanagedPodWatcher.selector unquoted render](https://github.com/cilium/cilium/pull/47952) — 5 comments · 1 reactions · open
- **Pull Request** [health/client: replace deprecated http.Transport.Dial with DialContext](https://github.com/cilium/cilium/pull/47858) — 2 comments · 1 reactions · open
- **Pull Request** [hubble/relay: stop gRPC health server on shutdown](https://github.com/cilium/cilium/pull/47942) — 3 comments · 1 reactions · open
- **Pull Request** [helm: add general busybox image values for substitution](https://github.com/cilium/cilium/pull/47973) — 2 comments · 2 reactions · open
- **Issue** [CI: Cilium Cluster Mesh upgrade: Non-zero (1) restart count of clustermesh-apiserver-* must be investigated](https://github.com/cilium/cilium/issues/47972) — 1 comments · 0 reactions · open
- **Pull Request** [bpf/lib/nat: rename icmpoff](https://github.com/cilium/cilium/pull/47797) — 1 comments · 2 reactions · open
- **Pull Request** [ipam/eni: Source the ENI VPC CIDRs from IMDS](https://github.com/cilium/cilium/pull/47974) — 1 comments · 2 reactions · open
- **Pull Request** [fix(bgp): only auto-discover the default gateway from the main table](https://github.com/cilium/cilium/pull/47971) — 0 comments · 1 reactions · open

### [Envoy](https://github.com/envoyproxy/envoy)

- **Pull Request** [Order dependent bug](https://github.com/envoyproxy/envoy/pull/46673) — 6 comments · 0 reactions · open
- **Pull Request** [otel: create migration mechanism to semantic convention attribute names](https://github.com/envoyproxy/envoy/pull/45184) — 7 comments · 0 reactions · closed
- **Pull Request** [ext_proc: Adding support to send empty body buffer with EoS = true](https://github.com/envoyproxy/envoy/pull/46355) — 3 comments · 0 reactions · open
- **Pull Request** [reverse_tunnel: add tunnel setup latency stats](https://github.com/envoyproxy/envoy/pull/46614) — 3 comments · 0 reactions · open
- **Pull Request** [filesystem: refactor win32 watcher_impl to use absl mutex and fix buffer alignment](https://github.com/envoyproxy/envoy/pull/46655) — 2 comments · 0 reactions · open
- **Pull Request** [Add extension point to OpenTelemetry tracer for custom exporters.](https://github.com/envoyproxy/envoy/pull/46679) — 2 comments · 0 reactions · open
- **Pull Request** [reverse_tunnel: count connection-limit denials as rejected](https://github.com/envoyproxy/envoy/pull/46389) — 1 comments · 0 reactions · closed
- **Pull Request** [tls_inspector: fix GREASE filtering in JA4_c signature algorithms](https://github.com/envoyproxy/envoy/pull/46658) — 1 comments · 0 reactions · open
- **Pull Request** [Reuse old SDS provider config when fetch timeout has changed](https://github.com/envoyproxy/envoy/pull/46154) — 3 comments · 0 reactions · open
- **Pull Request** [reverse_tunnel: emit initiator access logs on drain and post-drain close](https://github.com/envoyproxy/envoy/pull/46569) — 3 comments · 0 reactions · open
- **Pull Request** [reverse_tunnel: wake accept via activateFileEvents instead of a pipe](https://github.com/envoyproxy/envoy/pull/46571) — 2 comments · 0 reactions · open
- **Pull Request** [Allow ci/run_envoy_docker.sh callers to set SKIP_REMOTE_DETECTION](https://github.com/envoyproxy/envoy/pull/46704) — 0 comments · 0 reactions · open

### [Temporal](https://github.com/temporalio/temporal)

- **Issue** [tdbg dlq commands reject the archival task category (5)](https://github.com/temporalio/temporal/issues/11586) — 0 comments · 0 reactions · open
- **Pull Request** [Index GitHub Actions runs for flake bisecting](https://github.com/temporalio/temporal/pull/11524) — 1 comments · 1 reactions · open
- **Pull Request** [Add completion callbacks to SANOs](https://github.com/temporalio/temporal/pull/11415) — 2 comments · 0 reactions · closed
- **Pull Request** [Add support for worker-variant callbacks](https://github.com/temporalio/temporal/pull/11456) — 2 comments · 0 reactions · closed
- **Pull Request** [Improve flaky report presentation](https://github.com/temporalio/temporal/pull/11528) — 2 comments · 0 reactions · open
- **Pull Request** [Trace inbound Nexus HTTP requests](https://github.com/temporalio/temporal/pull/11560) — 2 comments · 0 reactions · open
- **Pull Request** [Annotate worker task spans](https://github.com/temporalio/temporal/pull/10739) — 0 comments · 0 reactions · open
- **Pull Request** [Adopt canonical Go test reporting pipeline](https://github.com/temporalio/temporal/pull/11033) — 1 comments · 0 reactions · open
- **Pull Request** [Add data race summary to CI report](https://github.com/temporalio/temporal/pull/11211) — 0 comments · 0 reactions · open
- **Pull Request** [Separate test diagnostics and timeout parsing](https://github.com/temporalio/temporal/pull/11487) — 1 comments · 0 reactions · closed
- **Pull Request** [Scope test diagnostics to canonical results](https://github.com/temporalio/temporal/pull/11488) — 1 comments · 0 reactions · closed
- **Pull Request** [move admin batch jobs to sys ns](https://github.com/temporalio/temporal/pull/11494) — 0 comments · 0 reactions · open
- **Pull Request** [admin-batch-1: run admin batch in temporal-system](https://github.com/temporalio/temporal/pull/11509) — 0 comments · 0 reactions · open
- **Pull Request** [Use generic JUnit documents at runner boundaries](https://github.com/temporalio/temporal/pull/11512) — 1 comments · 0 reactions · closed
- **Pull Request** [Harden shared JUnit report IO](https://github.com/temporalio/temporal/pull/11513) — 1 comments · 0 reactions · closed
- **Pull Request** [Define canonical Go test attempt results](https://github.com/temporalio/temporal/pull/11514) — 1 comments · 0 reactions · closed
- **Pull Request** [Record canonical Go test attempt results](https://github.com/temporalio/temporal/pull/11515) — 1 comments · 0 reactions · closed
- **Pull Request** [Plan test retries from canonical results](https://github.com/temporalio/temporal/pull/11516) — 1 comments · 0 reactions · closed
- **Pull Request** [Render JUnit from canonical attempt results](https://github.com/temporalio/temporal/pull/11517) — 1 comments · 0 reactions · closed
- **Pull Request** [Adopt canonical test reporting pipeline](https://github.com/temporalio/temporal/pull/11518) — 1 comments · 0 reactions · closed
- **Pull Request** [Use Go client for flaky report GitHub API calls](https://github.com/temporalio/temporal/pull/11523) — 1 comments · 0 reactions · open
- **Pull Request** [Fix sticky queue stats zeroed out](https://github.com/temporalio/temporal/pull/11527) — 0 comments · 0 reactions · closed
- **Pull Request** [Release gRPC resolver registrations on shutdown](https://github.com/temporalio/temporal/pull/11543) — 0 comments · 0 reactions · open
- **Pull Request** [Release OTEL logger registrations on shutdown](https://github.com/temporalio/temporal/pull/11551) — 0 comments · 0 reactions · open
- **Pull Request** [Limit flakereport size](https://github.com/temporalio/temporal/pull/11552) — 1 comments · 0 reactions · closed
- **Pull Request** [Only count reader reads that left tasks behind as stuck attempts](https://github.com/temporalio/temporal/pull/11554) — 0 comments · 0 reactions · open
- **Pull Request** [Add OpenTelemetry HTTP instrumentation](https://github.com/temporalio/temporal/pull/11558) — 1 comments · 0 reactions · open
- **Pull Request** [Trace outbound Nexus HTTP requests](https://github.com/temporalio/temporal/pull/11559) — 1 comments · 0 reactions · open
- **Pull Request** [Annotate Nexus spans](https://github.com/temporalio/temporal/pull/11561) — 0 comments · 0 reactions · open
- **Pull Request** [Emit namespace CRUD lifecycle wide events (register / update / failover / delete)](https://github.com/temporalio/temporal/pull/11563) — 0 comments · 0 reactions · open

### [containerd](https://github.com/containerd/containerd)

- **Issue** [Cross layer mounts between different registries of different account fails.](https://github.com/containerd/containerd/issues/12163) — 4 comments · 3 reactions · closed
- **Issue** [Support container checkpoint/restore for gVisor runtime](https://github.com/containerd/containerd/issues/12280) — 8 comments · 1 reactions · open
- **Pull Request** [cri: enable mount manager for image mounts](https://github.com/containerd/containerd/pull/13542) — 12 comments · 1 reactions · open
- **Issue** [Pod leak causing nodes to crash](https://github.com/containerd/containerd/issues/12390) — 7 comments · 0 reactions · closed
- **Issue** [test case is skipped  when use vscode to debug  even user is root](https://github.com/containerd/containerd/issues/13024) — 3 comments · 0 reactions · closed
- **Issue** [make test failed on almalinux/fedora/](https://github.com/containerd/containerd/issues/13026) — 2 comments · 0 reactions · closed
- **Pull Request** [metadata: bound snapshotter Remove during garbage collection](https://github.com/containerd/containerd/pull/13799) — 4 comments · 0 reactions · open
- **Pull Request** [core/runtime/v2: add timeout to shim.delete during loadShims](https://github.com/containerd/containerd/pull/13852) — 2 comments · 0 reactions · open
- **Pull Request** [runtime: invoke Shutdown after every task deletion](https://github.com/containerd/containerd/pull/13958) — 2 comments · 0 reactions · open
- **Pull Request** [Export config in CRI plugin](https://github.com/containerd/containerd/pull/13940) — 0 comments · 0 reactions · open
- **Pull Request** [fix(runtime): apply load timeout to load shim](https://github.com/containerd/containerd/pull/13954) — 0 comments · 0 reactions · closed
- **Pull Request** [build(deps): bump the otel group with 8 updates](https://github.com/containerd/containerd/pull/13961) — 0 comments · 0 reactions · open
- **Pull Request** [build(deps): bump github.com/klauspost/compress from 1.19.1 to 1.19.2](https://github.com/containerd/containerd/pull/13962) — 0 comments · 0 reactions · open
- **Pull Request** [build(deps): bump the codeql-actions group with 3 updates](https://github.com/containerd/containerd/pull/13963) — 0 comments · 0 reactions · open
- **Pull Request** [build(deps): bump azure/login from 3.0.0 to 3.0.1](https://github.com/containerd/containerd/pull/13964) — 0 comments · 0 reactions · open
- **Pull Request** [build(deps): bump actions/attest-build-provenance from 4.1.1 to 4.2.2](https://github.com/containerd/containerd/pull/13965) — 0 comments · 0 reactions · open
