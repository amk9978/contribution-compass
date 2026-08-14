# Claude Code Project News — 2026-08-14

> Public GitHub release and roadmap evidence. Upcoming items are indications, not commitments.

Repository: [anthropics/claude-code](https://github.com/anthropics/claude-code)

## Latest stable: [v2.1.232](https://github.com/anthropics/claude-code/releases/tag/v2.1.232)

- Tag: `v2.1.232`
- Published: 2026-08-13T23:29:59Z
- What's changed
- Subagent forking is now on by default: a subagenttype: "fork" subagent inherits the full conversation and prompt cache, and non-teammate agent spawns in interactive sessions now run in the background by default
- Type @ in the prompt to mention another Claude session by name; Claude then uses SendMessage to reach that session directly
- SendMessage now delivers to a bare name that exactly matches one live session, instead of asking to confirm with a ref first
- Interactive sessions on one machine now keep unique names: starting or renaming a session to a name another live session already uses gives it a name-word-word variant and tells you
- Added /config rows for "Dialog expiry" and "Messages from your other sessions" (cross-session inbound accept/hold/refuse)

## Publicly indicated upcoming work

- **Milestone** [P1](https://github.com/anthropics/claude-code/milestone/1)
- **Milestone** [P2](https://github.com/anthropics/claude-code/milestone/2)
- **Milestone** [P3](https://github.com/anthropics/claude-code/milestone/3)

## Hacker News discussions

No matching current Hacker News discussion was found.
