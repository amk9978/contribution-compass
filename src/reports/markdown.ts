import type { Signal } from "../signals/types.js";

export function markdownLink(label: string, url: string): string {
  return `[${label.replaceAll("[", "\\[").replaceAll("]", "\\]")}](${url})`;
}

export function signalLine(signal: Signal): string {
  const project = signal.project ? `${signal.project}: ` : "";
  const metrics = [
    signal.metrics?.score === undefined ? undefined : `${signal.metrics.score} points`,
    signal.metrics?.comments === undefined ? undefined : `${signal.metrics.comments} comments`,
    signal.metrics?.reactions === undefined ? undefined : `${signal.metrics.reactions} reactions`,
  ].filter(Boolean);
  const suffix = metrics.length > 0 ? ` — ${metrics.join(", ")}` : "";
  return `- ${markdownLink(`${project}${signal.title}`, signal.url)}${suffix}`;
}
