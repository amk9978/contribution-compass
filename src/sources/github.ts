import type { RepoConfig, RepoGroup } from "../config/schema.js";

export interface GitHubSignal {
  repository: string;
  group: string;
  kind: "issue" | "pull_request" | "release";
  number?: number;
  title: string;
  body?: string;
  url: string;
  createdAt?: string;
  updatedAt?: string;
  comments?: number;
  reactions?: number;
  labels?: string[];
  author?: string;
  state?: "open" | "closed";
  assignees?: string[];
}

interface GitHubUser {
  login?: string;
}

interface GitHubLabel {
  name?: string;
}

interface GitHubIssueResponse {
  number: number;
  title: string;
  body?: string | null;
  html_url: string;
  created_at: string;
  updated_at: string;
  comments?: number;
  reactions?: { total_count?: number };
  labels?: Array<GitHubLabel | string>;
  user?: GitHubUser | null;
  state?: "open" | "closed";
  assignees?: GitHubUser[];
  pull_request?: unknown;
}

interface GitHubReleaseResponse {
  id: number;
  tag_name: string;
  name?: string | null;
  body?: string | null;
  html_url: string;
  published_at?: string | null;
  created_at?: string;
  author?: GitHubUser | null;
}

export interface GitHubCollectorOptions {
  fetch?: typeof fetch;
  token?: string;
  pageSize?: number;
  maxPages?: number;
  logger?: Pick<Console, "log" | "error">;
}

function githubHeaders(token: string | undefined): Record<string, string> {
  return {
    ...(token ? { Authorization: `Bearer ${token}` } : {}),
    Accept: "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
    "User-Agent": "engineering-radar/0.1",
  };
}

function labelsOf(labels: Array<GitHubLabel | string> | undefined): string[] {
  return (labels ?? [])
    .map((label) => (typeof label === "string" ? label : label.name))
    .filter((label): label is string => Boolean(label));
}

function toIssueSignal(item: GitHubIssueResponse, repo: string, group: string): GitHubSignal {
  const body = item.body?.trim();
  return {
    repository: repo,
    group,
    kind: item.pull_request ? "pull_request" : "issue",
    number: item.number,
    title: item.title,
    ...(body ? { body } : {}),
    url: item.html_url,
    createdAt: item.created_at,
    updatedAt: item.updated_at,
    comments: item.comments ?? 0,
    reactions: item.reactions?.total_count ?? 0,
    labels: labelsOf(item.labels),
    ...(item.user?.login ? { author: item.user.login } : {}),
    ...(item.state ? { state: item.state } : {}),
    assignees: (item.assignees ?? [])
      .map((assignee) => assignee.login)
      .filter((login): login is string => Boolean(login)),
  };
}

function toReleaseSignal(item: GitHubReleaseResponse, repo: string, group: string): GitHubSignal {
  const body = item.body?.trim();
  const publishedAt = item.published_at ?? item.created_at;
  return {
    repository: repo,
    group,
    kind: "release",
    title: item.name?.trim() || item.tag_name,
    ...(body ? { body } : {}),
    url: item.html_url,
    ...(publishedAt ? { createdAt: publishedAt, updatedAt: publishedAt } : {}),
    ...(item.author?.login ? { author: item.author.login } : {}),
  };
}

async function getJson<T>(url: URL, options: GitHubCollectorOptions): Promise<T> {
  const response = await (options.fetch ?? fetch)(url, {
    headers: githubHeaders(options.token ?? process.env["GITHUB_TOKEN"]),
  });
  if (!response.ok) {
    const detail = (await response.text()).slice(0, 500);
    throw new Error(`GitHub API ${response.status} for ${url.pathname}: ${detail}`);
  }
  return (await response.json()) as T;
}

export async function fetchRecentGitHubItems(
  repo: RepoConfig,
  groupId: string,
  since: Date,
  options: GitHubCollectorOptions = {},
): Promise<GitHubSignal[]> {
  const pageSize = options.pageSize ?? 100;
  const maxPages = repo.paginated ? (options.maxPages ?? 5) : 1;
  const signals: GitHubSignal[] = [];

  for (let page = 1; page <= maxPages; page += 1) {
    const url = new URL(`https://api.github.com/repos/${repo.repo}/issues`);
    url.search = new URLSearchParams({
      state: "all",
      sort: "updated",
      direction: "desc",
      since: since.toISOString(),
      per_page: String(pageSize),
      page: String(page),
    }).toString();
    const items = await getJson<GitHubIssueResponse[]>(url, options);
    signals.push(...items.map((item) => toIssueSignal(item, repo.repo, groupId)));
    const oldest = items.at(-1);
    if (items.length < pageSize || !oldest || new Date(oldest.updated_at) < since) break;
  }

  for (let page = 1; page <= Math.min(maxPages, 3); page += 1) {
    const url = new URL(`https://api.github.com/repos/${repo.repo}/releases`);
    url.search = new URLSearchParams({ per_page: String(pageSize), page: String(page) }).toString();
    const releases = await getJson<GitHubReleaseResponse[]>(url, options);
    const recent = releases.filter((release) => {
      const timestamp = release.published_at ?? release.created_at;
      return timestamp !== undefined && new Date(timestamp) >= since;
    });
    signals.push(...recent.map((release) => toReleaseSignal(release, repo.repo, groupId)));
    const oldest = releases.at(-1);
    const oldestTimestamp = oldest?.published_at ?? oldest?.created_at;
    if (
      releases.length < pageSize ||
      oldestTimestamp === undefined ||
      new Date(oldestTimestamp) < since
    ) {
      break;
    }
  }

  return signals;
}

export async function collectGitHubSignals(
  groups: RepoGroup[],
  since: Date,
  options: GitHubCollectorOptions = {},
): Promise<GitHubSignal[]> {
  const logger = options.logger ?? console;
  const repositories = groups.flatMap((group) => group.repos.map((repo) => ({ group, repo })));
  const collected: GitHubSignal[] = [];
  const concurrency = 4;
  for (let offset = 0; offset < repositories.length; offset += concurrency) {
    const batch = repositories.slice(offset, offset + concurrency);
    const results = await Promise.all(
      batch.map(async ({ group, repo }) => {
        try {
          const signals = await fetchRecentGitHubItems(repo, group.id, since, options);
          logger.log(`[github] ${repo.repo}: ${signals.length} recent signals`);
          return signals;
        } catch (error) {
          const message = error instanceof Error ? error.message : String(error);
          logger.error(`[github] ${repo.repo}: ${message}`);
          return [];
        }
      }),
    );
    collected.push(...results.flat());
  }
  return collected;
}
