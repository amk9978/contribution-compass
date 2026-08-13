import { signalAnchor, truncate } from "./format.js";
import type { SiteContext, SiteDate, SiteGroup, SiteModel, SiteRepository } from "./model.js";
import type { LocatedContributionLead } from "./contributions.js";

function json(value: unknown): string {
  return `${JSON.stringify(value, null, 2)}\n`;
}

function signalCount(date: SiteDate): number {
  return date.groups.reduce(
    (dateTotal, group) =>
      dateTotal +
      group.repositories.reduce(
        (groupTotal, repository) => groupTotal + repository.signals.length,
        0,
      ),
    0,
  );
}

export function renderApiIndex(
  model: SiteModel,
  context: SiteContext,
  leads: LocatedContributionLead[],
): string {
  return json({
    schema_version: 1,
    generated_at: model.generatedAt,
    description:
      "Normalized, evidence-first GitHub updates. No generated analysis or inferred conclusions.",
    latest_date: model.dates[0]?.date ?? null,
    links: {
      website: `${context.siteUrl}/`,
      contribution_leads: `${context.siteUrl}/api/v1/opportunities.json`,
      json_feed: `${context.siteUrl}/feed.json`,
      rss_feed: `${context.siteUrl}/feed.xml`,
      schema: `${context.siteUrl}/api/v1/schema.json`,
      llm_guide: `${context.siteUrl}/llms.txt`,
      repository: context.repositoryUrl,
    },
    contribution_method:
      "Deterministic label/state/assignee rules. Leads are not guarantees that maintainers will accept a contribution.",
    latest_contribution_lead_count: leads.length,
    dates: model.dates.map((date) => ({
      date: date.date,
      collected_at: date.collectedAt,
      signal_count: signalCount(date),
      api_url: `${context.siteUrl}/api/v1/dates/${date.date}/index.json`,
      page_url: `${context.siteUrl}/updates/${date.date}/`,
    })),
  });
}

export function renderDateApi(date: SiteDate, context: SiteContext): string {
  return json({
    schema_version: 1,
    date: date.date,
    collected_at: date.collectedAt,
    signal_count: signalCount(date),
    page_url: `${context.siteUrl}/updates/${date.date}/`,
    groups: date.groups.map((group) => ({
      id: group.id,
      name: group.name,
      repository_count: group.repositories.length,
      signal_count: group.repositories.reduce(
        (total, repository) => total + repository.signals.length,
        0,
      ),
      api_url: `${context.siteUrl}/api/v1/dates/${date.date}/groups/${group.id}/index.json`,
      page_url: `${context.siteUrl}/updates/${date.date}/${group.id}/`,
    })),
  });
}

export function renderGroupApi(date: SiteDate, group: SiteGroup, context: SiteContext): string {
  return json({
    schema_version: 1,
    date: date.date,
    group: { id: group.id, name: group.name },
    page_url: `${context.siteUrl}/updates/${date.date}/${group.id}/`,
    repositories: group.repositories.map((repository) => ({
      id: repository.id,
      repository: repository.repo,
      name: repository.name,
      signal_count: repository.signals.length,
      api_url: `${context.siteUrl}/api/v1/dates/${date.date}/groups/${group.id}/repositories/${repository.id}.json`,
      page_url: `${context.siteUrl}/updates/${date.date}/${group.id}/${repository.id}.html`,
    })),
  });
}

export function renderRepositoryApi(
  date: SiteDate,
  group: SiteGroup,
  repository: SiteRepository,
  context: SiteContext,
): string {
  return json({
    schema_version: 1,
    date: date.date,
    group: { id: group.id, name: group.name },
    repository: {
      id: repository.id,
      repository: repository.repo,
      name: repository.name,
    },
    page_url: `${context.siteUrl}/updates/${date.date}/${group.id}/${repository.id}.html`,
    runs: repository.runs,
    signals: repository.signals,
  });
}

function leadJson(lead: LocatedContributionLead, context: SiteContext): Record<string, unknown> {
  return {
    tier: lead.tier,
    rank_score: lead.score,
    reasons: lead.reasons,
    caveat: lead.caveat,
    date: lead.date,
    group: { id: lead.groupId, name: lead.groupName },
    repository: {
      id: lead.repositoryId,
      repository: lead.repository,
      name: lead.repositoryName,
    },
    issue: lead.signal,
    evidence_url: lead.signal.url,
    page_url: `${context.siteUrl}/updates/${lead.date}/${lead.groupId}/${lead.repositoryId}.html#${signalAnchor(lead.signal)}`,
  };
}

