# Redpanda Project News — 2026-08-15

> Public GitHub release and roadmap evidence. Upcoming items are indications, not commitments.

Repository: [redpanda-data/redpanda](https://github.com/redpanda-data/redpanda)

## Latest stable: [v26.1.16](https://github.com/redpanda-data/redpanda/releases/tag/v26.1.16)

- Tag: `v26.1.16`
- Published: 2026-08-13T19:25:19Z
- Bug Fixes
- Fixed a crash that could occur when removing a partition with a very large number of log segments, e.g. during partition rebalancing. by @pgellert in #31505
- Fixed a crash where a snapshot write failing on a full disk (ENOSPC) aborted the node with a misleading "snapshot writer has to be closed" assertion instead of surfacing the I/O error. by @nvartolomei in #31186
- Fixed a double-free / use-after-free in c-ares query-completion handling (CVE-2026-33630). by @bartoszpiekny-redpanda in #31486
- Fixed a race in the internal Kafka client where a concurrent request on a freshly established SASL connection could be sent before authentication finished, causing the broker to drop the connection. by @nvartolomei in #31192
- 31550 rpk connect upgrade no longer fails to determine the currently-installed Redpanda Connect version when that version has a segment of three or more digits, which had blocked upgrading any Connect install since 4.100.0. by @JakeSCahill

## Publicly indicated upcoming work

- **Milestone** [v26.2.x-next](https://github.com/redpanda-data/redpanda/milestone/329)

## Hacker News discussions

No matching current Hacker News discussion was found.
