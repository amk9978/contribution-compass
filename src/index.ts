import { loadConfig } from "./config/load.js";
import { persistReports } from "./reports/persist.js";
import { normalizeGitHub } from "./signals/normalize.js";
import { collectGitHubSignals } from "./sources/github.js";
import { persistRepositoryDatasets } from "./storage/dataset.js";
import { SignalStateStore } from "./storage/state.js";

export async function run(): Promise<void> {
  const config = await loadConfig(process.env["RADAR_CONFIG"] ?? "config.yml");
  const now = new Date();
  const since = new Date(now.getTime() - config.lookbackHours * 3_600_000);
  const date = now.toISOString().slice(0, 10);
  if (!process.env["GITHUB_TOKEN"] && config.repoGroups.some((group) => group.repos.length > 0)) {
    throw new Error("GITHUB_TOKEN is required to collect configured repositories reliably");
  }

  console.log(`[radar] collecting GitHub updates since ${since.toISOString()}`);
  const observed = (await collectGitHubSignals(config.repoGroups, since)).map(normalizeGitHub);
  const changed = await new SignalStateStore().filterChanged(observed);
  console.log(`[radar] ${observed.length} observed; ${changed.length} new or updated`);

  const data = await persistRepositoryDatasets(
    date,
    now.toISOString(),
    since.toISOString(),
    config,
    observed,
    changed,
  );
  const reportDirectory = await persistReports(date, config, changed);
  console.log(`[radar] wrote ${data.directory} and ${reportDirectory}`);
}

run().catch((error: unknown) => {
  console.error(`[radar] ${error instanceof Error ? error.message : String(error)}`);
  process.exitCode = 1;
});
