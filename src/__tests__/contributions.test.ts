import { describe, expect, it } from "vitest";
import { classifyContributionLead, rankContributionLeads } from "../contributions/classify.js";
import type { Signal } from "../signals/types.js";

function issue(overrides: Partial<Signal> = {}): Signal {
  return {
    id: "github:acme/widget:issue:1",
    source: "github",
    project: "acme/widget",
    kind: "issue",
    title: "Improve cleanup",
    url: "https://github.com/acme/widget/issues/1",
    state: "open",
    assignees: [],
    labels: [],
    metrics: { comments: 0, reactions: 0 },
    ...overrides,
  };
}

describe("contribution lead classification", () => {
  it("prioritizes explicit maintainer invitations and explains the evidence", () => {
    const lead = classifyContributionLead(
      issue({
        labels: ["enhancement", "good first issue"],
        metrics: { comments: 8, reactions: 5 },
      }),
    );

    expect(lead).toMatchObject({ tier: "maintainer-invited" });
    expect(lead?.reasons).toContain("Maintainers marked this as a good first issue");
    expect(lead?.reasons).toContain("No assignee is listed");
  });

  it("rejects closed, assigned, stale, and non-issue signals", () => {
    expect(
      classifyContributionLead(issue({ state: "closed", labels: ["help wanted"] })),
    ).toBeUndefined();
    expect(
      classifyContributionLead(issue({ assignees: ["maintainer"], labels: ["help wanted"] })),
    ).toBeUndefined();
    expect(
      classifyContributionLead(issue({ labels: ["good first issue", "stale"] })),
    ).toBeUndefined();
    expect(
      classifyContributionLead(issue({ kind: "pull_request", labels: ["help wanted"] })),
    ).toBeUndefined();
  });

  it("keeps lower-confidence triage leads separate from explicit invitations", () => {
    const docs = classifyContributionLead(issue({ labels: ["area:docs"] }));
    const engagedBug = classifyContributionLead(
      issue({ id: "bug", labels: ["kind/bug"], metrics: { comments: 4, reactions: 2 } }),
    );
    const quietBug = classifyContributionLead(
      issue({ id: "quiet", labels: ["bug"], metrics: { comments: 1, reactions: 0 } }),
    );

    expect(docs?.tier).toBe("triage-lead");
    expect(engagedBug?.tier).toBe("triage-lead");
    expect(quietBug).toBeUndefined();
    expect(rankContributionLeads([docs!.signal, issue({ labels: ["help wanted"] })])[0]?.tier).toBe(
      "maintainer-invited",
    );
  });
});
