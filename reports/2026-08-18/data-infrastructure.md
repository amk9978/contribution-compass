# Data / Messaging / Storage Infrastructure — 2026-08-18

> Factual GitHub evidence collected by Contribution Compass. No LLM analysis is performed.

## Contribution Leads

### [allow_non_metadata_alters=0 does not block many mutation-triggering ALTERs and its documentation is unclear](https://github.com/ClickHouse/ClickHouse/issues/115058)

- Project: `ClickHouse/ClickHouse`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

## Important Updates

### [NATS Server](https://github.com/nats-io/nats-server)

- **Pull Request** [(2.15) Stream backup/restore v2](https://github.com/nats-io/nats-server/pull/7882) — 18 comments · 0 reactions · open
- **Pull Request** [Make reverse response map removal constant time](https://github.com/nats-io/nats-server/pull/8463) — 3 comments · 3 reactions · open
- **Issue** [Batch fast-batch JetStream proposals at the stream-to-RAFT boundary](https://github.com/nats-io/nats-server/issues/8325) — 5 comments · 1 reactions · open
- **Issue** [CRITICAL JetStream atomic batch publish leaves per-batch staging directories under <stream>/batches after commit](https://github.com/nats-io/nats-server/issues/8472) — 3 comments · 0 reactions · open
- **Pull Request** [(2.15) NRG: Relax SyncAlways for replicated streams](https://github.com/nats-io/nats-server/pull/8447) — 10 comments · 0 reactions · open
- **Pull Request** [\[FIXED\] Missing stream snapshot on shutdown, plus test de-flakes](https://github.com/nats-io/nats-server/pull/8465) — 7 comments · 1 reactions · closed
- **Pull Request** [(2.15) \[IMPROVED\] MQTT: Pipeline inbound QoS1 PUBLISH JetStream stores](https://github.com/nats-io/nats-server/pull/8415) — 4 comments · 2 reactions · open
- **Pull Request** [(2.15) Raft proposal fast path](https://github.com/nats-io/nats-server/pull/8445) — 8 comments · 0 reactions · open
- **Pull Request** [\[FIXED\] Preserve stream created time after recovery](https://github.com/nats-io/nats-server/pull/8471) — 4 comments · 1 reactions · open
- **Pull Request** [(2.15) \[IMPROVED\] Meta consumer assignment APIs & counter-based asset limits](https://github.com/nats-io/nats-server/pull/8466) — 3 comments · 1 reactions · open
- **Pull Request** [\[FIXED\] Inline block compaction ignores SyncAlways](https://github.com/nats-io/nats-server/pull/8475) — 2 comments · 1 reactions · open
- **Pull Request** [\[FIXED\] Reject stream update to replicas > 1 in non-clustered mode](https://github.com/nats-io/nats-server/pull/8464) — 1 comments · 0 reactions · closed
- **Pull Request** [fix: check AddWeightedMappings error in updateAccountClaimsWithRefresh](https://github.com/nats-io/nats-server/pull/8473) — 1 comments · 1 reactions · open
- **Pull Request** [(2.15) \[IMPROVED\] MQTT: Pipeline QoS2 PUBLISH and PUBREL processing](https://github.com/nats-io/nats-server/pull/8416) — 2 comments · 0 reactions · open
- **Pull Request** [(2.15) \[FIXED\] Remove leftover atomic-batch staging dirs after cleanup](https://github.com/nats-io/nats-server/pull/8474) — 2 comments · 0 reactions · open

### [Redpanda](https://github.com/redpanda-data/redpanda)

- **Pull Request** [ts-ct-migration: partition_mode substrate \[PR 0\]](https://github.com/redpanda-data/redpanda/pull/30977) — 18 comments · 0 reactions · open
- **Pull Request** [\[CORE-16604\] cluster_link: incremental Schema Registry sync by tailing _schemas](https://github.com/redpanda-data/redpanda/pull/31366) — 11 comments · 0 reactions · open
- **Pull Request** [hashing: back crc32c with abseil instead of google/crc32c](https://github.com/redpanda-data/redpanda/pull/31517) — 10 comments · 0 reactions · closed
- **Issue** [\[v26.2.x\] rpk connect upgrade rejects all currently installed Connect versions (two-digit version regex in VersionFromString)](https://github.com/redpanda-data/redpanda/issues/31548) — 0 comments · 0 reactions · closed
- **Issue** [\[v26.1.x\] rpk connect upgrade rejects all currently installed Connect versions (two-digit version regex in VersionFromString)](https://github.com/redpanda-data/redpanda/issues/31550) — 0 comments · 0 reactions · closed
- **Issue** [\[v25.3.x\] rpk connect upgrade rejects all currently installed Connect versions (two-digit version regex in VersionFromString)](https://github.com/redpanda-data/redpanda/issues/31552) — 0 comments · 0 reactions · closed
- **Pull Request** [bazel/seastar: enable task queue shuffling in debug builds](https://github.com/redpanda-data/redpanda/pull/31139) — 8 comments · 0 reactions · open
- **Pull Request** [\[CORE-16908\] cluster_link: incremental Schema Registry sync over the HTTP API](https://github.com/redpanda-data/redpanda/pull/31376) — 8 comments · 0 reactions · open
- **Pull Request** [sr: fix broker abort when a request fails before its deferred authz check](https://github.com/redpanda-data/redpanda/pull/31559) — 9 comments · 0 reactions · closed
- **Pull Request** [\[CORE-16806\] - KIP-848: assignor interface and the homogeneous uniform assignor](https://github.com/redpanda-data/redpanda/pull/31579) — 7 comments · 0 reactions · open
- **Pull Request** [cloud_topics: fast partition movement for tiered-storage v2](https://github.com/redpanda-data/redpanda/pull/31589) — 7 comments · 0 reactions · open
- **Issue** [\[v26.2.x\] schema_registry: pre-flight metadata probe auto-creates _schemas with cluster defaults (cleanup.policy=delete) when auto_create_topics_enabled=true](https://github.com/redpanda-data/redpanda/issues/31235) — 0 comments · 0 reactions · closed
- **Issue** [\[v26.2.x\] rpk connect install --connect-version rejects all Connect versions since 4.100.0 (two-digit version regex)](https://github.com/redpanda-data/redpanda/issues/31446) — 0 comments · 0 reactions · closed
- **Issue** [Add CPU-load caution to `enable_schema_id_validation` property description](https://github.com/redpanda-data/redpanda/issues/31596) — 0 comments · 0 reactions · open
- **Pull Request** [\[CORE-16998, CORE-17000, CORE-17001\] - Consumer Groups (Classic): Fix some bugs where the offset map could diverge from the log](https://github.com/redpanda-data/redpanda/pull/31483) — 4 comments · 0 reactions · open
- **Pull Request** [Tq more changes](https://github.com/redpanda-data/redpanda/pull/31542) — 5 comments · 0 reactions · open
- **Pull Request** [\[v25.3.x\] Implement cross-segment prefetching for small segments in cloud storage reads](https://github.com/redpanda-data/redpanda/pull/29795) — 3 comments · 0 reactions · closed
- **Pull Request** [\[v25.3.x\] kafka/server: cap fetch memory allocation at max message size limit](https://github.com/redpanda-data/redpanda/pull/30314) — 2 comments · 0 reactions · closed
- **Pull Request** [\[CORE-16804\] - KIP-848: deterministic subscription-metadata hash](https://github.com/redpanda-data/redpanda/pull/31499) — 2 comments · 0 reactions · open
- **Pull Request** [\[v26.2.x\] storage: bump segment_concatenation_test timeout](https://github.com/redpanda-data/redpanda/pull/31570) — 2 comments · 0 reactions · closed
- **Pull Request** [tests: make the llvm-symbolizer shim a static binary](https://github.com/redpanda-data/redpanda/pull/31578) — 3 comments · 0 reactions · open
- **Pull Request** [Mitigate `offset_not_available` races on follower fetches](https://github.com/redpanda-data/redpanda/pull/31581) — 2 comments · 0 reactions · open
- **Pull Request** [\[v26.2.x\] \[CORE-15822\] security/audit: make audit initialization controller-leader independent](https://github.com/redpanda-data/redpanda/pull/31586) — 3 comments · 0 reactions · closed
- **Pull Request** [\[v26.1.x\] \[CORE-15822\] security/audit: make audit initialization controller-leader independent](https://github.com/redpanda-data/redpanda/pull/31588) — 3 comments · 0 reactions · closed
- **Pull Request** [rpc/transport: retain memory semaphore units in queued request entry](https://github.com/redpanda-data/redpanda/pull/31594) — 3 comments · 0 reactions · open
- **Pull Request** [\[v26.2.x\] rpk/go tools: bump otel to v1.44.0 (snyk finding)](https://github.com/redpanda-data/redpanda/pull/31284) — 5 comments · 0 reactions · closed
- **Pull Request** [\[v26.2.x\] \[CORE-16742\] cluster_link: fix leaked "Partition not found" future in shadow-link reconciliation](https://github.com/redpanda-data/redpanda/pull/31287) — 5 comments · 0 reactions · closed
- **Pull Request** [kafka/server: reject client-produced control batches](https://github.com/redpanda-data/redpanda/pull/31369) — 4 comments · 0 reactions · closed
- **Pull Request** [\[CORE-16806\]: KIP-848: Assignor Interface and Uniform Assignors](https://github.com/redpanda-data/redpanda/pull/31426) — 0 comments · 0 reactions · open
- **Pull Request** [\[v26.2.x\] bazel: define an empty ci-remote-cache config](https://github.com/redpanda-data/redpanda/pull/31538) — 1 comments · 0 reactions · closed

### [ClickHouse](https://github.com/ClickHouse/ClickHouse)

- **Pull Request** [Cascades cost-based optimizer for distributed query plans](https://github.com/ClickHouse/ClickHouse/pull/86353) — 7 comments · 22 reactions · closed
- **Pull Request** [Columns Cache](https://github.com/ClickHouse/ClickHouse/pull/96844) — 78 comments · 5 reactions · open
- **Pull Request** [Fix count distinct rewrite safety](https://github.com/ClickHouse/ClickHouse/pull/81944) — 37 comments · 4 reactions · open
- **Pull Request** [Optimization of `GROUP BY` in the presence of `ORDER BY` and `LIMIT`](https://github.com/ClickHouse/ClickHouse/pull/96630) — 14 comments · 8 reactions · open
- **Pull Request** [Switch the default compression to ZSTD(3) for table data and network](https://github.com/ClickHouse/ClickHouse/pull/108786) — 72 comments · 1 reactions · open
- **Pull Request** [Push join key filters into MergeTree index during recursive CTE evaluation](https://github.com/ClickHouse/ClickHouse/pull/97254) — 81 comments · 1 reactions · open
- **Pull Request** [Disable read-in-order when primary key selectivity is poor](https://github.com/ClickHouse/ClickHouse/pull/100377) — 40 comments · 0 reactions · open
- **Pull Request** [Parallel read in order with multiple parts](https://github.com/ClickHouse/ClickHouse/pull/100394) — 73 comments · 0 reactions · open
- **Pull Request** [Add optimize_row_order_if_no_order_by (reopen #103919)](https://github.com/ClickHouse/ClickHouse/pull/104591) — 45 comments · 0 reactions · open
- **Pull Request** [Enable read_in_order_use_virtual_row by default](https://github.com/ClickHouse/ClickHouse/pull/106215) — 42 comments · 0 reactions · closed
- **Pull Request** [Minmax indices by default](https://github.com/ClickHouse/ClickHouse/pull/76867) — 88 comments · 0 reactions · open
- **Pull Request** [Improve the performance of `MODIFY TTL`](https://github.com/ClickHouse/ClickHouse/pull/63383) — 34 comments · 1 reactions · open
- **Pull Request** [Avoid copying data for the NONE compression codec when writing](https://github.com/ClickHouse/ClickHouse/pull/108096) — 37 comments · 0 reactions · open
- **Pull Request** [Add groupBloomFilter aggregate function and bloomFilterContains scalar function](https://github.com/ClickHouse/ClickHouse/pull/101841) — 6 comments · 13 reactions · open
- **Pull Request** [Add `GradualResizeProcessor` to limit effective parallelism for GROUP BY on small data volumes](https://github.com/ClickHouse/ClickHouse/pull/99495) — 35 comments · 0 reactions · open
- **Release** [Release v25.8.30.16-lts](https://github.com/ClickHouse/ClickHouse/releases/tag/v25.8.30.16-lts) — 
- **Release** [Release v26.3.18.32-lts](https://github.com/ClickHouse/ClickHouse/releases/tag/v26.3.18.32-lts) — 
- **Pull Request** [Support column matcher expansion for default value expressions and index expressions](https://github.com/ClickHouse/ClickHouse/pull/105045) — 51 comments · 3 reactions · open
- **Pull Request** [Predistinct step will use bf as first pass filter before hashset](https://github.com/ClickHouse/ClickHouse/pull/77728) — 22 comments · 2 reactions · open
- **Pull Request** [Randomize tests with DETACH/ATTACH table before query execution](https://github.com/ClickHouse/ClickHouse/pull/96130) — 91 comments · 2 reactions · open
- **Pull Request** [Added Parquet Shredded VARIANT Support to ParquetReaderv3](https://github.com/ClickHouse/ClickHouse/pull/102499) — 35 comments · 3 reactions · open
- **Pull Request** [Push down volume-reducing functions in query plan](https://github.com/ClickHouse/ClickHouse/pull/106199) — 15 comments · 2 reactions · open
- **Pull Request** [Push subcolumn reads into subqueries](https://github.com/ClickHouse/ClickHouse/pull/112688) — 19 comments · 1 reactions · open
- **Pull Request** [Make `arrayCount` return `UInt64` and rewrite `length(arrayFilter(...))`](https://github.com/ClickHouse/ClickHouse/pull/113023) — 23 comments · 0 reactions · open
- **Pull Request** [Make `if` with constant branches return `LowCardinality`](https://github.com/ClickHouse/ClickHouse/pull/80263) — 38 comments · 2 reactions · open
- **Pull Request** [Fix ALTER TABLE MODIFY TTL with DateTime causing data loss on 32-bit overflow](https://github.com/ClickHouse/ClickHouse/pull/101793) — 21 comments · 0 reactions · open
- **Pull Request** [Add SQLite input/output format](https://github.com/ClickHouse/ClickHouse/pull/104510) — 59 comments · 1 reactions · open
- **Pull Request** [Add Rewrite rules](https://github.com/ClickHouse/ClickHouse/pull/88234) — 63 comments · 1 reactions · open
- **Pull Request** [Add spatial_bbox skip index for MergeTree geometry columns](https://github.com/ClickHouse/ClickHouse/pull/104437) — 14 comments · 1 reactions · open
- **Pull Request** [Use `HashSet` for aggregations without aggregates](https://github.com/ClickHouse/ClickHouse/pull/108862) — 11 comments · 2 reactions · open

### [Dragonfly](https://github.com/dragonflydb/dragonfly)

- **Issue** [test_replicaof_reject_on_load](https://github.com/dragonflydb/dragonfly/issues/5662) — 40 comments · 0 reactions · open
- **Pull Request** [fix(facade): log V2 traffic before dispatch](https://github.com/dragonflydb/dragonfly/pull/8096) — 12 comments · 0 reactions · open
- **Issue** [Disabled python tests in tests/dragonfly](https://github.com/dragonflydb/dragonfly/issues/8028) — 0 comments · 0 reactions · open
- **Issue** [Tiering: Small bins don't account for key size](https://github.com/dragonflydb/dragonfly/issues/8029) — 1 comments · 1 reactions · closed
- **Pull Request** [feat(geo): add GEOSEARCHSTORE command](https://github.com/dragonflydb/dragonfly/pull/7984) — 9 comments · 0 reactions · open
- **Pull Request** [fix(tiering): tight small bin fragmentation cutoff](https://github.com/dragonflydb/dragonfly/pull/8081) — 8 comments · 0 reactions · closed
- **Issue** [crash: main_service.cc:1669\] Check failed: rb->RepliesRecorded() > replies_recorded_ (0 vs. 0) CF.ADD](https://github.com/dragonflydb/dragonfly/issues/8102) — 2 comments · 0 reactions · open
- **Pull Request** [ci(tests): add scheduled e2e workflow for ioredis client](https://github.com/dragonflydb/dragonfly/pull/8062) — 6 comments · 0 reactions · open
- **Pull Request** [fix(pubsub): preserve V2 message ordering](https://github.com/dragonflydb/dragonfly/pull/8075) — 7 comments · 0 reactions · open
- **Issue** [test_tiered_entries](https://github.com/dragonflydb/dragonfly/issues/8012) — 0 comments · 0 reactions · closed
- **Issue** [crash: main_service.cc:2241\] Script <sha> not found in script mgr — SCRIPT FLAGS on an unknown sha then EVALSHA](https://github.com/dragonflydb/dragonfly/issues/8103) — 0 comments · 0 reactions · open
- **Issue** [BF.LOADCHUNK of a header-only chunk produces an unloadable snapshot (data loss on restart) and aborts on COPY at generic_family.cc:435](https://github.com/dragonflydb/dragonfly/issues/8104) — 0 comments · 0 reactions · open
- **Pull Request** [server: Fix stream size memory accounting](https://github.com/dragonflydb/dragonfly/pull/8066) — 4 comments · 0 reactions · open
- **Pull Request** [fix(server): lower table growth margin default](https://github.com/dragonflydb/dragonfly/pull/8080) — 5 comments · 0 reactions · closed
- **Pull Request** [test: un-skip graceful shutdown test by asserting the guaranteed durability contract](https://github.com/dragonflydb/dragonfly/pull/8086) — 4 comments · 0 reactions · closed
- **Pull Request** [feat(server): make conn_use_incoming_cpu runtime mutable](https://github.com/dragonflydb/dragonfly/pull/8095) — 5 comments · 0 reactions · open
- **Pull Request** [fix: null reply shapes for blocking moves, LPOP COUNT, ZRANK WITHSCORE, EXEC and friends](https://github.com/dragonflydb/dragonfly/pull/8098) — 4 comments · 0 reactions · closed
- **Pull Request** [fix(ci): check out default branch for cache-reaper](https://github.com/dragonflydb/dragonfly/pull/8101) — 8 comments · 0 reactions · closed
- **Pull Request** [docs: add design doc for replication fanout (NOT FOR MERGE)](https://github.com/dragonflydb/dragonfly/pull/8002) — 2 comments · 0 reactions · open
- **Pull Request** [fix(chart): update vulnerable Go modules](https://github.com/dragonflydb/dragonfly/pull/8100) — 4 comments · 0 reactions · closed
- **Pull Request** [build(deps): bump golang.org/x/net from 0.44.0 to 0.55.0 in /contrib/charts/dragonfly](https://github.com/dragonflydb/dragonfly/pull/7769) — 2 comments · 0 reactions · closed
- **Pull Request** [chore(deps): bump golang.org/x/crypto from 0.42.0 to 0.52.0 in /contrib/charts/dragonfly](https://github.com/dragonflydb/dragonfly/pull/7835) — 2 comments · 0 reactions · closed
