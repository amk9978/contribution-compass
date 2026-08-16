# Claude Code Project News — 2026-08-15

> Public GitHub release and roadmap evidence. Upcoming items are indications, not commitments.

Repository: [anthropics/claude-code](https://github.com/anthropics/claude-code)

## Latest stable: [v2.1.233](https://github.com/anthropics/claude-code/releases/tag/v2.1.233)

- Tag: `v2.1.233`
- Published: 2026-08-14T22:20:57Z
- What's changed
- Added GitLab merge request URL support to the --worktree flag and the claude agents view (where MRs display as !N)
- Added an opt-in forwarduseridentity apps gateway setting on Anthropic upstreams that sends the signed-in user's identity as headers, so a proxy behind the gateway can attribute spend per user
- Added opt-in memory cgroup support for Bash tool commands on Linux (CLAUDECODETOOLMEMORYLIMIT) so a runaway build can't stall the session
- Added CLAUDECODEWEBFETCHCACHETTLMS environment variable to configure the WebFetch session URL cache TTL (default unchanged: 15 minutes)
- Fixed cloud sessions occasionally being marked as lost when the environment shut down while Claude was waiting on a permission prompt

## Publicly indicated upcoming work

- **Milestone** [P1](https://github.com/anthropics/claude-code/milestone/1)
- **Milestone** [P2](https://github.com/anthropics/claude-code/milestone/2)
- **Milestone** [P3](https://github.com/anthropics/claude-code/milestone/3)

## Hacker News discussions

- [Maximizing the value of your Claude Code sessions](https://claude.com/blog/maximizing-the-value-of-your-claude-code-sessions) — [139 points · 94 comments](https://news.ycombinator.com/item?id=49300800)

Community discussion; not maintainer evidence.
