import { describe, expect, it } from "vitest";
import { parseConfig } from "../config/schema.js";

function config(repoGroups: unknown): unknown {
  return { repo_groups: repoGroups };
}

describe("configuration", () => {
  it("loads arbitrary groups", () => {
    const result = parseConfig(
      config({
        compilers: {
          name: "Compilers",
          repos: [{ id: "llvm", repo: "llvm/llvm-project", name: "LLVM" }],
        },
      }),
    );
    expect(result.repoGroups).toEqual([
      {
        id: "compilers",
        name: "Compilers",
        repos: [{ id: "llvm", repo: "llvm/llvm-project", name: "LLVM" }],
      },
    ]);
  });

  it("keeps empty repository arrays empty", () => {
    const result = parseConfig(config({ empty: { name: "Empty", repos: [] } }));
    expect(result.repoGroups[0]?.repos).toEqual([]);
  });

  it("does not introduce hidden groups or repositories", () => {
    const result = parseConfig(config({ custom: { name: "Custom", repos: [] } }));
    expect(result.repoGroups.map((group) => group.id)).toEqual(["custom"]);
    expect(JSON.stringify(result)).not.toContain(["open", "claw"].join(""));
  });

  it("rejects malformed repository entries", () => {
    expect(() =>
      parseConfig(config({ bad: { name: "Bad", repos: [{ id: "x", repo: "not-a-slug" }] } })),
    ).toThrow(/name|owner\/repository/);
  });

  it("detects duplicate repository ids across groups", () => {
    expect(() =>
      parseConfig(
        config({
          first: { name: "First", repos: [{ id: "same", repo: "a/b", name: "A" }] },
          second: { name: "Second", repos: [{ id: "same", repo: "c/d", name: "B" }] },
        }),
      ),
    ).toThrow(/duplicate repository id/);
  });

  it("rejects identifiers that cannot safely become paths", () => {
    expect(() => parseConfig(config({ "../bad": { name: "Bad", repos: [] } }))).toThrow(
      /filesystem-safe/,
    );
  });
});
