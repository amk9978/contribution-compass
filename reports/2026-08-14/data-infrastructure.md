# Data / Messaging / Storage Infrastructure — 2026-08-14

> Factual GitHub evidence collected by Contribution Compass. No LLM analysis is performed.

## Contribution Leads

No evidence-qualified contribution leads changed in this collection.
## Important Updates

### [NATS Server](https://github.com/nats-io/nats-server)

- **Issue** [Always retain last message for each subject in a stream](https://github.com/nats-io/nats-server/issues/5811) — 2 comments · 1 reactions · open
- **Pull Request** [(2.15) \[ADDED\] Peer evacuation and reconciliation of assignments](https://github.com/nats-io/nats-server/pull/8443) — 5 comments · 1 reactions · open
- **Pull Request** [(2.15) \[FIXED\] Evict peer-removed peers for group below quorum](https://github.com/nats-io/nats-server/pull/8452) — 5 comments · 1 reactions · open
- **Pull Request** [(2.15) \[FIXED\] Migration added offline peers & removed peers before catchup](https://github.com/nats-io/nats-server/pull/8460) — 5 comments · 1 reactions · open

### [Redpanda](https://github.com/redpanda-data/redpanda)

- **Release** [v25.3.16](https://github.com/redpanda-data/redpanda/releases/tag/v25.3.16) — 
- **Release** [v26.1.16](https://github.com/redpanda-data/redpanda/releases/tag/v26.1.16) — 
- **Pull Request** [bazel: bump the toolchain sysroot to Ubuntu 24.04](https://github.com/redpanda-data/redpanda/pull/31560) — 13 comments · 0 reactions · open
- **Pull Request** [sr: fix broker abort when a request fails before its deferred authz check](https://github.com/redpanda-data/redpanda/pull/31559) — 5 comments · 0 reactions · open
- **Pull Request** [cluster_link: harden shadow link create against transient unavailable](https://github.com/redpanda-data/redpanda/pull/31268) — 6 comments · 0 reactions · open
- **Pull Request** [\[CORE-12930\] - Storage: Some observability improvements for unrecoverable segments](https://github.com/redpanda-data/redpanda/pull/31544) — 3 comments · 0 reactions · open
- **Pull Request** [kafka/client: fix node crash on concurrent pandaproxy consumer fetches](https://github.com/redpanda-data/redpanda/pull/31423) — 4 comments · 0 reactions · open
- **Pull Request** [\[CORE-8759\] storage: kill broker process if log_reader detects a corrupt segment](https://github.com/redpanda-data/redpanda/pull/31543) — 4 comments · 0 reactions · open
- **Pull Request** [pandaproxy: run REST proxy in a dedicated scheduling group](https://github.com/redpanda-data/redpanda/pull/31514) — 3 comments · 0 reactions · open
- **Pull Request** [rpk/registry: document print flag exclusivity in help text](https://github.com/redpanda-data/redpanda/pull/31574) — 2 comments · 0 reactions · open
- **Pull Request** [\[CORE-16806\]: KIP-848: Assignor Interface and Uniform Assignors](https://github.com/redpanda-data/redpanda/pull/31426) — 0 comments · 0 reactions · open
- **Pull Request** [\[CORE-16804\] - KIP-848: deterministic subscription-metadata hash](https://github.com/redpanda-data/redpanda/pull/31499) — 0 comments · 0 reactions · open
- **Pull Request** [kafka: create the consumer offsets topic as a local topic](https://github.com/redpanda-data/redpanda/pull/31576) — 0 comments · 0 reactions · open
- **Pull Request** [tests: make the llvm-symbolizer shim a static binary](https://github.com/redpanda-data/redpanda/pull/31578) — 1 comments · 0 reactions · open
- **Pull Request** [\[CORE-16806\] - KIP-848: assignor interface and the homogeneous uniform assignor](https://github.com/redpanda-data/redpanda/pull/31579) — 1 comments · 0 reactions · open
- **Pull Request** [kafka/raft: absorb offset_not_available races on follower fetches](https://github.com/redpanda-data/redpanda/pull/31580) — 0 comments · 0 reactions · closed
- **Pull Request** [Mitigate `offset_not_available` races on follower fetches](https://github.com/redpanda-data/redpanda/pull/31581) — 1 comments · 0 reactions · open

### [ClickHouse](https://github.com/ClickHouse/ClickHouse)

- **Pull Request** [Cascades cost-based optimizer for distributed query plans](https://github.com/ClickHouse/ClickHouse/pull/86353) — 7 comments · 22 reactions · open
- **Pull Request** [Optimization of `GROUP BY` in the presence of `ORDER BY` and `LIMIT`](https://github.com/ClickHouse/ClickHouse/pull/96630) — 13 comments · 8 reactions · open
- **Pull Request** [Parallel read in order with multiple parts](https://github.com/ClickHouse/ClickHouse/pull/100394) — 71 comments · 0 reactions · open
- **Issue** [How to handle duplicate records when doing data aggregation in Materialized Views](https://github.com/ClickHouse/ClickHouse/issues/27232) — 10 comments · 12 reactions · closed
- **Pull Request** [Improve the performance of `MODIFY TTL`](https://github.com/ClickHouse/ClickHouse/pull/63383) — 33 comments · 1 reactions · open
- **Pull Request** [Avoid copying data for the NONE compression codec when writing](https://github.com/ClickHouse/ClickHouse/pull/108096) — 36 comments · 0 reactions · open
- **Pull Request** [WIP: Projection Index Text](https://github.com/ClickHouse/ClickHouse/pull/93114) — 26 comments · 7 reactions · open
- **Pull Request** [Add `GradualResizeProcessor` to limit effective parallelism for GROUP BY on small data volumes](https://github.com/ClickHouse/ClickHouse/pull/99495) — 30 comments · 0 reactions · open
- **Pull Request** [In case of trivial views, push whole outer query to shards.](https://github.com/ClickHouse/ClickHouse/pull/101791) — 16 comments · 3 reactions · closed
- **Pull Request** [Implement CREATE HANDLER: SQL-defined HTTP handlers](https://github.com/ClickHouse/ClickHouse/pull/106231) — 79 comments · 2 reactions · open
- **Pull Request** [Add a Chinese tokenizer (jieba) for the tokens function and text indexes](https://github.com/ClickHouse/ClickHouse/pull/89945) — 37 comments · 3 reactions · open
- **Pull Request** [Randomize tests with DETACH/ATTACH table before query execution](https://github.com/ClickHouse/ClickHouse/pull/96130) — 91 comments · 2 reactions · open
- **Pull Request** [`WindowTransform`: stream `lagInFrame` via `StreamingLagTransform` to…](https://github.com/ClickHouse/ClickHouse/pull/105822) — 26 comments · 0 reactions · open
- **Pull Request** [Added Parquet Shredded VARIANT Support to ParquetReaderv3](https://github.com/ClickHouse/ClickHouse/pull/102499) — 33 comments · 3 reactions · open
- **Pull Request** [Push down volume-reducing functions in query plan](https://github.com/ClickHouse/ClickHouse/pull/106199) — 12 comments · 2 reactions · open
- **Pull Request** [Rewrite `length(arrayFilter(f, arr))` to `arrayCount(f, arr)`](https://github.com/ClickHouse/ClickHouse/pull/113023) — 19 comments · 0 reactions · open
- **Pull Request** [Add SQLite input/output format](https://github.com/ClickHouse/ClickHouse/pull/104510) — 57 comments · 1 reactions · open
- **Pull Request** [Detect when tables behind a query have changed](https://github.com/ClickHouse/ClickHouse/pull/108721) — 58 comments · 0 reactions · open
- **Pull Request** [Docs: internationalize master](https://github.com/ClickHouse/ClickHouse/pull/114466) — 58 comments · 0 reactions · open
- **Pull Request** [Make `if` with constant branches return `LowCardinality`](https://github.com/ClickHouse/ClickHouse/pull/80263) — 36 comments · 2 reactions · open
- **Pull Request** [Implement Prometheus /api/v1/series, /labels, /label/values endpoints](https://github.com/ClickHouse/ClickHouse/pull/97032) — 49 comments · 0 reactions · open
- **Pull Request** [Respect `date_time_overflow_behavior` for numeric temporal casts](https://github.com/ClickHouse/ClickHouse/pull/109299) — 38 comments · 0 reactions · open
- **Pull Request** [Revert "Revert "Use a lock-free queue for asynchronous logging""](https://github.com/ClickHouse/ClickHouse/pull/112803) — 19 comments · 0 reactions · open
- **Pull Request** [Replace the per-bucket hash map in `timeSeries*ToGrid` with a sorted-append sample array](https://github.com/ClickHouse/ClickHouse/pull/113681) — 10 comments · 1 reactions · closed
- **Pull Request** [Enable dynamic evaluation of whether a short-circuit function's argument should be lazily executed](https://github.com/ClickHouse/ClickHouse/pull/73776) — 14 comments · 0 reactions · open
- **Pull Request** [Add spatial_bbox skip index for MergeTree geometry columns](https://github.com/ClickHouse/ClickHouse/pull/104437) — 9 comments · 1 reactions · open
- **Pull Request** [Add server setting `additional_memory_tracking_per_thread`](https://github.com/ClickHouse/ClickHouse/pull/104965) — 37 comments · 0 reactions · open
- **Pull Request** [PromQL/TimeSeries: use bare samples-table PK columns and timestamp-range-first conditions in selector SQL](https://github.com/ClickHouse/ClickHouse/pull/113768) — 17 comments · 0 reactions · closed
- **Pull Request** [Use a continuous primary-key range for whole-metric PromQL selectors of TimeSeries tables](https://github.com/ClickHouse/ClickHouse/pull/114131) — 13 comments · 0 reactions · open
- **Pull Request** [Add early short-circuit evaluation for OR/AND in the analyzer to prevent unnecessary scalar subquery execution](https://github.com/ClickHouse/ClickHouse/pull/83505) — 12 comments · 0 reactions · open

### [Dragonfly](https://github.com/dragonflydb/dragonfly)

- **Issue** [test_replicaof_reject_on_load](https://github.com/dragonflydb/dragonfly/issues/5662) — 38 comments · 0 reactions · open
- **Pull Request** [feat(geo): add GEOSEARCHSTORE command](https://github.com/dragonflydb/dragonfly/pull/7984) — 8 comments · 0 reactions · open
