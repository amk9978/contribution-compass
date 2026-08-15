# Data / Messaging / Storage Infrastructure — 2026-08-15

> Factual GitHub evidence collected by Contribution Compass. No LLM analysis is performed.

## Contribution Leads

No evidence-qualified contribution leads changed in this collection.
## Important Updates

### [NATS Server](https://github.com/nats-io/nats-server)

- **Pull Request** [Make reverse response map removal constant time](https://github.com/nats-io/nats-server/pull/8463) — 0 comments · 3 reactions · open
- **Issue** [JetStream dynamic MaxStore shrinks after restart because it is recomputed from current free disk (Bavail), causing previously valid stream limits to fail](https://github.com/nats-io/nats-server/issues/8322) — 7 comments · 0 reactions · open
- **Issue** [Account JWT mapping updates that fail AddWeightedMappings are silently discarded, leaving stale or empty mappings](https://github.com/nats-io/nats-server/issues/8468) — 0 comments · 0 reactions · open
- **Pull Request** [\[FIXED\] Missing stream snapshot on shutdown, plus test de-flakes](https://github.com/nats-io/nats-server/pull/8465) — 1 comments · 0 reactions · open
- **Pull Request** [Add recovered stream usage back to dynamic MaxStore on restart](https://github.com/nats-io/nats-server/pull/8328) — 1 comments · 0 reactions · open

### [Redpanda](https://github.com/redpanda-data/redpanda)

- **Pull Request** [ts-ct-migration: partition_mode substrate \[PR 0\]](https://github.com/redpanda-data/redpanda/pull/30977) — 16 comments · 0 reactions · open
- **Pull Request** [sr: fix broker abort when a request fails before its deferred authz check](https://github.com/redpanda-data/redpanda/pull/31559) — 9 comments · 0 reactions · closed
- **Pull Request** [cloud_topics: fast partition movement for tiered-storage v2](https://github.com/redpanda-data/redpanda/pull/31589) — 7 comments · 0 reactions · open
- **Issue** [\[v25.3.x\] sr: fix broker abort when a request fails before its deferred authz check](https://github.com/redpanda-data/redpanda/issues/31592) — 0 comments · 0 reactions · open
- **Pull Request** [rptest: add OOM crash self-test; allow-list memory diagnostics](https://github.com/redpanda-data/redpanda/pull/31365) — 4 comments · 0 reactions · closed
- **Pull Request** [pandaproxy: run REST proxy in a dedicated scheduling group](https://github.com/redpanda-data/redpanda/pull/31514) — 4 comments · 0 reactions · closed
- **Pull Request** [\[CORE-16806\] - KIP-848: assignor interface and the homogeneous uniform assignor](https://github.com/redpanda-data/redpanda/pull/31579) — 2 comments · 0 reactions · open
- **Pull Request** [claude: add update-seastar-sha skill command](https://github.com/redpanda-data/redpanda/pull/29475) — 4 comments · 0 reactions · closed
- **Pull Request** [\[CORE-16806\]: KIP-848: Assignor Interface and Uniform Assignors](https://github.com/redpanda-data/redpanda/pull/31426) — 0 comments · 0 reactions · open
- **Pull Request** [\[CORE-16998, CORE-17000, CORE-17001\] - Consumer Groups (Classic): Fix some bugs where the offset map could diverge from the log](https://github.com/redpanda-data/redpanda/pull/31483) — 1 comments · 0 reactions · open
- **Pull Request** [rptest/redpanda_cloud: retry broker metrics health check](https://github.com/redpanda-data/redpanda/pull/31460) — 2 comments · 0 reactions · closed
- **Pull Request** [kafka: create the schema registry topic as a tiered topic](https://github.com/redpanda-data/redpanda/pull/31593) — 2 comments · 0 reactions · open
- **Pull Request** [\[v26.2.x\] sr: fix broker abort when a request fails before its deferred authz check](https://github.com/redpanda-data/redpanda/pull/31590) — 0 comments · 0 reactions · open
- **Pull Request** [\[v26.1.x\] sr: fix broker abort when a request fails before its deferred authz check](https://github.com/redpanda-data/redpanda/pull/31591) — 0 comments · 0 reactions · open

### [ClickHouse](https://github.com/ClickHouse/ClickHouse)

- **Issue** [ClickHouse roadmap 2026](https://github.com/ClickHouse/ClickHouse/issues/93288) — 29 comments · 43 reactions · open
- **Pull Request** [Cascades cost-based optimizer for distributed query plans](https://github.com/ClickHouse/ClickHouse/pull/86353) — 7 comments · 22 reactions · open
- **Pull Request** [Columns Cache](https://github.com/ClickHouse/ClickHouse/pull/96844) — 78 comments · 5 reactions · open
- **Pull Request** [Fix count distinct rewrite safety](https://github.com/ClickHouse/ClickHouse/pull/81944) — 36 comments · 4 reactions · open
- **Pull Request** [Parallelize read-in-order from a single part with PrefetchingConcatProcessor](https://github.com/ClickHouse/ClickHouse/pull/100391) — 42 comments · 1 reactions · open
- **Pull Request** [Switch the default compression to ZSTD(3) for table data and network](https://github.com/ClickHouse/ClickHouse/pull/108786) — 71 comments · 1 reactions · open
- **Pull Request** [Push join key filters into MergeTree index during recursive CTE evaluation](https://github.com/ClickHouse/ClickHouse/pull/97254) — 78 comments · 1 reactions · open
- **Pull Request** [Disable read-in-order when primary key selectivity is poor](https://github.com/ClickHouse/ClickHouse/pull/100377) — 40 comments · 0 reactions · open
- **Pull Request** [Parallel read in order with multiple parts](https://github.com/ClickHouse/ClickHouse/pull/100394) — 71 comments · 0 reactions · open
- **Pull Request** [Add optimize_row_order_if_no_order_by (reopen #103919)](https://github.com/ClickHouse/ClickHouse/pull/104591) — 45 comments · 0 reactions · open
- **Pull Request** [Minmax indices by default](https://github.com/ClickHouse/ClickHouse/pull/76867) — 81 comments · 0 reactions · open
- **Issue** [Assorted ideas to slightly improve JOINs](https://github.com/ClickHouse/ClickHouse/issues/21047) — 8 comments · 6 reactions · open
- **Pull Request** [Enable read_in_order_use_virtual_row by default](https://github.com/ClickHouse/ClickHouse/pull/106215) — 37 comments · 0 reactions · open
- **Pull Request** [Improve the performance of `MODIFY TTL`](https://github.com/ClickHouse/ClickHouse/pull/63383) — 33 comments · 1 reactions · open
- **Pull Request** [Add `GradualResizeProcessor` to limit effective parallelism for GROUP BY on small data volumes](https://github.com/ClickHouse/ClickHouse/pull/99495) — 33 comments · 0 reactions · open
- **Pull Request** [Adaptive Aggregator](https://github.com/ClickHouse/ClickHouse/pull/111459) — 14 comments · 4 reactions · open
- **Pull Request** [Support column matcher expansion for default value expressions and index expressions](https://github.com/ClickHouse/ClickHouse/pull/105045) — 50 comments · 3 reactions · open
- **Pull Request** [Iceberg: propagate table UUID from REST catalog to avoid metadata cac…](https://github.com/ClickHouse/ClickHouse/pull/99981) — 29 comments · 0 reactions · open
- **Pull Request** [`WindowTransform`: stream `lagInFrame` via `StreamingLagTransform` to…](https://github.com/ClickHouse/ClickHouse/pull/105822) — 27 comments · 0 reactions · open
- **Pull Request** [Implement CREATE HANDLER: SQL-defined HTTP handlers](https://github.com/ClickHouse/ClickHouse/pull/106231) — 79 comments · 2 reactions · closed
- **Pull Request** [Add table function `obfuscate`](https://github.com/ClickHouse/ClickHouse/pull/42701) — 44 comments · 2 reactions · open
- **Pull Request** [Randomize tests with DETACH/ATTACH table before query execution](https://github.com/ClickHouse/ClickHouse/pull/96130) — 91 comments · 2 reactions · open
- **Pull Request** [Added Parquet Shredded VARIANT Support to ParquetReaderv3](https://github.com/ClickHouse/ClickHouse/pull/102499) — 33 comments · 3 reactions · open
- **Pull Request** [Add SQLite input/output format](https://github.com/ClickHouse/ClickHouse/pull/104510) — 57 comments · 1 reactions · open
- **Pull Request** [Push down volume-reducing functions in query plan](https://github.com/ClickHouse/ClickHouse/pull/106199) — 12 comments · 2 reactions · open
- **Pull Request** [Make `if` with constant branches return `LowCardinality`](https://github.com/ClickHouse/ClickHouse/pull/80263) — 36 comments · 2 reactions · open
- **Pull Request** [Add Rewrite rules](https://github.com/ClickHouse/ClickHouse/pull/88234) — 62 comments · 1 reactions · open
- **Pull Request** [FileCache use RocksDB metadata index](https://github.com/ClickHouse/ClickHouse/pull/101618) — 19 comments · 1 reactions · closed
- **Pull Request** [Push subcolumn reads into subqueries](https://github.com/ClickHouse/ClickHouse/pull/112688) — 15 comments · 1 reactions · open
- **Pull Request** [Revert "Revert "Use a lock-free queue for asynchronous logging""](https://github.com/ClickHouse/ClickHouse/pull/112803) — 19 comments · 0 reactions · open

### [Dragonfly](https://github.com/dragonflydb/dragonfly)

- **Pull Request** [fix(server): lower table growth margin default](https://github.com/dragonflydb/dragonfly/pull/8080) — 4 comments · 0 reactions · open
