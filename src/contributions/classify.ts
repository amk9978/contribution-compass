import type { Signal } from "../signals/types.js";

export type ContributionTier = "maintainer-invited" | "triage-lead";

export interface ContributionLead {
  signal: Signal;
  tier: ContributionTier;
  score: number;
  reasons: string[];
  caveat: string;
}

const invitationLabels = new Map<string, string>([
  ["good first issue", "Maintainers marked this as a good first issue"],
  ["help wanted", "Maintainers explicitly requested help"],
  ["up for grabs", "Maintainers marked this as available"],
  ["first timers only", "Maintainers reserved this for a first-time contributor"],
  ["beginner friendly", "Maintainers marked this as beginner-friendly"],
  ["contributions welcome", "Maintainers explicitly welcome contributions"],
]);

const disqualifyingLabels = new Set([
  "blocked",
  "duplicate",
  "invalid",
  "needs info",
  "needs repro",
  "question",
  "stale",
  "waiting for author",
  "waiting for response",
  "wontfix",
  "won't fix",
]);

function normalizeLabel(value: string): string {
  return value.toLowerCase().replaceAll(/[_-]+/g, " ").replaceAll(/\s+/g, " ").trim();
}

function hasCategory(labels: string[], category: "bug" | "documentation" | "enhancement"): boolean {
  if (category === "documentation") {
    return labels.some(
      (label) =>
        label === "docs" ||
        label === "documentation" ||
        label.endsWith(" docs") ||
        label.endsWith(":docs") ||
        label.endsWith("/docs"),
    );
  }
  return labels.some(
    (label) =>
      label === category || label.endsWith(`/${category}`) || label.startsWith(`${category}:`),
  );
}

export function classifyContributionLead(signal: Signal): ContributionLead | undefined {
  if (signal.kind !== "issue" || signal.state !== "open" || signal.assignees?.length !== 0) {
    return undefined;
  }

  const labels = (signal.labels ?? []).map(normalizeLabel);
  if (labels.some((label) => disqualifyingLabels.has(label))) return undefined;

  const invitations = labels
    .map((label) => invitationLabels.get(label))
    .filter((reason): reason is string => reason !== undefined);
  const comments = signal.metrics?.comments ?? 0;
  const reactions = signal.metrics?.reactions ?? 0;
  const engagementScore = Math.min(reactions, 15) + Math.min(Math.floor(comments / 4), 10);

  if (invitations.length > 0) {
    const starterBonus =
      labels.includes("good first issue") || labels.includes("first timers only") ? 15 : 0;
    return {
      signal,
      tier: "maintainer-invited",
      score: 60 + starterBonus + engagementScore,
      reasons: [...new Set([...invitations, "No assignee is listed"])],
      caveat: "Confirm scope and availability with the maintainers before starting work.",
    };
  }

  const reasons: string[] = [];
  let categoryScore = 0;
  if (hasCategory(labels, "documentation")) {
    reasons.push("Documentation-related issue with no assignee listed");
    categoryScore = 24;
  } else if (hasCategory(labels, "bug") && comments + reactions >= 4) {
    reasons.push("Unassigned bug with visible community engagement");
    categoryScore = 18;
  } else if (hasCategory(labels, "enhancement") && reactions >= 3) {
    reasons.push("Unassigned enhancement with community reactions");
    categoryScore = 14;
  } else {
    return undefined;
  }

  return {
    signal,
    tier: "triage-lead",
    score: categoryScore + engagementScore,
    reasons,
    caveat:
      "No explicit contribution invitation was found; ask maintainers whether a contribution is wanted.",
  };
}

export function rankContributionLeads(signals: Signal[], limit = 100): ContributionLead[] {
  return signals
    .map(classifyContributionLead)
    .filter((lead): lead is ContributionLead => lead !== undefined)
    .sort(
      (left, right) => right.score - left.score || left.signal.id.localeCompare(right.signal.id),
    )
    .slice(0, limit);
}
