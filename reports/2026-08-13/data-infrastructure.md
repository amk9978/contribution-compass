# Data / Messaging / Storage Infrastructure — 2026-08-13

> Factual GitHub evidence collected by Contribution Compass. No LLM analysis is performed.

## Contribution Leads

No evidence-qualified contribution leads changed in this collection.
## Important Updates

### [NATS Server](https://github.com/nats-io/nats-server)

- **Pull Request** [(2.15) \[IMPROVED\] Source stream recreation detection](https://github.com/nats-io/nats-server/pull/8384) — 9 comments · 2 reactions · closed
- **Issue** [JetStream sourced stream reports lag=0 after source stream recreation but no longer ingests new messages](https://github.com/nats-io/nats-server/issues/8346) — 4 comments · 0 reactions · closed
- **Issue** [JetStream stream source stalls/is out of sync after sourced stream is re-created for unrelated reason \[v2.10.20\]](https://github.com/nats-io/nats-server/issues/6206) — 2 comments · 0 reactions · closed
- **Pull Request** [(2.15) \[FIXED\] Migration added offline peers & removed peers before catchup](https://github.com/nats-io/nats-server/pull/8460) — 3 comments · 1 reactions · open

### [Redpanda](https://github.com/redpanda-data/redpanda)

- **Pull Request** [\[CORE-16604\] cluster_link: incremental Schema Registry sync by tailing _schemas](https://github.com/redpanda-data/redpanda/pull/31366) — 8 comments · 0 reactions · open
- **Pull Request** [\[CORE-15822\] security/audit: make audit initialization controller-leader independent](https://github.com/redpanda-data/redpanda/pull/31411) — 9 comments · 0 reactions · open
- **Pull Request** [sr: fix broker abort when a request fails before its deferred authz check](https://github.com/redpanda-data/redpanda/pull/31559) — 4 comments · 0 reactions · open
- **Pull Request** [storage: bump segment_concatenation_test timeout](https://github.com/redpanda-data/redpanda/pull/31568) — 4 comments · 0 reactions · closed
- **Pull Request** [rptest: add OOM crash self-test; allow-list memory diagnostics](https://github.com/redpanda-data/redpanda/pull/31365) — 2 comments · 0 reactions · open
- **Pull Request** [\[v26.2.x\] k/s/tests: deflake fetch_memory_units cross-shard test](https://github.com/redpanda-data/redpanda/pull/31561) — 1 comments · 0 reactions · closed
- **Pull Request** [k/s/tests: deflake the offset_store producer lock test](https://github.com/redpanda-data/redpanda/pull/31566) — 0 comments · 0 reactions · open
- **Pull Request** [kafka/client/test: deflake data_queue blocking push test](https://github.com/redpanda-data/redpanda/pull/31567) — 1 comments · 0 reactions · closed
- **Pull Request** [\[v25.3.x\] storage: bump segment_concatenation_test timeout](https://github.com/redpanda-data/redpanda/pull/31569) — 0 comments · 0 reactions · open
- **Pull Request** [\[v26.2.x\] storage: bump segment_concatenation_test timeout](https://github.com/redpanda-data/redpanda/pull/31570) — 0 comments · 0 reactions · open
- **Pull Request** [\[v26.1.x\] storage: bump segment_concatenation_test timeout](https://github.com/redpanda-data/redpanda/pull/31571) — 0 comments · 0 reactions · open
- **Pull Request** [\[v26.2.x\] kafka/client/test: deflake data_queue blocking push test](https://github.com/redpanda-data/redpanda/pull/31572) — 0 comments · 0 reactions · open

### [ClickHouse](https://github.com/ClickHouse/ClickHouse)

- **Pull Request** [Cascades cost-based optimizer for distributed query plans](https://github.com/ClickHouse/ClickHouse/pull/86353) — 7 comments · 21 reactions · open
- **Pull Request** [Add optimize_row_order_if_no_order_by (reopen #103919)](https://github.com/ClickHouse/ClickHouse/pull/104591) — 44 comments · 0 reactions · open
- **Pull Request** [Improve the performance of `MODIFY TTL`](https://github.com/ClickHouse/ClickHouse/pull/63383) — 33 comments · 1 reactions · open
- **Pull Request** [Add `GradualResizeProcessor` to limit effective parallelism for GROUP BY on small data volumes](https://github.com/ClickHouse/ClickHouse/pull/99495) — 30 comments · 0 reactions · open
- **Pull Request** [In case of trivial views, push whole outer query to shards.](https://github.com/ClickHouse/ClickHouse/pull/101791) — 15 comments · 3 reactions · open
- **Pull Request** [Randomize tests with DETACH/ATTACH table before query execution](https://github.com/ClickHouse/ClickHouse/pull/96130) — 91 comments · 2 reactions · open
- **Issue** [Range condition in JOIN ON against a single-row side is not used for index analysis (no part pruning) since the logical join step became default](https://github.com/ClickHouse/ClickHouse/issues/112586) — 6 comments · 2 reactions · closed
- **Pull Request** [Add a Chinese tokenizer (jieba) for the tokens function and text indexes](https://github.com/ClickHouse/ClickHouse/pull/89945) — 36 comments · 3 reactions · open
- **Pull Request** [Push tuple element predicates into Parquet and ORC subcolumn reads](https://github.com/ClickHouse/ClickHouse/pull/113383) — 18 comments · 0 reactions · open
- **Pull Request** [Fix wrong results with parallel_hash JOIN and read-in-order-through-join](https://github.com/ClickHouse/ClickHouse/pull/109225) — 42 comments · 0 reactions · open
- **Pull Request** [Reintroduce borrowed threadgroup async uaf fix](https://github.com/ClickHouse/ClickHouse/pull/109891) — 47 comments · 0 reactions · open
- **Pull Request** [Docs: internationalize master](https://github.com/ClickHouse/ClickHouse/pull/114466) — 45 comments · 0 reactions · open
- **Pull Request** [Declarative function signatures, continuation of #3775](https://github.com/ClickHouse/ClickHouse/pull/104948) — 38 comments · 0 reactions · open
- **Pull Request** [Add geo aggregate functions #80186](https://github.com/ClickHouse/ClickHouse/pull/101273) — 36 comments · 0 reactions · open
- **Pull Request** [Add spatial_bbox skip index for MergeTree geometry columns](https://github.com/ClickHouse/ClickHouse/pull/104437) — 9 comments · 1 reactions · open
- **Pull Request** [Add server setting `additional_memory_tracking_per_thread`](https://github.com/ClickHouse/ClickHouse/pull/104965) — 37 comments · 0 reactions · open
- **Pull Request** [Replace the per-bucket hash map in `timeSeries*ToGrid` with a sorted-append sample array](https://github.com/ClickHouse/ClickHouse/pull/113681) — 8 comments · 1 reactions · open
- **Pull Request** [Avoid scans for constant sort keys](https://github.com/ClickHouse/ClickHouse/pull/113899) — 13 comments · 0 reactions · closed
- **Pull Request** [Use a continuous primary-key range for whole-metric PromQL selectors of TimeSeries tables](https://github.com/ClickHouse/ClickHouse/pull/114131) — 12 comments · 0 reactions · open
- **Issue** [NATS JetStream pull consumer does not recover after failover (or change server)](https://github.com/ClickHouse/ClickHouse/issues/96651) — 2 comments · 7 reactions · closed
- **Issue** [Push dynamic TopN thresholds into MergeTree reads for ORDER BY ... LIMIT (2-3x on ClickBench Q24/Q26)](https://github.com/ClickHouse/ClickHouse/issues/114639) — 1 comments · 0 reactions · open
- **Pull Request** [Add `borrow_from_cache` object storage and `memory` metadata types](https://github.com/ClickHouse/ClickHouse/pull/100371) — 32 comments · 0 reactions · open
- **Pull Request** [Respect `date_time_overflow_behavior` for numeric temporal casts](https://github.com/ClickHouse/ClickHouse/pull/109299) — 37 comments · 0 reactions · open
- **Pull Request** [Let read-in-order propagate through SpillingHashJoin](https://github.com/ClickHouse/ClickHouse/pull/111973) — 9 comments · 0 reactions · open
- **Pull Request** [Text index: add trivial count optimization](https://github.com/ClickHouse/ClickHouse/pull/111494) — 7 comments · 0 reactions · open
- **Pull Request** [Lazy materialization for reading local Parquet files (`file` / `File`)](https://github.com/ClickHouse/ClickHouse/pull/114262) — 6 comments · 0 reactions · open
- **Pull Request** [Enable reading in reverse order with FINAL for ReplacingMergeTree](https://github.com/ClickHouse/ClickHouse/pull/114479) — 3 comments · 1 reactions · open
- **Pull Request** [Enable the query condition cache for `ORDER BY ... LIMIT n` queries by default](https://github.com/ClickHouse/ClickHouse/pull/114539) — 6 comments · 0 reactions · closed
- **Pull Request** [Fix target access checks for the Alias engine](https://github.com/ClickHouse/ClickHouse/pull/114596) — 6 comments · 0 reactions · open
- **Pull Request** [Fix LazilyReadFromMergeTree optimization with ALIAS columns (#96452)](https://github.com/ClickHouse/ClickHouse/pull/96487) — 31 comments · 1 reactions · open

### [Dragonfly](https://github.com/dragonflydb/dragonfly)

- **Pull Request** [fix(generic): avoid data loss on RENAME when destination write fails](https://github.com/dragonflydb/dragonfly/pull/8053) — 8 comments · 0 reactions · open
- **Pull Request** [fix(search): reject FT.CREATE missing the SCHEMA keyword](https://github.com/dragonflydb/dragonfly/pull/8054) — 7 comments · 0 reactions · closed
- **Pull Request** [fix(pubsub): preserve V2 message ordering](https://github.com/dragonflydb/dragonfly/pull/8075) — 7 comments · 0 reactions · open
- **Issue** [FT.CREATE without SCHEMA returns OK but creates unusable listed index](https://github.com/dragonflydb/dragonfly/issues/7953) — 0 comments · 0 reactions · closed
- **Issue** [Disabled python tests in tests/dragonfly](https://github.com/dragonflydb/dragonfly/issues/8028) — 0 comments · 0 reactions · open
- **Pull Request** [feat(geo): add GEOSEARCHSTORE command](https://github.com/dragonflydb/dragonfly/pull/7984) — 8 comments · 0 reactions · open
- **Pull Request** [chore: remove dead test_replication_onmove_flow](https://github.com/dragonflydb/dragonfly/pull/8078) — 4 comments · 0 reactions · closed
- **Pull Request** [docs: add design doc for replication fanout (NOT FOR MERGE)](https://github.com/dragonflydb/dragonfly/pull/8002) — 1 comments · 0 reactions · open
