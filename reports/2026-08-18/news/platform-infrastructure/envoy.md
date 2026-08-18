# Envoy Project News — 2026-08-18

> Public GitHub release and roadmap evidence. Upcoming items are indications, not commitments.

Repository: [envoyproxy/envoy](https://github.com/envoyproxy/envoy)

## Latest stable: [v1.39.0](https://github.com/envoyproxy/envoy/releases/tag/v1.39.0)

- Tag: `v1.39.0`
- Published: 2026-07-14T22:03:18Z
- Summary of changes
- Breaking changes
- build: Envoy now uses Bazel 8. Because Envoy still uses WORKSPACE mode, --enableworkspace and --noenablebzlmod are required and have been added to .bazelrc; external-repository runfiles now appear directly under the runfiles root.
- build: the Intel DLB connection balancer (envoy.network.connectionbalance.dlb) is disabled for all builds due to a broken source archive.
- TLS: enforcersakeyusage is deprecated and ignored; Envoy now always enforces the certificate keyUsage extension.
- TLS inspector: client TLS versions are validated and must be between TLS 1.0 and TLS 1.3 (revertible via envoy.reloadablefeatures.tlsinspectorenforceclienttlsversion).

## Publicly indicated upcoming work

- **Milestone** [Publicly available signed binaries/releases](https://github.com/envoyproxy/envoy/milestone/36)
- **Milestone** [Stabilizing the Golang filter](https://github.com/envoyproxy/envoy/milestone/48)
- **Milestone** [Switch to bzlmod](https://github.com/envoyproxy/envoy/milestone/106)

## Hacker News discussions

No matching current Hacker News discussion was found.
