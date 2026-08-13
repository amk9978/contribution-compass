# Cilium Project News — 2026-08-13

> Public GitHub release and roadmap evidence. Upcoming items are indications, not commitments.

Repository: [cilium/cilium](https://github.com/cilium/cilium)

## Latest stable: [1.20.0](https://github.com/cilium/cilium/releases/tag/v1.20.0)

- Tag: `v1.20.0`
- Published: 2026-07-29T15:00:29Z
- ⛩️ Gateway API
- 🚀 Gateway API v1.6.1: Cilium moves from Gateway API v1.4 to v1.6.1, bringing support for capabilities that graduated across both upstream releases. (cilium/cilium#45251, @youngnick; cilium/cilium#46827, cilium/cilium#47274, @arybolovlev)
- 👥 Delegate Gateway Listeners: ListenerSets let application teams attach and manage their own listeners while the platform team retains ownership of the shared Gateway. (cilium/cilium#46303, cilium/cilium#46785, @asauber)
- 🔏 Encrypt Traffic to Backends: Gateway API BackendTLSPolicy support lets operators configure TLS and backend certificate validation for traffic between the gateway and application services. (cilium/cilium#43045, @youngnick)
- 🔀 TCPRoute and UDPRoute: Databases, DNS servers, game servers and other non-HTTP services can now be managed through the same Gateway API model as HTTP and gRPC traffic. (cilium/cilium#46184, cilium/cilium#46970, @eminaktas; cilium/cilium#4
- 🔐 External Authorization: HTTPRoute requests can now be authenticated and authorized through an external service before they reach the application, using the Gateway API ExternalAuth filter from GEP-1494. (cilium/cilium#45739, @gauteoh)

## Publicly indicated upcoming work

- **Prerelease** [1.21.0-pre.0](https://github.com/cilium/cilium/releases/tag/v1.21.0-pre.0)
- **Milestone** [Network namespaces test consolidation](https://github.com/cilium/cilium/milestone/44)
- **Milestone** [clang-free](https://github.com/cilium/cilium/milestone/45)
- **Milestone** [loader refactor](https://github.com/cilium/cilium/milestone/46)
- **Milestone** [ZTunnel Integration](https://github.com/cilium/cilium/milestone/54)
- **Milestone** [1.22-feature-freeze](https://github.com/cilium/cilium/milestone/56)
