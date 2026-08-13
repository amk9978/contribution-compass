export type SignalSource = "github";

export type SignalKind = "issue" | "pull_request" | "release";

export interface SignalMetrics {
  reactions?: number;
  comments?: number;
  score?: number;
}

export interface Signal {
  id: string;
  source: SignalSource;
  group?: string;
  project?: string;
  kind: SignalKind;
  title: string;
  text?: string;
  url: string;
  createdAt?: string;
  updatedAt?: string;
  timestamp?: string;
  metrics?: SignalMetrics;
  labels?: string[];
  author?: string;
  state?: "open" | "closed";
  assignees?: string[];
  change?: "new" | "updated";
}