export function renderOpportunitiesApi(
  model: SiteModel,
  context: SiteContext,
  leads: LocatedContributionLead[],
): string {
  return json({
    schema_version: 1,
    generated_at: model.generatedAt,
    date: model.dates[0]?.date ?? null,
    description:
      "Evidence-backed contribution leads from open, unassigned issues in the latest collection.",
    methodology: {
      maintainer_invited:
        "Open, unassigned issues carrying an explicit invitation label such as good first issue or help wanted.",
      triage_lead:
        "Open, unassigned documentation issues or engaged bugs/enhancements without an explicit invitation.",
      exclusions:
        "Closed, assigned, stale, duplicate, invalid, blocked, question, needs-info, and needs-reproduction issues.",
      warning:
        "Ranking is deterministic discovery assistance, not an assertion of difficulty, suitability, or maintainer acceptance.",
    },
    count: leads.length,
    leads: leads.map((lead) => leadJson(lead, context)),
  });
}

interface FeedEntry {
  date: string;
  groupId: string;
  repositoryId: string;
  repositoryName: string;
  signal: SiteRepository["signals"][number];
}

function latestSignals(model: SiteModel, limit = 100): FeedEntry[] {
  return model.dates
    .flatMap((date) =>
      date.groups.flatMap((group) =>
        group.repositories.flatMap((repository) =>
          repository.signals.map((signal) => ({
            date: date.date,
            groupId: group.id,
            repositoryId: repository.id,
            repositoryName: repository.name,
            signal,
          })),
        ),
      ),
    )
    .sort(
      (left, right) =>
        new Date(right.signal.timestamp ?? `${right.date}T00:00:00Z`).getTime() -
        new Date(left.signal.timestamp ?? `${left.date}T00:00:00Z`).getTime(),
    )
    .slice(0, limit);
}

export function renderJsonFeed(model: SiteModel, context: SiteContext): string {
  return json({
    version: "https://jsonfeed.org/version/1.1",
    title: "Engineering Radar",
    home_page_url: `${context.siteUrl}/`,
    feed_url: `${context.siteUrl}/feed.json`,
    description: "Normalized GitHub engineering updates with direct primary evidence.",
    items: latestSignals(model).map(({ date, groupId, repositoryId, repositoryName, signal }) => ({
      id: `${date}:${signal.id}`,
      url: `${context.siteUrl}/updates/${date}/${groupId}/${repositoryId}.html#${signalAnchor(signal)}`,
      external_url: signal.url,
      title: `[${repositoryName}] ${signal.title}`,
      content_text:
        truncate(signal.text, 1200) || `${signal.kind} in ${signal.project ?? repositoryName}`,
      ...(signal.createdAt ? { date_published: signal.createdAt } : {}),
      ...((signal.updatedAt ?? signal.timestamp)
        ? { date_modified: signal.updatedAt ?? signal.timestamp }
        : {}),
      ...(signal.author ? { authors: [{ name: signal.author }] } : {}),
      tags: [signal.kind, ...(signal.labels ?? [])],
      _engineering_radar: {
        source: signal.source,
        kind: signal.kind,
        project: signal.project,
        group: signal.group,
        state: signal.state,
        assignees: signal.assignees,
        metrics: signal.metrics,
        change: signal.change,
      },
    })),
  });
}

export function renderApiSchema(context: SiteContext): string {
  return json({
    $schema: "https://json-schema.org/draft/2020-12/schema",
    $id: `${context.siteUrl}/api/v1/schema.json`,
    title: "Engineering Radar Signal",
    type: "object",
    required: ["id", "source", "kind", "title", "url"],
    properties: {
      id: { type: "string", description: "Stable source-qualified identity" },
      source: { const: "github" },
      group: { type: "string" },
      project: { type: "string", description: "GitHub owner/repository slug" },
      kind: { enum: ["issue", "pull_request", "release"] },
      title: { type: "string" },
      text: { type: "string" },
      url: { type: "string", format: "uri", description: "Original GitHub evidence" },
      createdAt: { type: "string", format: "date-time" },
      updatedAt: { type: "string", format: "date-time" },
      timestamp: { type: "string", format: "date-time" },
      metrics: {
        type: "object",
        properties: {
          reactions: { type: "integer", minimum: 0 },
          comments: { type: "integer", minimum: 0 },
        },
      },
      labels: { type: "array", items: { type: "string" } },
      author: { type: "string" },
      state: { enum: ["open", "closed"] },
      assignees: { type: "array", items: { type: "string" } },
      change: { enum: ["new", "updated"] },
    },
  });
}
