# Data / Messaging / Storage Infrastructure — 2026-08-19

> Factual GitHub evidence collected by Contribution Compass. No LLM analysis is performed.

## Contribution Leads

No evidence-qualified contribution leads changed in this collection.
## Important Updates

### [NATS Server](https://github.com/nats-io/nats-server)

- **Pull Request** [(2.15) Stream backup/restore v2](https://github.com/nats-io/nats-server/pull/7882) — 20 comments · 1 reactions · open
- **Pull Request** [(2.15) Raft proposal fast path](https://github.com/nats-io/nats-server/pull/8445) — 10 comments · 1 reactions · open
- **Pull Request** [(2.15) NRG: Relax SyncAlways for replicated streams](https://github.com/nats-io/nats-server/pull/8447) — 10 comments · 1 reactions · open
- **Pull Request** [\[FIXED\] Inline block compaction ignores SyncAlways](https://github.com/nats-io/nats-server/pull/8475) — 2 comments · 1 reactions · open
- **Pull Request** [(2.15) \[IMPROVED\] Index stream sources to avoid backward scans](https://github.com/nats-io/nats-server/pull/8282) — 7 comments · 0 reactions · open
- **Pull Request** [\[ADDED\] Expose highest sourced seq in StreamSourceInfo](https://github.com/nats-io/nats-server/pull/8283) — 3 comments · 1 reactions · open
- **Pull Request** [(2.15) \[IMPROVED\] Finalize desired meta reconciliation](https://github.com/nats-io/nats-server/pull/8476) — 3 comments · 1 reactions · open
- **Pull Request** [\[FIXED\] Data race reading consumer config in stream consumer getters](https://github.com/nats-io/nats-server/pull/8478) — 0 comments · 1 reactions · open
- **Pull Request** [(2.15) NRG: Maximize batch size](https://github.com/nats-io/nats-server/pull/8477) — 0 comments · 0 reactions · open

### [Redpanda](https://github.com/redpanda-data/redpanda)

- **Pull Request** [ts-ct-migration: partition_mode substrate \[PR 0\]](https://github.com/redpanda-data/redpanda/pull/30977) — 20 comments · 0 reactions · open
- **Pull Request** [\[CORE-16604\] cluster_link: incremental Schema Registry sync by tailing _schemas](https://github.com/redpanda-data/redpanda/pull/31366) — 13 comments · 0 reactions · open
- **Issue** [rpk: Add RAID0 setup support](https://github.com/redpanda-data/redpanda/issues/16564) — 7 comments · 0 reactions · closed
- **Pull Request** [\[CORE-16908\] cluster_link: incremental Schema Registry sync over the HTTP API](https://github.com/redpanda-data/redpanda/pull/31376) — 8 comments · 0 reactions · open
- **Pull Request** [sr: fix broker abort when a request fails before its deferred authz check](https://github.com/redpanda-data/redpanda/pull/31559) — 9 comments · 0 reactions · closed
- **Pull Request** [\[CORE-16806\] - KIP-848: assignor interface and the homogeneous uniform assignor](https://github.com/redpanda-data/redpanda/pull/31579) — 8 comments · 0 reactions · open
- **Pull Request** [\[CORE-16998, CORE-17000, CORE-17001\] - Consumer Groups (Classic): Fix some bugs where the offset map could diverge from the log](https://github.com/redpanda-data/redpanda/pull/31483) — 6 comments · 0 reactions · open
- **Pull Request** [rpc/transport: retain memory semaphore units in queued request entry](https://github.com/redpanda-data/redpanda/pull/31594) — 6 comments · 0 reactions · open
- **Pull Request** [\[CORE-16972\] pandaproxy/rest: return table identity for pre-translation iceberg topics](https://github.com/redpanda-data/redpanda/pull/31600) — 6 comments · 0 reactions · closed
- **Issue** [\[v25.3.x\] \[CORE-16972\] pandaproxy/rest: return table identity for pre-translation iceberg topics](https://github.com/redpanda-data/redpanda/issues/31618) — 0 comments · 0 reactions · open
- **Issue** [Rust transform SDK discards the input record offset that the ABI provides (Go SDK exposes Record.Offset)](https://github.com/redpanda-data/redpanda/issues/31624) — 0 comments · 0 reactions · open
- **Pull Request** [\[CORE-14911\] Fix `_schemas` replay for a truncated log](https://github.com/redpanda-data/redpanda/pull/31602) — 5 comments · 0 reactions · open
- **Pull Request** [kafka: add fetch_busy_latency_us metric](https://github.com/redpanda-data/redpanda/pull/30858) — 6 comments · 0 reactions · open
- **Pull Request** [ts-ct-migration: STM coexistence \[PR 2\]](https://github.com/redpanda-data/redpanda/pull/30887) — 2 comments · 0 reactions · open
- **Pull Request** [serde: write fixed envelopes contiguously](https://github.com/redpanda-data/redpanda/pull/31230) — 7 comments · 0 reactions · open
- **Pull Request** [\[CORE-16804\] - KIP-848: deterministic subscription-metadata hash](https://github.com/redpanda-data/redpanda/pull/31499) — 3 comments · 0 reactions · open
- **Pull Request** [iceberg: Reduce coroutine yields and allocs in conversion hot path](https://github.com/redpanda-data/redpanda/pull/31541) — 2 comments · 0 reactions · open
- **Pull Request** [rpk: add stretch cluster grafana dashboard as --dashboard operations-stretch](https://github.com/redpanda-data/redpanda/pull/31573) — 2 comments · 0 reactions · closed
- **Pull Request** [Mitigate `offset_not_available` races on follower fetches](https://github.com/redpanda-data/redpanda/pull/31581) — 2 comments · 0 reactions · open
- **Pull Request** [\[CORE-16980\] iceberg/avro: handle UUID logical type for fixed(16) columns](https://github.com/redpanda-data/redpanda/pull/31601) — 2 comments · 0 reactions · open
- **Pull Request** [Fix unbounded s3_fifo growth](https://github.com/redpanda-data/redpanda/pull/31609) — 2 comments · 0 reactions · open
- **Pull Request** [\[v25.3.x\] iceberg: accept singular "source-id" when parsing sort fields](https://github.com/redpanda-data/redpanda/pull/30478) — 1 comments · 0 reactions · closed
- **Pull Request** [serde: Some read perf improvements](https://github.com/redpanda-data/redpanda/pull/31211) — 4 comments · 0 reactions · open
- **Pull Request** [\[v26.2.x\] iceberg: bring back in-manifest stats](https://github.com/redpanda-data/redpanda/pull/31496) — 1 comments · 0 reactions · closed
- **Pull Request** [datalake: Configure parquet writing using Iceberg table properties](https://github.com/redpanda-data/redpanda/pull/31515) — 1 comments · 0 reactions · open
- **Pull Request** [\[v26.1.x\] sr: fix broker abort when a request fails before its deferred authz check](https://github.com/redpanda-data/redpanda/pull/31591) — 1 comments · 0 reactions · closed
- **Pull Request** [gha: backport - push branches directly instead of via a bot fork](https://github.com/redpanda-data/redpanda/pull/31595) — 1 comments · 0 reactions · closed
- **Pull Request** [kafka/server/tests: deflake quota_manager_test under load](https://github.com/redpanda-data/redpanda/pull/31599) — 0 comments · 0 reactions · open
- **Pull Request** [rpk: bump twmb/avro to v1.8.0](https://github.com/redpanda-data/redpanda/pull/31604) — 1 comments · 0 reactions · closed
- **Pull Request** [\[v26.2.x\] kafka/server: reject client-produced control batches](https://github.com/redpanda-data/redpanda/pull/31605) — 1 comments · 0 reactions · closed

### [ClickHouse](https://github.com/ClickHouse/ClickHouse)

- **Pull Request** [Fix count distinct rewrite safety](https://github.com/ClickHouse/ClickHouse/pull/81944) — 38 comments · 4 reactions · open
- **Pull Request** [Optimization of `GROUP BY` in the presence of `ORDER BY` and `LIMIT`](https://github.com/ClickHouse/ClickHouse/pull/96630) — 14 comments · 8 reactions · open
- **Pull Request** [Parallelize read-in-order from a single part with PrefetchingConcatProcessor](https://github.com/ClickHouse/ClickHouse/pull/100391) — 44 comments · 1 reactions · open
- **Pull Request** [Switch the default compression to ZSTD(3) for table data and network](https://github.com/ClickHouse/ClickHouse/pull/108786) — 72 comments · 1 reactions · open
- **Pull Request** [Push join key filters into MergeTree index during recursive CTE evaluation](https://github.com/ClickHouse/ClickHouse/pull/97254) — 81 comments · 1 reactions · open
- **Pull Request** [Disable read-in-order when primary key selectivity is poor](https://github.com/ClickHouse/ClickHouse/pull/100377) — 40 comments · 0 reactions · open
- **Pull Request** [Parallel read in order with multiple parts](https://github.com/ClickHouse/ClickHouse/pull/100394) — 73 comments · 0 reactions · open
- **Pull Request** [Add optimize_row_order_if_no_order_by (reopen #103919)](https://github.com/ClickHouse/ClickHouse/pull/104591) — 45 comments · 0 reactions · open
- **Pull Request** [Minmax indices by default](https://github.com/ClickHouse/ClickHouse/pull/76867) — 91 comments · 0 reactions · open
- **Pull Request** [Avoid copying data for the NONE compression codec when writing](https://github.com/ClickHouse/ClickHouse/pull/108096) — 37 comments · 0 reactions · open
- **Pull Request** [Add `GradualResizeProcessor` to limit effective parallelism for GROUP BY on small data volumes](https://github.com/ClickHouse/ClickHouse/pull/99495) — 35 comments · 0 reactions · open
- **Release** [Release v26.3.19.3-lts](https://github.com/ClickHouse/ClickHouse/releases/tag/v26.3.19.3-lts) — 
- **Pull Request** [Predistinct step will use bf as first pass filter before hashset](https://github.com/ClickHouse/ClickHouse/pull/77728) — 22 comments · 2 reactions · open
- **Pull Request** [Push down volume-reducing functions in query plan](https://github.com/ClickHouse/ClickHouse/pull/106199) — 16 comments · 2 reactions · open
- **Pull Request** [Randomize tests with DETACH/ATTACH table before query execution](https://github.com/ClickHouse/ClickHouse/pull/96130) — 91 comments · 2 reactions · open
- **Pull Request** [Add spatial_bbox skip index for MergeTree geometry columns](https://github.com/ClickHouse/ClickHouse/pull/104437) — 18 comments · 1 reactions · open
- **Pull Request** [Make `arrayCount` return `UInt64` and rewrite `length(arrayFilter(...))`](https://github.com/ClickHouse/ClickHouse/pull/113023) — 23 comments · 0 reactions · open
- **Pull Request** [Make `if` with constant branches return `LowCardinality`](https://github.com/ClickHouse/ClickHouse/pull/80263) — 38 comments · 2 reactions · open
- **Pull Request** [Add Rewrite rules](https://github.com/ClickHouse/ClickHouse/pull/88234) — 63 comments · 1 reactions · open
- **Pull Request** [Read the smallest on-disk column when a query reads no columns](https://github.com/ClickHouse/ClickHouse/pull/107368) — 23 comments · 0 reactions · open
- **Pull Request** [Use `HashSet` for aggregations without aggregates](https://github.com/ClickHouse/ClickHouse/pull/108862) — 11 comments · 2 reactions · open
- **Pull Request** [Share the speculatively built IN set between the part tasks of a mutation](https://github.com/ClickHouse/ClickHouse/pull/112941) — 18 comments · 0 reactions · open
- **Pull Request** [LowCardinality merge optimization](https://github.com/ClickHouse/ClickHouse/pull/114870) — 6 comments · 3 reactions · open
- **Pull Request** [Add leader election for non-replicated MergeTree on shared storage](https://github.com/ClickHouse/ClickHouse/pull/101039) — 88 comments · 0 reactions · open
- **Pull Request** [Fix correlated subquery + GROUP BY ROLLUP under group_by_use_nulls](https://github.com/ClickHouse/ClickHouse/pull/104350) — 61 comments · 0 reactions · open
- **Pull Request** [Parallelize reads from a single Parquet file in StorageFile, again](https://github.com/ClickHouse/ClickHouse/pull/104431) — 77 comments · 0 reactions · open
- **Pull Request** [Declarative function signatures, continuation of #3775](https://github.com/ClickHouse/ClickHouse/pull/104948) — 44 comments · 0 reactions · open
- **Pull Request** [Add server setting `additional_memory_tracking_per_thread`](https://github.com/ClickHouse/ClickHouse/pull/104965) — 40 comments · 0 reactions · open
- **Pull Request** [Avoid per-row heap allocations in blocked Myers edit distance](https://github.com/ClickHouse/ClickHouse/pull/108185) — 16 comments · 1 reactions · open
- **Pull Request** [Fix sort order violation for TTL GROUP BY with SET on a sorting key column](https://github.com/ClickHouse/ClickHouse/pull/108550) — 43 comments · 0 reactions · open

### [Dragonfly](https://github.com/dragonflydb/dragonfly)

- **Issue** [test_replicaof_reject_on_load](https://github.com/dragonflydb/dragonfly/issues/5662) — 42 comments · 0 reactions · open
- **Issue** [crash: main_service.cc:1669\] Check failed: rb->RepliesRecorded() > replies_recorded_ (0 vs. 0) CF.ADD](https://github.com/dragonflydb/dragonfly/issues/8102) — 9 comments · 0 reactions · open
- **Pull Request** [fix(facade): log V2 traffic before dispatch](https://github.com/dragonflydb/dragonfly/pull/8096) — 13 comments · 0 reactions · open
- **Issue** [Partial sync limitations](https://github.com/dragonflydb/dragonfly/issues/7994) — 6 comments · 0 reactions · closed
- **Pull Request** [feat: add time limitation for replication backlog](https://github.com/dragonflydb/dragonfly/pull/8039) — 10 comments · 0 reactions · closed
- **Issue** [P1 — A heterogeneous blocking queue can hide XREADGROUP forever](https://github.com/dragonflydb/dragonfly/issues/8067) — 0 comments · 0 reactions · open
- **Issue** [P1 — `NotifyPending()` is reentrant through a suspending expiry checker](https://github.com/dragonflydb/dragonfly/issues/8068) — 0 comments · 0 reactions · open
- **Issue** [P1 — Active expiry never runs for non-default namespaces](https://github.com/dragonflydb/dragonfly/issues/8069) — 0 comments · 0 reactions · open
- **Issue** [P1 — Multi-stream `XREADGROUP` mutates group state and then returns an error](https://github.com/dragonflydb/dragonfly/issues/8070) — 0 comments · 0 reactions · open
- **Issue** [P1 — A blocked multi-stream read returns only one stream when several become ready together](https://github.com/dragonflydb/dragonfly/issues/8071) — 0 comments · 0 reactions · open
- **Issue** [P2 — Multi-shard error precedence follows shard placement instead of argument order](https://github.com/dragonflydb/dragonfly/issues/8072) — 0 comments · 0 reactions · open
- **Issue** [test_heartbeat_eviction_propagation](https://github.com/dragonflydb/dragonfly/issues/8090) — 0 comments · 0 reactions · open
- **Issue** [crash: main_service.cc:2241\] Script <sha> not found in script mgr — SCRIPT FLAGS on an unknown sha then EVALSHA](https://github.com/dragonflydb/dragonfly/issues/8103) — 0 comments · 0 reactions · closed
- **Pull Request** [feat(geo): add GEOSEARCHSTORE command](https://github.com/dragonflydb/dragonfly/pull/7984) — 9 comments · 0 reactions · open
- **Issue** [test_replication_timeout_on_full_sync](https://github.com/dragonflydb/dragonfly/issues/4538) — 3 comments · 0 reactions · open
- **Issue** [test_slot_migration_oom_replica_rollback](https://github.com/dragonflydb/dragonfly/issues/8106) — 2 comments · 0 reactions · open
- **Pull Request** [ci(tests): add scheduled e2e workflow for ioredis client](https://github.com/dragonflydb/dragonfly/pull/8062) — 7 comments · 0 reactions · closed
- **Pull Request** [fix(pubsub): preserve V2 message ordering](https://github.com/dragonflydb/dragonfly/pull/8075) — 7 comments · 0 reactions · closed
- **Pull Request** [fix(server): probe heterogeneous blocking waiters instead of aborting…](https://github.com/dragonflydb/dragonfly/pull/8088) — 6 comments · 0 reactions · closed
- **Pull Request** [feat(server): make conn_use_incoming_cpu runtime mutable](https://github.com/dragonflydb/dragonfly/pull/8095) — 6 comments · 0 reactions · open
- **Issue** [test_policy_based_eviction_propagation](https://github.com/dragonflydb/dragonfly/issues/7925) — 0 comments · 0 reactions · open
- **Pull Request** [fix(tiering): Use TraverseBySegmentOrder and export more metrics/configs](https://github.com/dragonflydb/dragonfly/pull/8077) — 4 comments · 0 reactions · open
- **Pull Request** [fix(server): handle exceptions in squashed MULTI stub callback](https://github.com/dragonflydb/dragonfly/pull/8105) — 6 comments · 0 reactions · closed
- **Pull Request** [server: Add warning to defragment commands about time based CPU use](https://github.com/dragonflydb/dragonfly/pull/8107) — 4 comments · 0 reactions · open
- **Pull Request** [fix: reply NOSCRIPT for a sha that only has SCRIPT FLAGS set](https://github.com/dragonflydb/dragonfly/pull/8108) — 4 comments · 0 reactions · closed
- **Pull Request** [fix(server): skip evicting keys in buckets a full sync hasn't capture…](https://github.com/dragonflydb/dragonfly/pull/8109) — 4 comments · 0 reactions · open
- **Pull Request** [fix: stop SCRIPT FLUSH from deadlocking against a borrowed interpreter](https://github.com/dragonflydb/dragonfly/pull/8110) — 4 comments · 0 reactions · open
- **Pull Request** [fix: release the global shard lock in the mode it was taken](https://github.com/dragonflydb/dragonfly/pull/8111) — 4 comments · 0 reactions · open
- **Pull Request** [feat(tiering): Skip forced snapshot serialization for redundant writes](https://github.com/dragonflydb/dragonfly/pull/8112) — 0 comments · 0 reactions · open
