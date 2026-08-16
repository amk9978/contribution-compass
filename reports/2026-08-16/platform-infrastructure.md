# Platform / Networking / Runtime Infrastructure — 2026-08-16

> Factual GitHub evidence collected by Contribution Compass. No LLM analysis is performed.

## Contribution Leads

### [Communication from world with lower MTU is failing to LoadBalancer services](https://github.com/cilium/cilium/issues/34380)

- Project: `cilium/cilium`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [Design Proposal: Agent2Agent(A2A) Support in Envoy](https://github.com/envoyproxy/envoy/issues/43268)

- Project: `envoyproxy/envoy`
- Tier: `triage-lead`
- Evidence: Unassigned enhancement with community reactions
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

## Important Updates

### [Cilium](https://github.com/cilium/cilium)

- **Issue** [Communication from world with lower MTU is failing to LoadBalancer services](https://github.com/cilium/cilium/issues/34380) — 22 comments · 11 reactions · open
- **Pull Request** [k8s: migrate from legacy config to ClusterInfo](https://github.com/cilium/cilium/pull/47854) — 15 comments · 2 reactions · closed
- **Pull Request** [Add various routing fixes for ENI IPv6 support](https://github.com/cilium/cilium/pull/47034) — 6 comments · 2 reactions · open
- **Pull Request** [bpf, datapath: move the CT_* params to runtime config](https://github.com/cilium/cilium/pull/47537) — 11 comments · 2 reactions · open
- **Issue** [Dependency Dashboard](https://github.com/cilium/cilium/issues/33550) — 2 comments · 0 reactions · open
- **Issue** [CFP: First Class MCS Support for GAMMA Routes](https://github.com/cilium/cilium/issues/47790) — 3 comments · 1 reactions · open
- **Pull Request** [v1.20 Backports 2026-08-14](https://github.com/cilium/cilium/pull/47967) — 2 comments · 2 reactions · closed
- **Issue** [CFP: Make fixed (reserved/well known) identities granular per cluster for Cluster Mesh](https://github.com/cilium/cilium/issues/45065) — 4 comments · 0 reactions · open
- **Issue** [Corrupted IP address in OLD_CILIUM_POST_nat rule reconciliation](https://github.com/cilium/cilium/issues/47956) — 1 comments · 0 reactions · open
- **Issue** [clustermesh: security hardening](https://github.com/cilium/cilium/issues/47968) — 1 comments · 0 reactions · open
- **Issue** [host-firewall-egress-to-fqdns connectivity test fails on RHEL8.10](https://github.com/cilium/cilium/issues/47975) — 4 comments · 0 reactions · open
- **Pull Request** [Improve output for `cilium-dbg policy selectors`](https://github.com/cilium/cilium/pull/46634) — 4 comments · 2 reactions · closed
- **Pull Request** [node: Migrate `IPv{4,6}IngressIP` to netip](https://github.com/cilium/cilium/pull/47165) — 4 comments · 2 reactions · closed
- **Pull Request** [gateway-api: skip proxy_protocol filter for GAMMA CECs](https://github.com/cilium/cilium/pull/47555) — 5 comments · 2 reactions · open
- **Issue** [bpf: migrate non-branching config macros to runtime configuration](https://github.com/cilium/cilium/issues/38370) — 2 comments · 0 reactions · open
- **Pull Request** [policy: migrate from legacy config to ClusterInfo](https://github.com/cilium/cilium/pull/47855) — 2 comments · 2 reactions · open
- **Pull Request** [bpf: don't reclassify an already reverse-NATed service reply](https://github.com/cilium/cilium/pull/47914) — 3 comments · 1 reactions · open
- **Pull Request** [chore(deps): update all lvh-images main (main) (patch)](https://github.com/cilium/cilium/pull/47983) — 2 comments · 2 reactions · closed
- **Pull Request** [chore(deps): update quay.io/cilium/cilium-envoy docker tag to v1.38.3-1786810643-4408e58b2a8a16a921d3f13c8c690a788655f0ba (main)](https://github.com/cilium/cilium/pull/47984) — 2 comments · 2 reactions · closed
- **Pull Request** [chore(deps): update quay.io/goswagger/swagger docker tag to v0.36.4 (main)](https://github.com/cilium/cilium/pull/47985) — 2 comments · 2 reactions · closed
- **Pull Request** [fix(deps): update all go dependencies main (main)](https://github.com/cilium/cilium/pull/47986) — 2 comments · 2 reactions · open
- **Pull Request** [chore(deps): update all github action dependencies (main)](https://github.com/cilium/cilium/pull/47987) — 2 comments · 2 reactions · open
- **Pull Request** [chore(deps): update dependency protocolbuffers/protobuf-go to v1.36.12 (v1.20)](https://github.com/cilium/cilium/pull/47988) — 2 comments · 2 reactions · open
- **Pull Request** [chore(deps): update quay.io/cilium/cilium-envoy docker tag to v1.37.5-1786810558-766ccfb37260a43e9d228837aa84ce3faf9f64e7 (v1.20)](https://github.com/cilium/cilium/pull/47989) — 2 comments · 2 reactions · open
- **Pull Request** [chore(deps): update stable lvh-images (v1.20) (patch)](https://github.com/cilium/cilium/pull/47990) — 2 comments · 2 reactions · open
- **Pull Request** [chore(deps): update all github action dependencies (v1.20)](https://github.com/cilium/cilium/pull/47991) — 2 comments · 2 reactions · closed
- **Issue** [Migrate `pkg/node/types.Node` to `netip`](https://github.com/cilium/cilium/issues/46924) — 0 comments · 0 reactions · open
- **Issue** [Per-packet service LB: embedded packet inside ICMP Fragmentation Needed is not reverse-translated, breaking PMTUD for ClusterIP flows](https://github.com/cilium/cilium/issues/47755) — 1 comments · 0 reactions · closed
- **Issue** [Gateway API Envoy cannot connect to backend pod on the same node while remote-node backend works](https://github.com/cilium/cilium/issues/47898) — 1 comments · 0 reactions · open
- **Issue** [The working (hostNetwork) per-Ingress configs show up properly wired — Selected: true, with a real listener. kube-system/cilium-ingress — the shared LoadBalancer Service — has no entry in this table at all.](https://github.com/cilium/cilium/issues/47976) — 1 comments · 0 reactions · closed

### [Envoy](https://github.com/envoyproxy/envoy)

- **Issue** [Design Proposal: Agent2Agent(A2A) Support in Envoy](https://github.com/envoyproxy/envoy/issues/43268) — 5 comments · 7 reactions · open
- **Issue** [Support sending access logs to syslog](https://github.com/envoyproxy/envoy/issues/45523) — 5 comments · 1 reactions · open
- **Issue** [aws_lambda filter forwards reserved x-amzn-* headers to Lambda Invoke API, causing 403](https://github.com/envoyproxy/envoy/issues/45609) — 6 comments · 0 reactions · open
- **Issue** [\[ext_proc\] add a control message directs modes overrides before request header response](https://github.com/envoyproxy/envoy/issues/46125) — 6 comments · 0 reactions · open
- **Issue** [Newer release available `rules_python`: 2.3.0 (current: 2.2.0)](https://github.com/envoyproxy/envoy/issues/46698) — 1 comments · 0 reactions · closed
- **Issue** [reverse tunnels: allow node sharing among clusters](https://github.com/envoyproxy/envoy/issues/46016) — 3 comments · 0 reactions · open
- **Issue** [oauth2: add RequestId (x-request-id) tag to OAuth2 filter application logs for correlation with access logs](https://github.com/envoyproxy/envoy/issues/46164) — 2 comments · 0 reactions · open
- **Pull Request** [Support subset lb using dynamically-set metadata for shadow HTTP traffic](https://github.com/envoyproxy/envoy/pull/46161) — 11 comments · 0 reactions · open
- **Pull Request** [redis filter: support `CLUSTER SHARDS`](https://github.com/envoyproxy/envoy/pull/46480) — 3 comments · 2 reactions · open
- **Issue** [Newer release available `boringssl`: 0.20260803.0 (current: 0.20260413.0)](https://github.com/envoyproxy/envoy/issues/46530) — 1 comments · 0 reactions · closed
- **Issue** [Newer release available `boringssl`: 0.20260813.0 (current: 0.20260413.0)](https://github.com/envoyproxy/envoy/issues/46705) — 0 comments · 0 reactions · open
- **Issue** [Newer release available `qatzip`: v2.0.0 (current: v1.3.2)](https://github.com/envoyproxy/envoy/issues/46706) — 0 comments · 0 reactions · open
- **Issue** [Newer release available `rules_python`: 2.3.1 (current: 2.2.0)](https://github.com/envoyproxy/envoy/issues/46707) — 0 comments · 0 reactions · open
- **Issue** [Datadog tracer ignores Ingress/Egress — all spans get `span.kind:internal` (client/server metrics gone)](https://github.com/envoyproxy/envoy/issues/46712) — 0 comments · 0 reactions · open
- **Issue** [pre-push check fails on macOS trying to use a Linux jq binary](https://github.com/envoyproxy/envoy/issues/46716) — 1 comments · 0 reactions · open
- **Pull Request** [reverse_tunnel: emit initiator access logs on drain and post-drain close](https://github.com/envoyproxy/envoy/pull/46569) — 4 comments · 0 reactions · open
- **Pull Request** [transport_sockets: fix proxy protocol format_string in added_tlvs](https://github.com/envoyproxy/envoy/pull/46497) — 2 comments · 0 reactions · open
- **Pull Request** [network: send zero-length UDP datagrams](https://github.com/envoyproxy/envoy/pull/46613) — 3 comments · 0 reactions · open
- **Pull Request** [reverse_tunnel: add tunnel setup latency stats](https://github.com/envoyproxy/envoy/pull/46614) — 3 comments · 0 reactions · open
- **Pull Request** [fix: health check probes blocked indefinitely when EDS initialFetchTimeout is 0s](https://github.com/envoyproxy/envoy/pull/46667) — 2 comments · 0 reactions · open
- **Pull Request** [Add extension point to OpenTelemetry tracer for custom exporters.](https://github.com/envoyproxy/envoy/pull/46679) — 2 comments · 0 reactions · open
- **Pull Request** [Allow ci/run_envoy_docker.sh callers to set SKIP_REMOTE_DETECTION](https://github.com/envoyproxy/envoy/pull/46704) — 3 comments · 0 reactions · closed
- **Pull Request** [cluster specifier: support new attempt aware cluster specifier](https://github.com/envoyproxy/envoy/pull/46640) — 1 comments · 0 reactions · open
- **Pull Request** [ExtProc: clarify docs on end_of_stream_without_message field](https://github.com/envoyproxy/envoy/pull/46671) — 1 comments · 0 reactions · closed
- **Pull Request** [SubstitutionFormatUtils can log multiple occurrences of same header](https://github.com/envoyproxy/envoy/pull/46688) — 1 comments · 0 reactions · open
- **Pull Request** [quic: support P-384 and P-521 EC certificates](https://github.com/envoyproxy/envoy/pull/46701) — 1 comments · 0 reactions · open
- **Pull Request** [router: classify remote resets as external-origin failures](https://github.com/envoyproxy/envoy/pull/46058) — 3 comments · 0 reactions · closed
- **Pull Request** [\[WIP\] deps: Bump `rules_rust` -> 0.71.3](https://github.com/envoyproxy/envoy/pull/46188) — 3 comments · 0 reactions · open
- **Pull Request** [cache_v2: support If-None-Match validation](https://github.com/envoyproxy/envoy/pull/46708) — 2 comments · 0 reactions · open
- **Pull Request** [user-space socket: emulate RST behaviour](https://github.com/envoyproxy/envoy/pull/46713) — 2 comments · 0 reactions · open

### [Temporal](https://github.com/temporalio/temporal)

- **Pull Request** [Index GitHub Actions runs for flake bisecting](https://github.com/temporalio/temporal/pull/11524) — 1 comments · 1 reactions · open
- **Pull Request** [Improve flaky report presentation](https://github.com/temporalio/temporal/pull/11528) — 2 comments · 0 reactions · open
- **Pull Request** [Trace inbound Nexus HTTP requests](https://github.com/temporalio/temporal/pull/11560) — 2 comments · 0 reactions · open
- **Pull Request** [Use Go client for flaky report GitHub API calls](https://github.com/temporalio/temporal/pull/11523) — 1 comments · 0 reactions · closed
- **Pull Request** [Release gRPC resolver registrations on shutdown](https://github.com/temporalio/temporal/pull/11543) — 0 comments · 0 reactions · open
- **Pull Request** [Release OTEL logger registrations on shutdown](https://github.com/temporalio/temporal/pull/11551) — 1 comments · 0 reactions · open
- **Pull Request** [Add OpenTelemetry HTTP instrumentation](https://github.com/temporalio/temporal/pull/11558) — 1 comments · 0 reactions · open
- **Pull Request** [Update test shard salt](https://github.com/temporalio/temporal/pull/11572) — 0 comments · 0 reactions · closed
- **Pull Request** [Support ExecutionStatus filter in s3store and gcloud visibility archi…](https://github.com/temporalio/temporal/pull/11298) — 1 comments · 0 reactions · closed
- **Pull Request** [Update test shard salt](https://github.com/temporalio/temporal/pull/11590) — 0 comments · 0 reactions · open
- **Pull Request** [1.32.0: Prepare release branch](https://github.com/temporalio/temporal/pull/11591) — 1 comments · 0 reactions · closed
- **Pull Request** [WIP: Add HostHealthAggregator](https://github.com/temporalio/temporal/pull/9980) — 1 comments · 0 reactions · open

### [containerd](https://github.com/containerd/containerd)

- **Issue** [CRI plugin: container stuck as RUNNING after process exit](https://github.com/containerd/containerd/issues/12678) — 39 comments · 0 reactions · open
- **Issue** [Excessive CPU usage during stat collection for BTRFS](https://github.com/containerd/containerd/issues/6067) — 12 comments · 0 reactions · closed
- **Issue** [btrfs snapshotter: stats collection walks 1.5M inodes per pass on an idle node](https://github.com/containerd/containerd/issues/13967) — 0 comments · 1 reactions · open
- **Issue** [Ctr checkpoint export image failure](https://github.com/containerd/containerd/issues/6812) — 14 comments · 0 reactions · open
- **Issue** [Live-restore option for containerd](https://github.com/containerd/containerd/issues/12172) — 12 comments · 0 reactions · closed
- **Issue** [Terminate a process group grandchildren on exec timeout](https://github.com/containerd/containerd/issues/4594) — 4 comments · 2 reactions · open
- **Issue** [Pass tracing context from containerd-shim to runc and OCI hooks](https://github.com/containerd/containerd/issues/12300) — 7 comments · 0 reactions · open
- **Issue** [The unexpected exit of copyPipe is blocking the container's stdout and stderr.](https://github.com/containerd/containerd/issues/12462) — 11 comments · 0 reactions · closed
- **Issue** [`docker load` fails with "no target for symlink layer" on docker-archive images containing symlinked layers (containerd 2.x)](https://github.com/containerd/containerd/issues/12890) — 3 comments · 1 reactions · closed
- **Issue** [High and steadily increasing memory usage in containerd-shim for calico-node-windows](https://github.com/containerd/containerd/issues/12781) — 4 comments · 0 reactions · closed
- **Issue** [`RemoveVolatileOption` cannot recognize mount type "fuse.nydus-overlayfs" from nydus-snapshotter](https://github.com/containerd/containerd/issues/13573) — 1 comments · 0 reactions · open
- **Pull Request** [Let containerd run in a separate mnt namespace](https://github.com/containerd/containerd/pull/11912) — 8 comments · 0 reactions · closed
- **Pull Request** [ci:fix container must be created error on shimv1](https://github.com/containerd/containerd/pull/11639) — 7 comments · 0 reactions · closed
- **Pull Request** [cgroupv2: set max_user_instances at least 1024](https://github.com/containerd/containerd/pull/11652) — 6 comments · 0 reactions · closed
- **Pull Request** [core/runtime/v2: add timeout to shim.delete during loadShims](https://github.com/containerd/containerd/pull/13852) — 2 comments · 0 reactions · closed
- **Pull Request** [cni:support to reload cni config when receive create event](https://github.com/containerd/containerd/pull/11711) — 4 comments · 0 reactions · closed
- **Pull Request** [\[release/2.0\] avoid import to testing pkg outside of tests](https://github.com/containerd/containerd/pull/11833) — 4 comments · 0 reactions · closed
- **Pull Request** [contrib: Require CAP_SYS_ADMIN for lsm_set_self_attr](https://github.com/containerd/containerd/pull/11906) — 4 comments · 0 reactions · closed
- **Pull Request** [images/archive: fix relative symlink resolution during import](https://github.com/containerd/containerd/pull/12900) — 1 comments · 1 reactions · open
- **Pull Request** [\[pkg/shim\] implement Windows support for the shim server](https://github.com/containerd/containerd/pull/13948) — 1 comments · 0 reactions · closed
- **Pull Request** [fix(runtime): apply load timeout to load shim](https://github.com/containerd/containerd/pull/13954) — 0 comments · 0 reactions · closed
- **Pull Request** [runtime: invoke Shutdown after every task deletion](https://github.com/containerd/containerd/pull/13958) — 1 comments · 0 reactions · open
- **Pull Request** [set debug level in discard event](https://github.com/containerd/containerd/pull/11876) — 3 comments · 0 reactions · closed
- **Pull Request** [core/runtime/v2: bound leaked shim cleanup at load](https://github.com/containerd/containerd/pull/13850) — 2 comments · 0 reactions · closed
- **Pull Request** [metadata/content: add media type label on ingest](https://github.com/containerd/containerd/pull/12895) — 1 comments · 0 reactions · open
- **Pull Request** [core/unpack: fetch layers of every config-sharing manifest](https://github.com/containerd/containerd/pull/13966) — 0 comments · 0 reactions · open
