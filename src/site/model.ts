import type { Signal } from "../signals/types.js";
import type { CrawlRun } from "../storage/dataset.js";

export interface SiteRepository {
  id: string;
  repo: string;
  name: string;
  runs: CrawlRun[];
  signals: Signal[];
}

export interface SiteGroup {
  id: string;
  name: string;
  repositories: SiteRepository[];
}

export interface SiteDate {
  date: string;
  collectedAt: string;
  groups: SiteGroup[];
}

export interface SiteModel {
  generatedAt: string;
  dates: SiteDate[];
}

export interface SiteOptions {
  dataRoot?: string;
  outputRoot?: string;
  siteUrl?: string;
  repositoryUrl?: string;
}

export interface SiteContext {
  siteUrl: string;
  repositoryUrl: string;
}
