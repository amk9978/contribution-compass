import { createHash } from "node:crypto";
import { mkdir, readFile, rename, writeFile } from "node:fs/promises";
import path from "node:path";
import type { Signal } from "../signals/types.js";

interface StateItem {
  fingerprint: string;
  lastSeen: string;
}

interface StateFile {
  version: 1;
  items: Record<string, StateItem>;
}

function fingerprint(signal: Signal): string {
  const stable = {
    title: signal.title,
    text: signal.text,
    timestamp: signal.timestamp,
    metrics: signal.metrics,
    labels: signal.labels,
    url: signal.url,
    state: signal.state,
    assignees: signal.assignees,
  };
  return createHash("sha256").update(JSON.stringify(stable)).digest("hex");
}

async function loadState(file: string): Promise<StateFile> {
  try {
    const parsed = JSON.parse(await readFile(file, "utf8")) as StateFile;
    if (parsed.version !== 1 || typeof parsed.items !== "object")
      throw new Error("unsupported state");
    return parsed;
  } catch (error) {
    if ((error as NodeJS.ErrnoException).code === "ENOENT") return { version: 1, items: {} };
    throw new Error(`Unable to load state ${file}`, { cause: error });
  }
}

async function saveState(file: string, state: StateFile): Promise<void> {
  await mkdir(path.dirname(file), { recursive: true });
  const temporary = `${file}.tmp`;
  await writeFile(temporary, `${JSON.stringify(state, null, 2)}\n`, "utf8");
  await rename(temporary, file);
}

export class SignalStateStore {
  constructor(private readonly directory = ".state") {}

  async filterChanged(signals: Signal[]): Promise<Signal[]> {
    const partitions = new Map<string, Signal[]>();
    for (const signal of signals) {
      const namespace = signal.source === "github" ? "github" : "feeds";
      partitions.set(namespace, [...(partitions.get(namespace) ?? []), signal]);
    }

    const changed: Signal[] = [];
    for (const [namespace, values] of partitions) {
      const file = path.join(this.directory, `${namespace}.json`);
      const state = await loadState(file);
      const now = new Date().toISOString();
      for (const signal of values) {
        const nextFingerprint = fingerprint(signal);
        const previous = state.items[signal.id];
        if (previous?.fingerprint !== nextFingerprint) {
          changed.push({ ...signal, change: previous ? "updated" : "new" });
        }
        state.items[signal.id] = { fingerprint: nextFingerprint, lastSeen: now };
      }
      await saveState(file, state);
    }
    return changed;
  }
}
