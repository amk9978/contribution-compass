import type { Signal } from "../signals/types.js";
import {
  compactNumber,
  escapeHtml,
  formatDate,
  formatTimestamp,
  safeUrl,
  signalAnchor,
  truncate,
} from "./format.js";
import type { SiteContext, SiteDate, SiteGroup, SiteModel, SiteRepository } from "./model.js";

interface Stats {
  total: number;
  issues: number;
  pullRequests: number;
  releases: number;
}

function stats(signals: Signal[]): Stats {
  return {
    total: signals.length,
    issues: signals.filter((signal) => signal.kind === "issue").length,
    pullRequests: signals.filter((signal) => signal.kind === "pull_request").length,
    releases: signals.filter((signal) => signal.kind === "release").length,
  };
}

function allSignals(date: SiteDate): Signal[] {
  return date.groups.flatMap((group) =>
    group.repositories.flatMap((repository) => repository.signals),
  );
}

function page(
  title: string,
  description: string,
  content: string,
  context: SiteContext,
  options: { bodyClass?: string } = {},
): string {
  return `<!doctype html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="${escapeHtml(description)}">
  <meta name="color-scheme" content="dark light">
  <title>${escapeHtml(title)} · Engineering Radar</title>
  <link rel="icon" href="${context.siteUrl}/assets/favicon.svg" type="image/svg+xml">
  <link rel="alternate" type="application/rss+xml" title="Engineering Radar RSS" href="${context.siteUrl}/feed.xml">
  <link rel="stylesheet" href="${context.siteUrl}/assets/styles.css">
</head>
<body class="${escapeHtml(options.bodyClass ?? "")}">
  <header class="topbar">
    <a class="brand" href="${context.siteUrl}/"><span class="brand-mark" aria-hidden="true">◉</span><span>engineering/<strong>radar</strong></span></a>
    <nav class="topnav" aria-label="Primary">
      <a href="${context.siteUrl}/feed.xml">RSS</a>
      <a href="${context.repositoryUrl}">GitHub</a>
      <button class="theme-toggle" type="button" aria-label="Toggle color theme">◐</button>
    </nav>
  </header>
  ${content}
  <footer class="footer"><span>Collected from primary GitHub evidence.</span><span>No generated analysis.</span></footer>
  <script src="${context.siteUrl}/assets/app.js" defer></script>
</body>
</html>`;
}

function metricCard(label: string, value: number, detail: string): string {
  return `<div class="metric"><span>${escapeHtml(label)}</span><strong>${compactNumber(value)}</strong><small>${escapeHtml(detail)}</small></div>`;
}

function kindBadges(values: Stats): string {
  return `<div class="kind-row"><span class="kind issue">${values.issues} issues</span><span class="kind pull_request">${values.pullRequests} PRs</span><span class="kind release">${values.releases} releases</span></div>`;
}

function breadcrumb(items: Array<{ label: string; url?: string }>): string {
  return `<nav class="breadcrumbs" aria-label="Breadcrumb">${items
    .map((item, index) => {
      const separator = index === 0 ? "" : '<span aria-hidden="true">/</span>';
      return `${separator}${item.url ? `<a href="${item.url}">${escapeHtml(item.label)}</a>` : `<span>${escapeHtml(item.label)}</span>`}`;
    })
    .join("")}</nav>`;
}

function signalRow(signal: Signal): string {
  const body = truncate(signal.text, 360);
  const labels = (signal.labels ?? []).slice(0, 5);
  const search = [
    signal.title,
    truncate(signal.text, 600),
    signal.author,
    signal.kind,
    ...(signal.labels ?? []),
  ]
    .filter(Boolean)
    .join(" ")
    .toLowerCase();
  return `<article class="signal-card" id="${signalAnchor(signal)}" data-kind="${signal.kind}" data-search="${escapeHtml(search)}">
    <div class="signal-head">
      <span class="kind ${signal.kind}">${signal.kind === "pull_request" ? "pull request" : signal.kind}</span>
      <time datetime="${escapeHtml(signal.timestamp ?? "")}">${escapeHtml(formatTimestamp(signal.timestamp))} UTC</time>
    </div>
    <h3><a href="${safeUrl(signal.url)}">${escapeHtml(signal.title)}</a></h3>
    ${body ? `<p>${escapeHtml(body)}</p>` : ""}
    <div class="signal-meta">
      ${signal.author ? `<span>@${escapeHtml(signal.author)}</span>` : ""}
      ${signal.metrics?.comments !== undefined ? `<span>${signal.metrics.comments} comments</span>` : ""}
      ${signal.metrics?.reactions !== undefined ? `<span>${signal.metrics.reactions} reactions</span>` : ""}
      ${labels.map((label) => `<span class="label">${escapeHtml(label)}</span>`).join("")}
      <a class="evidence" href="${safeUrl(signal.url)}">Original evidence ↗</a>
    </div>
  </article>`;
}

