import { mkdtemp, readFile, rm } from "node:fs/promises";
import { tmpdir } from "node:os";
import path from "node:path";
import { afterEach, describe, expect, it } from "vitest";
import type { Signal } from "../signals/types.js";
import { SignalStateStore } from "../storage/state.js";

const temporaryDirectories: string[] = [];

afterEach(async () => {
  await Promise.all(
    temporaryDirectories.splice(0).map((directory) => rm(directory, { recursive: true })),
  );
});

async function store(): Promise<{ directory: string; state: SignalStateStore }> {
  const directory = await mkdtemp(path.join(tmpdir(), "engineering-radar-state-"));
  temporaryDirectories.push(directory);
  return { directory, state: new SignalStateStore(directory) };
}

const signal: Signal = {
  id: "github:acme/widget:issue:1",
  source: "github",
  project: "acme/widget",
  kind: "issue",
  title: "A leak",
  url: "https://github.com/acme/widget/issues/1",
  timestamp: "2026-08-13T00:00:00Z",
  metrics: { comments: 1 },
};

describe("signal state", () => {
  it("emits new and substantially changed items but not unchanged items", async () => {
    const { directory, state } = await store();
    expect(await state.filterChanged([signal])).toMatchObject([{ change: "new" }]);
    expect(await state.filterChanged([signal])).toEqual([]);
    expect(await state.filterChanged([{ ...signal, metrics: { comments: 2 } }])).toMatchObject([
      { change: "updated" },
    ]);
    const persisted = JSON.parse(await readFile(path.join(directory, "github.json"), "utf8")) as {
      items: object;
    };
    expect(Object.keys(persisted.items)).toHaveLength(1);
  });
});
