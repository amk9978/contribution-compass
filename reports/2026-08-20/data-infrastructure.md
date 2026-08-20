# Data / Messaging / Storage Infrastructure — 2026-08-20

> Factual GitHub evidence collected by Contribution Compass. No LLM analysis is performed.

## Contribution Leads

### [`DESCRIBE` and `SHOW CREATE TABLE` report stale column types for TO-target materialized views after upstream `ALTER MODIFY COLUMN`](https://github.com/ClickHouse/ClickHouse/issues/106919)

- Project: `ClickHouse/ClickHouse`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

### [allow_non_metadata_alters=0 does not block many mutation-triggering ALTERs and its documentation is unclear](https://github.com/ClickHouse/ClickHouse/issues/115058)

- Project: `ClickHouse/ClickHouse`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

## Important Updates

### [NATS Server](https://github.com/nats-io/nats-server)

- **Pull Request** [(2.15) Stream backup/restore v2](https://github.com/nats-io/nats-server/pull/7882) — 20 comments · 1 reactions · closed
- **Pull Request** [(2.15) Raft proposal fast path](https://github.com/nats-io/nats-server/pull/8445) — 10 comments · 1 reactions · open
- **Pull Request** [(2.15) NRG: Relax SyncAlways for replicated streams](https://github.com/nats-io/nats-server/pull/8447) — 10 comments · 1 reactions · open
- **Issue** [CRITICAL JetStream atomic batch publish leaves per-batch staging directories under <stream>/batches after commit](https://github.com/nats-io/nats-server/issues/8472) — 4 comments · 0 reactions · closed
- **Pull Request** [\[FIXED\] Inline block compaction ignores SyncAlways](https://github.com/nats-io/nats-server/pull/8475) — 2 comments · 1 reactions · closed
- **Pull Request** [(2.15) \[IMPROVED\] Finalize desired meta reconciliation](https://github.com/nats-io/nats-server/pull/8476) — 3 comments · 1 reactions · closed
- **Issue** [Leaf interest arriving over a route does not skip when isolate_leafnode_interest is true](https://github.com/nats-io/nats-server/issues/8481) — 0 comments · 0 reactions · open
- **Issue** [Tiered JetStream consumer limits are not additive](https://github.com/nats-io/nats-server/issues/8483) — 0 comments · 0 reactions · open
- **Issue** [JetStream memory footprint grows with subject & dedup cardinailty despite storageType=File](https://github.com/nats-io/nats-server/issues/8485) — 0 comments · 0 reactions · open
- **Pull Request** [(2.15) NRG: Maximize batch size](https://github.com/nats-io/nats-server/pull/8477) — 0 comments · 1 reactions · open
- **Pull Request** [(2.15) \[FIXED\] Remove leftover atomic-batch staging dirs after cleanup](https://github.com/nats-io/nats-server/pull/8474) — 3 comments · 0 reactions · closed
- **Pull Request** [De-flake TestJetStreamClusterStreamResetOnExpirationDuringPeerDownAndRestartWithLeaderChange](https://github.com/nats-io/nats-server/pull/8480) — 0 comments · 1 reactions · closed
- **Pull Request** [Update to Go 1.26.7/1.25.14](https://github.com/nats-io/nats-server/pull/8482) — 1 comments · 1 reactions · open
- **Pull Request** [Fix cross-tier JetStream consumer counting for limits](https://github.com/nats-io/nats-server/pull/8484) — 0 comments · 1 reactions · open
- **Pull Request** [\[FIXED\] Prevent duplicate JetStream ingestion subscriptions during concurrent stream updates](https://github.com/nats-io/nats-server/pull/8479) — 0 comments · 0 reactions · open
- **Pull Request** [\[IMPROVED\] Direct get performance and stream lock decoupling](https://github.com/nats-io/nats-server/pull/8486) — 1 comments · 0 reactions · open

### [Redpanda](https://github.com/redpanda-data/redpanda)

- **Release** [v25.3.17](https://github.com/redpanda-data/redpanda/releases/tag/v25.3.17) — 
- **Release** [v26.1.17](https://github.com/redpanda-data/redpanda/releases/tag/v26.1.17) — 
- **Pull Request** [ts-ct-migration: partition_mode substrate \[PR 0\]](https://github.com/redpanda-data/redpanda/pull/30977) — 22 comments · 0 reactions · open
- **Pull Request** [\[CORE-16604\] cluster_link: incremental Schema Registry sync by tailing _schemas](https://github.com/redpanda-data/redpanda/pull/31366) — 14 comments · 0 reactions · open
- **Issue** [\[v25.3.x\] \[CORE-16972\] pandaproxy/rest: return table identity for pre-translation iceberg topics](https://github.com/redpanda-data/redpanda/issues/31618) — 1 comments · 0 reactions · closed
- **Pull Request** [\[CORE-16908\] cluster_link: incremental Schema Registry sync over the HTTP API](https://github.com/redpanda-data/redpanda/pull/31376) — 8 comments · 0 reactions · open
- **Pull Request** [\[CORE-16998, CORE-17000, CORE-17001\] - Consumer Groups (Classic): Fix some bugs where the offset map could diverge from the log](https://github.com/redpanda-data/redpanda/pull/31483) — 8 comments · 0 reactions · open
- **Pull Request** [\[CORE-16806\] - KIP-848: assignor interface and the homogeneous uniform assignor](https://github.com/redpanda-data/redpanda/pull/31579) — 9 comments · 0 reactions · open
- **Pull Request** [cloud_topics: fast partition movement for tiered-storage v2](https://github.com/redpanda-data/redpanda/pull/31589) — 8 comments · 0 reactions · closed
- **Pull Request** [kafka: add fetch_busy_latency_us metric](https://github.com/redpanda-data/redpanda/pull/30858) — 6 comments · 0 reactions · open
- **Pull Request** [serde: write fixed envelopes contiguously](https://github.com/redpanda-data/redpanda/pull/31230) — 7 comments · 0 reactions · open
- **Pull Request** [\[CORE-16804\] - KIP-848: deterministic subscription-metadata hash](https://github.com/redpanda-data/redpanda/pull/31499) — 7 comments · 0 reactions · closed
- **Pull Request** [rpc/transport: retain memory semaphore units in queued request entry](https://github.com/redpanda-data/redpanda/pull/31594) — 6 comments · 0 reactions · open
- **Pull Request** [ts-ct-migration: STM coexistence \[PR 2\]](https://github.com/redpanda-data/redpanda/pull/30887) — 4 comments · 0 reactions · open
- **Pull Request** [bazel/seastar: enable task queue shuffling in debug builds](https://github.com/redpanda-data/redpanda/pull/31139) — 4 comments · 0 reactions · open
- **Pull Request** [serde: Some read perf improvements](https://github.com/redpanda-data/redpanda/pull/31211) — 4 comments · 0 reactions · closed
- **Pull Request** [\[CORE-8759\] storage: kill broker process if log_reader detects a corrupt segment](https://github.com/redpanda-data/redpanda/pull/31543) — 4 comments · 0 reactions · closed
- **Pull Request** [kafka/server/tests: deflake quota_manager_test under load](https://github.com/redpanda-data/redpanda/pull/31599) — 5 comments · 0 reactions · closed
- **Pull Request** [Fix unbounded s3_fifo growth](https://github.com/redpanda-data/redpanda/pull/31609) — 4 comments · 0 reactions · closed
- **Pull Request** [\[CORE-17063\] - security/audit: report misconfigured auth from client init](https://github.com/redpanda-data/redpanda/pull/31629) — 8 comments · 0 reactions · closed
- **Pull Request** [json/tests: add fuzz testing for the parser](https://github.com/redpanda-data/redpanda/pull/26671) — 7 comments · 0 reactions · closed
- **Pull Request** [\[v26.2.x\] `ct`: seek timestamp index to predecessor entry](https://github.com/redpanda-data/redpanda/pull/31417) — 2 comments · 0 reactions · closed
- **Pull Request** [iceberg: Reduce coroutine yields and allocs in conversion hot path](https://github.com/redpanda-data/redpanda/pull/31541) — 2 comments · 0 reactions · open
- **Pull Request** [rpk: add stretch cluster grafana dashboard as --dashboard operations-stretch](https://github.com/redpanda-data/redpanda/pull/31573) — 3 comments · 0 reactions · closed
- **Pull Request** [\[v26.2.x\] \[CORE-15822\] security/audit: make audit initialization controller-leader independent](https://github.com/redpanda-data/redpanda/pull/31586) — 3 comments · 0 reactions · closed
- **Pull Request** [\[CORE-16980\] iceberg/avro: handle UUID logical type for fixed(16) columns](https://github.com/redpanda-data/redpanda/pull/31601) — 2 comments · 0 reactions · open
- **Pull Request** [bazel: fetch pip wheels via the Bazel downloader](https://github.com/redpanda-data/redpanda/pull/31623) — 2 comments · 0 reactions · closed
- **Pull Request** [\[v26.2.x\] \[UX-1375\] rpk shadow: support role sync for Redpanda Cloud links](https://github.com/redpanda-data/redpanda/pull/31625) — 2 comments · 0 reactions · closed
- **Pull Request** [kafka/server: fix quota_manager gc use-after-free at shutdown](https://github.com/redpanda-data/redpanda/pull/31598) — 0 comments · 0 reactions · open
- **Pull Request** [\[v26.2.x\] kafka/server: reject client-produced control batches](https://github.com/redpanda-data/redpanda/pull/31605) — 1 comments · 0 reactions · closed

### [ClickHouse](https://github.com/ClickHouse/ClickHouse)

- **Issue** [Allow interactive queries finish in the background](https://github.com/ClickHouse/ClickHouse/issues/49683) — 15 comments · 45 reactions · closed
- **Pull Request** [Columns Cache](https://github.com/ClickHouse/ClickHouse/pull/96844) — 78 comments · 5 reactions · open
- **Pull Request** [Fix count distinct rewrite safety](https://github.com/ClickHouse/ClickHouse/pull/81944) — 38 comments · 4 reactions · open
- **Pull Request** [Optimization of `GROUP BY` in the presence of `ORDER BY` and `LIMIT`](https://github.com/ClickHouse/ClickHouse/pull/96630) — 15 comments · 8 reactions · open
- **Pull Request** [Parallelize read-in-order from a single part with PrefetchingConcatProcessor](https://github.com/ClickHouse/ClickHouse/pull/100391) — 44 comments · 1 reactions · open
- **Pull Request** [Switch the default compression to ZSTD(3) for table data and network](https://github.com/ClickHouse/ClickHouse/pull/108786) — 72 comments · 1 reactions · open
- **Pull Request** [Push join key filters into MergeTree index during recursive CTE evaluation](https://github.com/ClickHouse/ClickHouse/pull/97254) — 81 comments · 1 reactions · open
- **Pull Request** [Disable read-in-order when primary key selectivity is poor](https://github.com/ClickHouse/ClickHouse/pull/100377) — 41 comments · 0 reactions · open
- **Pull Request** [Add optimize_row_order_if_no_order_by (reopen #103919)](https://github.com/ClickHouse/ClickHouse/pull/104591) — 45 comments · 0 reactions · open
- **Pull Request** [Minmax indices by default](https://github.com/ClickHouse/ClickHouse/pull/76867) — 94 comments · 0 reactions · open
- **Pull Request** [Avoid copying data for the NONE compression codec when writing](https://github.com/ClickHouse/ClickHouse/pull/108096) — 38 comments · 0 reactions · open
- **Pull Request** [Improve the performance of `MODIFY TTL`](https://github.com/ClickHouse/ClickHouse/pull/63383) — 34 comments · 1 reactions · open
- **Pull Request** [Add `GradualResizeProcessor` to limit effective parallelism for GROUP BY on small data volumes](https://github.com/ClickHouse/ClickHouse/pull/99495) — 35 comments · 0 reactions · open
- **Pull Request** [Async insert parallel parsing](https://github.com/ClickHouse/ClickHouse/pull/79509) — 25 comments · 2 reactions · open
- **Release** [Release v26.7.4.58-stable](https://github.com/ClickHouse/ClickHouse/releases/tag/v26.7.4.58-stable) — 
- **Release** [Release v26.5.7.64-stable](https://github.com/ClickHouse/ClickHouse/releases/tag/v26.5.7.64-stable) — 
- **Release** [Release v26.6.3.62-stable](https://github.com/ClickHouse/ClickHouse/releases/tag/v26.6.3.62-stable) — 
- **Pull Request** [Predistinct step will use bf as first pass filter before hashset](https://github.com/ClickHouse/ClickHouse/pull/77728) — 22 comments · 2 reactions · open
- **Pull Request** [Add spatial_bbox skip index for MergeTree geometry columns](https://github.com/ClickHouse/ClickHouse/pull/104437) — 25 comments · 1 reactions · open
- **Pull Request** [Support column matcher expansion for default value expressions and index expressions](https://github.com/ClickHouse/ClickHouse/pull/105045) — 51 comments · 3 reactions · open
- **Pull Request** [Statically linked binary](https://github.com/ClickHouse/ClickHouse/pull/109239) — 4 comments · 7 reactions · open
- **Pull Request** [Transform JOIN hash table payload to row major](https://github.com/ClickHouse/ClickHouse/pull/104884) — 14 comments · 4 reactions · open
- **Pull Request** [Push down volume-reducing functions in query plan](https://github.com/ClickHouse/ClickHouse/pull/106199) — 16 comments · 2 reactions · open
- **Pull Request** [Randomize tests with DETACH/ATTACH table before query execution](https://github.com/ClickHouse/ClickHouse/pull/96130) — 91 comments · 2 reactions · open
- **Pull Request** [Fix ALTER TABLE MODIFY TTL with DateTime causing data loss on 32-bit overflow](https://github.com/ClickHouse/ClickHouse/pull/101793) — 23 comments · 0 reactions · open
- **Pull Request** [Added Parquet Shredded VARIANT Support to ParquetReaderv3](https://github.com/ClickHouse/ClickHouse/pull/102499) — 35 comments · 3 reactions · open
- **Pull Request** [Push subcolumn reads into subqueries](https://github.com/ClickHouse/ClickHouse/pull/112688) — 19 comments · 1 reactions · open
- **Pull Request** [Make `if` with constant branches return `LowCardinality`](https://github.com/ClickHouse/ClickHouse/pull/80263) — 38 comments · 2 reactions · open
- **Pull Request** [Add SQLite input/output format](https://github.com/ClickHouse/ClickHouse/pull/104510) — 59 comments · 1 reactions · open
- **Pull Request** [Use `HashSet` for aggregations without aggregates](https://github.com/ClickHouse/ClickHouse/pull/108862) — 11 comments · 2 reactions · closed

### [Dragonfly](https://github.com/dragonflydb/dragonfly)

- **Issue** [crash: main_service.cc:1669\] Check failed: rb->RepliesRecorded() > replies_recorded_ (0 vs. 0) CF.ADD](https://github.com/dragonflydb/dragonfly/issues/8102) — 9 comments · 0 reactions · closed
- **Issue** [test_slot_migration_oom_replica_rollback](https://github.com/dragonflydb/dragonfly/issues/8106) — 5 comments · 0 reactions · open
- **Pull Request** [fix(facade): log V2 traffic before dispatch](https://github.com/dragonflydb/dragonfly/pull/8096) — 13 comments · 0 reactions · open
- **Issue** [BF.LOADCHUNK of a header-only chunk produces an unloadable snapshot (data loss on restart) and aborts on COPY at generic_family.cc:435](https://github.com/dragonflydb/dragonfly/issues/8104) — 0 comments · 0 reactions · closed
- **Pull Request** [fix: stop SCRIPT FLUSH from deadlocking against a borrowed interpreter](https://github.com/dragonflydb/dragonfly/pull/8110) — 9 comments · 0 reactions · open
- **Pull Request** [feat(server): make conn_use_incoming_cpu runtime mutable](https://github.com/dragonflydb/dragonfly/pull/8095) — 6 comments · 0 reactions · open
- **Pull Request** [fix(tiering): Use TraverseBySegmentOrder and export more metrics/configs](https://github.com/dragonflydb/dragonfly/pull/8077) — 4 comments · 0 reactions · open
- **Pull Request** [server: Add warning to defragment commands about time based CPU use](https://github.com/dragonflydb/dragonfly/pull/8107) — 4 comments · 0 reactions · closed
- **Pull Request** [fix: release the global shard lock in the mode it was taken](https://github.com/dragonflydb/dragonfly/pull/8111) — 5 comments · 0 reactions · closed
- **Pull Request** [feat(tiering): Skip forced snapshot serialization for redundant writes](https://github.com/dragonflydb/dragonfly/pull/8112) — 1 comments · 0 reactions · open
- **Pull Request** [fix(bloom): reject SBF filters the rdb loader would refuse to load back](https://github.com/dragonflydb/dragonfly/pull/8113) — 4 comments · 0 reactions · closed
- **Pull Request** [fix: handle bad_alloc in squashed MULTI callback and surface hop status](https://github.com/dragonflydb/dragonfly/pull/8114) — 4 comments · 0 reactions · closed
- **Pull Request** [feat(server): throttle defrag task CPU duty cycle](https://github.com/dragonflydb/dragonfly/pull/8115) — 4 comments · 0 reactions · open
- **Pull Request** [fix(acl): script context acl and enable flaky tests](https://github.com/dragonflydb/dragonfly/pull/8116) — 4 comments · 0 reactions · open
- **Pull Request** [fix: test_slot_migration_oom_replica_rollback](https://github.com/dragonflydb/dragonfly/pull/8117) — 4 comments · 0 reactions · open
- **Pull Request** [chore: split python cluster tests](https://github.com/dragonflydb/dragonfly/pull/8118) — 4 comments · 0 reactions · open