export function renderHome(model: SiteModel, context: SiteContext): string {
  const latest = model.dates[0];
  if (!latest) {
    return page(
      "Engineering updates",
      "Collected GitHub engineering signals",
      `<main class="empty-state"><span class="eyebrow">ENGINEERING RADAR</span><h1>Waiting for the first scan</h1><p>Run the Engineering Radar workflow to publish collected updates.</p></main>`,
      context,
    );
  }

  const signals = allSignals(latest);
  const totals = stats(signals);
  const activeRepositories = latest.groups
    .flatMap((group) => group.repositories)
    .filter((repository) => repository.signals.length > 0).length;
  const recent = [...signals]
    .sort(
      (left, right) =>
        new Date(right.timestamp ?? 0).getTime() - new Date(left.timestamp ?? 0).getTime(),
    )
    .slice(0, 12);
  const maxGroup = Math.max(
    1,
    ...latest.groups.map((group) =>
      group.repositories.reduce((sum, repository) => sum + repository.signals.length, 0),
    ),
  );
  const content = `<main>
    <section class="hero shell">
      <div><span class="eyebrow">LATEST COLLECTION · ${escapeHtml(latest.date)}</span><h1>Open-source engineering,<br><em>as it changes.</em></h1><p>Issues, pull requests, and releases collected from ${latest.groups.reduce((sum, group) => sum + group.repositories.length, 0)} curated repositories. Every update links to primary evidence.</p></div>
      <a class="date-chip" href="${context.siteUrl}/updates/${latest.date}/"><span>Browse snapshot</span><strong>${escapeHtml(formatDate(latest.date))}</strong></a>
    </section>
    <section class="metrics shell" aria-label="Latest collection statistics">
      ${metricCard("Signals", totals.total, "new or changed")}
      ${metricCard("Repositories", activeRepositories, "with activity")}
      ${metricCard("Issues", totals.issues, "tracked updates")}
      ${metricCard("Pull requests", totals.pullRequests, "tracked updates")}
      ${metricCard("Releases", totals.releases, "published versions")}
    </section>
    <section class="section shell">
      <div class="section-heading"><div><span class="eyebrow">ACTIVITY MAP</span><h2>Repository groups</h2></div><span>${latest.groups.length} configured ecosystems</span></div>
      <div class="group-grid">
        ${latest.groups
          .map((group) => {
            const count = group.repositories.reduce(
              (sum, repository) => sum + repository.signals.length,
              0,
            );
            const groupStats = stats(
              group.repositories.flatMap((repository) => repository.signals),
            );
            return `<a class="group-card" href="${context.siteUrl}/updates/${latest.date}/${group.id}/">
              <div class="group-title"><h3>${escapeHtml(group.name)}</h3><strong>${compactNumber(count)}</strong></div>
              <div class="activity-bar"><span style="width:${Math.max(1, Math.round((count / maxGroup) * 100))}%"></span></div>
              <div class="group-meta"><span>${group.repositories.length} repos</span><span>${groupStats.issues} issues · ${groupStats.pullRequests} PRs · ${groupStats.releases} releases</span></div>
            </a>`;
          })
          .join("")}
      </div>
    </section>
    <section class="section shell">
      <div class="section-heading"><div><span class="eyebrow">LATEST EVIDENCE</span><h2>Recently updated</h2></div><a href="${context.siteUrl}/updates/${latest.date}/">View full snapshot →</a></div>
      <div class="signal-list compact-list">${recent.map(signalRow).join("")}</div>
    </section>
    <section class="section shell archive">
      <div class="section-heading"><div><span class="eyebrow">ARCHIVE</span><h2>Collection history</h2></div><a href="${context.siteUrl}/feed.xml">Subscribe via RSS →</a></div>
      <div class="date-grid">${model.dates
        .map((date) => {
          const dateSignals = allSignals(date);
          return `<a href="${context.siteUrl}/updates/${date.date}/"><strong>${escapeHtml(formatDate(date.date))}</strong><span>${compactNumber(dateSignals.length)} updates</span></a>`;
        })
        .join("")}</div>
    </section>
  </main>`;
  return page(
    "Engineering updates",
    "Daily issues, pull requests, and releases from curated open-source projects",
    content,
    context,
  );
}

