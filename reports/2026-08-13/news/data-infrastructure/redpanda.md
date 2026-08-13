# Redpanda Project News — 2026-08-13

> Public GitHub release and roadmap evidence. Upcoming items are indications, not commitments.

Repository: [redpanda-data/redpanda](https://github.com/redpanda-data/redpanda)

## Latest stable: [v26.1.15](https://github.com/redpanda-data/redpanda/releases/tag/v26.1.15)

- Tag: `v26.1.15`
- Published: 2026-08-07T03:37:58Z
- Bug Fixes
- Fix the registered config name for leaderbalancernodemutetimeout. by @WillemKauf in #31360
- Fixes a bug in which L0 batches in a cloud topic forgot to preserve lastoffsetdelta in their header, leading to an under-declared last offset which can stall consumers, skip records, or halt exact-offset replication. by @WillemKauf in #3136
- Fixes a bug in which topics with min.compaction.lag.ms left unconfigured with produced batches holding timestamps in the future would be considered ineligible for compaction by @WillemKauf in #31459
- Fixes a bug in which transient TOPICAUTHORIZATIONFAILED errors and SASL authentication failures were possible during application of a controller snapshot. by @WillemKauf in #31437
- Fixes a bug where corrupted storage would not yield a bad CRC in returned record batches. by @andrwng in #31388

## Publicly indicated upcoming work

- **Milestone** [v26.2.x-next](https://github.com/redpanda-data/redpanda/milestone/329)
- **Milestone** [v26.1.16](https://github.com/redpanda-data/redpanda/milestone/332)
