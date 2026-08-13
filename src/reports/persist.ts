import { mkdir, writeFile } from "node:fs/promises";
import path from "node:path";
import type { RadarConfig } from "../config/schema.js";
import type { Signal } from "../signals/types.js";
import { renderGroupReport, renderSummaryReport } from "./daily.js";

export async function persistReports(
  date: string,
  config: RadarConfig,
  signals: Signal[],
  root = "reports",
): Promise<string> {
  const directory = path.join(root, date);
  await mkdir(directory, { recursive: true });
  const counts: Array<{ group: (typeof config.repoGroups)[number]; changedCount: number }> = [];
  for (const group of config.repoGroups) {
    const groupSignals = signals.filter((signal) => signal.group === group.id);
    counts.push({ group, changedCount: groupSignals.length });
    await writeFile(path.join(directory, `${group.id}.md`), renderGroupReport(date, group, groupSignals));
  }
  await writeFile(path.join(directory, "summary.md"), renderSummaryReport(date, counts));
  return directory;
}
