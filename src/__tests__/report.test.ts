import { describe, expect, it } from "vitest";
import type { RadarConfig } from "../config/schema.js";
import { renderGroupReport, renderSummaryReport } from "../reports/daily.js";
import type { Signal } from "../signals/types.js";

const config: RadarConfig = {
  repoGroups: [
    {
      id: "compilers",
      name: "Compiler Engineering",
      repos: [{ id: "llvm", repo: "llvm/llvm-project", name: "LLVM" }],
    },
  ],
  lookbackHours: 24,
};

const signal: Signal = {
  id: "github:llvm/llvm-project:issue:1",
  source: "github",
  group: "compilers",
  project: "llvm/llvm-project",
  kind: "issue",
  title: "Incorrect lowering",
  url: "https://github.com/llvm/llvm-project/issues/1",
  metrics: { comments: 3 },
};

describe("daily report", () => {
  it("renders a group report with primary evidence", () => {
    const report = renderGroupReport("2026-08-13", config.repoGroups[0]!, [signal]);
    expect(report).toContain("# Compiler Engineering Updates");
    expect(report).toContain("https://github.com/llvm/llvm-project/issues/1");
    expect(report).toContain("No analysis or synthesis is performed");
    expect(report).not.toContain("FoundationDB");
  });

  it("renders a summary that links to separate group reports", () => {
    const report = renderSummaryReport("2026-08-13", [
      { group: config.repoGroups[0]!, changedCount: 1 },
    ]);
    expect(report).toContain("./compilers.md");
    expect(report).not.toContain(signal.url);
  });
});
