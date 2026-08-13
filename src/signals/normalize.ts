import type { GitHubSignal } from "../sources/github.js";
import type { Signal } from "./types.js";

function compactText(text: string | undefined): string | undefined {
  const compact = text?.replace(/\s+/g, " ").trim();
  return compact || undefined;
}

export function normalizeGitHub(signal: GitHubSignal): Signal {
  const numberOrUrl = signal.number === undefined ? signal.url : String(signal.number);
  const text = compactText(signal.body);
  return {
    id: `github:${signal.repository}:${signal.kind}:${numberOrUrl}`,
    source: "github",
    group: signal.group,
    project: signal.repository,
    kind: signal.kind,
    title: signal.title,
    ...(text ? { text } : {}),
    url: signal.url,
    ...(signal.createdAt ? { createdAt: signal.createdAt } : {}),
    ...(signal.updatedAt ? { updatedAt: signal.updatedAt } : {}),
    ...(signal.updatedAt || signal.createdAt
      ? { timestamp: signal.updatedAt ?? signal.createdAt }
      : {}),
    ...(signal.kind === "release"
      ? {}
      : { metrics: { comments: signal.comments ?? 0, reactions: signal.reactions ?? 0 } }),
    ...(signal.labels ? { labels: signal.labels } : {}),
    ...(signal.author ? { author: signal.author } : {}),
    ...(signal.state ? { state: signal.state } : {}),
    ...(signal.assignees ? { assignees: signal.assignees } : {}),
  };
}
