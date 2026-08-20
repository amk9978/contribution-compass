# Dagger Project News — 2026-08-20

> Public GitHub release and roadmap evidence. Upcoming items are indications, not commitments.

Repository: [dagger/dagger](https://github.com/dagger/dagger)

## Latest stable: [v0.21.8](https://github.com/dagger/dagger/releases/tag/v0.21.8)

- Tag: `v0.21.8`
- Published: 2026-07-29T17:07:24Z
- v0.21.8 - 2026-07-29
- Changed
- Changeset diffs are now computed from filesystem metadata instead of full-content comparison, significantly speeding up diff computation for large directories. by @marcosnils in
- Fixed
- Dockerfile build layer caching so unrelated build-context changes no longer bust the cache: COPY-ed directories now get a content-based cache identity, re-keying downstream steps only when copied content
- The --x-release CLI re-exec so EXPERIMENTALDAGGERRUNNERHOST is preserved (with a warning) instead of being stripped, and clarified its startup message to avoid implying it runs from any build. by

## Publicly indicated upcoming work

- **Milestone** [vsometime](https://github.com/dagger/dagger/milestone/37)
- **Milestone** [v1.0.1](https://github.com/dagger/dagger/milestone/130)
- **Milestone** [v1.0.0-beta.8](https://github.com/dagger/dagger/milestone/131)
- **Milestone** [v0.21.9](https://github.com/dagger/dagger/milestone/132)

## Hacker News discussions

No matching current Hacker News discussion was found.
