# Data / Messaging / Storage Infrastructure — 2026-08-17

> Factual GitHub evidence collected by Contribution Compass. No LLM analysis is performed.

## Contribution Leads

No evidence-qualified contribution leads changed in this collection.
## Important Updates

### [NATS Server](https://github.com/nats-io/nats-server)

- **Issue** [Apply clustered expected-last-subject-sequence checks during replicated apply](https://github.com/nats-io/nats-server/issues/8469) — 2 comments · 0 reactions · closed
- **Issue** [JetStream file stream Created timestamp changes after restart and configuration update](https://github.com/nats-io/nats-server/issues/8470) — 0 comments · 0 reactions · open
- **Issue** [CRITICAL JetStream atomic batch publish leaves per-batch staging directories under <stream>/batches after commit](https://github.com/nats-io/nats-server/issues/8472) — 0 comments · 0 reactions · open
- **Pull Request** [\[FIXED\] Preserve stream created time after recovery](https://github.com/nats-io/nats-server/pull/8471) — 1 comments · 0 reactions · open

### [Redpanda](https://github.com/redpanda-data/redpanda)

- **Pull Request** [\[CORE-16806\] - KIP-848: assignor interface and the homogeneous uniform assignor](https://github.com/redpanda-data/redpanda/pull/31579) — 4 comments · 0 reactions · open

### [ClickHouse](https://github.com/ClickHouse/ClickHouse)

- **Pull Request** [Cascades cost-based optimizer for distributed query plans](https://github.com/ClickHouse/ClickHouse/pull/86353) — 7 comments · 22 reactions · open
- **Pull Request** [Columns Cache](https://github.com/ClickHouse/ClickHouse/pull/96844) — 78 comments · 5 reactions · open
- **Pull Request** [Fix count distinct rewrite safety](https://github.com/ClickHouse/ClickHouse/pull/81944) — 37 comments · 4 reactions · open
- **Pull Request** [Optimization of `GROUP BY` in the presence of `ORDER BY` and `LIMIT`](https://github.com/ClickHouse/ClickHouse/pull/96630) — 14 comments · 8 reactions · open
- **Pull Request** [Parallelize read-in-order from a single part with PrefetchingConcatProcessor](https://github.com/ClickHouse/ClickHouse/pull/100391) — 44 comments · 1 reactions · open
- **Pull Request** [Switch the default compression to ZSTD(3) for table data and network](https://github.com/ClickHouse/ClickHouse/pull/108786) — 72 comments · 1 reactions · open
- **Pull Request** [Push join key filters into MergeTree index during recursive CTE evaluation](https://github.com/ClickHouse/ClickHouse/pull/97254) — 81 comments · 1 reactions · open
- **Pull Request** [Disable read-in-order when primary key selectivity is poor](https://github.com/ClickHouse/ClickHouse/pull/100377) — 40 comments · 0 reactions · open
- **Pull Request** [Parallel read in order with multiple parts](https://github.com/ClickHouse/ClickHouse/pull/100394) — 71 comments · 0 reactions · open
- **Pull Request** [Add optimize_row_order_if_no_order_by (reopen #103919)](https://github.com/ClickHouse/ClickHouse/pull/104591) — 45 comments · 0 reactions · open
- **Pull Request** [Enable read_in_order_use_virtual_row by default](https://github.com/ClickHouse/ClickHouse/pull/106215) — 41 comments · 0 reactions · open
- **Pull Request** [Minmax indices by default](https://github.com/ClickHouse/ClickHouse/pull/76867) — 87 comments · 0 reactions · open
- **Pull Request** [Improve the performance of `MODIFY TTL`](https://github.com/ClickHouse/ClickHouse/pull/63383) — 34 comments · 1 reactions · open
- **Pull Request** [Avoid copying data for the NONE compression codec when writing](https://github.com/ClickHouse/ClickHouse/pull/108096) — 37 comments · 0 reactions · open
- **Pull Request** [Add `GradualResizeProcessor` to limit effective parallelism for GROUP BY on small data volumes](https://github.com/ClickHouse/ClickHouse/pull/99495) — 35 comments · 0 reactions · open
- **Pull Request** [Adaptive Aggregator](https://github.com/ClickHouse/ClickHouse/pull/111459) — 15 comments · 4 reactions · closed
- **Pull Request** [WIP: Projection Index Text](https://github.com/ClickHouse/ClickHouse/pull/93114) — 26 comments · 7 reactions · open
- **Pull Request** [Support column matcher expansion for default value expressions and index expressions](https://github.com/ClickHouse/ClickHouse/pull/105045) — 51 comments · 3 reactions · open
- **Pull Request** [Iceberg: propagate table UUID from REST catalog to avoid metadata cac…](https://github.com/ClickHouse/ClickHouse/pull/99981) — 29 comments · 0 reactions · open
- **Pull Request** [Add table function `obfuscate`](https://github.com/ClickHouse/ClickHouse/pull/42701) — 48 comments · 2 reactions · closed
- **Pull Request** [Randomize tests with DETACH/ATTACH table before query execution](https://github.com/ClickHouse/ClickHouse/pull/96130) — 91 comments · 2 reactions · open
- **Pull Request** [Added Parquet Shredded VARIANT Support to ParquetReaderv3](https://github.com/ClickHouse/ClickHouse/pull/102499) — 35 comments · 3 reactions · open
- **Pull Request** [Push down volume-reducing functions in query plan](https://github.com/ClickHouse/ClickHouse/pull/106199) — 15 comments · 2 reactions · open
- **Pull Request** [Push subcolumn reads into subqueries](https://github.com/ClickHouse/ClickHouse/pull/112688) — 19 comments · 1 reactions · open
- **Pull Request** [Make `arrayCount` return `UInt64` and rewrite `length(arrayFilter(...))`](https://github.com/ClickHouse/ClickHouse/pull/113023) — 23 comments · 0 reactions · open
- **Pull Request** [Make `if` with constant branches return `LowCardinality`](https://github.com/ClickHouse/ClickHouse/pull/80263) — 38 comments · 2 reactions · open
- **Pull Request** [Add SQLite input/output format](https://github.com/ClickHouse/ClickHouse/pull/104510) — 58 comments · 1 reactions · open
- **Pull Request** [Push tuple element predicates into Parquet and ORC subcolumn reads](https://github.com/ClickHouse/ClickHouse/pull/113383) — 21 comments · 0 reactions · closed
- **Pull Request** [Add Rewrite rules](https://github.com/ClickHouse/ClickHouse/pull/88234) — 63 comments · 1 reactions · open
- **Issue** [Import/export AST as JSON](https://github.com/ClickHouse/ClickHouse/issues/88799) — 11 comments · 7 reactions · closed

### [Dragonfly](https://github.com/dragonflydb/dragonfly)

- **Issue** [test_replicaof_reject_on_load](https://github.com/dragonflydb/dragonfly/issues/5662) — 39 comments · 0 reactions · open
- **Issue** [test_pubsub_pipeline_starvation](https://github.com/dragonflydb/dragonfly/issues/8009) — 5 comments · 0 reactions · closed
- **Issue** [test_client_pause_v2_inflight_async_write_gap](https://github.com/dragonflydb/dragonfly/issues/8079) — 2 comments · 0 reactions · closed
- **Issue** [ZMPOP RESP2 reply is incompatibile with Redis](https://github.com/dragonflydb/dragonfly/issues/8087) — 3 comments · 0 reactions · closed
- **Issue** [Return RESP3 null for empty XREAD and XREADGROUP replies](https://github.com/dragonflydb/dragonfly/issues/8076) — 0 comments · 0 reactions · closed
- **Issue** [ZADD GT/LT are silently ignored once a sorted set leaves listpack encoding](https://github.com/dragonflydb/dragonfly/issues/8089) — 1 comments · 0 reactions · closed
- **Pull Request** [fix(facade): log V2 traffic before dispatch](https://github.com/dragonflydb/dragonfly/pull/8096) — 12 comments · 0 reactions · open
- **Pull Request** [ci(tests): add scheduled e2e workflow for ioredis client](https://github.com/dragonflydb/dragonfly/pull/8062) — 4 comments · 0 reactions · open
- **Pull Request** [fix(facade): Handle RESP3 null array response](https://github.com/dragonflydb/dragonfly/pull/8085) — 4 comments · 0 reactions · closed
- **Pull Request** [fix(zset): honor GT/LT flags for skiplist-encoded sorted sets](https://github.com/dragonflydb/dragonfly/pull/8091) — 4 comments · 0 reactions · closed
- **Pull Request** [fix: reply with a null array for empty ZMPOP/BZMPOP/LMPOP/BLMPOP](https://github.com/dragonflydb/dragonfly/pull/8092) — 4 comments · 0 reactions · closed
- **Pull Request** [fix(tests): extend pause wait (Fixes #8079)](https://github.com/dragonflydb/dragonfly/pull/8093) — 4 comments · 0 reactions · closed
- **Pull Request** [fix(tests): fix test_pubsub_pipeline_starvation test](https://github.com/dragonflydb/dragonfly/pull/8094) — 4 comments · 0 reactions · closed
- **Pull Request** [feat(server): make conn_use_incoming_cpu runtime mutable](https://github.com/dragonflydb/dragonfly/pull/8095) — 4 comments · 0 reactions · open
- **Pull Request** [fix(ci): run cache reaper hourly](https://github.com/dragonflydb/dragonfly/pull/8097) — 4 comments · 0 reactions · closed
- **Pull Request** [fix: null reply shapes for blocking moves, LPOP COUNT, ZRANK WITHSCORE, EXEC and friends](https://github.com/dragonflydb/dragonfly/pull/8098) — 4 comments · 0 reactions · open
- **Pull Request** [test(fuzz): repair seed corpus so every seed executes and harden coverage guard](https://github.com/dragonflydb/dragonfly/pull/8099) — 3 comments · 0 reactions · open
