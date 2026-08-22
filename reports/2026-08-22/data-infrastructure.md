# Data / Messaging / Storage Infrastructure — 2026-08-22

> Factual GitHub evidence collected by Contribution Compass. No LLM analysis is performed.

## Contribution Leads

### [Malformed ORC/Avro files reach `LOGICAL_ERROR` through the exception formatter (aborts on debug builds, silently, from schema inference)](https://github.com/ClickHouse/ClickHouse/issues/115412)

- Project: `ClickHouse/ClickHouse`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [`SELECT count()` never terminates on corrupted Avro / MsgPack / ProtobufList files — the `optimize_count_from_files` fast path counts rows without requiring forward progress](https://github.com/ClickHouse/ClickHouse/issues/115437)

- Project: `ClickHouse/ClickHouse`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

## Important Updates

### [NATS Server](https://github.com/nats-io/nats-server)

- **Pull Request** [Update to Go 1.27.0/1.26.7](https://github.com/nats-io/nats-server/pull/8482) — 1 comments · 2 reactions · open
- **Pull Request** [(2.15) \[FIXED\] prepareForWALReplay failed to Truncate deleted sequence](https://github.com/nats-io/nats-server/pull/8493) — 4 comments · 1 reactions · open
- **Pull Request** [(2.15) \[FIXED\] Preserve FirstSeq during WAL replay](https://github.com/nats-io/nats-server/pull/8490) — 2 comments · 1 reactions · closed
- **Pull Request** [Various de-flakes and fixes](https://github.com/nats-io/nats-server/pull/8492) — 3 comments · 1 reactions · closed
- **Pull Request** [(2.15) NRG: Don't campaign as managed node outside the peer set](https://github.com/nats-io/nats-server/pull/8489) — 1 comments · 1 reactions · closed
- **Pull Request** [\[FIXED\] Rejected consumer create destroys existing consumer state](https://github.com/nats-io/nats-server/pull/8491) — 3 comments · 0 reactions · closed

### [Redpanda](https://github.com/redpanda-data/redpanda)

- **Release** [v26.2.2](https://github.com/redpanda-data/redpanda/releases/tag/v26.2.2) — 
- **Pull Request** [tests: add a CDT smoke suite covering the ducktape image dependencies](https://github.com/redpanda-data/redpanda/pull/31612) — 4 comments · 0 reactions · closed
- **Pull Request** [tests: make the llvm-symbolizer shim a static binary](https://github.com/redpanda-data/redpanda/pull/31578) — 3 comments · 0 reactions · closed
- **Pull Request** [rptest/consumer_group_test: widen api-version probe timeout in large group test](https://github.com/redpanda-data/redpanda/pull/31603) — 1 comments · 0 reactions · open

### [ClickHouse](https://github.com/ClickHouse/ClickHouse)

- **Pull Request** [Optimization of `GROUP BY` in the presence of `ORDER BY` and `LIMIT`](https://github.com/ClickHouse/ClickHouse/pull/96630) — 16 comments · 8 reactions · open
- **Pull Request** [Switch the default compression to ZSTD(3) for table data and network](https://github.com/ClickHouse/ClickHouse/pull/108786) — 74 comments · 1 reactions · open
- **Pull Request** [Disable read-in-order when primary key selectivity is poor](https://github.com/ClickHouse/ClickHouse/pull/100377) — 42 comments · 0 reactions · open
- **Pull Request** [Avoid copying data for the NONE compression codec when writing](https://github.com/ClickHouse/ClickHouse/pull/108096) — 41 comments · 0 reactions · open
- **Pull Request** [Add `GradualResizeProcessor` to limit effective parallelism for GROUP BY on small data volumes](https://github.com/ClickHouse/ClickHouse/pull/99495) — 36 comments · 0 reactions · open
- **Pull Request** [Add groupBloomFilter aggregate function and bloomFilterContains scalar function](https://github.com/ClickHouse/ClickHouse/pull/101841) — 6 comments · 13 reactions · open
- **Pull Request** [Statically linked binary](https://github.com/ClickHouse/ClickHouse/pull/109239) — 5 comments · 7 reactions · open
- **Release** [Release v25.8.32.4-lts](https://github.com/ClickHouse/ClickHouse/releases/tag/v25.8.32.4-lts) — 
- **Release** [Release v26.7.5.10-stable](https://github.com/ClickHouse/ClickHouse/releases/tag/v26.7.5.10-stable) — 
- **Pull Request** [Transform JOIN hash table payload to row major](https://github.com/ClickHouse/ClickHouse/pull/104884) — 14 comments · 4 reactions · open
- **Pull Request** [Push down volume-reducing functions in query plan](https://github.com/ClickHouse/ClickHouse/pull/106199) — 19 comments · 2 reactions · closed
- **Pull Request** [Added Parquet Shredded VARIANT Support to ParquetReaderv3](https://github.com/ClickHouse/ClickHouse/pull/102499) — 37 comments · 3 reactions · open
- **Pull Request** [Avoid per-row heap allocations in blocked Myers edit distance](https://github.com/ClickHouse/ClickHouse/pull/108185) — 17 comments · 1 reactions · closed
- **Pull Request** [Add Rewrite rules](https://github.com/ClickHouse/ClickHouse/pull/88234) — 64 comments · 1 reactions · open
- **Pull Request** [Skip writing all-default columns during MergeTree INSERT](https://github.com/ClickHouse/ClickHouse/pull/98472) — 33 comments · 3 reactions · open
- **Pull Request** [Add INSERT ... RETURNING (non-atomic, user-supplied SELECT)](https://github.com/ClickHouse/ClickHouse/pull/105714) — 34 comments · 2 reactions · open
- **Pull Request** [Real cache size](https://github.com/ClickHouse/ClickHouse/pull/79490) — 38 comments · 1 reactions · open
- **Pull Request** [Add leader election for non-replicated MergeTree on shared storage](https://github.com/ClickHouse/ClickHouse/pull/101039) — 88 comments · 0 reactions · open
- **Pull Request** [Declarative function signatures, continuation of #3775](https://github.com/ClickHouse/ClickHouse/pull/104948) — 44 comments · 0 reactions · open
- **Pull Request** [Add server setting `additional_memory_tracking_per_thread`](https://github.com/ClickHouse/ClickHouse/pull/104965) — 40 comments · 0 reactions · open
- **Pull Request** [Fix sort order violation for TTL GROUP BY with SET on a sorting key column](https://github.com/ClickHouse/ClickHouse/pull/108550) — 50 comments · 0 reactions · open
- **Pull Request** [Reserve memory for merges up front](https://github.com/ClickHouse/ClickHouse/pull/109433) — 73 comments · 0 reactions · open
- **Pull Request** [Compare stored table definition expressions by AST instead of formatted text](https://github.com/ClickHouse/ClickHouse/pull/110833) — 85 comments · 0 reactions · open
- **Pull Request** [MaterializedPostgreSQL: coordinated Replicated/Shared nested tables for HA](https://github.com/ClickHouse/ClickHouse/pull/110886) — 50 comments · 0 reactions · open
- **Pull Request** [Docs: internationalize master](https://github.com/ClickHouse/ClickHouse/pull/115641) — 51 comments · 0 reactions · open
- **Pull Request** [Add early short-circuit evaluation for OR/AND in the analyzer to prevent unnecessary scalar subquery execution](https://github.com/ClickHouse/ClickHouse/pull/83505) — 16 comments · 0 reactions · closed
- **Pull Request** [Fix JSON/XML format statistics race condition with parallel replicas](https://github.com/ClickHouse/ClickHouse/pull/96978) — 56 comments · 0 reactions · open
- **Pull Request** [Make SQL SECURITY views an optimization barrier](https://github.com/ClickHouse/ClickHouse/pull/112847) — 14 comments · 0 reactions · open
- **Pull Request** [Optimize aggregations of LowCardinality of 128 and 256 bit integers](https://github.com/ClickHouse/ClickHouse/pull/114982) — 6 comments · 2 reactions · open
- **Pull Request** [Validate IN tuple/subquery column count mismatch in analyzer](https://github.com/ClickHouse/ClickHouse/pull/97540) — 38 comments · 0 reactions · open

### [Dragonfly](https://github.com/dragonflydb/dragonfly)

- **Issue** [test_replicaof_reject_on_load](https://github.com/dragonflydb/dragonfly/issues/5662) — 44 comments · 0 reactions · open
- **Pull Request** [feat(server): Implement COMMAND LIST (#5466)](https://github.com/dragonflydb/dragonfly/pull/7385) — 11 comments · 0 reactions · open
- **Pull Request** [fix(generic): avoid data loss on RENAME when destination write fails](https://github.com/dragonflydb/dragonfly/pull/8053) — 11 comments · 0 reactions · open
- **Pull Request** [fix(server): Skip forced snapshot serialization for redundant writes with second replica, add support for expire](https://github.com/dragonflydb/dragonfly/pull/8112) — 7 comments · 0 reactions · open
- **Issue** [`test_rss_oom_ratio` failed](https://github.com/dragonflydb/dragonfly/issues/7690) — 1 comments · 0 reactions · closed
- **Pull Request** [feat(server): throttle defrag task CPU duty cycle](https://github.com/dragonflydb/dragonfly/pull/8115) — 4 comments · 0 reactions · open
- **Pull Request** [fix(acl): script context acl and enable flaky tests](https://github.com/dragonflydb/dragonfly/pull/8116) — 4 comments · 0 reactions · open
- **Pull Request** [feat(tiering): Account for tiered storage utility RAM](https://github.com/dragonflydb/dragonfly/pull/8126) — 5 comments · 0 reactions · open
- **Pull Request** [fix(tests): use FLUSHALL SYNC in test_rss_oom_ratio to stop RSS-drop …](https://github.com/dragonflydb/dragonfly/pull/8135) — 6 comments · 0 reactions · closed
- **Pull Request** [fix(server): Bound DeleteExpiredStep traversal with TraverseBySegment…](https://github.com/dragonflydb/dragonfly/pull/8129) — 4 comments · 0 reactions · open
- **Pull Request** [fix: validate COUNT in ZMPOP/BZMPOP/LMPOP/BLMPOP and fix large-count overflow](https://github.com/dragonflydb/dragonfly/pull/8130) — 4 comments · 0 reactions · closed
- **Pull Request** [fix(server): guard policy-based eviction against full-sync snapshot race](https://github.com/dragonflydb/dragonfly/pull/8131) — 4 comments · 0 reactions · open
- **Pull Request** [fix(server): run active expiry and wake for all namespaces in heartbeat](https://github.com/dragonflydb/dragonfly/pull/8132) — 4 comments · 0 reactions · open
- **Pull Request** [refactor: improve OAHTable::GetRandomMember](https://github.com/dragonflydb/dragonfly/pull/8134) — 4 comments · 0 reactions · open
- **Pull Request** [chore: disable test_debug_traffic_v2_parse_in_proactor_does_not_preempt](https://github.com/dragonflydb/dragonfly/pull/8133) — 3 comments · 0 reactions · closed
