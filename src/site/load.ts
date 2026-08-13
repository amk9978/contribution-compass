import { readdir, readFile } from "node:fs/promises";
import path from "node:path";
import type { DatasetManifest, RepositoryDataset } from "../storage/dataset.js";
import type { SiteDate, SiteGroup, SiteModel } from "./model.js";

const DATE_PATTERN = /^\d{4}-\d{2}-\d{2}$/;

async function readJson<T>(file: string): Promise<T> {
  return JSON.parse(await readFile(file, "utf8")) as T;
}

async function loadDate(dataRoot: string, date: string): Promise<SiteDate> {
  const directory = path.join(dataRoot, date);
  const manifest = await readJson<DatasetManifest>(path.join(directory, "manifest.json"));
  const groups = new Map<string, SiteGroup>();

  for (const entry of manifest.repositories) {
    const dataset = await readJson<RepositoryDataset>(path.join(directory, entry.path));
    const group = groups.get(dataset.group.id) ?? {
      id: dataset.group.id,
      name: dataset.group.name,
      repositories: [],
    };
    group.repositories.push({
      id: dataset.repository.id,
      repo: dataset.repository.repo,
      name: dataset.repository.name,
      runs: dataset.runs,
      signals: dataset.signals,
    });
    groups.set(group.id, group);
  }

  return {
    date,
    collectedAt: manifest.collectedAt,
    groups: [...groups.values()],
  };
}

export async function loadSiteModel(dataRoot = "data"): Promise<SiteModel> {
  let dates: string[];
  try {
    dates = (await readdir(dataRoot, { withFileTypes: true }))
      .filter((entry) => entry.isDirectory() && DATE_PATTERN.test(entry.name))
      .map((entry) => entry.name)
      .sort()
      .reverse();
  } catch (error) {
    if ((error as NodeJS.ErrnoException).code === "ENOENT") {
      return { generatedAt: new Date().toISOString(), dates: [] };
    }
    throw error;
  }

  const loaded = await Promise.all(dates.map((date) => loadDate(dataRoot, date)));
  return { generatedAt: new Date().toISOString(), dates: loaded };
}
