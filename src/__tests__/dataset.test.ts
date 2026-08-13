import { mkdtemp, readFile, rm } from "node:fs/promises";
import { tmpdir } from "node:os";
import path from "node:path";
import { afterEach, describe, expect, it } from "vitest";
import type { RadarConfig } from "../config/schema.js";
import type { Signal } from "../signals/types.js";
import { persistRepositoryDatasets } from "../storage/dataset.js";

const directories: string[] = [];

afterEach(async () => {
  await Promise.all(directories.splice(0).map((directory) => rm(directory, { recursive: true })));
});

const config: RadarConfig = {
  repoGroups: [
    {
      id: "systems",
      name: "Systems",
      repos: [
        { id: "widget", repo: "acme/widget", name: "Widget" },
        { id: "gadget", repo: "example/gadget", name: "Gadget" },
      ],
    },
  ],
  lookbackHours: 24,
};

const signal: Signal = {
  id: "github:acme/widget:issue:1",
  source: "github",
  group: "systems",
  project: "acme/widget",
  kind: "issue",
  title: "A leak",
  text: "Full collected issue body",
  url: "https://github.com/acme/widget/issues/1",
  change: "new",
};

describe("repository datasets", () => {
  it("writes date/group/repository files and keeps same-day repository history", async () => {
    const root = await mkdtemp(path.join(tmpdir(), "engineering-radar-data-"));
    directories.push(root);
    await persistRepositoryDatasets(
      "2026-08-13",
      "2026-08-13T01:00:00Z",
      "2026-08-12T01:00:00Z",
      config,
      [signal],
      [signal],
      root,
    );
    await persistRepositoryDatasets(
      "2026-08-13",
      "2026-08-13T02:00:00Z",
      "2026-08-12T02:00:00Z",
      config,
      [],
      [],
      root,
    );

    const widget = JSON.parse(
      await readFile(path.join(root, "2026-08-13/systems/widget.json"), "utf8"),
    ) as { runs: unknown[]; signals: Signal[] };
    const gadget = JSON.parse(
      await readFile(path.join(root, "2026-08-13/systems/gadget.json"), "utf8"),
    ) as { signals: Signal[] };
    const manifest = JSON.parse(
      await readFile(path.join(root, "2026-08-13/manifest.json"), "utf8"),
    ) as { repositories: Array<{ path: string }> };

    expect(widget.runs).toHaveLength(2);
    expect(widget.signals).toEqual([signal]);
    expect(gadget.signals).toEqual([]);
    expect(manifest.repositories.map((entry) => entry.path)).toEqual([
      "systems/widget.json",
      "systems/gadget.json",
    ]);
  });
});
