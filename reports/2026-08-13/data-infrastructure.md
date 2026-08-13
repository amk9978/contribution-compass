# Data / Messaging / Storage Infrastructure — 2026-08-13

> Factual GitHub evidence collected by Contribution Compass. No LLM analysis is performed.

## Contribution Leads

No evidence-qualified contribution leads changed in this collection.
## Important Updates

### [NATS Server](https://github.com/nats-io/nats-server)

No new or materially changed signals.

### [Redpanda](https://github.com/redpanda-data/redpanda)

- **Pull Request** [\[v26.2.x\] storage: bump segment_concatenation_test timeout](https://github.com/redpanda-data/redpanda/pull/31570) — 1 comments · 0 reactions · open
- **Pull Request** [\[v26.2.x\] kafka/client/test: deflake data_queue blocking push test](https://github.com/redpanda-data/redpanda/pull/31572) — 1 comments · 0 reactions · closed
- **Pull Request** [rpk: add stretch cluster grafana dashboard behind --cluster-type flag](https://github.com/redpanda-data/redpanda/pull/31573) — 0 comments · 0 reactions · open

### [ClickHouse](https://github.com/ClickHouse/ClickHouse)

- **Pull Request** [Cascades cost-based optimizer for distributed query plans](https://github.com/ClickHouse/ClickHouse/pull/86353) — 7 comments · 22 reactions · open
- **Pull Request** [Add `GradualResizeProcessor` to limit effective parallelism for GROUP BY on small data volumes](https://github.com/ClickHouse/ClickHouse/pull/99495) — 30 comments · 0 reactions · open
- **Pull Request** [In case of trivial views, push whole outer query to shards.](https://github.com/ClickHouse/ClickHouse/pull/101791) — 16 comments · 3 reactions · open
- **Pull Request** [Randomize tests with DETACH/ATTACH table before query execution](https://github.com/ClickHouse/ClickHouse/pull/96130) — 91 comments · 2 reactions · open
- **Pull Request** [Reintroduce borrowed threadgroup async uaf fix](https://github.com/ClickHouse/ClickHouse/pull/109891) — 47 comments · 0 reactions · open
- **Pull Request** [Docs: internationalize master](https://github.com/ClickHouse/ClickHouse/pull/114466) — 47 comments · 0 reactions · open
- **Pull Request** [Replace the per-bucket hash map in `timeSeries*ToGrid` with a sorted-append sample array](https://github.com/ClickHouse/ClickHouse/pull/113681) — 9 comments · 1 reactions · open
- **Pull Request** [Let read-in-order propagate through SpillingHashJoin](https://github.com/ClickHouse/ClickHouse/pull/111973) — 9 comments · 0 reactions · open
- **Pull Request** [Assign merges for all partitions at once for OPTIMIZE FINAL](https://github.com/ClickHouse/ClickHouse/pull/109004) — 6 comments · 0 reactions · open
- **Pull Request** [Optimize merges of the text index](https://github.com/ClickHouse/ClickHouse/pull/114525) — 3 comments · 0 reactions · open
- **Pull Request** [Speed up `IN (subquery)` set building by pre-deduplicating each `MergeTree` partition independently](https://github.com/ClickHouse/ClickHouse/pull/114645) — 3 comments · 0 reactions · open
- **Pull Request** [S3 tables engine](https://github.com/ClickHouse/ClickHouse/pull/113505) — 2 comments · 3 reactions · open
- **Pull Request** [Fsync backup files and directories when writing a backup to local disk](https://github.com/ClickHouse/ClickHouse/pull/111394) — 13 comments · 0 reactions · open
- **Pull Request** [Add per-user filesystem cache disk usage metrics](https://github.com/ClickHouse/ClickHouse/pull/107865) — 11 comments · 0 reactions · open
- **Pull Request** [Support `GROUPS` frame mode for window functions](https://github.com/ClickHouse/ClickHouse/pull/108653) — 3 comments · 2 reactions · closed
- **Pull Request** [Fix double free when finalizing -State aggregates under looping combinators](https://github.com/ClickHouse/ClickHouse/pull/111287) — 11 comments · 0 reactions · open
- **Pull Request** [Implementing generic block nested loop join](https://github.com/ClickHouse/ClickHouse/pull/114184) — 3 comments · 2 reactions · open
- **Pull Request** [Merge filters into join during join reordering](https://github.com/ClickHouse/ClickHouse/pull/107637) — 8 comments · 0 reactions · open
- **Pull Request** [Do not drop a named collection that a detached table still uses](https://github.com/ClickHouse/ClickHouse/pull/112805) — 6 comments · 0 reactions · open
- **Pull Request** [Fix `theilsU` window state returning noise when the frame's first argument is constant](https://github.com/ClickHouse/ClickHouse/pull/113691) — 6 comments · 0 reactions · closed
- **Pull Request** [Allowlist the expected FileLog bad-path reattach error in the upgrade check](https://github.com/ClickHouse/ClickHouse/pull/113983) — 6 comments · 0 reactions · open
- **Pull Request** [Backport #113291 to 26.6: Fix for virtual row is not being applied in some cases](https://github.com/ClickHouse/ClickHouse/pull/114220) — 7 comments · 0 reactions · open
- **Pull Request** [Add test: A `\N` CSV field belonging to a nested `Tuple` / `Nullable(Tuple)` element of a separate-columns `Tuple` is untested](https://github.com/ClickHouse/ClickHouse/pull/114273) — 6 comments · 0 reactions · open
- **Pull Request** [Add pre-hook to insert CI links into PR body](https://github.com/ClickHouse/ClickHouse/pull/114283) — 3 comments · 1 reactions · open
- **Pull Request** [Reject a lossy codec on columns backing keys and indexes](https://github.com/ClickHouse/ClickHouse/pull/114531) — 7 comments · 0 reactions · open
- **Pull Request** [Re-land aggregate function `gini` in the `sum` family](https://github.com/ClickHouse/ClickHouse/pull/114643) — 7 comments · 0 reactions · open
- **Pull Request** [Compare read-in-order virtual row on its covered sort-key prefix](https://github.com/ClickHouse/ClickHouse/pull/111457) — 4 comments · 0 reactions · open
- **Pull Request** [Silk integration](https://github.com/ClickHouse/ClickHouse/pull/112667) — 1 comments · 1 reactions · open
- **Pull Request** [Use the vector similarity index for integer reference vectors](https://github.com/ClickHouse/ClickHouse/pull/114316) — 5 comments · 0 reactions · open
- **Pull Request** [Revert "Revert the PromQL topk/limitk streaming plan and its shared-subquery materialization"](https://github.com/ClickHouse/ClickHouse/pull/114409) — 5 comments · 0 reactions · open

### [Dragonfly](https://github.com/dragonflydb/dragonfly)

- **Pull Request** [fix(tiering): Use TraverseBySegmentOrder and export more metrics/configs](https://github.com/dragonflydb/dragonfly/pull/8077) — 4 comments · 0 reactions · open
