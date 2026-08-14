# Data / Messaging / Storage Infrastructure — 2026-08-14

> Factual GitHub evidence collected by Contribution Compass. No LLM analysis is performed.

## Contribution Leads

No evidence-qualified contribution leads changed in this collection.
## Important Updates

### [NATS Server](https://github.com/nats-io/nats-server)

- **Issue** [Pod Memory Leak with Gradual Increase on K8S](https://github.com/nats-io/nats-server/issues/6307) — 20 comments · 8 reactions · open
- **Pull Request** [(2.15) \[ADDED\] Report requested stream config while running at desired origin](https://github.com/nats-io/nats-server/pull/8439) — 5 comments · 1 reactions · closed
- **Pull Request** [(2.15) \[ADDED\] Peer evacuation and reconciliation of assignments](https://github.com/nats-io/nats-server/pull/8443) — 5 comments · 1 reactions · closed
- **Pull Request** [(2.15) \[FIXED\] Evict peer-removed peers for group below quorum](https://github.com/nats-io/nats-server/pull/8452) — 5 comments · 1 reactions · closed
- **Pull Request** [(2.15) \[FIXED\] Migration added offline peers & removed peers before catchup](https://github.com/nats-io/nats-server/pull/8460) — 5 comments · 1 reactions · closed
- **Pull Request** [(2.15) \[ADDED\] JetStream system-wide asset limits](https://github.com/nats-io/nats-server/pull/8337) — 6 comments · 1 reactions · open
- **Pull Request** [(2.15) \[ADDED\] Desired state reconcilitation for scaling and moves](https://github.com/nats-io/nats-server/pull/8432) — 6 comments · 0 reactions · closed
- **Pull Request** [(2.15) NRG: Relax SyncAlways for replicated streams](https://github.com/nats-io/nats-server/pull/8447) — 10 comments · 0 reactions · open
- **Pull Request** [(2.15) \[ADDED\] Drive stream move and cancel move via desired state](https://github.com/nats-io/nats-server/pull/8437) — 5 comments · 0 reactions · closed
- **Pull Request** [(2.15) Raft proposal fast path](https://github.com/nats-io/nats-server/pull/8445) — 8 comments · 0 reactions · open
- **Pull Request** [Make reverse response map removal constant time](https://github.com/nats-io/nats-server/pull/8463) — 0 comments · 2 reactions · open
- **Pull Request** [\[FIXED\] Missing stream snapshot on shutdown, plus test de-flakes](https://github.com/nats-io/nats-server/pull/8465) — 1 comments · 1 reactions · open
- **Pull Request** [\[FIXED\] Reject stream update to replicas > 1 in non-clustered mode](https://github.com/nats-io/nats-server/pull/8464) — 1 comments · 0 reactions · open
- **Pull Request** [(2.15) \[IMPROVED\] Meta consumer assignment APIs & counter-based asset limits](https://github.com/nats-io/nats-server/pull/8466) — 1 comments · 0 reactions · open

### [Redpanda](https://github.com/redpanda-data/redpanda)

- **Pull Request** [\[CORE-15822\] security/audit: make audit initialization controller-leader independent](https://github.com/redpanda-data/redpanda/pull/31411) — 12 comments · 0 reactions · closed
- **Pull Request** [\[CORE-16604\] cluster_link: incremental Schema Registry sync by tailing _schemas](https://github.com/redpanda-data/redpanda/pull/31366) — 8 comments · 0 reactions · open
- **Pull Request** [hashing: back crc32c with abseil instead of google/crc32c](https://github.com/redpanda-data/redpanda/pull/31517) — 8 comments · 0 reactions · closed
- **Pull Request** [pandaproxy: run REST proxy in a dedicated scheduling group](https://github.com/redpanda-data/redpanda/pull/31514) — 4 comments · 0 reactions · open
- **Pull Request** [\[CORE-12930\] - Storage: Some observability improvements for unrecoverable segments](https://github.com/redpanda-data/redpanda/pull/31544) — 4 comments · 0 reactions · open
- **Pull Request** [sr: fix broker abort when a request fails before its deferred authz check](https://github.com/redpanda-data/redpanda/pull/31559) — 5 comments · 0 reactions · open
- **Pull Request** [\[CORE-16908\] cluster_link: incremental Schema Registry sync over the HTTP API](https://github.com/redpanda-data/redpanda/pull/31376) — 7 comments · 0 reactions · open
- **Pull Request** [\[CORE-16631\] tests/rptest: wait for target HWM to settle after failover](https://github.com/redpanda-data/redpanda/pull/31533) — 2 comments · 0 reactions · open
- **Pull Request** [\[v26.2.x\] storage: bump segment_concatenation_test timeout](https://github.com/redpanda-data/redpanda/pull/31570) — 2 comments · 0 reactions · closed
- **Pull Request** [rpk/registry: document print flag exclusivity in help text](https://github.com/redpanda-data/redpanda/pull/31574) — 2 comments · 0 reactions · closed
- **Pull Request** [\[CORE-16806\] - KIP-848: assignor interface and the homogeneous uniform assignor](https://github.com/redpanda-data/redpanda/pull/31579) — 2 comments · 0 reactions · open
- **Pull Request** [Mitigate `offset_not_available` races on follower fetches](https://github.com/redpanda-data/redpanda/pull/31581) — 2 comments · 0 reactions · open
- **Pull Request** [\[INC-1227\] dl/translation: fix busy loop under coordinator backpressure](https://github.com/redpanda-data/redpanda/pull/31419) — 5 comments · 0 reactions · closed
- **Pull Request** [\[CORE-16806\]: KIP-848: Assignor Interface and Uniform Assignors](https://github.com/redpanda-data/redpanda/pull/31426) — 0 comments · 0 reactions · open
- **Pull Request** [\[CORE-16804\] - KIP-848: deterministic subscription-metadata hash](https://github.com/redpanda-data/redpanda/pull/31499) — 0 comments · 0 reactions · open
- **Pull Request** [rpk: consolidate plugin version validation on pkg](https://github.com/redpanda-data/redpanda/pull/31557) — 1 comments · 0 reactions · open
- **Pull Request** [rpk: add stretch cluster grafana dashboard behind --cluster-type flag](https://github.com/redpanda-data/redpanda/pull/31573) — 0 comments · 0 reactions · open
- **Pull Request** [\[v25.3.x\] \[INC-1227\] dl/translation: fix busy loop under coordinator backpressure](https://github.com/redpanda-data/redpanda/pull/31584) — 2 comments · 0 reactions · open
- **Pull Request** [\[v26.2.x\] \[CORE-15822\] security/audit: make audit initialization controller-leader independent](https://github.com/redpanda-data/redpanda/pull/31586) — 2 comments · 0 reactions · open
- **Pull Request** [\[v26.1.x\] \[CORE-15822\] security/audit: make audit initialization controller-leader independent](https://github.com/redpanda-data/redpanda/pull/31588) — 2 comments · 0 reactions · open
- **Pull Request** [cloud_topics: fast partition movement for tiered-storage v2](https://github.com/redpanda-data/redpanda/pull/31589) — 2 comments · 0 reactions · open
- **Pull Request** [\[v26.1.x\] \[INC-1227\] dl/translation: fix busy loop under coordinator backpressure](https://github.com/redpanda-data/redpanda/pull/31582) — 0 comments · 0 reactions · closed
- **Pull Request** [\[v26.2.x\] \[INC-1227\] dl/translation: fix busy loop under coordinator backpressure](https://github.com/redpanda-data/redpanda/pull/31583) — 1 comments · 0 reactions · closed
- **Pull Request** [\[v25.3.x\] \[CORE-15822\] security/audit: make audit initialization controller-leader independent](https://github.com/redpanda-data/redpanda/pull/31587) — 0 comments · 0 reactions · open

### [ClickHouse](https://github.com/ClickHouse/ClickHouse)

- **Pull Request** [Cascades cost-based optimizer for distributed query plans](https://github.com/ClickHouse/ClickHouse/pull/86353) — 7 comments · 22 reactions · open
- **Pull Request** [WIP some perf optimizations](https://github.com/ClickHouse/ClickHouse/pull/81944) — 36 comments · 4 reactions · open
- **Pull Request** [Parallelize read-in-order from a single part with PrefetchingConcatProcessor](https://github.com/ClickHouse/ClickHouse/pull/100391) — 42 comments · 1 reactions · open
- **Pull Request** [Switch the default compression to ZSTD(3) for table data and network](https://github.com/ClickHouse/ClickHouse/pull/108786) — 70 comments · 1 reactions · open
- **Pull Request** [Optimization of `GROUP BY` in the presence of `ORDER BY` and `LIMIT`](https://github.com/ClickHouse/ClickHouse/pull/96630) — 13 comments · 8 reactions · open
- **Pull Request** [Push join key filters into MergeTree index during recursive CTE evaluation](https://github.com/ClickHouse/ClickHouse/pull/97254) — 77 comments · 1 reactions · open
- **Pull Request** [Disable read-in-order when primary key selectivity is poor](https://github.com/ClickHouse/ClickHouse/pull/100377) — 40 comments · 0 reactions · open
- **Pull Request** [Add optimize_row_order_if_no_order_by (reopen #103919)](https://github.com/ClickHouse/ClickHouse/pull/104591) — 45 comments · 0 reactions · open
- **Pull Request** [Materialize column statistics on INSERT for small tables by default](https://github.com/ClickHouse/ClickHouse/pull/109454) — 45 comments · 0 reactions · closed
- **Pull Request** [Minmax indices by default](https://github.com/ClickHouse/ClickHouse/pull/76867) — 81 comments · 0 reactions · open
- **Pull Request** [Enable read_in_order_use_virtual_row by default](https://github.com/ClickHouse/ClickHouse/pull/106215) — 37 comments · 0 reactions · open
- **Pull Request** [Avoid copying data for the NONE compression codec when writing](https://github.com/ClickHouse/ClickHouse/pull/108096) — 36 comments · 0 reactions · open
- **Pull Request** [In case of trivial views, push whole outer query to shards.](https://github.com/ClickHouse/ClickHouse/pull/101791) — 18 comments · 4 reactions · closed
- **Pull Request** [Push ORDER BY from outer query into simple VIEWs for distributed optimization](https://github.com/ClickHouse/ClickHouse/pull/94102) — 23 comments · 3 reactions · closed
- **Pull Request** [Add `GradualResizeProcessor` to limit effective parallelism for GROUP BY on small data volumes](https://github.com/ClickHouse/ClickHouse/pull/99495) — 31 comments · 0 reactions · open
- **Pull Request** [Support column matcher expansion for default value expressions and index expressions](https://github.com/ClickHouse/ClickHouse/pull/105045) — 50 comments · 3 reactions · open
- **Pull Request** [Adaptive Aggregator](https://github.com/ClickHouse/ClickHouse/pull/111459) — 12 comments · 4 reactions · open
- **Pull Request** [Add table function `obfuscate`](https://github.com/ClickHouse/ClickHouse/pull/42701) — 44 comments · 2 reactions · open
- **Pull Request** [Added Parquet Shredded VARIANT Support to ParquetReaderv3](https://github.com/ClickHouse/ClickHouse/pull/102499) — 33 comments · 3 reactions · open
- **Pull Request** [Add Rewrite rules](https://github.com/ClickHouse/ClickHouse/pull/88234) — 62 comments · 1 reactions · open
- **Pull Request** [Push subcolumn reads into subqueries](https://github.com/ClickHouse/ClickHouse/pull/112688) — 15 comments · 1 reactions · open
- **Pull Request** [Revert "Revert "Use a lock-free queue for asynchronous logging""](https://github.com/ClickHouse/ClickHouse/pull/112803) — 19 comments · 0 reactions · open
- **Pull Request** [Push tuple element predicates into Parquet and ORC subcolumn reads](https://github.com/ClickHouse/ClickHouse/pull/113383) — 19 comments · 0 reactions · open
- **Pull Request** [Add leader election for non-replicated MergeTree on shared storage](https://github.com/ClickHouse/ClickHouse/pull/101039) — 88 comments · 0 reactions · open
- **Pull Request** [Support specifying or auto-assigning Parquet field_ids for output columns](https://github.com/ClickHouse/ClickHouse/pull/101783) — 45 comments · 0 reactions · open
- **Pull Request** [Not a fix: "Not-ready Set" exception when buildOrderedSetInplace fails](https://github.com/ClickHouse/ClickHouse/pull/102192) — 54 comments · 0 reactions · open
- **Pull Request** [Parallelize reads from a single Parquet file in StorageFile, again](https://github.com/ClickHouse/ClickHouse/pull/104431) — 71 comments · 0 reactions · open
- **Pull Request** [Accessing tables as files, query construction and out-of-band modification in HTTP interface](https://github.com/ClickHouse/ClickHouse/pull/105249) — 84 comments · 0 reactions · open
- **Pull Request** [Reserve memory for merges up front](https://github.com/ClickHouse/ClickHouse/pull/109433) — 70 comments · 0 reactions · open
- **Pull Request** [Compare stored table definition expressions by AST instead of formatted text](https://github.com/ClickHouse/ClickHouse/pull/110833) — 73 comments · 0 reactions · open

### [Dragonfly](https://github.com/dragonflydb/dragonfly)

- **Issue** [Disabled python tests in tests/dragonfly](https://github.com/dragonflydb/dragonfly/issues/8028) — 0 comments · 0 reactions · open
- **Issue** [test_replicate_old_master](https://github.com/dragonflydb/dragonfly/issues/8063) — 1 comments · 0 reactions · closed
- **Pull Request** [feat(geo): add GEOSEARCHSTORE command](https://github.com/dragonflydb/dragonfly/pull/7984) — 9 comments · 0 reactions · open
- **Issue** [test_pubsub_pipeline_starvation](https://github.com/dragonflydb/dragonfly/issues/8009) — 3 comments · 0 reactions · open
- **Pull Request** [chore: add docs/replication.md](https://github.com/dragonflydb/dragonfly/pull/7997) — 7 comments · 0 reactions · open
- **Issue** [test_replication_info](https://github.com/dragonflydb/dragonfly/issues/7932) — 1 comments · 0 reactions · closed
- **Issue** [test_client_pause_v2_inflight_async_write_gap](https://github.com/dragonflydb/dragonfly/issues/8079) — 1 comments · 0 reactions · open
- **Issue** [ZMPOP RESP2 reply is incompatibile with Redis](https://github.com/dragonflydb/dragonfly/issues/8087) — 0 comments · 0 reactions · open
- **Pull Request** [fix(server): emit expired keyspace events for already-past expirations](https://github.com/dragonflydb/dragonfly/pull/8065) — 4 comments · 0 reactions · closed
- **Pull Request** [fix(tiering): tight small bin fragmentation cutoff](https://github.com/dragonflydb/dragonfly/pull/8081) — 7 comments · 0 reactions · open
- **Pull Request** [fix: test_cron_snapshot_failed_saving](https://github.com/dragonflydb/dragonfly/pull/8083) — 6 comments · 0 reactions · closed
- **Pull Request** [docs: add design doc for replication fanout (NOT FOR MERGE)](https://github.com/dragonflydb/dragonfly/pull/8002) — 1 comments · 0 reactions · open
- **Pull Request** [fix(server): lower table growth margin default](https://github.com/dragonflydb/dragonfly/pull/8080) — 4 comments · 0 reactions · open
- **Pull Request** [fix: SET with a past expiration honors NX/XX/GET and journals the delete](https://github.com/dragonflydb/dragonfly/pull/8082) — 5 comments · 0 reactions · closed
- **Pull Request** [fix(tests): Sample lag continuously in test_replication_info](https://github.com/dragonflydb/dragonfly/pull/8084) — 4 comments · 0 reactions · closed
- **Pull Request** [fix(facade): Handle RESP3 null array response](https://github.com/dragonflydb/dragonfly/pull/8085) — 4 comments · 0 reactions · open
- **Pull Request** [test: un-skip graceful shutdown test by asserting the guaranteed durability contract](https://github.com/dragonflydb/dragonfly/pull/8086) — 4 comments · 0 reactions · open
- **Pull Request** [fix(server): probe heterogeneous blocking waiters instead of aborting…](https://github.com/dragonflydb/dragonfly/pull/8088) — 4 comments · 0 reactions · open
- **Pull Request** [fix(server): emit expired keyspace events when the new expiration is already in the past](https://github.com/dragonflydb/dragonfly/pull/7915) — 3 comments · 0 reactions · closed
