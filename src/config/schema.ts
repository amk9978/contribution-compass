export interface RepoConfig {
  id: string;
  repo: string;
  name: string;
  paginated?: boolean;
}

export interface RepoGroup {
  id: string;
  name: string;
  description?: string;
  repos: RepoConfig[];
}

export interface RadarConfig {
  repoGroups: RepoGroup[];
  lookbackHours: number;
}

type UnknownRecord = Record<string, unknown>;

function isRecord(value: unknown): value is UnknownRecord {
  return typeof value === "object" && value !== null && !Array.isArray(value);
}

function fail(path: string, message: string): never {
  throw new Error(`Invalid config at ${path}: ${message}`);
}

function requiredString(record: UnknownRecord, key: string, path: string): string {
  const value = record[key];
  if (typeof value !== "string" || value.trim() === "") {
    return fail(`${path}.${key}`, "expected a non-empty string");
  }
  return value.trim();
}

function optionalBoolean(
  record: UnknownRecord,
  key: string,
  fallback: boolean,
  path: string,
): boolean {
  const value = record[key];
  if (value === undefined) return fallback;
  if (typeof value !== "boolean") return fail(`${path}.${key}`, "expected a boolean");
  return value;
}

function positiveInteger(
  record: UnknownRecord,
  key: string,
  fallback: number,
  path: string,
): number {
  const value = record[key];
  if (value === undefined) return fallback;
  if (!Number.isInteger(value) || (value as number) <= 0) {
    return fail(`${path}.${key}`, "expected a positive integer");
  }
  return value as number;
}

function parseRepo(value: unknown, path: string): RepoConfig {
  if (!isRecord(value)) return fail(path, "expected a repository object");
  const id = requiredString(value, "id", path);
  if (!/^[a-z0-9][a-z0-9._-]*$/i.test(id)) {
    return fail(`${path}.id`, "expected a filesystem-safe identifier");
  }
  const repo = requiredString(value, "repo", path);
  const name = requiredString(value, "name", path);
  if (!/^[^/\s]+\/[^/\s]+$/.test(repo)) {
    return fail(`${path}.repo`, "expected a GitHub owner/repository slug");
  }
  const paginated = optionalBoolean(value, "paginated", false, path);
  return paginated ? { id, repo, name, paginated } : { id, repo, name };
}

export function parseConfig(value: unknown): RadarConfig {
  if (!isRecord(value)) return fail("root", "expected a YAML object");
  const rawGroups = value["repo_groups"];
  if (!isRecord(rawGroups)) return fail("repo_groups", "expected an object of repository groups");

  const ids = new Set<string>();
  const repoGroups = Object.entries(rawGroups).map(([id, rawGroup]) => {
    const path = `repo_groups.${id}`;
    if (!/^[a-z0-9][a-z0-9._-]*$/i.test(id)) {
      return fail(path, "group id must be a filesystem-safe identifier");
    }
    if (!isRecord(rawGroup)) return fail(path, "expected a group object");
    const rawRepos = rawGroup["repos"];
    if (!Array.isArray(rawRepos)) return fail(`${path}.repos`, "expected an array");
    const repos = rawRepos.map((repo, index) => parseRepo(repo, `${path}.repos[${index}]`));
    for (const repo of repos) {
      if (ids.has(repo.id)) return fail(`${path}.repos`, `duplicate repository id "${repo.id}"`);
      ids.add(repo.id);
    }
    const name = requiredString(rawGroup, "name", path);
    const description = rawGroup["description"];
    if (description !== undefined && typeof description !== "string") {
      return fail(`${path}.description`, "expected a string");
    }
    return description === undefined
      ? { id, name, repos }
      : { id, name, description: description.trim(), repos };
  });

  return {
    repoGroups,
    lookbackHours: positiveInteger(value, "lookback_hours", 24, "root"),
  };
}
