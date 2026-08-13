# Data / Messaging / Storage Infrastructure — 2026-08-13

> Factual GitHub evidence collected by Contribution Compass. No LLM analysis is performed.

## Contribution Leads

No evidence-qualified contribution leads changed in this collection.
## Important Updates

### [NATS Server](https://github.com/nats-io/nats-server)

- **Pull Request** [(2.15) \[ADDED\] Peer evacuation and reconciliation of assignments](https://github.com/nats-io/nats-server/pull/8443) — 3 comments · 0 reactions · open
- **Pull Request** [(2.15) \[FIXED\] Evict peer-removed peers for group below quorum](https://github.com/nats-io/nats-server/pull/8452) — 3 comments · 0 reactions · open
- **Pull Request** [(2.15) \[FIXED\] Migration added offline peers & removed peers before catchup](https://github.com/nats-io/nats-server/pull/8460) — 3 comments · 0 reactions · open

### [Redpanda](https://github.com/redpanda-data/redpanda)

- **Pull Request** [bazel: bump the toolchain sysroot to Ubuntu 24.04](https://github.com/redpanda-data/redpanda/pull/31560) — 11 comments · 0 reactions · open
- **Pull Request** [rpk: fix grammar and wording defects in help text](https://github.com/redpanda-data/redpanda/pull/31521) — 7 comments · 0 reactions · closed
- **Pull Request** [rptest: add OOM crash self-test; allow-list memory diagnostics](https://github.com/redpanda-data/redpanda/pull/31365) — 4 comments · 0 reactions · open
- **Pull Request** [\[v26.1.x\] bazel: define an empty ci-remote-cache config](https://github.com/redpanda-data/redpanda/pull/31540) — 3 comments · 0 reactions · closed
- **Pull Request** [\[CORE-12930\] - Storage: Some observability improvements for unrecoverable segments](https://github.com/redpanda-data/redpanda/pull/31544) — 2 comments · 0 reactions · open
- **Pull Request** [\[v26.1.x\] rpk/connect: don't cap version segments at two digits in VersionFromString](https://github.com/redpanda-data/redpanda/pull/31551) — 0 comments · 0 reactions · closed
- **Pull Request** [\[UX-1427\] chore: bump franz-go to 1.21.6](https://github.com/redpanda-data/redpanda/pull/31556) — 1 comments · 0 reactions · closed
- **Pull Request** [k/s/tests: deflake the offset_store producer lock test](https://github.com/redpanda-data/redpanda/pull/31566) — 0 comments · 0 reactions · closed
- **Pull Request** [\[v25.3.x\] storage: bump segment_concatenation_test timeout](https://github.com/redpanda-data/redpanda/pull/31569) — 1 comments · 0 reactions · closed
- **Pull Request** [\[v26.1.x\] storage: bump segment_concatenation_test timeout](https://github.com/redpanda-data/redpanda/pull/31571) — 1 comments · 0 reactions · closed
- **Pull Request** [rpk: add stretch cluster grafana dashboard behind --cluster-type flag](https://github.com/redpanda-data/redpanda/pull/31573) — 0 comments · 0 reactions · open

### [ClickHouse](https://github.com/ClickHouse/ClickHouse)

- **Pull Request** [Cascades cost-based optimizer for distributed query plans](https://github.com/ClickHouse/ClickHouse/pull/86353) — 7 comments · 21 reactions · open
- **Pull Request** [Improve the performance of `MODIFY TTL`](https://github.com/ClickHouse/ClickHouse/pull/63383) — 33 comments · 1 reactions · open
- **Pull Request** [Add `GradualResizeProcessor` to limit effective parallelism for GROUP BY on small data volumes](https://github.com/ClickHouse/ClickHouse/pull/99495) — 30 comments · 0 reactions · open
- **Pull Request** [In case of trivial views, push whole outer query to shards.](https://github.com/ClickHouse/ClickHouse/pull/101791) — 15 comments · 3 reactions · open
- **Pull Request** [Add a Chinese tokenizer (jieba) for the tokens function and text indexes](https://github.com/ClickHouse/ClickHouse/pull/89945) — 36 comments · 3 reactions · open
- **Pull Request** [WIP: Projection Index Text](https://github.com/ClickHouse/ClickHouse/pull/93114) — 25 comments · 7 reactions · open
- **Pull Request** [Randomize tests with DETACH/ATTACH table before query execution](https://github.com/ClickHouse/ClickHouse/pull/96130) — 91 comments · 2 reactions · open
- **Pull Request** [Add leader election for non-replicated MergeTree on shared storage](https://github.com/ClickHouse/ClickHouse/pull/101039) — 87 comments · 0 reactions · open
- **Pull Request** [Docs: internationalize master](https://github.com/ClickHouse/ClickHouse/pull/114466) — 47 comments · 0 reactions · open
- **Pull Request** [Feature: Enable overlay databases for server.](https://github.com/ClickHouse/ClickHouse/pull/86768) — 108 comments · 0 reactions · open
- **Pull Request** [Add spatial_bbox skip index for MergeTree geometry columns](https://github.com/ClickHouse/ClickHouse/pull/104437) — 9 comments · 1 reactions · open
- **Pull Request** [Detect when tables behind a query have changed](https://github.com/ClickHouse/ClickHouse/pull/108721) — 56 comments · 0 reactions · open
- **Pull Request** [Avoid scans for constant sort keys](https://github.com/ClickHouse/ClickHouse/pull/113899) — 13 comments · 0 reactions · closed
- **Issue** [Push dynamic TopN thresholds into MergeTree reads for ORDER BY ... LIMIT (2-3x on ClickBench Q24/Q26)](https://github.com/ClickHouse/ClickHouse/issues/114639) — 2 comments · 0 reactions · open
- **Pull Request** [Fix LazilyReadFromMergeTree optimization with ALIAS columns (#96452)](https://github.com/ClickHouse/ClickHouse/pull/96487) — 31 comments · 1 reactions · open
- **Pull Request** [Add `borrow_from_cache` object storage and `memory` metadata types](https://github.com/ClickHouse/ClickHouse/pull/100371) — 32 comments · 0 reactions · open
- **Pull Request** [Let read-in-order propagate through SpillingHashJoin](https://github.com/ClickHouse/ClickHouse/pull/111973) — 9 comments · 0 reactions · open
- **Pull Request** [Text index: add trivial count optimization](https://github.com/ClickHouse/ClickHouse/pull/111494) — 7 comments · 0 reactions · open
- **Pull Request** [Reject divergent same-named parts in parallel replicas coordinator](https://github.com/ClickHouse/ClickHouse/pull/105710) — 28 comments · 0 reactions · open
- **Pull Request** [Handle non-constant RHS for `IN`](https://github.com/ClickHouse/ClickHouse/pull/104993) — 27 comments · 0 reactions · closed
- **Pull Request** [Require a join subquery alias only when it removes a real ambiguity](https://github.com/ClickHouse/ClickHouse/pull/109368) — 26 comments · 0 reactions · open
- **Pull Request** [Use `pread` when `preadv2` with `RWF_NOWAIT` cannot be used, and recognize `EPERM` from it](https://github.com/ClickHouse/ClickHouse/pull/112945) — 26 comments · 0 reactions · open
- **Pull Request** [\[WIP\] Seal-gated reading: gate the probe side of a hash JOIN on the runtime filter and prune read ranges by it](https://github.com/ClickHouse/ClickHouse/pull/113512) — 3 comments · 1 reactions · open
- **Pull Request** [Optimize merges of the text index](https://github.com/ClickHouse/ClickHouse/pull/114525) — 3 comments · 0 reactions · open
- **Pull Request** [Speed up `IN (subquery)` set building by pre-deduplicating each `MergeTree` partition independently](https://github.com/ClickHouse/ClickHouse/pull/114645) — 3 comments · 0 reactions · open
- **Pull Request** [Redis-wire protocol](https://github.com/ClickHouse/ClickHouse/pull/80353) — 10 comments · 4 reactions · open
- **Pull Request** [Record TopK-filtered granules in the query condition cache](https://github.com/ClickHouse/ClickHouse/pull/114659) — 1 comments · 0 reactions · open
- **Pull Request** [Fix toTime key-expression type mismatch under use_legacy_to_time](https://github.com/ClickHouse/ClickHouse/pull/110958) — 22 comments · 0 reactions · open
- **Pull Request** [Add introspection TCP port](https://github.com/ClickHouse/ClickHouse/pull/110838) — 16 comments · 1 reactions · open
- **Pull Request** [Randomize parallel_replicas_min_number_of_rows_per_replica](https://github.com/ClickHouse/ClickHouse/pull/71028) — 24 comments · 0 reactions · open

### [Dragonfly](https://github.com/dragonflydb/dragonfly)

- **Pull Request** [fix(server): emit expired keyspace events for already-past expirations](https://github.com/dragonflydb/dragonfly/pull/8065) — 4 comments · 0 reactions · open
