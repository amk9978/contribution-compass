# Redpanda Project News — 2026-08-21

> Public GitHub release and roadmap evidence. Upcoming items are indications, not commitments.

Repository: [redpanda-data/redpanda](https://github.com/redpanda-data/redpanda)

## Latest stable: [v26.1.17](https://github.com/redpanda-data/redpanda/releases/tag/v26.1.17)

- Tag: `v26.1.17`
- Published: 2026-08-20T00:03:34Z
- Bug Fixes
- Fixed an issue where audit-log initialization unconditionally sent a CreateTopics request to the controller leader, causing authentication and the admin API to be rejected cluster-wide (with auditfailurepolicy=reject) for the duration of an
- Fixed an issue where backpressure from the Iceberg coordinator caused high CPU load on the Datalake translators. The translation loop was treating a backpressured fetch as a successful iteration and cancelling its retry jitter, causing it t
- Reverted the c-ares DNS resolver from 1.34.7 back to 1.34.6. c-ares 1.34.7 contains an upstream regression (c-ares/c-ares#1256) where a DNS query completion callback can silently never be invoked, which could leave an internal broker-to-bro

## Publicly indicated upcoming work

- **Milestone** [v26.2.x-next](https://github.com/redpanda-data/redpanda/milestone/329)
- **Milestone** [v26.2.2](https://github.com/redpanda-data/redpanda/milestone/333)

## Hacker News discussions

No matching current Hacker News discussion was found.
