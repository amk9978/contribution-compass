# Dragonfly Project News — 2026-08-15

> Public GitHub release and roadmap evidence. Upcoming items are indications, not commitments.

Repository: [dragonflydb/dragonfly](https://github.com/dragonflydb/dragonfly)

## Latest stable: [v1.40.1](https://github.com/dragonflydb/dragonfly/releases/tag/v1.40.1)

- Tag: `v1.40.1`
- Published: 2026-08-06T06:54:05Z
- This is a patch release.
- What's Changed
- Fixed connection-state handling in squashed pipelines. Commands following AUTH, SELECT, HELLO, CLIENT, or RESET now observe the updated connection state instead of stale authentication, database, or RESP protocol state (#8016).
- Fixed compressed QList node memory accounting and defragmentation (#8011, #8014).

## Publicly indicated upcoming work

- **Milestone** [Cluster Search](https://github.com/dragonflydb/dragonfly/milestone/19) — due 2025-12-31T00:00:00Z
- **Milestone** [v1.41](https://github.com/dragonflydb/dragonfly/milestone/24) — due 2026-09-10T00:00:00Z

## Hacker News discussions

No matching current Hacker News discussion was found.
