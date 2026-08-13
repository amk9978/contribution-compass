import type { Signal } from "../signals/types.js";
import { escapeXml, signalAnchor, truncate } from "./format.js";
import type { SiteContext, SiteModel } from "./model.js";

interface FeedSignal {
  date: string;
  groupId: string;
  repositoryId: string;
  repositoryName: string;
  signal: Signal;
}

function feedSignals(model: SiteModel): FeedSignal[] {
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
    .slice(0, 100);
}

export function renderRss(model: SiteModel, context: SiteContext): string {
  const entries = feedSignals(model);
  const latestBuild = model.dates[0]?.collectedAt ?? model.generatedAt;
  const items = entries
    .map(({ date, groupId, repositoryId, repositoryName, signal }) => {
      const pageUrl = `${context.siteUrl}/updates/${date}/${groupId}/${repositoryId}.html#${signalAnchor(signal)}`;
      const summary =
        truncate(signal.text, 700) || `${signal.kind} in ${signal.project ?? repositoryName}`;
      const description = `${summary}\n\nOriginal evidence: ${signal.url}`;
      const published = new Date(signal.timestamp ?? `${date}T00:00:00Z`).toUTCString();
      return `    <item>
      <title>${escapeXml(`[${repositoryName}] ${signal.title}`)}</title>
      <link>${escapeXml(pageUrl)}</link>
      <guid isPermaLink="false">${escapeXml(`${date}:${signal.id}`)}</guid>
      <pubDate>${published}</pubDate>
      <category>${escapeXml(signal.kind)}</category>
      <description>${escapeXml(description)}</description>
      <source url="${escapeXml(signal.url)}">GitHub evidence</source>
    </item>`;
    })
    .join("\n");

  return `<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>Engineering Radar</title>
    <link>${escapeXml(context.siteUrl)}</link>
    <description>Issues, pull requests, and releases collected from curated open-source projects.</description>
    <language>en</language>
    <lastBuildDate>${new Date(latestBuild).toUTCString()}</lastBuildDate>
    <atom:link href="${escapeXml(`${context.siteUrl}/feed.xml`)}" rel="self" type="application/rss+xml"/>
${items}
  </channel>
</rss>
`;
}

export function renderSitemap(model: SiteModel, context: SiteContext): string {
  const urls = [
    `${context.siteUrl}/`,
    `${context.siteUrl}/contribute/`,
    ...model.dates.flatMap((date) => [
      `${context.siteUrl}/updates/${date.date}/`,
      ...date.groups.flatMap((group) => [
        `${context.siteUrl}/updates/${date.date}/${group.id}/`,
        ...group.repositories.map(
          (repository) =>
            `${context.siteUrl}/updates/${date.date}/${group.id}/${repository.id}.html`,
        ),
      ]),
    ]),
  ];
  return `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${urls.map((url) => `  <url><loc>${escapeXml(url)}</loc></url>`).join("\n")}
</urlset>
`;
}
