import { rankContributionLeads, type ContributionLead } from "../contributions/classify.js";
import type { SiteModel } from "./model.js";

export interface LocatedContributionLead extends ContributionLead {
  date: string;
  groupId: string;
  groupName: string;
  repositoryId: string;
  repositoryName: string;
  repository: string;
}

export function latestContributionLeads(model: SiteModel, limit = 100): LocatedContributionLead[] {
  const latest = model.dates[0];
  if (!latest) return [];

  const located = latest.groups.flatMap((group) =>
    group.repositories.flatMap((repository) =>
      rankContributionLeads(repository.signals, Number.POSITIVE_INFINITY).map((lead) => ({
        ...lead,
        date: latest.date,
        groupId: group.id,
        groupName: group.name,
        repositoryId: repository.id,
        repositoryName: repository.name,
        repository: repository.repo,
      })),
    ),
  );
  return located
    .sort(
      (left, right) => right.score - left.score || left.signal.id.localeCompare(right.signal.id),
    )
    .slice(0, limit);
}
