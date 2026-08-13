import { mkdir, readFile, rename, writeFile } from "node:fs/promises";
import path from "node:path";
import type { RadarConfig, RepoConfig, RepoGroup } from "../config/schema.js";
import type { Signal } from "../signals/types.js";

export interface CrawlRun {
  collectedAt: string;
  since: string;
  observedCount: number;
  changedCount: number;
}

export interface RepositoryDataset {
  version: 1;
  date: string;
  group: { id: string; name: string };
  repository: { id: string; repo: string; name: string };
  runs: CrawlRun[];
  signals: Signal[];
}

export interface DatasetManifest {
  version: 1;
  date: string;
  collectedAt: string;
  since: string;
  repositories: Array<{
    group: string;
    repository: string;
    path: string;
    observedCount: number;
    changedCount: number;
  }>;
}

async function readDataset(
  destination: string,
  date: string,
  group: RepoGroup,
  repository: RepoConfig,
): Promise<RepositoryDataset> {
  try {
    const parsed = JSON.parse(await readFile(destination, "utf8")) as RepositoryDataset;
    if (
      parsed.version !== 1 ||
      parsed.date !== date ||
      parsed.group.id !== group.id ||
      parsed.repository.id !== repository.id ||
      !Array.isArray(parsed.signals)
    ) {
      throw new Error("unsupported repository dataset");
    }
    return parsed;
  } catch (error) {
    if ((error as NodeJS.ErrnoException).code !== "ENOENT") {
      throw new Error(`Unable to load repository dataset ${destination}`, { cause: error });
    }
    return {
      version: 1,
      date,
      group: { id: group.id, name: group.name },
      repository: { id: repository.id, repo: repository.repo, name: repository.name },
      runs: [],
      signals: [],
    };
  }
}

async function writeJson(destination: string, value: unknown): Promise<void> {
  await mkdir(path.dirname(destination), { recursive: true });
  const temporary = `${destination}.tmp`;
  await writeFile(temporary, `${JSON.stringify(value, null, 2)}\n`, "utf8");
  await rename(temporary, destination);
}

export async function persistRepositoryDatasets(
  date: string,
  collectedAt: string,
  since: string,
  config: RadarConfig,
  observed: Signal[],
  changed: Signal[],
  root = "data",
): Promise<{ directory: string; manifest: DatasetManifest }> {
  const directory = path.join(root, date);
  const repositories: DatasetManifest["repositories"] = [];

  for (const group of config.repoGroups) {
    for (const repository of group.repos) {
      const observedForRepo = observed.filter((signal) => signal.project === repository.repo);
      const changedForRepo = changed.filter((signal) => signal.project === repository.repo);
      const relativePath = path.posix.join(group.id, `${repository.id}.json`);
      const destination = path.join(directory, group.id, `${repository.id}.json`);
      const current = await readDataset(destination, date, group, repository);
      const merged = new Map(current.signals.map((signal) => [signal.id, signal]));
      for (const signal of changedForRepo) merged.set(signal.id, signal);
      const run: CrawlRun = {
        collectedAt,
        since,
        observedCount: observedForRepo.length,
        changedCount: changedForRepo.length,
      };
      await writeJson(destination, {
        ...current,
        runs: [...current.runs, run],
        signals: [...merged.values()].sort((left, right) => left.id.localeCompare(right.id)),
      } satisfies RepositoryDataset);
      repositories.push({
        group: group.id,
        repository: repository.repo,
        path: relativePath,
        observedCount: observedForRepo.length,
        changedCount: changedForRepo.length,
      });
    }
  }

  const manifest: DatasetManifest = {
    version: 1,
    date,
    collectedAt,
    since,
    repositories,
  };
  await writeJson(path.join(directory, "manifest.json"), manifest);
  return { directory, manifest };
}
