import { describe, expect, it } from "vitest";
import { normalizeGitHub } from "../signals/normalize.js";

describe("signal normalization", () => {
  it("normalizes GitHub observations into serializable signals", () => {
    const signal = normalizeGitHub({
      repository: "acme/widget",
      group: "systems",
      kind: "issue",
      number: 42,
      title: "  Cleanup is unreliable  ",
      body: "Line one\n\nLine two",
      url: "https://github.com/acme/widget/issues/42",
      createdAt: "2026-08-12T00:00:00Z",
      updatedAt: "2026-08-13T00:00:00Z",
      comments: 3,
      reactions: 2,
      labels: ["bug"],
      state: "open",
      assignees: [],
    });
    expect(signal).toMatchObject({
      id: "github:acme/widget:issue:42",
      source: "github",
      group: "systems",
      project: "acme/widget",
      text: "Line one Line two",
      timestamp: "2026-08-13T00:00:00Z",
      createdAt: "2026-08-12T00:00:00Z",
      updatedAt: "2026-08-13T00:00:00Z",
      metrics: { comments: 3, reactions: 2 },
      state: "open",
      assignees: [],
    });
    expect(() => JSON.stringify(signal)).not.toThrow();
  });
});
