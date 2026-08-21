# Data / Messaging / Storage Infrastructure — 2026-08-21

> Factual GitHub evidence collected by Contribution Compass. No LLM analysis is performed.

## Contribution Leads

### [RESTORE DATABASE ... AS ... corrupts/crashes views using FROM table AS alias FINAL,  other_table](https://github.com/ClickHouse/ClickHouse/issues/115479)

- Project: `ClickHouse/ClickHouse`
- Tier: `triage-lead`
- Evidence: Unassigned bug with visible community engagement
- Caveat: No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.

## Important Updates

### [NATS Server](https://github.com/nats-io/nats-server)

- **Pull Request** [(2.15) \[IMPROVED\] Faster durable source/mirror consumer resets](https://github.com/nats-io/nats-server/pull/8323) — 14 comments · 1 reactions · closed
- **Pull Request** [(2.15) Raft proposal fast path](https://github.com/nats-io/nats-server/pull/8445) — 10 comments · 1 reactions · closed
- **Pull Request** [Make reverse response map removal constant time](https://github.com/nats-io/nats-server/pull/8463) — 3 comments · 3 reactions · closed
- **Pull Request** [\[FIXED\] Data race reading consumer config in stream consumer getters](https://github.com/nats-io/nats-server/pull/8478) — 10 comments · 1 reactions · closed
- **Pull Request** [(2.15) NRG: Relax SyncAlways for replicated streams](https://github.com/nats-io/nats-server/pull/8447) — 12 comments · 0 reactions · closed
- **Pull Request** [\[IMPROVED\] Direct get performance and stream lock decoupling](https://github.com/nats-io/nats-server/pull/8486) — 7 comments · 1 reactions · closed
- **Issue** [JetStream file stream Created timestamp changes after restart and configuration update](https://github.com/nats-io/nats-server/issues/8470) — 0 comments · 0 reactions · closed
- **Issue** [Tiered JetStream consumer limits are not additive](https://github.com/nats-io/nats-server/issues/8483) — 0 comments · 0 reactions · closed
- **Issue** [JetStream memory footprint grows with subject & dedup cardinailty despite storageType=File](https://github.com/nats-io/nats-server/issues/8485) — 1 comments · 0 reactions · open
- **Pull Request** [(2.15) \[IMPROVED\] Index stream sources to avoid backward scans](https://github.com/nats-io/nats-server/pull/8282) — 9 comments · 0 reactions · closed
- **Pull Request** [\[FIXED\] Preserve stream created time after recovery](https://github.com/nats-io/nats-server/pull/8471) — 4 comments · 1 reactions · closed
- **Pull Request** [Update to Go 1.27.0/1.26.7](https://github.com/nats-io/nats-server/pull/8482) — 1 comments · 2 reactions · open
- **Pull Request** [Fix cross-tier JetStream consumer counting for limits](https://github.com/nats-io/nats-server/pull/8484) — 3 comments · 1 reactions · closed
- **Pull Request** [(2.15) NRG: Maximize batch size](https://github.com/nats-io/nats-server/pull/8477) — 0 comments · 1 reactions · open
- **Pull Request** [De-flake TestJetStreamSourceStreamRecreated](https://github.com/nats-io/nats-server/pull/8487) — 1 comments · 1 reactions · closed
- **Pull Request** [\[IMPROVED\] Deterministic max_ha_assets enforcement on the meta leader](https://github.com/nats-io/nats-server/pull/8334) — 2 comments · 0 reactions · open
- **Pull Request** [\[FIXED\] Auth callout rejection reported as account connection limit](https://github.com/nats-io/nats-server/pull/8442) — 0 comments · 0 reactions · open
- **Pull Request** [\[FIXED\] Stale flow control stalls consumer after leader change](https://github.com/nats-io/nats-server/pull/8488) — 1 comments · 0 reactions · closed

### [Redpanda](https://github.com/redpanda-data/redpanda)

- **Pull Request** [ts-ct-migration: partition_mode substrate \[PR 0\]](https://github.com/redpanda-data/redpanda/pull/30977) — 23 comments · 0 reactions · closed
- **Pull Request** [\[CORE-16806\] - KIP-848: assignor interface and the homogeneous uniform assignor](https://github.com/redpanda-data/redpanda/pull/31579) — 10 comments · 0 reactions · closed
- **Pull Request** [serde: write fixed envelopes contiguously](https://github.com/redpanda-data/redpanda/pull/31230) — 8 comments · 0 reactions · open
- **Pull Request** [\[CORE-16908\] cluster_link: incremental Schema Registry sync over the HTTP API](https://github.com/redpanda-data/redpanda/pull/31376) — 8 comments · 0 reactions · open
- **Pull Request** [\[CORE-16998, CORE-17000, CORE-17001\] - Consumer Groups (Classic): Fix some bugs where the offset map could diverge from the log](https://github.com/redpanda-data/redpanda/pull/31483) — 9 comments · 0 reactions · closed
- **Pull Request** [ts-ct-migration: STM coexistence \[PR 2\]](https://github.com/redpanda-data/redpanda/pull/30887) — 6 comments · 0 reactions · closed
- **Pull Request** [bazel/seastar: enable task queue shuffling in debug builds](https://github.com/redpanda-data/redpanda/pull/31139) — 4 comments · 0 reactions · closed
- **Pull Request** [rptest: propagate log_config to the shadow link source cluster](https://github.com/redpanda-data/redpanda/pull/31409) — 9 comments · 0 reactions · closed
- **Pull Request** [\[CORE-12930\] - Storage: Some observability improvements for unrecoverable segments](https://github.com/redpanda-data/redpanda/pull/31544) — 5 comments · 0 reactions · closed
- **Pull Request** [tests: add a CDT smoke suite covering the ducktape image dependencies](https://github.com/redpanda-data/redpanda/pull/31612) — 4 comments · 0 reactions · open
- **Pull Request** [\[CORE-14003\] dt/ct: Add cloud topic support to Flink tests](https://github.com/redpanda-data/redpanda/pull/29699) — 7 comments · 0 reactions · closed
- **Pull Request** [POC: Shadow Linking: shadow topic storage mode + opt-in failover promotion](https://github.com/redpanda-data/redpanda/pull/31309) — 7 comments · 0 reactions · closed
- **Pull Request** [tests: make the llvm-symbolizer shim a static binary](https://github.com/redpanda-data/redpanda/pull/31578) — 3 comments · 0 reactions · open
- **Pull Request** [\[v25.3.x\] CORE-17096 Revert "build/deps: upgrade c-ares to 1.34.7 (CVE-2026-33630)"](https://github.com/redpanda-data/redpanda/pull/31639) — 2 comments · 0 reactions · closed
- **Pull Request** [`cluster`: reconcile without a fiber per ntp](https://github.com/redpanda-data/redpanda/pull/31652) — 2 comments · 0 reactions · open
- **Pull Request** [\[CORE-16806\]: KIP-848: Assignor Interface and Uniform Assignors](https://github.com/redpanda-data/redpanda/pull/31426) — 1 comments · 0 reactions · closed
- **Pull Request** [kafka/server: fix quota_manager gc use-after-free at shutdown](https://github.com/redpanda-data/redpanda/pull/31598) — 0 comments · 0 reactions · open
- **Pull Request** [\[CORE-16802\] - KIP-848: the consumer group type and heartbeat dispatch](https://github.com/redpanda-data/redpanda/pull/31621) — 1 comments · 0 reactions · closed
- **Pull Request** [\[CORE-16803\] - KIP-848: consumer group persistence and recovery](https://github.com/redpanda-data/redpanda/pull/31622) — 1 comments · 0 reactions · closed
- **Pull Request** [bazel: cap the http downloader retry backoff](https://github.com/redpanda-data/redpanda/pull/31627) — 0 comments · 0 reactions · open
- **Pull Request** [serde: fix scope-guard underflow and add decode-side fuzzing](https://github.com/redpanda-data/redpanda/pull/31628) — 1 comments · 0 reactions · open
- **Pull Request** [\[v26.2.x\] rpk: sql debug bundle fixes — metrics layout, per-node queries, default CPU profile, k8s resources, parallel collection](https://github.com/redpanda-data/redpanda/pull/31631) — 1 comments · 0 reactions · closed
- **Pull Request** [docs: Move coding guidelines from the cupboard into redpanda](https://github.com/redpanda-data/redpanda/pull/31632) — 0 comments · 0 reactions · closed
- **Pull Request** [\[v26.2.x\] CORE-17096 Revert "build/deps: upgrade c-ares to 1.34.7 (CVE-2026-33630)"](https://github.com/redpanda-data/redpanda/pull/31638) — 1 comments · 0 reactions · closed
- **Pull Request** [net: bound DNS lookups and replace the resolver on a 60s timeout](https://github.com/redpanda-data/redpanda/pull/31644) — 0 comments · 0 reactions · closed
- **Pull Request** [heartbeat_manager: harden connection timeout handling](https://github.com/redpanda-data/redpanda/pull/31645) — 0 comments · 0 reactions · closed
- **Pull Request** [\[v25.3.x\] \[CORE-17063\] - security/audit: report misconfigured auth from client init](https://github.com/redpanda-data/redpanda/pull/31648) — 1 comments · 0 reactions · closed
- **Pull Request** [\[v26.1.x\] \[CORE-17063\] - security/audit: report misconfigured auth from client init](https://github.com/redpanda-data/redpanda/pull/31649) — 0 comments · 0 reactions · closed
- **Pull Request** [\[v26.2.x\] \[CORE-17063\] - security/audit: report misconfigured auth from client init](https://github.com/redpanda-data/redpanda/pull/31650) — 0 comments · 0 reactions · closed
- **Pull Request** [ct/reconciler: replace loop with per-topic scheduling](https://github.com/redpanda-data/redpanda/pull/30136) — 2 comments · 0 reactions · closed

### [ClickHouse](https://github.com/ClickHouse/ClickHouse)

- **Pull Request** [Columns Cache](https://github.com/ClickHouse/ClickHouse/pull/96844) — 79 comments · 5 reactions · open
- **Pull Request** [Optimization of `GROUP BY` in the presence of `ORDER BY` and `LIMIT`](https://github.com/ClickHouse/ClickHouse/pull/96630) — 15 comments · 8 reactions · open
- **Pull Request** [Switch the default compression to ZSTD(3) for table data and network](https://github.com/ClickHouse/ClickHouse/pull/108786) — 72 comments · 1 reactions · open
- **Pull Request** [Add optimize_row_order_if_no_order_by (reopen #103919)](https://github.com/ClickHouse/ClickHouse/pull/104591) — 45 comments · 0 reactions · open
- **Pull Request** [Improve the performance of `MODIFY TTL`](https://github.com/ClickHouse/ClickHouse/pull/63383) — 36 comments · 1 reactions · open
- **Pull Request** [Minmax indices by default](https://github.com/ClickHouse/ClickHouse/pull/76867) — 95 comments · 0 reactions · open
- **Pull Request** [Avoid copying data for the NONE compression codec when writing](https://github.com/ClickHouse/ClickHouse/pull/108096) — 39 comments · 0 reactions · open
- **Issue** [\[Easy Money\] ClickHouse Bug Bounty Program](https://github.com/ClickHouse/ClickHouse/issues/38986) — 4 comments · 13 reactions · open
- **Pull Request** [Statically linked binary](https://github.com/ClickHouse/ClickHouse/pull/109239) — 5 comments · 7 reactions · open
- **Pull Request** [Predistinct step will use bf as first pass filter before hashset](https://github.com/ClickHouse/ClickHouse/pull/77728) — 24 comments · 2 reactions · open
- **Release** [Release v25.8.31.9-lts](https://github.com/ClickHouse/ClickHouse/releases/tag/v25.8.31.9-lts) — 
- **Release** [Release v26.3.20.7-lts](https://github.com/ClickHouse/ClickHouse/releases/tag/v26.3.20.7-lts) — 
- **Pull Request** [Add spatial_bbox skip index for MergeTree geometry columns](https://github.com/ClickHouse/ClickHouse/pull/104437) — 27 comments · 1 reactions · open
- **Pull Request** [Transform JOIN hash table payload to row major](https://github.com/ClickHouse/ClickHouse/pull/104884) — 14 comments · 4 reactions · open
- **Pull Request** [WIP: Projection Index Text](https://github.com/ClickHouse/ClickHouse/pull/93114) — 26 comments · 7 reactions · open
- **Pull Request** [Support column matcher expansion for default value expressions and index expressions](https://github.com/ClickHouse/ClickHouse/pull/105045) — 52 comments · 3 reactions · open
- **Pull Request** [Push subcolumn reads into subqueries](https://github.com/ClickHouse/ClickHouse/pull/112688) — 20 comments · 2 reactions · open
- **Pull Request** [Fix ALTER TABLE MODIFY TTL with DateTime causing data loss on 32-bit overflow](https://github.com/ClickHouse/ClickHouse/pull/101793) — 25 comments · 0 reactions · open
- **Pull Request** [Added Parquet Shredded VARIANT Support to ParquetReaderv3](https://github.com/ClickHouse/ClickHouse/pull/102499) — 36 comments · 3 reactions · open
- **Pull Request** [Make `arrayCount` return `UInt64` and rewrite `length(arrayFilter(...))`](https://github.com/ClickHouse/ClickHouse/pull/113023) — 25 comments · 0 reactions · open
- **Pull Request** [Add SQLite input/output format](https://github.com/ClickHouse/ClickHouse/pull/104510) — 60 comments · 1 reactions · open
- **Pull Request** [Avoid per-row heap allocations in blocked Myers edit distance](https://github.com/ClickHouse/ClickHouse/pull/108185) — 17 comments · 1 reactions · open
- **Pull Request** [LowCardinality merge optimization](https://github.com/ClickHouse/ClickHouse/pull/114870) — 9 comments · 3 reactions · open
- **Pull Request** [Share the speculatively built IN set between the part tasks of a mutation](https://github.com/ClickHouse/ClickHouse/pull/112941) — 18 comments · 0 reactions · closed
- **Pull Request** [Skip writing all-default columns during MergeTree INSERT](https://github.com/ClickHouse/ClickHouse/pull/98472) — 31 comments · 3 reactions · open
- **Pull Request** [Not a fix: "Not-ready Set" exception when buildOrderedSetInplace fails](https://github.com/ClickHouse/ClickHouse/pull/102192) — 59 comments · 0 reactions · open
- **Pull Request** [Use text index for LIKE/ILIKE with ESCAPE](https://github.com/ClickHouse/ClickHouse/pull/105848) — 40 comments · 0 reactions · open
- **Pull Request** [Deny mergeTreeProjection and mergeTreeIndex reads that bypass a SELECT row policy](https://github.com/ClickHouse/ClickHouse/pull/108462) — 16 comments · 0 reactions · closed
- **Pull Request** [Allow creating a Distributed table over a table function](https://github.com/ClickHouse/ClickHouse/pull/110073) — 50 comments · 0 reactions · open
- **Pull Request** [MaterializedPostgreSQL: coordinated Replicated/Shared nested tables for HA](https://github.com/ClickHouse/ClickHouse/pull/110886) — 49 comments · 0 reactions · open

### [Dragonfly](https://github.com/dragonflydb/dragonfly)

- **Issue** [test_slot_migration_oom_replica_rollback](https://github.com/dragonflydb/dragonfly/issues/8106) — 6 comments · 0 reactions · closed
- **Pull Request** [fix(facade): log V2 traffic before dispatch](https://github.com/dragonflydb/dragonfly/pull/8096) — 13 comments · 0 reactions · closed
- **Pull Request** [fix(generic): avoid data loss on RENAME when destination write fails](https://github.com/dragonflydb/dragonfly/pull/8053) — 11 comments · 0 reactions · open
- **Pull Request** [fix: stop SCRIPT FLUSH from deadlocking against a borrowed interpreter](https://github.com/dragonflydb/dragonfly/pull/8110) — 11 comments · 0 reactions · open
- **Issue** [test_debug_traffic_v2_parse_in_proactor_does_not_preempt](https://github.com/dragonflydb/dragonfly/issues/8120) — 4 comments · 0 reactions · open
- **Issue** [test_debug_traffic_records_pipeline_in_dispatch_order](https://github.com/dragonflydb/dragonfly/issues/8119) — 2 comments · 0 reactions · closed
- **Issue** [test_debug_traffic_v2_logs_retried_sync_command_once](https://github.com/dragonflydb/dragonfly/issues/8121) — 2 comments · 0 reactions · closed
- **Pull Request** [feat(server): Implement COMMAND LIST (#5466)](https://github.com/dragonflydb/dragonfly/pull/7385) — 10 comments · 0 reactions · open
- **Pull Request** [fix(server): skip evicting keys in buckets a full sync hasn't capture…](https://github.com/dragonflydb/dragonfly/pull/8109) — 6 comments · 0 reactions · open
- **Issue** [stuck in heartbeat](https://github.com/dragonflydb/dragonfly/issues/8125) — 1 comments · 0 reactions · open
- **Issue** [Eviction can delete a key mid-full-sync before its baseline is captured, causing the replica to retain keys the master already evicted (#8090, #7925)](https://github.com/dragonflydb/dragonfly/issues/8128) — 0 comments · 0 reactions · open
- **Pull Request** [fix(tiering): Use TraverseBySegmentOrder and export more metrics/configs](https://github.com/dragonflydb/dragonfly/pull/8077) — 5 comments · 0 reactions · open
- **Pull Request** [fix(acl): script context acl and enable flaky tests](https://github.com/dragonflydb/dragonfly/pull/8116) — 4 comments · 0 reactions · open
- **Pull Request** [fix: test_slot_migration_oom_replica_rollback](https://github.com/dragonflydb/dragonfly/pull/8117) — 4 comments · 0 reactions · closed
- **Pull Request** [chore: split python cluster tests](https://github.com/dragonflydb/dragonfly/pull/8118) — 4 comments · 0 reactions · closed
- **Pull Request** [fix(server): Skip forced snapshot serialization for redundant writes with second replica, add support for expire](https://github.com/dragonflydb/dragonfly/pull/8112) — 2 comments · 0 reactions · open
- **Pull Request** [fix: apple clang16 crash on FloatToBf16](https://github.com/dragonflydb/dragonfly/pull/8123) — 4 comments · 0 reactions · closed
- **Pull Request** [fix(cluster): delete slots when OOM is discovered via ACK](https://github.com/dragonflydb/dragonfly/pull/8127) — 4 comments · 0 reactions · closed
- **Pull Request** [test(facade): exclude debug traffic tests on epoll](https://github.com/dragonflydb/dragonfly/pull/8124) — 3 comments · 0 reactions · closed
- **Pull Request** [feat(tiering): Tiered bin-bucket defragmentation](https://github.com/dragonflydb/dragonfly/pull/8007) — 0 comments · 0 reactions · open
- **Pull Request** [Tiered device usage](https://github.com/dragonflydb/dragonfly/pull/8122) — 0 comments · 0 reactions · open
- **Pull Request** [feat(tiering): Account for tiered storage utility RAM](https://github.com/dragonflydb/dragonfly/pull/8126) — 0 comments · 0 reactions · open
