import type { RepoGroup } from "../config/schema.js";
import type { Signal } from "../signals/types.js";
import { signalLine } from "./markdown.js";

function byTimestampDescending(left: Signal, right: Signal): number {
  return (
    new Date(right.timestamp ?? 0).getTime() - new Date(left.timestamp ?? 0).getTime() ||
    left.id.localeCompare(right.id)
  );
}

export function renderGroupReport(date: string, group: RepoGroup, signals: Signal[]): string {
  const sorted = [...signals].sort(byTimestampDescending);
  const newCount = signals.filter((signal) => signal.change === "new").length;
  const updatedCount = signals.filter((signal) => signal.change === "updated").length;
  return `${[
    `# ${group.name} Updates — ${date}`,
    "",
    "> Automatically collected from GitHub. No analysis or synthesis is performed.",
    "",
    `Collected changes: ${signals.length} (${newCount} new, ${updatedCount} updated).`,
    "",
    ...(sorted.length ? sorted.map(signalLine) : ["No updates."]),
    "",
  ].join("\n").trim()}\n`;
}

export function renderSummaryReport(
  date: string,
  groups: Array<{ group: RepoGroup; changedCount: number }>,
): string {
  const total = groups.reduce((sum, entry) => sum + entry.changedCount, 0);
  return `${[
    `# Engineering Radar Collection — ${date}`,
    "",
    "> Collection summary only. Repository data is stored separately under `data/`.",
    "",
    `Total changed signals: ${total}.`,
    "",
    ...groups.map(
      ({ group, changedCount }) =>
        `- [${group.name}](./${group.id}.md): ${changedCount} changed signals`,
    ),
    "",
  ].join("\n").trim()}\n`;
}
