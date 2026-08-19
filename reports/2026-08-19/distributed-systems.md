# Distributed Systems & Correctness — 2026-08-19

> Factual GitHub evidence collected by Contribution Compass. No LLM analysis is performed.

## Contribution Leads

No evidence-qualified contribution leads changed in this collection.
## Important Updates

### [FoundationDB](https://github.com/apple/foundationdb)

- **Pull Request** [Update the base image to RockyLinux 10.2](https://github.com/apple/foundationdb/pull/12549) — 37 comments · 1 reactions · open
- **Pull Request** [Move TSS load balancing logic out of `fdbrpc`](https://github.com/apple/foundationdb/pull/13180) — 93 comments · 0 reactions · closed
- **Pull Request** [Fix stateless process recruitment in small configurations](https://github.com/apple/foundationdb/pull/13731) — 77 comments · 0 reactions · open
- **Pull Request** [Convert `ActorCollection` to standard coroutines](https://github.com/apple/foundationdb/pull/13836) — 67 comments · 0 reactions · closed
- **Pull Request** [\[release-7.4\] documentation: sphinx-6.2.1 and release-notes cleanup](https://github.com/apple/foundationdb/pull/13882) — 40 comments · 0 reactions · closed
- **Pull Request** [Make no-throw coroutine cancellation reentrant-safe](https://github.com/apple/foundationdb/pull/13885) — 39 comments · 0 reactions · closed
- **Pull Request** [Audit: bound validate_restore's slowest task instead of its average batch](https://github.com/apple/foundationdb/pull/13886) — 36 comments · 0 reactions · open
- **Pull Request** [documentation: update downloads links with foundationdb-7.3.77](https://github.com/apple/foundationdb/pull/13855) — 30 comments · 0 reactions · closed
- **Pull Request** [Remove redundant `explicit(false)` from copy and move constructors](https://github.com/apple/foundationdb/pull/13889) — 30 comments · 0 reactions · closed
- **Pull Request** [Convert LoadBalance.actor.h to standard coroutines](https://github.com/apple/foundationdb/pull/13854) — 29 comments · 0 reactions · open
- **Pull Request** [Plumb TraceID/SpanID into debug tracing logs](https://github.com/apple/foundationdb/pull/13673) — 26 comments · 0 reactions · open
- **Pull Request** [Wait for a spare storage server before perpetual wiggle migration](https://github.com/apple/foundationdb/pull/13884) — 26 comments · 0 reactions · closed
- **Pull Request** [Retire old TLog roles after terminal recovery](https://github.com/apple/foundationdb/pull/13893) — 24 comments · 0 reactions · open
- **Pull Request** [tests: simpler fallible authorization_venv_setup](https://github.com/apple/foundationdb/pull/13901) — 24 comments · 0 reactions · closed
- **Pull Request** [docker: update base to rockylinux-9.8, golang build base, README](https://github.com/apple/foundationdb/pull/13757) — 23 comments · 0 reactions · closed
- **Pull Request** [docker: update base to rockylinux-9.8, golang builder, README](https://github.com/apple/foundationdb/pull/13810) — 23 comments · 0 reactions · closed
- **Pull Request** [Bound degraded-team relocation retries across pipeline transitions](https://github.com/apple/foundationdb/pull/13838) — 18 comments · 0 reactions · open
- **Pull Request** [Backport four bug fixes from main to release-7.4 (#12318, #12643, #12750, #12755)](https://github.com/apple/foundationdb/pull/13871) — 19 comments · 0 reactions · closed
- **Pull Request** [Replace explicit-self helpers with member coroutines](https://github.com/apple/foundationdb/pull/13891) — 18 comments · 0 reactions · closed
- **Pull Request** [\[release-7.4\] packaging: remove python-2.7 package from macOS pkg build](https://github.com/apple/foundationdb/pull/13890) — 16 comments · 0 reactions · closed
- **Pull Request** [cherry-pick: tests: keep storage wiggle disabled for minimum throughput](https://github.com/apple/foundationdb/pull/13892) — 17 comments · 0 reactions · closed
- **Pull Request** [bindings/python: update pycodestyle test](https://github.com/apple/foundationdb/pull/13898) — 21 comments · 0 reactions · closed
- **Pull Request** [Exercise duplicate snapshot requests on the current binary](https://github.com/apple/foundationdb/pull/13879) — 14 comments · 0 reactions · open
- **Pull Request** [fdbclient: after unlink of per-thread library copy, symlink to original](https://github.com/apple/foundationdb/pull/13903) — 18 comments · 0 reactions · open
- **Pull Request** [add new commit statistics metrics](https://github.com/apple/foundationdb/pull/13416) — 16 comments · 0 reactions · open
- **Pull Request** [always increment finishedQueries counter if incrementing allQueries](https://github.com/apple/foundationdb/pull/13786) — 16 comments · 0 reactions · open
- **Pull Request** [ci: codebuild-cleanup action: consolidate graphql queries](https://github.com/apple/foundationdb/pull/13724) — 15 comments · 0 reactions · closed
- **Pull Request** [Backport call-site aware memory tracking to release-7.4 (PR #13344)](https://github.com/apple/foundationdb/pull/13818) — 14 comments · 0 reactions · open
- **Pull Request** [packaging/docker: update to kubectl 1.31.14 for YCSB image](https://github.com/apple/foundationdb/pull/13888) — 11 comments · 0 reactions · closed
- **Pull Request** [Make DD relocation retry observations resilient to delay jitter](https://github.com/apple/foundationdb/pull/13897) — 10 comments · 0 reactions · open

### [TigerBeetle](https://github.com/tigerbeetle/tigerbeetle)

- **Issue** [How to use from rust?](https://github.com/tigerbeetle/tigerbeetle/issues/3443) — 4 comments · 2 reactions · open
- **Issue** [~1s commit stall once per 960 ops (checkpoint interval) under small batches on a grown data file; reproducible with tigerbeetle benchmark on stock 0.17.9](https://github.com/tigerbeetle/tigerbeetle/issues/3915) — 0 comments · 0 reactions · open

### [etcd Raft](https://github.com/etcd-io/raft)

- **Pull Request** [build(deps): bump google.golang.org/protobuf from 1.36.11 to 1.36.12](https://github.com/etcd-io/raft/pull/495) — 6 comments · 0 reactions · closed
- **Pull Request** [build(deps): bump github.com/stretchr/testify from 1.11.1 to 1.12.0](https://github.com/etcd-io/raft/pull/496) — 4 comments · 0 reactions · closed
- **Pull Request** [build(deps): bump github/codeql-action/init from 4.36.2 to 4.37.7](https://github.com/etcd-io/raft/pull/497) — 4 comments · 0 reactions · open
- **Pull Request** [build(deps): bump github/codeql-action/autobuild from 4.36.2 to 4.37.7](https://github.com/etcd-io/raft/pull/498) — 4 comments · 0 reactions · open
- **Pull Request** [build(deps): bump github/codeql-action/analyze from 4.36.2 to 4.37.7](https://github.com/etcd-io/raft/pull/499) — 4 comments · 0 reactions · open
- **Pull Request** [bump go 1.26.6](https://github.com/etcd-io/raft/pull/492) — 1 comments · 0 reactions · closed
- **Pull Request** [\[release-3.7\] bump go 1.26.6](https://github.com/etcd-io/raft/pull/493) — 1 comments · 0 reactions · closed
- **Pull Request** [\[release-3.6\] bump go 1.25.13](https://github.com/etcd-io/raft/pull/494) — 1 comments · 0 reactions · closed
- **Pull Request** [build(deps): bump golang.org/x/net from 0.50.0 to 0.55.0 in /tools/mod](https://github.com/etcd-io/raft/pull/461) — 2 comments · 0 reactions · open
- **Pull Request** [build(deps): bump actions/checkout from 7.0.0 to 7.0.1](https://github.com/etcd-io/raft/pull/481) — 3 comments · 0 reactions · closed

### [raft-rs](https://github.com/tikv/raft-rs)

No new or materially changed signals.

### [Jepsen](https://github.com/jepsen-io/jepsen)

No new or materially changed signals.
