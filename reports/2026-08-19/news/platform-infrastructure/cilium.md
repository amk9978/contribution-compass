# Cilium Project News — 2026-08-19

> Public GitHub release and roadmap evidence. Upcoming items are indications, not commitments.

Repository: [cilium/cilium](https://github.com/cilium/cilium)

## Latest stable: [1.20.1](https://github.com/cilium/cilium/releases/tag/v1.20.1)

- Tag: `v1.20.1`
- Published: 2026-08-18T10:36:16Z
- docs/clustermesh: overhaul Cluster Mesh documentation with a new introduction, improved load-balancing guidance, and Helm-first setup and certificate configuration instructions (Backport PR cilium/cilium#47615, Upstream PR cilium/cilium#473
- envoy: demote stale ADS endpoint warning (Backport PR cilium/cilium#47805, Upstream PR cilium/cilium#47148, @nezdolik)
- Speed up recovery time for disrupted TCP connections that access a DSR-enabled Service. (Backport PR cilium/cilium#47881, Upstream PR cilium/cilium#47529, @julianwiedmann)
- azure: Stop issuing redundant CiliumNode status updates on every IPAM sync when the node's Azure interfaces are unchanged. (Backport PR cilium/cilium#47690, Upstream PR cilium/cilium#47449, @jaredledvina)
- bpf: dsr: don't look for TCP header on fragmented packets (Backport PR cilium/cilium#47881, Upstream PR cilium/cilium#47640, @julianwiedmann)
- bpf: hostfw: tolerate unknown CT protocols and rely on policies (Backport PR cilium/cilium#47621, Upstream PR cilium/cilium#47343, @smagnani96)

## Publicly indicated upcoming work

- **Milestone** [Network namespaces test consolidation](https://github.com/cilium/cilium/milestone/44)
- **Milestone** [clang-free](https://github.com/cilium/cilium/milestone/45)
- **Milestone** [loader refactor](https://github.com/cilium/cilium/milestone/46)
- **Milestone** [ZTunnel Integration](https://github.com/cilium/cilium/milestone/54)
- **Milestone** [1.22-feature-freeze](https://github.com/cilium/cilium/milestone/56)

## Hacker News discussions

No matching current Hacker News discussion was found.
