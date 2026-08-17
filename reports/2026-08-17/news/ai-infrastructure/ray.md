# Ray Project News — 2026-08-17

> Public GitHub release and roadmap evidence. Upcoming items are indications, not commitments.

Repository: [ray-project/ray](https://github.com/ray-project/ray)

## Latest stable: [Ray-2.57.0](https://github.com/ray-project/ray/releases/tag/ray-2.57.0)

- Tag: `ray-2.57.0`
- Published: 2026-08-11T01:15:44Z
- Ray Data: In this Ray release, we've enabled DataSourceV2 by default (#64821), so readparquet and friends use the new scan/listing infrastructure with row-group-aware chunking and predicate splitting. Hash Shuffle V2 eliminates the aggregat
- HashShuffleV2 supports join (#63598, #64538, #64687). This lets shuffles reuse standard map/reduce scheduling, backpressure, and resource accounting.
- Ray Serve: The HAProxy ingress is now distributed as the ray-haproxy PyPI package instead of being compiled into images, and it is the default HAProxy binary (#64141, #64163, #64164). We've also added gRPC support to the HAProxy direct-ingr
- Ray Core: We've added an embedded RocksDB storage backend for GCS fault tolerance (REP-64), selectable with RAYgcsstorage=rocksdb and RAYgcsstoragepath (#63657). GCS fault tolerance no longer requires an external Redis instance. We've also
- 🎉 New Features
- Enable DataSourceV2 by default via DataContext.usedatasourcev2 (#64821)

## Publicly indicated upcoming work

- **Milestone** [Infra Backlog](https://github.com/ray-project/ray/milestone/11)
- **Milestone** [Packaging and Dependency Management](https://github.com/ray-project/ray/milestone/36)
- **Milestone** [\[serve\] Support Java as language](https://github.com/ray-project/ray/milestone/45)
- **Milestone** [runtime_env backlog](https://github.com/ray-project/ray/milestone/48)
- **Milestone** [Workflows after-alpha](https://github.com/ray-project/ray/milestone/52)

## Hacker News discussions

No matching current Hacker News discussion was found.
