# Platform / Networking / Runtime Infrastructure — 2026-08-18

> Factual GitHub evidence collected by Contribution Compass. No LLM analysis is performed.

## Contribution Leads

### [ACME support](https://github.com/envoyproxy/envoy/issues/96)

- Project: `envoyproxy/envoy`
- Tier: `maintainer-invited`
- Evidence: Maintainer invitation label: help wanted; No assignee is listed
- Caveat: Confirm scope and availability with the maintainers before starting work.

### [Liveness probes coming from "world" entity](https://github.com/cilium/cilium/issues/43012)

- Project: `cilium/cilium`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [containerd crash with program exceeds 10000-thread limit - container-log FIFO open leaks an OS thread per failed CreateContainer](https://github.com/containerd/containerd/issues/13952)

- Project: `containerd/containerd`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

## Important Updates

### [Cilium](https://github.com/cilium/cilium)

- **Issue** [cilium-agent <-> cilium-envoy livelock on cilium.NetworkPolicy xDS after upgrading to 1.20.0 — sustained 85-100% CPU on every node, no CiliumNetworkPolicy/CiliumEnvoyConfig present](https://github.com/cilium/cilium/issues/47624) — 15 comments · 3 reactions · open
- **Issue** [Liveness probes coming from "world" entity](https://github.com/cilium/cilium/issues/43012) — 17 comments · 4 reactions · open
- **Pull Request** [.github: Enable unsafe tests in cloud workflows](https://github.com/cilium/cilium/pull/47220) — 20 comments · 3 reactions · open
- **Pull Request** [bpf: populate fib lookup L4 tuple for ECMP path selection](https://github.com/cilium/cilium/pull/45608) — 12 comments · 4 reactions · open
- **Pull Request** [\[envoy\] Add HTTP CONNECT support](https://github.com/cilium/cilium/pull/45051) — 10 comments · 3 reactions · open
- **Pull Request** [chore(deps): update all-dependencies (main)](https://github.com/cilium/cilium/pull/47859) — 15 comments · 2 reactions · open
- **Pull Request** [bpf: lb: reply to ICMP echo (ping) for service VIPs (opt-in)](https://github.com/cilium/cilium/pull/47130) — 4 comments · 4 reactions · open
- **Pull Request** [network driver: use statedb to manage agent devices](https://github.com/cilium/cilium/pull/47558) — 13 comments · 2 reactions · closed
- **Pull Request** [node/manager: Populate node table from manager](https://github.com/cilium/cilium/pull/45953) — 11 comments · 2 reactions · open
- **Pull Request** [Fix multiple regressions in Cilium LocalRedirectPolicy](https://github.com/cilium/cilium/pull/46638) — 15 comments · 2 reactions · open
- **Pull Request** [ces: fix shutdown deadlock](https://github.com/cilium/cilium/pull/47802) — 10 comments · 2 reactions · closed
- **Issue** [ExternalAuth filter fails unsafely if backendRef is missing a ReferenceGrant](https://github.com/cilium/cilium/issues/47877) — 1 comments · 2 reactions · closed
- **Pull Request** [gateway-api: add support for ExtensionRef using Envoy ext_proc filter](https://github.com/cilium/cilium/pull/46479) — 9 comments · 3 reactions · open
- **Pull Request** [standalone-dns-proxy: return an error when no endpoint is found](https://github.com/cilium/cilium/pull/47791) — 8 comments · 2 reactions · closed
- **Pull Request** [images: update cilium-envoy](https://github.com/cilium/cilium/pull/47895) — 5 comments · 3 reactions · closed
- **Pull Request** [chore(deps): update base-images (v1.19)](https://github.com/cilium/cilium/pull/47950) — 8 comments · 2 reactions · closed
- **Pull Request** [clustermesh: transition service exports to observer](https://github.com/cilium/cilium/pull/47955) — 9 comments · 2 reactions · closed
- **Pull Request** [Mark terminating Envoy backends as DRAINING](https://github.com/cilium/cilium/pull/46642) — 10 comments · 2 reactions · open
- **Pull Request** [Add various routing fixes for ENI IPv6 support](https://github.com/cilium/cilium/pull/47034) — 7 comments · 2 reactions · open
- **Pull Request** [Update documentation dependencies](https://github.com/cilium/cilium/pull/47750) — 10 comments · 2 reactions · closed
- **Pull Request** [policy: fix bug causing policies using label selectors of long namespace labels being dropped](https://github.com/cilium/cilium/pull/47845) — 7 comments · 2 reactions · open
- **Pull Request** [bpf: trace: turn trace_notify msg into auxvar](https://github.com/cilium/cilium/pull/47875) — 10 comments · 2 reactions · closed
- **Pull Request** [test: Forbid `reflect.DeepEqual` in test code](https://github.com/cilium/cilium/pull/47891) — 3 comments · 4 reactions · open
- **Issue** [CFP: Make fixed (reserved/well known) identities granular per cluster for Cluster Mesh](https://github.com/cilium/cilium/issues/45065) — 4 comments · 0 reactions · open
- **Issue** [With Gateway API, the 3-way handshake fails when Envoy and the Backend Pod are running on the same Node.](https://github.com/cilium/cilium/issues/47591) — 5 comments · 0 reactions · open
- **Pull Request** [Add zone locality info to envoy endpoints if service EndPointSlices have zone information.](https://github.com/cilium/cilium/pull/47335) — 5 comments · 2 reactions · open
- **Pull Request** [kvstore: let \[UserEnforcePresence\] additionally revoke stale roles](https://github.com/cilium/cilium/pull/47915) — 5 comments · 2 reactions · closed
- **Pull Request** [install: detect GKE from kubelet path](https://github.com/cilium/cilium/pull/47945) — 9 comments · 1 reactions · open
- **Pull Request** [chore(deps): update base-images (main)](https://github.com/cilium/cilium/pull/47947) — 4 comments · 2 reactions · closed
- **Issue** [Dependency Dashboard](https://github.com/cilium/cilium/issues/33550) — 2 comments · 0 reactions · open

### [Envoy](https://github.com/envoyproxy/envoy)

- **Issue** [ACME support](https://github.com/envoyproxy/envoy/issues/96) — 30 comments · 173 reactions · open
- **Pull Request** [oauth2: chunk large token cookies](https://github.com/envoyproxy/envoy/pull/43135) — 33 comments · 5 reactions · open
- **Pull Request** [Ext authz caching](https://github.com/envoyproxy/envoy/pull/44874) — 31 comments · 0 reactions · open
- **Pull Request** [vhds: add support for initial xdstp collection](https://github.com/envoyproxy/envoy/pull/44129) — 26 comments · 0 reactions · open
- **Pull Request** [Queue policy extension](https://github.com/envoyproxy/envoy/pull/43355) — 20 comments · 0 reactions · open
- **Pull Request** [internal_upstream: reverse-propagate filter state across the internal listener boundary at close](https://github.com/envoyproxy/envoy/pull/45237) — 24 comments · 0 reactions · open
- **Pull Request** [network: fix stream leak when a user-space peer fully closes under half-close](https://github.com/envoyproxy/envoy/pull/45198) — 14 comments · 2 reactions · open
- **Pull Request** [vhds: use vhds virtual host over rds one upon name conflict](https://github.com/envoyproxy/envoy/pull/44401) — 21 comments · 0 reactions · open
- **Pull Request** [hot restart: propagate programmatic stat tags across restart](https://github.com/envoyproxy/envoy/pull/45674) — 16 comments · 0 reactions · open
- **Pull Request** [add ratelimit descriptor extension to use jwt claims as descriptors](https://github.com/envoyproxy/envoy/pull/46138) — 12 comments · 1 reactions · open
- **Pull Request** [xDS: add flow control fields to ext_proc protocol](https://github.com/envoyproxy/envoy/pull/45509) — 19 comments · 0 reactions · open
- **Pull Request** [redis filter: support `CLUSTER SHARDS`](https://github.com/envoyproxy/envoy/pull/46480) — 4 comments · 2 reactions · open
- **Issue** [http1: unsafe ctype usage and size_t to int narrowing in the HTTP/1 parser](https://github.com/envoyproxy/envoy/issues/46505) — 3 comments · 0 reactions · open
- **Issue** [HTTP3/QUIC listeners do not support 384-bit EC certificates](https://github.com/envoyproxy/envoy/issues/46694) — 3 comments · 0 reactions · open
- **Issue** [pre-push check fails on macOS trying to use a Linux jq binary](https://github.com/envoyproxy/envoy/issues/46716) — 2 comments · 0 reactions · open
- **Pull Request** [quic: populate peer certificate details in QUIC connection info](https://github.com/envoyproxy/envoy/pull/45978) — 15 comments · 0 reactions · open
- **Pull Request** [upstream: add per-worker subset load balancer](https://github.com/envoyproxy/envoy/pull/45979) — 15 comments · 0 reactions · open
- **Pull Request** [Revert #45073 c-ares: make qcache_max_ttl configurable](https://github.com/envoyproxy/envoy/pull/46577) — 15 comments · 0 reactions · closed
- **Issue** [http: propose exact request-target rewrite early-header-mutation extension](https://github.com/envoyproxy/envoy/issues/46700) — 1 comments · 0 reactions · open
- **Issue** [Datadog tracer ignores Ingress/Egress — all spans get `span.kind:internal` (client/server metrics gone)](https://github.com/envoyproxy/envoy/issues/46712) — 1 comments · 0 reactions · open
- **Issue** [access log: expose the negotiated downstream and upstream TLS group](https://github.com/envoyproxy/envoy/issues/46725) — 1 comments · 0 reactions · closed
- **Pull Request** [metadata: supported to access specific item of ListValue by the MetadataKey](https://github.com/envoyproxy/envoy/pull/45948) — 9 comments · 0 reactions · open
- **Pull Request** [QUIC eBPF hot restart part 0](https://github.com/envoyproxy/envoy/pull/45504) — 11 comments · 0 reactions · open
- **Pull Request** [oauth2: add cookie expiration margin](https://github.com/envoyproxy/envoy/pull/45810) — 6 comments · 1 reactions · closed
- **Pull Request** [dynamic_modules: expose current log level getter for HttpFilterConfigHandle in GO SDK](https://github.com/envoyproxy/envoy/pull/46116) — 7 comments · 0 reactions · open
- **Pull Request** [reverse_tunnel: defer downstream initiation until the parent stops accepting new connections](https://github.com/envoyproxy/envoy/pull/46166) — 7 comments · 0 reactions · closed
- **Pull Request** [match_delegate: lazily create the delegated filter](https://github.com/envoyproxy/envoy/pull/46259) — 10 comments · 0 reactions · open
- **Pull Request** [jwt_authn: sanitize payload and claim headers filter-wide](https://github.com/envoyproxy/envoy/pull/46586) — 7 comments · 0 reactions · open
- **Pull Request** [Disable fmtlib Unicode support on Windows](https://github.com/envoyproxy/envoy/pull/46601) — 6 comments · 0 reactions · open
- **Pull Request** [fix: health check probes blocked indefinitely when EDS initialFetchTimeout is 0s](https://github.com/envoyproxy/envoy/pull/46667) — 6 comments · 0 reactions · open

### [Temporal](https://github.com/temporalio/temporal)

- **Issue** [DeleteWorkerDeploymentVersion fails permanently when a version summary outlives its version workflow](https://github.com/temporalio/temporal/issues/11539) — 1 comments · 0 reactions · open
- **Issue** [PostgreSQL visibility v1.14 schema upgrade misses the v1.10–v1.13 rewrite optimization](https://github.com/temporalio/temporal/issues/11594) — 1 comments · 0 reactions · open
- **Issue** [Data race in UpdateWithStart: ExecutionState.Status read after workflow lock release](https://github.com/temporalio/temporal/issues/11600) — 0 comments · 0 reactions · open
- **Pull Request** [perf: replace sharedScopeCache with sync.Map for zero-alloc metrics cache lookups](https://github.com/temporalio/temporal/pull/10115) — 8 comments · 0 reactions · closed
- **Pull Request** [Index GitHub Actions runs for flake bisecting](https://github.com/temporalio/temporal/pull/11524) — 1 comments · 1 reactions · closed
- **Pull Request** [Improve flaky report presentation](https://github.com/temporalio/temporal/pull/11528) — 2 comments · 0 reactions · open
- **Pull Request** [Trace inbound Nexus HTTP requests](https://github.com/temporalio/temporal/pull/11560) — 2 comments · 0 reactions · open
- **Pull Request** [Await 2.0](https://github.com/temporalio/temporal/pull/10377) — 0 comments · 0 reactions · open
- **Pull Request** [Adaptive test timeouts via Await](https://github.com/temporalio/temporal/pull/10417) — 0 comments · 0 reactions · open
- **Pull Request** [Annotate worker task spans](https://github.com/temporalio/temporal/pull/10739) — 0 comments · 0 reactions · open
- **Pull Request** [Richer await timeout diagnostics](https://github.com/temporalio/temporal/pull/10781) — 0 comments · 0 reactions · open
- **Pull Request** [Add replication stream lane wire protocol and receiver-side lane routing](https://github.com/temporalio/temporal/pull/11303) — 0 comments · 0 reactions · open
- **Pull Request** [NEXUS-504: Refactor Nexus frontend interceptors](https://github.com/temporalio/temporal/pull/11464) — 0 comments · 0 reactions · open
- **Pull Request** [Gradual connect shedding tasks](https://github.com/temporalio/temporal/pull/11492) — 0 comments · 0 reactions · open
- **Pull Request** [Release gRPC resolver registrations on shutdown](https://github.com/temporalio/temporal/pull/11543) — 0 comments · 0 reactions · open
- **Pull Request** [Release OTEL logger registrations on shutdown](https://github.com/temporalio/temporal/pull/11551) — 1 comments · 0 reactions · open
- **Pull Request** [Only count reader reads that left tasks behind as stuck attempts](https://github.com/temporalio/temporal/pull/11554) — 0 comments · 0 reactions · open
- **Pull Request** [Activate pending starts after schedule migration](https://github.com/temporalio/temporal/pull/11557) — 0 comments · 0 reactions · open
- **Pull Request** [Add OpenTelemetry HTTP instrumentation](https://github.com/temporalio/temporal/pull/11558) — 1 comments · 0 reactions · open
- **Pull Request** [Trace outbound Nexus HTTP requests](https://github.com/temporalio/temporal/pull/11559) — 1 comments · 0 reactions · open
- **Pull Request** [Annotate Nexus spans](https://github.com/temporalio/temporal/pull/11561) — 0 comments · 0 reactions · open
- **Pull Request** [\[Visibility\]\[Elasticsearch\] Change datetime format to always include nanos component in pagination filter](https://github.com/temporalio/temporal/pull/11564) — 0 comments · 0 reactions · closed
- **Pull Request** [Recreate only the activity timers whose deadline actually moved](https://github.com/temporalio/temporal/pull/11565) — 1 comments · 0 reactions · open
- **Pull Request** [Add completion callbacks to SANOs](https://github.com/temporalio/temporal/pull/11567) — 1 comments · 0 reactions · open
- **Pull Request** [Release removed shared cluster test references](https://github.com/temporalio/temporal/pull/11575) — 1 comments · 0 reactions · closed
- **Pull Request** [Fix execution last running clock on start](https://github.com/temporalio/temporal/pull/11578) — 0 comments · 0 reactions · closed
- **Pull Request** [Enable HTTP/2 keepalive on nexus and callback transports](https://github.com/temporalio/temporal/pull/11581) — 0 comments · 0 reactions · closed
- **Pull Request** [Use fully qualified name for archetype tag instead of display name](https://github.com/temporalio/temporal/pull/11583) — 0 comments · 0 reactions · open
- **Pull Request** [Support Worker-variant callbacks](https://github.com/temporalio/temporal/pull/11589) — 1 comments · 0 reactions · open
- **Pull Request** [Update test shard salt](https://github.com/temporalio/temporal/pull/11592) — 0 comments · 0 reactions · closed

### [containerd](https://github.com/containerd/containerd)

- **Issue** [containerd fails on start: "failed to get metadata for stored sandbox"](https://github.com/containerd/containerd/issues/10848) — 11 comments · 2 reactions · closed
- **Issue** [CTR downloads of images get interrupted for unknown reason](https://github.com/containerd/containerd/issues/12314) — 14 comments · 0 reactions · closed
- **Issue** [containerd crash with program exceeds 10000-thread limit - container-log FIFO open leaks an OS thread per failed CreateContainer](https://github.com/containerd/containerd/issues/13952) — 8 comments · 0 reactions · open
- **Issue** [\[SIG-Node\]: <KEP-5607 - Allow HostNetwork Pods to Use User Namespaces>](https://github.com/containerd/containerd/issues/12489) — 10 comments · 0 reactions · open
- **Issue** [have customized hosts.toml for docker.io. but the link is server instead of host.*** when pulling nginx images](https://github.com/containerd/containerd/issues/12550) — 8 comments · 0 reactions · closed
- **Issue** [TestIssue10244LoopbackV2 failed](https://github.com/containerd/containerd/issues/12780) — 9 comments · 0 reactions · closed
- **Issue** [Containerd multipart fetch cancelled by progress timeout](https://github.com/containerd/containerd/issues/12811) — 5 comments · 0 reactions · closed
- **Issue** [Make known vendors for --gpus configurable](https://github.com/containerd/containerd/issues/12924) — 4 comments · 0 reactions · closed
- **Issue** [cimfs causes BSOD (crash) on real workloads for windows](https://github.com/containerd/containerd/issues/12982) — 4 comments · 0 reactions · closed
- **Issue** [Bond CNI fails with "Link not found" in chained CNI config after upgrading to 1.7.29+](https://github.com/containerd/containerd/issues/13545) — 2 comments · 0 reactions · open
- **Issue** [Normalize image tag update behavior on image pull](https://github.com/containerd/containerd/issues/13874) — 0 comments · 0 reactions · open
- **Issue** [Pulling tag+digest in k8s.io namespace confuses crictl](https://github.com/containerd/containerd/issues/13969) — 0 comments · 0 reactions · open
- **Issue** [Proposal: Support Pod-level checkpoint and restore](https://github.com/containerd/containerd/issues/13970) — 1 comments · 0 reactions · open
- **Pull Request** [metadata: bound snapshotter Remove during garbage collection](https://github.com/containerd/containerd/pull/13799) — 4 comments · 0 reactions · open
- **Pull Request** [runtime: invoke Shutdown after every task deletion](https://github.com/containerd/containerd/pull/13958) — 2 comments · 0 reactions · closed
- **Pull Request** [warning if notfound on containerStatus api](https://github.com/containerd/containerd/pull/11613) — 4 comments · 0 reactions · closed
- **Pull Request** [debug: add disk space usage logs for failed snapshotter tests](https://github.com/containerd/containerd/pull/12056) — 4 comments · 0 reactions · closed
- **Pull Request** [feat: add additional metadata to image-verification plugin](https://github.com/containerd/containerd/pull/12541) — 5 comments · 0 reactions · closed
- **Pull Request** [pkg/shim: Report bootstrap API mismatch on startup](https://github.com/containerd/containerd/pull/13910) — 0 comments · 0 reactions · open
- **Pull Request** [Export config in CRI plugin](https://github.com/containerd/containerd/pull/13940) — 0 comments · 0 reactions · open
- **Pull Request** [cri, nri: record resolved image name and digest in container metadata](https://github.com/containerd/containerd/pull/13960) — 0 comments · 0 reactions · open
- **Pull Request** [core/unpack: fetch layers of every config-sharing manifest](https://github.com/containerd/containerd/pull/13966) — 0 comments · 0 reactions · open
- **Pull Request** [Update win documentation for command prompt users](https://github.com/containerd/containerd/pull/12087) — 3 comments · 0 reactions · closed
- **Pull Request** [Protect content ingest with temporary lease](https://github.com/containerd/containerd/pull/13968) — 0 comments · 0 reactions · open
- **Pull Request** [Support Pod-level checkpoint and restore](https://github.com/containerd/containerd/pull/13971) — 1 comments · 0 reactions · open
- **Pull Request** [internal/cri/server: avoid debug log formatting for container spec](https://github.com/containerd/containerd/pull/13972) — 0 comments · 0 reactions · open
- **Pull Request** [vendor: github.com/stretchr/testify v1.12.0](https://github.com/containerd/containerd/pull/13973) — 0 comments · 0 reactions · open
- **Pull Request** [fix: preserve tag in ParseImageReferences when reference has both tag and digest](https://github.com/containerd/containerd/pull/13974) — 0 comments · 0 reactions · open
- **Pull Request** [Update mount manager schema](https://github.com/containerd/containerd/pull/13975) — 0 comments · 0 reactions · open