export function renderDatePage(date: SiteDate, context: SiteContext): string {
  const signals = allSignals(date);
  const totals = stats(signals);
  const content = `<main class="shell detail-page">
    ${breadcrumb([{ label: "Radar", url: `${context.siteUrl}/` }, { label: date.date }])}
    <section class="detail-hero"><span class="eyebrow">DAILY SNAPSHOT</span><h1>${escapeHtml(formatDate(date.date))}</h1><p>Collected ${escapeHtml(formatTimestamp(date.collectedAt))} UTC</p></section>
    <section class="metrics compact-metrics">${metricCard("Signals", totals.total, "new or changed")}${metricCard("Issues", totals.issues, "updates")}${metricCard("Pull requests", totals.pullRequests, "updates")}${metricCard("Releases", totals.releases, "published")}</section>
    <section class="section"><div class="section-heading"><div><span class="eyebrow">GROUPS</span><h2>Browse by ecosystem</h2></div></div>
      <div class="group-grid">${date.groups
        .map((group) => {
          const groupSignals = group.repositories.flatMap((repository) => repository.signals);
          return `<a class="group-card" href="${context.siteUrl}/updates/${date.date}/${group.id}/"><div class="group-title"><h3>${escapeHtml(group.name)}</h3><strong>${compactNumber(groupSignals.length)}</strong></div>${kindBadges(stats(groupSignals))}<div class="group-meta"><span>${group.repositories.length} repositories</span><span>Explore →</span></div></a>`;
        })
        .join("")}</div>
    </section>
  </main>`;
  return page(
    `${formatDate(date.date)} snapshot`,
    `Collected GitHub updates for ${date.date}`,
    content,
    context,
  );
}

export function renderGroupPage(date: SiteDate, group: SiteGroup, context: SiteContext): string {
  const signals = group.repositories.flatMap((repository) => repository.signals);
  const content = `<main class="shell detail-page">
    ${breadcrumb([
      { label: "Radar", url: `${context.siteUrl}/` },
      { label: date.date, url: `${context.siteUrl}/updates/${date.date}/` },
      { label: group.name },
    ])}
    <section class="detail-hero"><span class="eyebrow">${escapeHtml(date.date)}</span><h1>${escapeHtml(group.name)}</h1><p>${signals.length} new or changed signals across ${group.repositories.length} repositories.</p></section>
    <section class="repository-grid">${group.repositories
      .map((repository) => {
        const repositoryStats = stats(repository.signals);
        return `<a class="repository-card" href="${context.siteUrl}/updates/${date.date}/${group.id}/${repository.id}.html"><div><span class="repo-slug">${escapeHtml(repository.repo)}</span><h2>${escapeHtml(repository.name)}</h2></div><strong>${compactNumber(repositoryStats.total)}</strong>${kindBadges(repositoryStats)}<span class="repo-link">View evidence →</span></a>`;
      })
      .join("")}</section>
  </main>`;
  return page(
    `${group.name} · ${date.date}`,
    `${group.name} GitHub updates for ${date.date}`,
    content,
    context,
  );
}

export function renderRepositoryPage(
  date: SiteDate,
  group: SiteGroup,
  repository: SiteRepository,
  context: SiteContext,
): string {
  const repositoryStats = stats(repository.signals);
  const signals = [...repository.signals].sort(
    (left, right) =>
      new Date(right.timestamp ?? 0).getTime() - new Date(left.timestamp ?? 0).getTime(),
  );
  const content = `<main class="shell detail-page">
    ${breadcrumb([
      { label: "Radar", url: `${context.siteUrl}/` },
      { label: date.date, url: `${context.siteUrl}/updates/${date.date}/` },
      { label: group.name, url: `${context.siteUrl}/updates/${date.date}/${group.id}/` },
      { label: repository.name },
    ])}
    <section class="repo-hero"><div><span class="eyebrow">${escapeHtml(repository.repo)}</span><h1>${escapeHtml(repository.name)}</h1><p>${repositoryStats.total} new or changed signals collected for ${escapeHtml(date.date)}.</p></div><a class="primary-button" href="https://github.com/${escapeHtml(repository.repo)}">Open repository ↗</a></section>
    <section class="metrics compact-metrics">${metricCard("Signals", repositoryStats.total, "new or changed")}${metricCard("Issues", repositoryStats.issues, "updates")}${metricCard("Pull requests", repositoryStats.pullRequests, "updates")}${metricCard("Releases", repositoryStats.releases, "published")}</section>
    <section class="filter-bar" aria-label="Filter updates"><input id="signal-search" type="search" placeholder="Search titles, bodies, labels…" autocomplete="off"><div class="filter-buttons"><button type="button" class="active" data-filter="all">All</button><button type="button" data-filter="issue">Issues</button><button type="button" data-filter="pull_request">PRs</button><button type="button" data-filter="release">Releases</button></div><span id="filter-count">${signals.length} shown</span></section>
    <section class="signal-list" id="signal-list">${signals.length ? signals.map(signalRow).join("") : '<div class="no-signals">No updates were collected for this repository.</div>'}</section>
  </main>`;
  return page(
    `${repository.name} · ${date.date}`,
    `${repository.repo} GitHub updates collected on ${date.date}`,
    content,
    context,
    { bodyClass: "repository-page" },
  );
}
