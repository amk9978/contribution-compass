# Data / Messaging / Storage Infrastructure — 2026-08-13

> Factual GitHub evidence collected by Contribution Compass. No LLM analysis is performed.

## Contribution Leads

No evidence-qualified contribution leads changed in this collection.
## Important Updates

### [NATS Server](https://github.com/nats-io/nats-server)

- **Release** [Release v2.14.5](https://github.com/nats-io/nats-server/releases/tag/v2.14.5) — 
- **Release** [Release v2.12.15](https://github.com/nats-io/nats-server/releases/tag/v2.12.15) — 
- **Pull Request** [(2.15) \[IMPROVED\] Source stream recreation detection](https://github.com/nats-io/nats-server/pull/8384) — 9 comments · 2 reactions · open
- **Issue** [Always retain last message for each subject in a stream](https://github.com/nats-io/nats-server/issues/5811) — 2 comments · 0 reactions · open
- **Pull Request** [\[ADDED\] Support PROXY protocol for websocket listeners](https://github.com/nats-io/nats-server/pull/8133) — 2 comments · 2 reactions · open
- **Pull Request** [(2.15) \[ADDED\] Report requested stream config while running at desired origin](https://github.com/nats-io/nats-server/pull/8439) — 5 comments · 1 reactions · open
- **Pull Request** [(2.15) \[ADDED\] Desired state reconcilitation for scaling and moves](https://github.com/nats-io/nats-server/pull/8432) — 6 comments · 0 reactions · open
- **Pull Request** [(2.15) \[FIXED\] Evict peer-removed peers for group below quorum](https://github.com/nats-io/nats-server/pull/8452) — 3 comments · 1 reactions · open
- **Pull Request** [De-flake TestJetStreamSuperClusterStreamDirectGetMirrorQueueGroup](https://github.com/nats-io/nats-server/pull/8457) — 2 comments · 1 reactions · closed
- **Pull Request** [(2.15) \[FIXED\] Migration added offline peers & removed peers before catchup](https://github.com/nats-io/nats-server/pull/8460) — 3 comments · 1 reactions · open
- **Pull Request** [\[IMPROVED\] Sync the block directory once in syncBlocks](https://github.com/nats-io/nats-server/pull/8461) — 2 comments · 1 reactions · closed
- **Pull Request** [(2.15) \[ADDED\] Drive stream move and cancel move via desired state](https://github.com/nats-io/nats-server/pull/8437) — 5 comments · 0 reactions · open
- **Pull Request** [Update dependencies](https://github.com/nats-io/nats-server/pull/8459) — 1 comments · 1 reactions · closed
- **Pull Request** [\[FIXED\] Extend dios to cover filestore block syncs](https://github.com/nats-io/nats-server/pull/8462) — 0 comments · 1 reactions · closed
- **Pull Request** [(2.15) \[ADDED\] Peer evacuation and reconciliation of assignments](https://github.com/nats-io/nats-server/pull/8443) — 3 comments · 0 reactions · open

### [Redpanda](https://github.com/redpanda-data/redpanda)

- **Issue** [Add healthcheck for Docker](https://github.com/redpanda-data/redpanda/issues/2749) — 7 comments · 1 reactions · closed
- **Issue** [Add rpk standalone installscript for OSX,Linux](https://github.com/redpanda-data/redpanda/issues/4191) — 10 comments · 0 reactions · closed
- **Pull Request** [bazel: bump the toolchain sysroot to Ubuntu 24.04](https://github.com/redpanda-data/redpanda/pull/31560) — 10 comments · 0 reactions · open
- **Issue** [rpk connect upgrade rejects all currently installed Connect versions (two-digit version regex in VersionFromString)](https://github.com/redpanda-data/redpanda/issues/31545) — 0 comments · 0 reactions · closed
- **Issue** [\[v26.2.x\] rpk connect upgrade rejects all currently installed Connect versions (two-digit version regex in VersionFromString)](https://github.com/redpanda-data/redpanda/issues/31548) — 0 comments · 0 reactions · closed
- **Issue** [\[v26.1.x\] rpk connect upgrade rejects all currently installed Connect versions (two-digit version regex in VersionFromString)](https://github.com/redpanda-data/redpanda/issues/31550) — 0 comments · 0 reactions · closed
- **Issue** [\[v25.3.x\] rpk connect upgrade rejects all currently installed Connect versions (two-digit version regex in VersionFromString)](https://github.com/redpanda-data/redpanda/issues/31552) — 0 comments · 0 reactions · closed
- **Pull Request** [bazel/seastar: enable task queue shuffling in debug builds](https://github.com/redpanda-data/redpanda/pull/31139) — 8 comments · 0 reactions · open
- **Pull Request** [\[CORE-16604\] cluster_link: incremental Schema Registry sync by tailing _schemas](https://github.com/redpanda-data/redpanda/pull/31366) — 8 comments · 0 reactions · open
- **Pull Request** [\[CORE-15822\] security/audit: make audit initialization controller-leader independent](https://github.com/redpanda-data/redpanda/pull/31411) — 9 comments · 0 reactions · open
- **Pull Request** [\[ CORE-14329\] tests/node_ops: tolerate chaos testing in decommission progress check](https://github.com/redpanda-data/redpanda/pull/31461) — 6 comments · 0 reactions · closed
- **Pull Request** [hashing: back crc32c with abseil instead of google/crc32c](https://github.com/redpanda-data/redpanda/pull/31517) — 7 comments · 0 reactions · closed
- **Pull Request** [rpk: fix grammar and wording defects in help text](https://github.com/redpanda-data/redpanda/pull/31521) — 7 comments · 0 reactions · open
- **Pull Request** [\[v25.3.x\] Kgo Verifier Producer set linger to 0](https://github.com/redpanda-data/redpanda/pull/29258) — 5 comments · 0 reactions · closed
- **Pull Request** [metrics: remove one-shot IMDS connect probe](https://github.com/redpanda-data/redpanda/pull/31301) — 5 comments · 0 reactions · closed
- **Pull Request** [bazel: add a remote_download_minimal config to cut CI download volume](https://github.com/redpanda-data/redpanda/pull/31536) — 5 comments · 0 reactions · closed
- **Pull Request** [Tq more changes](https://github.com/redpanda-data/redpanda/pull/31542) — 5 comments · 0 reactions · open
- **Pull Request** [rpk/connect: don't cap version segments at two digits in VersionFromString](https://github.com/redpanda-data/redpanda/pull/31546) — 4 comments · 0 reactions · closed
- **Pull Request** [sr: fix broker abort when a request fails before its deferred authz check](https://github.com/redpanda-data/redpanda/pull/31559) — 4 comments · 0 reactions · open
- **Pull Request** [\[v25.3.x\] Implement cross-segment prefetching for small segments in cloud storage reads](https://github.com/redpanda-data/redpanda/pull/29795) — 3 comments · 0 reactions · closed
- **Pull Request** [\[v25.3.x\] kafka/server: cap fetch memory allocation at max message size limit](https://github.com/redpanda-data/redpanda/pull/30314) — 2 comments · 0 reactions · closed
- **Pull Request** [\[v25.3.x\] `compaction`: avoid recompression of unchanged batches](https://github.com/redpanda-data/redpanda/pull/30673) — 2 comments · 0 reactions · closed
- **Pull Request** [\[v26.1.x\] kafka/client: authenticate under the reconnect mutex](https://github.com/redpanda-data/redpanda/pull/31192) — 2 comments · 0 reactions · closed
- **Pull Request** [rptest: add OOM crash self-test; allow-list memory diagnostics](https://github.com/redpanda-data/redpanda/pull/31365) — 2 comments · 0 reactions · open
- **Pull Request** [k/s/tests: deflake fetch_memory_units cross-shard test](https://github.com/redpanda-data/redpanda/pull/31512) — 2 comments · 0 reactions · closed
- **Pull Request** [\[v26.1.x\] bazel: define an empty ci-remote-cache config](https://github.com/redpanda-data/redpanda/pull/31540) — 3 comments · 0 reactions · closed
- **Pull Request** [\[CORE-12930\] - Storage: Some observability improvements for unrecoverable segments](https://github.com/redpanda-data/redpanda/pull/31544) — 2 comments · 0 reactions · open
- **Pull Request** [rpk: add load-factor dashboard to generate grafana-dashboard](https://github.com/redpanda-data/redpanda/pull/31554) — 3 comments · 0 reactions · closed
- **Pull Request** [\[v25.3.x\] Add comparison operators to iobuf fuzz test (and other enchancements)](https://github.com/redpanda-data/redpanda/pull/29280) — 1 comments · 0 reactions · closed
- **Pull Request** [\[v26.1.x\] config: refresh iceberg_enabled docstring](https://github.com/redpanda-data/redpanda/pull/30531) — 0 comments · 0 reactions · closed

### [ClickHouse](https://github.com/ClickHouse/ClickHouse)

- **Pull Request** [Cascades cost-based optimizer for distributed query plans](https://github.com/ClickHouse/ClickHouse/pull/86353) — 7 comments · 21 reactions · open
- **Pull Request** [Columns Cache](https://github.com/ClickHouse/ClickHouse/pull/96844) — 77 comments · 5 reactions · open
- **Pull Request** [WIP some perf optimizations](https://github.com/ClickHouse/ClickHouse/pull/81944) — 35 comments · 4 reactions · open
- **Pull Request** [Parallelize read-in-order from a single part with PrefetchingConcatProcessor](https://github.com/ClickHouse/ClickHouse/pull/100391) — 41 comments · 1 reactions · open
- **Pull Request** [Switch the default compression to ZSTD(3) for table data and network](https://github.com/ClickHouse/ClickHouse/pull/108786) — 69 comments · 1 reactions · open
- **Pull Request** [Push join key filters into MergeTree index during recursive CTE evaluation](https://github.com/ClickHouse/ClickHouse/pull/97254) — 77 comments · 1 reactions · open
- **Pull Request** [Disable read-in-order when primary key selectivity is poor](https://github.com/ClickHouse/ClickHouse/pull/100377) — 40 comments · 0 reactions · open
- **Pull Request** [Add optimize_row_order_if_no_order_by (reopen #103919)](https://github.com/ClickHouse/ClickHouse/pull/104591) — 44 comments · 0 reactions · open
- **Pull Request** [Parallel full sorting merge join (parallel_full_sorting_merge)](https://github.com/ClickHouse/ClickHouse/pull/109005) — 37 comments · 2 reactions · closed
- **Pull Request** [Materialize column statistics on INSERT for small tables by default](https://github.com/ClickHouse/ClickHouse/pull/109454) — 44 comments · 0 reactions · closed
- **Pull Request** [Minmax indices by default](https://github.com/ClickHouse/ClickHouse/pull/76867) — 79 comments · 0 reactions · open
- **Pull Request** [Enable read_in_order_use_virtual_row by default](https://github.com/ClickHouse/ClickHouse/pull/106215) — 37 comments · 0 reactions · open
- **Pull Request** [Improve the performance of `MODIFY TTL`](https://github.com/ClickHouse/ClickHouse/pull/63383) — 33 comments · 1 reactions · open
- **Pull Request** [Async insert parallel parsing](https://github.com/ClickHouse/ClickHouse/pull/79509) — 24 comments · 2 reactions · open
- **Pull Request** [Add groupBloomFilter aggregate function and bloomFilterContains scalar function](https://github.com/ClickHouse/ClickHouse/pull/101841) — 5 comments · 13 reactions · open
- **Pull Request** [Support column matcher expansion for default value expressions and index expressions](https://github.com/ClickHouse/ClickHouse/pull/105045) — 49 comments · 3 reactions · open
- **Pull Request** [Iceberg: propagate table UUID from REST catalog to avoid metadata cac…](https://github.com/ClickHouse/ClickHouse/pull/99981) — 29 comments · 0 reactions · open
- **Pull Request** [In case of trivial views, push whole outer query to shards.](https://github.com/ClickHouse/ClickHouse/pull/101791) — 15 comments · 3 reactions · open
- **Pull Request** [Adaptive Aggregator](https://github.com/ClickHouse/ClickHouse/pull/111459) — 11 comments · 4 reactions · open
- **Pull Request** [Add `GradualResizeProcessor` to limit effective parallelism for GROUP BY on small data volumes](https://github.com/ClickHouse/ClickHouse/pull/99495) — 30 comments · 0 reactions · open
- **Pull Request** [Add table function `obfuscate`](https://github.com/ClickHouse/ClickHouse/pull/42701) — 44 comments · 2 reactions · open
- **Pull Request** [Randomize tests with DETACH/ATTACH table before query execution](https://github.com/ClickHouse/ClickHouse/pull/96130) — 91 comments · 2 reactions · open
- **Issue** [Range condition in JOIN ON against a single-row side is not used for index analysis (no part pruning) since the logical join step became default](https://github.com/ClickHouse/ClickHouse/issues/112586) — 6 comments · 2 reactions · closed
- **Pull Request** [Push down volume-reducing functions in query plan](https://github.com/ClickHouse/ClickHouse/pull/106199) — 12 comments · 2 reactions · open
- **Pull Request** [Implement CREATE HANDLER: SQL-defined HTTP handlers](https://github.com/ClickHouse/ClickHouse/pull/106231) — 79 comments · 1 reactions · open
- **Pull Request** [Add Rewrite rules](https://github.com/ClickHouse/ClickHouse/pull/88234) — 61 comments · 1 reactions · open
- **Pull Request** [Added Parquet Shredded VARIANT Support to ParquetReaderv3](https://github.com/ClickHouse/ClickHouse/pull/102499) — 31 comments · 3 reactions · open
- **Pull Request** [Push subcolumn reads into subqueries](https://github.com/ClickHouse/ClickHouse/pull/112688) — 15 comments · 1 reactions · open
- **Pull Request** [Rewrite `length(arrayFilter(f, arr))` to `arrayCount(f, arr)`](https://github.com/ClickHouse/ClickHouse/pull/113023) — 19 comments · 0 reactions · open
- **Pull Request** [Add leader election for non-replicated MergeTree on shared storage](https://github.com/ClickHouse/ClickHouse/pull/101039) — 87 comments · 0 reactions · open

### [Dragonfly](https://github.com/dragonflydb/dragonfly)

- **Issue** [test_replicaof_reject_on_load](https://github.com/dragonflydb/dragonfly/issues/5662) — 37 comments · 0 reactions · open
- **Pull Request** [feat: add time limitation for replication backlog](https://github.com/dragonflydb/dragonfly/pull/8039) — 10 comments · 0 reactions · open
- **Issue** [Blocked XREADGROUP is not woken when the watched stream is deleted or retyped](https://github.com/dragonflydb/dragonfly/issues/7903) — 0 comments · 0 reactions · closed
- **Issue** [XREAD BLOCK replies in RESP2 array shape on a RESP3 connection](https://github.com/dragonflydb/dragonfly/issues/8056) — 1 comments · 0 reactions · closed
- **Issue** [test_replicate_old_master](https://github.com/dragonflydb/dragonfly/issues/8063) — 0 comments · 0 reactions · open
- **Issue** [P1 — A heterogeneous blocking queue can hide XREADGROUP forever](https://github.com/dragonflydb/dragonfly/issues/8067) — 0 comments · 0 reactions · open
- **Issue** [P1 — `NotifyPending()` is reentrant through a suspending expiry checker](https://github.com/dragonflydb/dragonfly/issues/8068) — 0 comments · 0 reactions · open
- **Issue** [P1 — Active expiry never runs for non-default namespaces](https://github.com/dragonflydb/dragonfly/issues/8069) — 0 comments · 0 reactions · open
- **Issue** [P1 — Multi-stream `XREADGROUP` mutates group state and then returns an error](https://github.com/dragonflydb/dragonfly/issues/8070) — 0 comments · 0 reactions · open
- **Issue** [P1 — A blocked multi-stream read returns only one stream when several become ready together](https://github.com/dragonflydb/dragonfly/issues/8071) — 0 comments · 0 reactions · open
- **Issue** [P2 — Multi-shard error precedence follows shard placement instead of argument order](https://github.com/dragonflydb/dragonfly/issues/8072) — 0 comments · 0 reactions · open
- **Issue** [P2 — `DFLYCLUSTER FLUSHSLOTS` operates on the default namespace regardless of the caller](https://github.com/dragonflydb/dragonfly/issues/8073) — 0 comments · 0 reactions · open
- **Issue** [P3 — FLUSHSLOTS TOCTOU between the validation and action hops of a woken multi-stream read](https://github.com/dragonflydb/dragonfly/issues/8074) — 0 comments · 0 reactions · open
- **Issue** [Return RESP3 null for empty XREAD and XREADGROUP replies](https://github.com/dragonflydb/dragonfly/issues/8076) — 0 comments · 0 reactions · open
- **Pull Request** [chore: add docs/replication.md](https://github.com/dragonflydb/dragonfly/pull/7997) — 6 comments · 0 reactions · open
- **Pull Request** [fix(generic): avoid data loss on RENAME when destination write fails](https://github.com/dragonflydb/dragonfly/pull/8053) — 7 comments · 0 reactions · open
- **Pull Request** [fix(search): reject FT.CREATE missing the SCHEMA keyword](https://github.com/dragonflydb/dragonfly/pull/8054) — 6 comments · 0 reactions · open
- **Pull Request** [fix(cluster): scope slot migration finalize pause to migrated slots only](https://github.com/dragonflydb/dragonfly/pull/8058) — 6 comments · 0 reactions · open
- **Pull Request** [fix(pubsub): preserve V2 message ordering](https://github.com/dragonflydb/dragonfly/pull/8075) — 7 comments · 0 reactions · open
- **Pull Request** [fix(tiering): preserve offloaded hashes during serialization](https://github.com/dragonflydb/dragonfly/pull/8026) — 5 comments · 0 reactions · closed
- **Pull Request** [chore(server): Prefetch + cid caching for speedup](https://github.com/dragonflydb/dragonfly/pull/8033) — 5 comments · 0 reactions · closed
- **Pull Request** [ci(tests): add scheduled e2e workflow for ioredis client](https://github.com/dragonflydb/dragonfly/pull/8062) — 4 comments · 0 reactions · open
- **Pull Request** [fix(stream): Reply with RESP3 map for XREAD BLOCK](https://github.com/dragonflydb/dragonfly/pull/8064) — 4 comments · 0 reactions · closed
- **Pull Request** [fix(server): emit expired keyspace events for already-past expirations](https://github.com/dragonflydb/dragonfly/pull/8065) — 4 comments · 0 reactions · open
- **Pull Request** [server: Fix stream size memory accounting](https://github.com/dragonflydb/dragonfly/pull/8066) — 4 comments · 0 reactions · open
- **Pull Request** [fix(tiering): Use TraverseBySegmentOrder and export more metrics/configs](https://github.com/dragonflydb/dragonfly/pull/8077) — 4 comments · 0 reactions · open
- **Pull Request** [Use pcre2 regex & enable auto async](https://github.com/dragonflydb/dragonfly/pull/6991) — 3 comments · 0 reactions · closed
