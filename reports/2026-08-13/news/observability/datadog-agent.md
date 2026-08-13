# Datadog Agent Project News — 2026-08-13

> Public GitHub release and roadmap evidence. Upcoming items are indications, not commitments.

Repository: [DataDog/datadog-agent](https://github.com/DataDog/datadog-agent)

## Latest stable: [7.82.1](https://github.com/DataDog/datadog-agent/releases/tag/7.82.1)

- Tag: `7.82.1`
- Published: 2026-08-10T15:37:55Z
- Prelude
- Please refer to the 7.82.1 tag on integrations-core for the list of changes on the Core Checks
- Bug Fixes
- Windows: Fixed an issue where an explicit DDAGENTUSERKEEPRIGHTS or DDAGENTUSERNAME value passed as an install argument to a Fleet Automation-triggered Windows Agent install/upgrade could be silently overridden by a stale fallback value (res
- Fix an issue where GPU monitoring could trigger a kernel panic on multi-GPU nodes with Hopper/Blackwell GPUs.

## Publicly indicated upcoming work

- **Milestone** [Triage](https://github.com/DataDog/datadog-agent/milestone/22)
- **Milestone** [Release Maintenance](https://github.com/DataDog/datadog-agent/milestone/127)
- **Milestone** [no-mile](https://github.com/DataDog/datadog-agent/milestone/180)
