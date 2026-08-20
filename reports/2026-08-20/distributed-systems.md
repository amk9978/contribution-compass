# Distributed Systems & Correctness — 2026-08-20

> Factual GitHub evidence collected by Contribution Compass. No LLM analysis is performed.

## Contribution Leads

### [Remove the double logging for open trace file failure from the TraceEvent cache based implementation](https://github.com/apple/foundationdb/issues/2739)

- Project: `apple/foundationdb`
- Tier: `maintainer-invited`
- Evidence: Maintainer invitation label: good first issue; No assignee is listed
- Caveat: Confirm scope and availability with the maintainers before starting work.

## Important Updates

### [FoundationDB](https://github.com/apple/foundationdb)

- **Pull Request** [Convert Data Distribution monitoring actors to coroutines](https://github.com/apple/foundationdb/pull/13870) — 44 comments · 1 reactions · open
- **Pull Request** [DD: config-driven bounded-time rollback of shard-encoded location metadata](https://github.com/apple/foundationdb/pull/13752) — 38 comments · 0 reactions · open
- **Pull Request** [report degraded multi-region status when failover is stuck waiting on the unavailable remote DC #12071](https://github.com/apple/foundationdb/pull/13295) — 36 comments · 0 reactions · open
- **Pull Request** [Backport to 7.4: Add metadata encoding (SHARD_ENCODE_LOCATION_METADATA) audit, rollback support, and tests (#13310)](https://github.com/apple/foundationdb/pull/13722) — 36 comments · 0 reactions · open
- **Pull Request** [Convert LoadBalance.actor.h to standard coroutines](https://github.com/apple/foundationdb/pull/13854) — 37 comments · 0 reactions · open
- **Pull Request** [Audit: bound validate_restore's slowest task instead of its average batch](https://github.com/apple/foundationdb/pull/13886) — 36 comments · 0 reactions · open
- **Pull Request** [always increment finishedQueries counter if incrementing allQueries](https://github.com/apple/foundationdb/pull/13786) — 32 comments · 0 reactions · open
- **Pull Request** [Convert NativeAPI header actors to standard coroutines](https://github.com/apple/foundationdb/pull/13887) — 29 comments · 0 reactions · open
- **Pull Request** [Plumb TraceID/SpanID into debug tracing logs](https://github.com/apple/foundationdb/pull/13673) — 27 comments · 0 reactions · closed
- **Pull Request** [Move storage simulation capabilities out of `fdbrpc`](https://github.com/apple/foundationdb/pull/13902) — 22 comments · 0 reactions · open
- **Pull Request** [Exercise streaming range selector boundary cases](https://github.com/apple/foundationdb/pull/13877) — 21 comments · 0 reactions · closed
- **Pull Request** [fdbclient: after unlink of per-thread library copy, symlink to original](https://github.com/apple/foundationdb/pull/13903) — 20 comments · 0 reactions · open
- **Pull Request** [(Backport to 7.4): DD finishMoveKeys: move waitForShardReady outside transaction (#13364)](https://github.com/apple/foundationdb/pull/13642) — 22 comments · 0 reactions · open
- **Pull Request** [build: always compress debug section, cleanup debug level](https://github.com/apple/foundationdb/pull/13904) — 16 comments · 0 reactions · open
- **Pull Request** [Move FDB well-known endpoint registry into `fdbclient`](https://github.com/apple/foundationdb/pull/13906) — 21 comments · 0 reactions · open
- **Pull Request** [Convert CoroFlow actors to standard C++ coroutines](https://github.com/apple/foundationdb/pull/13907) — 21 comments · 0 reactions · open
- **Pull Request** [bindings/python: install python "build" pkg only if missing](https://github.com/apple/foundationdb/pull/13910) — 21 comments · 0 reactions · open
- **Pull Request** [Test unsupported mapped-range read options](https://github.com/apple/foundationdb/pull/13875) — 15 comments · 0 reactions · closed
- **Pull Request** [Move proxy load metric decoding into `fdbclient`](https://github.com/apple/foundationdb/pull/13909) — 19 comments · 0 reactions · open
- **Pull Request** [Make DD relocation retry observations resilient to delay jitter](https://github.com/apple/foundationdb/pull/13897) — 10 comments · 0 reactions · open
- **Issue** [Remove the double logging for open trace file failure from the TraceEvent cache based implementation](https://github.com/apple/foundationdb/issues/2739) — 4 comments · 0 reactions · open
- **Pull Request** [\[release-7.4\] Forward-port stale peer fixes (storage server, commit/grv proxy)](https://github.com/apple/foundationdb/pull/13912) — 12 comments · 0 reactions · open
- **Pull Request** [\[release-7.4\] packaging/docker: update to kubectl 1.31.14 for YCSB image](https://github.com/apple/foundationdb/pull/13905) — 11 comments · 0 reactions · closed
- **Pull Request** [\[release-7.3\] Fix some potential DatabaseContext leaks in NativeApi](https://github.com/apple/foundationdb/pull/12309) — 5 comments · 0 reactions · closed
- **Pull Request** [always increment finishedQueries counter if incrementing allQueries](https://github.com/apple/foundationdb/pull/13908) — 1 comments · 0 reactions · open
- **Pull Request** [always increment finishedQueries counter if incrementing allQueries](https://github.com/apple/foundationdb/pull/13911) — 1 comments · 0 reactions · open

### [TigerBeetle](https://github.com/tigerbeetle/tigerbeetle)

- **Issue** [~1s commit stall once per 960 ops (checkpoint interval) under small batches on a grown data file; reproducible with tigerbeetle benchmark on stock 0.17.9](https://github.com/tigerbeetle/tigerbeetle/issues/3915) — 1 comments · 0 reactions · open

### [etcd Raft](https://github.com/etcd-io/raft)

No new or materially changed signals.

### [raft-rs](https://github.com/tikv/raft-rs)

No new or materially changed signals.

### [Jepsen](https://github.com/jepsen-io/jepsen)

No new or materially changed signals.
