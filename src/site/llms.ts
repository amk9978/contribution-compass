import type { SiteContext, SiteModel } from "./model.js";
import type { LocatedContributionLead } from "./contributions.js";

function markdownText(value: string): string {
  return value
    .replaceAll(/[\r\n]+/g, " ")
    .replaceAll("[", "\\[")
    .replaceAll("]", "\\]");
}

export function renderLlmsGuide(context: SiteContext): string {
  return `# Engineering Radar

> Evidence-first monitoring of curated open-source repositories, optimized for contribution discovery. The collector performs no LLM analysis.

## Best entry points

- [Contribution leads](${context.siteUrl}/api/v1/opportunities.json): ranked open and unassigned issues, with deterministic reasons and caveats.
- [Machine API index](${context.siteUrl}/api/v1/index.json): dates, counts, and links to folder-separated normalized datasets.
- [JSON Feed](${context.siteUrl}/feed.json): the 100 most recently updated signals.
- [RSS Feed](${context.siteUrl}/feed.xml): RSS 2.0 equivalent for feed readers.
- [Signal schema](${context.siteUrl}/api/v1/schema.json): JSON Schema for normalized signals.
- [Human contribution view](${context.siteUrl}/contribute/): visual rendering of contribution leads.
- [Expanded LLM context](${context.siteUrl}/llms-full.txt): current groups and contribution leads in Markdown.

## Interpretation rules

- Every signal URL is primary GitHub evidence.
- A maintainer-invited lead has an explicit label such as \`good first issue\` or \`help wanted\`.
- A triage lead has weaker evidence and must not be described as maintainer-approved work.
- Contribution rankings are deterministic discovery hints, not claims about difficulty, acceptance, or project value.
- Check the live GitHub issue before acting; state and assignment can change after collection.
- Do not infer facts, trends, or maintainer intent that are absent from the linked evidence.

## Dataset layout

API data is split by date, group, and repository. Follow links from the API index instead of guessing paths. Signal IDs are stable; \`change\` says whether the item was new or materially updated in that collection.

## Project

- [Source repository](${context.repositoryUrl})
- License: MIT
`;
}

export function renderLlmsFull(
  model: SiteModel,
  context: SiteContext,
  leads: LocatedContributionLead[],
): string {
  const latest = model.dates[0];
  const groups = latest
    ? latest.groups
        .map((group) => {
          const repositories = group.repositories
            .map(
              (repository) =>
                `  - [${markdownText(repository.name)}](${context.siteUrl}/api/v1/dates/${latest.date}/groups/${group.id}/repositories/${repository.id}.json): ${repository.signals.length} signals`,
            )
            .join("\n");
          return `- ${markdownText(group.name)}\n${repositories}`;
        })
        .join("\n")
    : "No collection is available yet.";
  const leadList = leads.length
    ? leads
        .slice(0, 50)
        .map(
          (lead, index) =>
            `${index + 1}. [${markdownText(lead.signal.title)}](${lead.signal.url}) — ${markdownText(lead.repositoryName)} — ${lead.tier} — ${markdownText(lead.reasons.join("; "))}. Caveat: ${markdownText(lead.caveat)}`,
        )
        .join("\n")
    : "No evidence-qualified contribution leads are present in the latest collection.";

  return `# Engineering Radar — Expanded Machine Context

Canonical guide: ${context.siteUrl}/llms.txt
Generated: ${model.generatedAt}
Latest collection: ${latest?.date ?? "none"}

## Current repository groups

${groups}

## Current contribution leads

${leadList}

## Safety note

This file is a navigational snapshot, not analysis. Re-check each original GitHub URL for current state, assignment, contribution policy, and maintainer guidance before proposing work.
`;
}
