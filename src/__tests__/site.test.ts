import { mkdir, mkdtemp, readFile, rm, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import path from "node:path";
import { afterEach, describe, expect, it } from "vitest";
import { generateSite } from "../site/generate.js";
import type { Signal } from "../signals/types.js";
import type { DatasetManifest, RepositoryDataset } from "../storage/dataset.js";

const directories: string[] = [];

afterEach(async () => {
  await Promise.all(directories.splice(0).map((directory) => rm(directory, { recursive: true })));
});

async function fixture(): Promise<{ dataRoot: string; outputRoot: string; signal: Signal }> {
  const root = await mkdtemp(path.join(tmpdir(), "engineering-radar-site-"));
  directories.push(root);
  const dataRoot = path.join(root, "data");
  const outputRoot = path.join(root, "site");
  const dateRoot = path.join(dataRoot, "2026-08-13");
  const signal: Signal = {
    id: "github:acme/widget:issue:42",
    source: "github",
    group: "runtime-tools",
    project: "acme/widget",
    kind: "issue",
    title: "Unsafe <script>alert('radar')</script> cleanup",
    text: "Resources remain open after cancellation & timeout.",
    url: "https://github.com/acme/widget/issues/42",
    createdAt: "2026-08-12T09:30:00Z",
    updatedAt: "2026-08-13T09:30:00Z",
    timestamp: "2026-08-13T09:30:00Z",
    metrics: { comments: 7, reactions: 3 },
    labels: ["good first issue", "bug"],
    author: "octocat",
    state: "open",
    assignees: [],
    change: "new",
  };
  const dataset: RepositoryDataset = {
    version: 1,
    date: "2026-08-13",
    group: { id: "runtime-tools", name: "Runtime Tools" },
    repository: { id: "widget", repo: "acme/widget", name: "Widget" },
    runs: [
      {
        collectedAt: "2026-08-13T10:00:00Z",
        since: "2026-08-12T10:00:00Z",
        observedCount: 1,
        changedCount: 1,
      },
    ],
    signals: [signal],
  };
  const manifest: DatasetManifest = {
    version: 1,
    date: "2026-08-13",
    collectedAt: "2026-08-13T10:00:00Z",
    since: "2026-08-12T10:00:00Z",
    repositories: [
      {
        group: "runtime-tools",
        repository: "acme/widget",
        path: "runtime-tools/widget.json",
        observedCount: 1,
        changedCount: 1,
      },
    ],
  };

  await mkdir(path.join(dateRoot, "runtime-tools"), { recursive: true });
  await Promise.all([
    writeFile(path.join(dateRoot, "manifest.json"), JSON.stringify(manifest), "utf8"),
    writeFile(path.join(dateRoot, "runtime-tools/widget.json"), JSON.stringify(dataset), "utf8"),
  ]);
  return { dataRoot, outputRoot, signal };
}

describe("static site generation", () => {
  it("creates navigable date, group, repository, sitemap, and RSS files", async () => {
    const { dataRoot, outputRoot, signal } = await fixture();
    const result = await generateSite({
      dataRoot,
      outputRoot,
      siteUrl: "https://example.github.io/radar",
      repositoryUrl: "https://github.com/example/radar",
    });

    const [
      home,
      date,
      group,
      repository,
      contribute,
      feed,
      jsonFeed,
      api,
      repositoryApi,
      opportunities,
      llms,
      sitemap,
    ] = await Promise.all([
      readFile(path.join(outputRoot, "index.html"), "utf8"),
      readFile(path.join(outputRoot, "updates/2026-08-13/index.html"), "utf8"),
      readFile(path.join(outputRoot, "updates/2026-08-13/runtime-tools/index.html"), "utf8"),
      readFile(path.join(outputRoot, "updates/2026-08-13/runtime-tools/widget.html"), "utf8"),
      readFile(path.join(outputRoot, "contribute/index.html"), "utf8"),
      readFile(path.join(outputRoot, "feed.xml"), "utf8"),
      readFile(path.join(outputRoot, "feed.json"), "utf8"),
      readFile(path.join(outputRoot, "api/v1/index.json"), "utf8"),
      readFile(
        path.join(
          outputRoot,
          "api/v1/dates/2026-08-13/groups/runtime-tools/repositories/widget.json",
        ),
        "utf8",
      ),
      readFile(path.join(outputRoot, "api/v1/opportunities.json"), "utf8"),
      readFile(path.join(outputRoot, "llms.txt"), "utf8"),
      readFile(path.join(outputRoot, "sitemap.xml"), "utf8"),
    ]);

    expect(result).toMatchObject({ dates: 1, pages: 5 });
    expect(home).toContain("Runtime Tools");
    expect(home).toContain("1 configured ecosystems");
    expect(date).toContain("Browse by ecosystem");
    expect(group).toContain("acme/widget");
    expect(repository).toContain(signal.url);
    expect(repository).toContain("Unsafe &lt;script&gt;");
    expect(repository).not.toContain("<script>alert('radar')</script>");
    expect(contribute).toContain("Maintainer invited");
    expect(contribute).toContain(signal.url);
    expect(feed).toContain('<rss version="2.0"');
    expect(feed).toContain(signal.url.replaceAll("&", "&amp;"));
    expect(feed).toContain("runtime-tools/widget.html#signal-");
    expect(JSON.parse(jsonFeed)).toMatchObject({
      version: "https://jsonfeed.org/version/1.1",
      items: [{ external_url: signal.url }],
    });
    expect(JSON.parse(api)).toMatchObject({
      schema_version: 1,
      latest_date: "2026-08-13",
      latest_contribution_lead_count: 1,
    });
    expect(JSON.parse(repositoryApi)).toMatchObject({
      repository: { repository: "acme/widget" },
      signals: [{ id: signal.id, url: signal.url }],
    });
    expect(JSON.parse(opportunities)).toMatchObject({
      count: 1,
      leads: [{ tier: "maintainer-invited", evidence_url: signal.url }],
    });
    expect(llms).toContain("Do not infer facts");
    expect(sitemap).toContain("updates/2026-08-13/runtime-tools/widget.html");
    expect(sitemap).toContain("/contribute/");
  });

  it("builds a useful empty site before the first collection", async () => {
    const root = await mkdtemp(path.join(tmpdir(), "engineering-radar-empty-site-"));
    directories.push(root);
    const outputRoot = path.join(root, "site");

    const result = await generateSite({
      dataRoot: path.join(root, "missing"),
      outputRoot,
      siteUrl: "https://example.github.io/radar",
    });
    const home = await readFile(path.join(outputRoot, "index.html"), "utf8");

    expect(result).toMatchObject({ dates: 0, pages: 2 });
    expect(home).toContain("Waiting for the first scan");
  });
});
