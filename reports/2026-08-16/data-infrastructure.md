# Data / Messaging / Storage Infrastructure — 2026-08-16

> Factual GitHub evidence collected by Contribution Compass. No LLM analysis is performed.

## Contribution Leads

No evidence-qualified contribution leads changed in this collection.
## Important Updates

### [NATS Server](https://github.com/nats-io/nats-server)

- **Pull Request** [(2.15) NRG: Relax SyncAlways for replicated streams](https://github.com/nats-io/nats-server/pull/8447) — 10 comments · 0 reactions · open
- **Pull Request** [(2.15) Raft proposal fast path](https://github.com/nats-io/nats-server/pull/8445) — 8 comments · 0 reactions · open
- **Issue** [Apply clustered expected-last-subject-sequence checks during replicated apply](https://github.com/nats-io/nats-server/issues/8469) — 1 comments · 0 reactions · open
- **Pull Request** [\[FIXED\] Route TLS: preserve saved hostname on HostnameError when URL is an IP](https://github.com/nats-io/nats-server/pull/8446) — 2 comments · 0 reactions · open

### [Redpanda](https://github.com/redpanda-data/redpanda)

- **Pull Request** [\[CORE-16998, CORE-17000, CORE-17001\] - Consumer Groups (Classic): Fix some bugs where the offset map could diverge from the log](https://github.com/redpanda-data/redpanda/pull/31483) — 3 comments · 0 reactions · open
- **Pull Request** [tests: make the llvm-symbolizer shim a static binary](https://github.com/redpanda-data/redpanda/pull/31578) — 2 comments · 0 reactions · open
- **Pull Request** [\[CORE-16806\] - KIP-848: assignor interface and the homogeneous uniform assignor](https://github.com/redpanda-data/redpanda/pull/31579) — 3 comments · 0 reactions · open
- **Pull Request** [\[CORE-16806\]: KIP-848: Assignor Interface and Uniform Assignors](https://github.com/redpanda-data/redpanda/pull/31426) — 0 comments · 0 reactions · open
- **Pull Request** [rpc/transport: retain memory semaphore units in queued request entry](https://github.com/redpanda-data/redpanda/pull/31594) — 1 comments · 0 reactions · open

### [ClickHouse](https://github.com/ClickHouse/ClickHouse)

- **Issue** [ClickHouse roadmap 2026](https://github.com/ClickHouse/ClickHouse/issues/93288) — 29 comments · 43 reactions · open
- **Pull Request** [Cascades cost-based optimizer for distributed query plans](https://github.com/ClickHouse/ClickHouse/pull/86353) — 7 comments · 22 reactions · open
- **Pull Request** [Columns Cache](https://github.com/ClickHouse/ClickHouse/pull/96844) — 78 comments · 5 reactions · open
- **Pull Request** [Fix count distinct rewrite safety](https://github.com/ClickHouse/ClickHouse/pull/81944) — 37 comments · 4 reactions · open
- **Pull Request** [Optimization of `GROUP BY` in the presence of `ORDER BY` and `LIMIT`](https://github.com/ClickHouse/ClickHouse/pull/96630) — 14 comments · 8 reactions · open
- **Pull Request** [Parallelize read-in-order from a single part with PrefetchingConcatProcessor](https://github.com/ClickHouse/ClickHouse/pull/100391) — 44 comments · 1 reactions · open
- **Pull Request** [Switch the default compression to ZSTD(3) for table data and network](https://github.com/ClickHouse/ClickHouse/pull/108786) — 72 comments · 1 reactions · open
- **Pull Request** [Push join key filters into MergeTree index during recursive CTE evaluation](https://github.com/ClickHouse/ClickHouse/pull/97254) — 80 comments · 1 reactions · open
- **Pull Request** [Disable read-in-order when primary key selectivity is poor](https://github.com/ClickHouse/ClickHouse/pull/100377) — 40 comments · 0 reactions · open
- **Pull Request** [Parallel read in order with multiple parts](https://github.com/ClickHouse/ClickHouse/pull/100394) — 71 comments · 0 reactions · open
- **Pull Request** [Add optimize_row_order_if_no_order_by (reopen #103919)](https://github.com/ClickHouse/ClickHouse/pull/104591) — 45 comments · 0 reactions · open
- **Pull Request** [Minmax indices by default](https://github.com/ClickHouse/ClickHouse/pull/76867) — 84 comments · 0 reactions · open
- **Pull Request** [Enable read_in_order_use_virtual_row by default](https://github.com/ClickHouse/ClickHouse/pull/106215) — 37 comments · 0 reactions · open
- **Pull Request** [Avoid copying data for the NONE compression codec when writing](https://github.com/ClickHouse/ClickHouse/pull/108096) — 36 comments · 0 reactions · open
- **Pull Request** [Improve the performance of `MODIFY TTL`](https://github.com/ClickHouse/ClickHouse/pull/63383) — 33 comments · 1 reactions · open
- **Pull Request** [Add experimental cuckoo_filter and binary_fuse_filter skip indexes](https://github.com/ClickHouse/ClickHouse/pull/101796) — 38 comments · 0 reactions · open
- **Pull Request** [Add `GradualResizeProcessor` to limit effective parallelism for GROUP BY on small data volumes](https://github.com/ClickHouse/ClickHouse/pull/99495) — 35 comments · 0 reactions · open
- **Pull Request** [Adaptive Aggregator](https://github.com/ClickHouse/ClickHouse/pull/111459) — 14 comments · 4 reactions · closed
- **Pull Request** [Support column matcher expansion for default value expressions and index expressions](https://github.com/ClickHouse/ClickHouse/pull/105045) — 50 comments · 3 reactions · open
- **Pull Request** [Iceberg: propagate table UUID from REST catalog to avoid metadata cac…](https://github.com/ClickHouse/ClickHouse/pull/99981) — 29 comments · 0 reactions · open
- **Pull Request** [`WindowTransform`: stream `lagInFrame` via `StreamingLagTransform` to…](https://github.com/ClickHouse/ClickHouse/pull/105822) — 27 comments · 0 reactions · open
- **Issue** [optimize_inverse_dictionary_lookup does not work with views](https://github.com/ClickHouse/ClickHouse/issues/114271) — 1 comments · 5 reactions · open
- **Pull Request** [Add table function `obfuscate`](https://github.com/ClickHouse/ClickHouse/pull/42701) — 46 comments · 2 reactions · open
- **Pull Request** [Randomize tests with DETACH/ATTACH table before query execution](https://github.com/ClickHouse/ClickHouse/pull/96130) — 91 comments · 2 reactions · open
- **Pull Request** [Added Parquet Shredded VARIANT Support to ParquetReaderv3](https://github.com/ClickHouse/ClickHouse/pull/102499) — 34 comments · 3 reactions · open
- **Pull Request** [Push down volume-reducing functions in query plan](https://github.com/ClickHouse/ClickHouse/pull/106199) — 15 comments · 2 reactions · open
- **Pull Request** [Make `if` with constant branches return `LowCardinality`](https://github.com/ClickHouse/ClickHouse/pull/80263) — 38 comments · 2 reactions · open
- **Pull Request** [Add SQLite input/output format](https://github.com/ClickHouse/ClickHouse/pull/104510) — 58 comments · 1 reactions · open
- **Pull Request** [Push subcolumn reads into subqueries](https://github.com/ClickHouse/ClickHouse/pull/112688) — 17 comments · 1 reactions · open
- **Pull Request** [Make `arrayCount` return `UInt64` and rewrite `length(arrayFilter(...))`](https://github.com/ClickHouse/ClickHouse/pull/113023) — 21 comments · 0 reactions · open

### [Dragonfly](https://github.com/dragonflydb/dragonfly)

- **Issue** [ZMPOP RESP2 reply is incompatibile with Redis](https://github.com/dragonflydb/dragonfly/issues/8087) — 3 comments · 0 reactions · open
- **Pull Request** [feat(geo): add GEOSEARCHSTORE command](https://github.com/dragonflydb/dragonfly/pull/7984) — 9 comments · 0 reactions · open
- **Pull Request** [fix(server): probe heterogeneous blocking waiters instead of aborting…](https://github.com/dragonflydb/dragonfly/pull/8088) — 6 comments · 0 reactions · open
- **Issue** [ZADD GT/LT are silently ignored once a sorted set leaves listpack encoding](https://github.com/dragonflydb/dragonfly/issues/8089) — 1 comments · 0 reactions · open
- **Issue** [test_heartbeat_eviction_propagation](https://github.com/dragonflydb/dragonfly/issues/8090) — 0 comments · 0 reactions · open
- **Pull Request** [fix(server): lower table growth margin default](https://github.com/dragonflydb/dragonfly/pull/8080) — 5 comments · 0 reactions · open
- **Pull Request** [fix(zset): honor GT/LT flags for skiplist-encoded sorted sets](https://github.com/dragonflydb/dragonfly/pull/8091) — 4 comments · 0 reactions · open
- **Pull Request** [fix: reply with a null array for empty ZMPOP/BZMPOP/LMPOP/BLMPOP](https://github.com/dragonflydb/dragonfly/pull/8092) — 4 comments · 0 reactions · open
