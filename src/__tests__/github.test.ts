import { describe, expect, it } from "vitest";
import { fetchRecentGitHubItems } from "../sources/github.js";

const repo = { id: "widget", repo: "acme/widget", name: "Widget", paginated: true };
const since = new Date("2026-08-12T00:00:00.000Z");

function response(value: unknown): Response {
  return new Response(JSON.stringify(value), {
    status: 200,
    headers: { "Content-Type": "application/json" },
  });
}

describe("GitHub collection", () => {
  it("separates issues from pull requests and extracts evidence fields", async () => {
    const fetchMock: typeof fetch = (input) => {
      const url = new URL(input instanceof Request ? input.url : input);
      if (url.pathname.endsWith("/releases")) return Promise.resolve(response([]));
      return Promise.resolve(
        response([
          {
            number: 1,
            title: "Resource leak",
            body: "Workers remain alive",
            html_url: "https://github.com/acme/widget/issues/1",
            created_at: "2026-08-12T01:00:00Z",
            updated_at: "2026-08-13T01:00:00Z",
            comments: 7,
            reactions: { total_count: 4 },
            labels: [{ name: "bug" }],
            user: { login: "dev" },
            state: "open",
            assignees: [],
          },
          {
            number: 2,
            title: "Fix resource leak",
            html_url: "https://github.com/acme/widget/pull/2",
            created_at: "2026-08-12T02:00:00Z",
            updated_at: "2026-08-13T02:00:00Z",
            comments: 2,
            reactions: { total_count: 1 },
            labels: ["cleanup"],
            user: { login: "fixer" },
            state: "closed",
            assignees: [{ login: "maintainer" }],
            pull_request: { url: "api-url" },
          },
        ]),
      );
    };

    const signals = await fetchRecentGitHubItems(repo, "systems", since, {
      fetch: fetchMock,
      pageSize: 100,
    });
    expect(signals.map((signal) => signal.kind)).toEqual(["issue", "pull_request"]);
    expect(signals[0]).toMatchObject({
      labels: ["bug"],
      reactions: 4,
      comments: 7,
      author: "dev",
      state: "open",
      assignees: [],
      updatedAt: "2026-08-13T01:00:00Z",
    });
    expect(signals[1]).toMatchObject({ state: "closed", assignees: ["maintainer"] });
  });

  it("stops pagination when the oldest item predates the cutoff", async () => {
    const requestedIssuePages: string[] = [];
    const fetchMock: typeof fetch = (input) => {
      const url = new URL(input instanceof Request ? input.url : input);
      if (url.pathname.endsWith("/releases")) return Promise.resolve(response([]));
      requestedIssuePages.push(url.searchParams.get("page") ?? "");
      return Promise.resolve(
        response([
          {
            number: 1,
            title: "Recent",
            html_url: "https://github.com/acme/widget/issues/1",
            created_at: "2026-08-13T00:00:00Z",
            updated_at: "2026-08-13T00:00:00Z",
          },
          {
            number: 2,
            title: "Old",
            html_url: "https://github.com/acme/widget/issues/2",
            created_at: "2026-08-01T00:00:00Z",
            updated_at: "2026-08-01T00:00:00Z",
          },
        ]),
      );
    };

    await fetchRecentGitHubItems(repo, "systems", since, {
      fetch: fetchMock,
      pageSize: 2,
      maxPages: 5,
    });
    expect(requestedIssuePages).toEqual(["1"]);
  });
});
