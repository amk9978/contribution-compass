from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any, Literal, Self, cast

SignalKind = Literal["issue", "pull_request", "release"]
SignalState = Literal["open", "closed"]
ChangeKind = Literal["new", "updated"]
EventKind = Literal["discovered", "changed"]
LeadTier = Literal["maintainer-invited", "triage-lead"]
UpcomingKind = Literal["prerelease", "milestone"]


def _without_none(value: Any) -> Any:
    if isinstance(value, dict):
        return {key: _without_none(item) for key, item in value.items() if item is not None}
    if isinstance(value, list):
        return [_without_none(item) for item in value]
    return value


@dataclass(frozen=True, slots=True)
class RepoConfig:
    id: str
    repo: str
    name: str
    paginated: bool = False


@dataclass(frozen=True, slots=True)
class RepoGroup:
    id: str
    name: str
    repos: tuple[RepoConfig, ...]
    description: str | None = None


@dataclass(frozen=True, slots=True)
class CompassConfig:
    repo_groups: tuple[RepoGroup, ...]
    lookback_hours: int = 24


@dataclass(frozen=True, slots=True)
class SignalMetrics:
    reactions: int = 0
    comments: int = 0
    score: int | None = None

    @classmethod
    def from_dict(cls, value: dict[str, Any] | None) -> Self:
        value = value or {}
        return cls(
            reactions=int(value.get("reactions", 0)),
            comments=int(value.get("comments", 0)),
            score=int(value["score"]) if value.get("score") is not None else None,
        )

    def to_dict(self) -> dict[str, Any]:
        return cast(dict[str, Any], _without_none(asdict(self)))


@dataclass(frozen=True, slots=True)
class Signal:
    id: str
    source: Literal["github"]
    kind: SignalKind
    title: str
    url: str
    group: str | None = None
    project: str | None = None
    text: str | None = None
    created_at: str | None = None
    updated_at: str | None = None
    timestamp: str | None = None
    metrics: SignalMetrics | None = None
    labels: tuple[str, ...] = ()
    author: str | None = None
    state: SignalState | None = None
    assignees: tuple[str, ...] = ()
    change: ChangeKind | None = None

    @classmethod
    def from_dict(cls, value: dict[str, Any]) -> Self:
        metrics = value.get("metrics")
        return cls(
            id=str(value["id"]),
            source="github",
            kind=value["kind"],
            title=str(value["title"]),
            url=str(value["url"]),
            group=value.get("group"),
            project=value.get("project"),
            text=value.get("text"),
            created_at=value.get("createdAt", value.get("created_at")),
            updated_at=value.get("updatedAt", value.get("updated_at")),
            timestamp=value.get("timestamp"),
            metrics=SignalMetrics.from_dict(metrics) if isinstance(metrics, dict) else None,
            labels=tuple(str(label) for label in value.get("labels", [])),
            author=value.get("author"),
            state=value.get("state"),
            assignees=tuple(str(name) for name in value.get("assignees", [])),
            change=value.get("change"),
        )

    def to_dict(self) -> dict[str, Any]:
        value: dict[str, Any] = {
            "id": self.id,
            "source": self.source,
            "group": self.group,
            "project": self.project,
            "kind": self.kind,
            "title": self.title,
            "text": self.text,
            "url": self.url,
            "createdAt": self.created_at,
            "updatedAt": self.updated_at,
            "timestamp": self.timestamp,
            "metrics": self.metrics.to_dict() if self.metrics else None,
            "labels": list(self.labels),
            "author": self.author,
            "state": self.state,
            "assignees": list(self.assignees),
            "change": self.change,
        }
        return cast(dict[str, Any], _without_none(value))

    def with_change(self, change: ChangeKind) -> Signal:
        value = self.to_dict()
        value["change"] = change
        return Signal.from_dict(value)


@dataclass(frozen=True, slots=True)
class ProjectContext:
    repository: str
    url: str
    description: str | None = None
    homepage: str | None = None
    language: str | None = None
    topics: tuple[str, ...] = ()
    license: str | None = None
    default_branch: str | None = None
    stars: int = 0
    forks: int = 0
    open_issues: int = 0
    archived: bool = False
    collected_at: str | None = None

    @classmethod
    def from_dict(cls, value: dict[str, Any]) -> Self:
        return cls(
            repository=str(value["repository"]),
            url=str(value["url"]),
            description=value.get("description"),
            homepage=value.get("homepage"),
            language=value.get("language"),
            topics=tuple(str(topic) for topic in value.get("topics", [])),
            license=value.get("license"),
            default_branch=value.get("defaultBranch", value.get("default_branch")),
            stars=int(value.get("stars", 0)),
            forks=int(value.get("forks", 0)),
            open_issues=int(value.get("openIssues", value.get("open_issues", 0))),
            archived=bool(value.get("archived", False)),
            collected_at=value.get("collectedAt", value.get("collected_at")),
        )

    def to_dict(self) -> dict[str, Any]:
        return cast(
            dict[str, Any],
            _without_none(
                {
                    "repository": self.repository,
                    "url": self.url,
                    "description": self.description,
                    "homepage": self.homepage,
                    "language": self.language,
                    "topics": list(self.topics),
                    "license": self.license,
                    "defaultBranch": self.default_branch,
                    "stars": self.stars,
                    "forks": self.forks,
                    "openIssues": self.open_issues,
                    "archived": self.archived,
                    "collectedAt": self.collected_at,
                },
            ),
        )


@dataclass(frozen=True, slots=True)
class ReleaseBulletin:
    repository: str
    tag: str
    title: str
    url: str
    published_at: str
    notes: str | None = None
    highlights: tuple[str, ...] = ()
    prerelease: bool = False

    @classmethod
    def from_dict(cls, value: dict[str, Any]) -> Self:
        return cls(
            repository=str(value["repository"]),
            tag=str(value["tag"]),
            title=str(value["title"]),
            url=str(value["url"]),
            published_at=str(value["publishedAt"]),
            notes=value.get("notes"),
            highlights=tuple(str(item) for item in value.get("highlights", [])),
            prerelease=bool(value.get("prerelease", False)),
        )

    def to_dict(self) -> dict[str, Any]:
        return cast(
            dict[str, Any],
            _without_none(
                {
                    "repository": self.repository,
                    "tag": self.tag,
                    "title": self.title,
                    "url": self.url,
                    "publishedAt": self.published_at,
                    "notes": self.notes,
                    "highlights": list(self.highlights),
                    "prerelease": self.prerelease,
                }
            ),
        )


@dataclass(frozen=True, slots=True)
class UpcomingItem:
    repository: str
    kind: UpcomingKind
    title: str
    url: str
    description: str | None = None
    due_at: str | None = None
    progress: int | None = None
    open_issues: int | None = None
    closed_issues: int | None = None
    tag: str | None = None
    published_at: str | None = None

    @classmethod
    def from_dict(cls, value: dict[str, Any]) -> Self:
        return cls(
            repository=str(value["repository"]),
            kind=value["kind"],
            title=str(value["title"]),
            url=str(value["url"]),
            description=value.get("description"),
            due_at=value.get("dueAt"),
            progress=int(value["progress"]) if value.get("progress") is not None else None,
            open_issues=(int(value["openIssues"]) if value.get("openIssues") is not None else None),
            closed_issues=(
                int(value["closedIssues"]) if value.get("closedIssues") is not None else None
            ),
            tag=value.get("tag"),
            published_at=value.get("publishedAt"),
        )

    def to_dict(self) -> dict[str, Any]:
        return cast(
            dict[str, Any],
            _without_none(
                {
                    "repository": self.repository,
                    "kind": self.kind,
                    "title": self.title,
                    "url": self.url,
                    "description": self.description,
                    "dueAt": self.due_at,
                    "progress": self.progress,
                    "openIssues": self.open_issues,
                    "closedIssues": self.closed_issues,
                    "tag": self.tag,
                    "publishedAt": self.published_at,
                }
            ),
        )


@dataclass(frozen=True, slots=True)
class ProjectNewsSnapshot:
    repository: str
    collected_at: str
    latest_release: ReleaseBulletin | None = None
    upcoming: tuple[UpcomingItem, ...] = ()

    @classmethod
    def from_dict(cls, value: dict[str, Any]) -> Self:
        latest = value.get("latestRelease")
        return cls(
            repository=str(value["repository"]),
            collected_at=str(value["collectedAt"]),
            latest_release=(
                ReleaseBulletin.from_dict(latest) if isinstance(latest, dict) else None
            ),
            upcoming=tuple(UpcomingItem.from_dict(item) for item in value.get("upcoming", [])),
        )

    def to_dict(self) -> dict[str, Any]:
        return cast(
            dict[str, Any],
            _without_none(
                {
                    "repository": self.repository,
                    "collectedAt": self.collected_at,
                    "latestRelease": (
                        self.latest_release.to_dict() if self.latest_release else None
                    ),
                    "upcoming": [item.to_dict() for item in self.upcoming],
                }
            ),
        )


@dataclass(frozen=True, slots=True)
class ObservationEvent:
    id: str
    signal_id: str
    event: EventKind
    observed_at: str
    changed_fields: tuple[str, ...]
    signal: Signal

    @classmethod
    def from_dict(cls, value: dict[str, Any]) -> Self:
        return cls(
            id=str(value["id"]),
            signal_id=str(value["signalId"]),
            event=value["event"],
            observed_at=str(value["observedAt"]),
            changed_fields=tuple(str(name) for name in value.get("changedFields", [])),
            signal=Signal.from_dict(value["signal"]),
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "signalId": self.signal_id,
            "event": self.event,
            "observedAt": self.observed_at,
            "changedFields": list(self.changed_fields),
            "signal": self.signal.to_dict(),
        }


@dataclass(frozen=True, slots=True)
class ContributionLead:
    signal: Signal
    tier: LeadTier
    score: int
    reasons: tuple[str, ...]
    caveat: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "tier": self.tier,
            "rankScore": self.score,
            "reasons": list(self.reasons),
            "caveat": self.caveat,
            "signal": self.signal.to_dict(),
            "evidenceUrl": self.signal.url,
        }


@dataclass(frozen=True, slots=True)
class CollectionBatch:
    signals: tuple[Signal, ...]
    contexts: tuple[ProjectContext, ...]
    failures: tuple[str, ...] = ()
    news: tuple[ProjectNewsSnapshot, ...] = ()


@dataclass(frozen=True, slots=True)
class ChangeSet:
    signals: tuple[Signal, ...]
    events: tuple[ObservationEvent, ...]


@dataclass(frozen=True, slots=True)
class CrawlRun:
    collected_at: str
    since: str
    observed_count: int
    changed_count: int

    def to_dict(self) -> dict[str, Any]:
        return {
            "collectedAt": self.collected_at,
            "since": self.since,
            "observedCount": self.observed_count,
            "changedCount": self.changed_count,
        }


@dataclass(slots=True)
class RepositoryDataset:
    date: str
    group_id: str
    group_name: str
    repository_id: str
    repository: str
    repository_name: str
    runs: list[CrawlRun] = field(default_factory=list)
    signals: list[Signal] = field(default_factory=list)
    events: list[ObservationEvent] = field(default_factory=list)
    context: ProjectContext | None = None
    news: ProjectNewsSnapshot | None = None

    @classmethod
    def from_dict(cls, value: dict[str, Any]) -> Self:
        return cls(
            date=str(value["date"]),
            group_id=str(value["group"]["id"]),
            group_name=str(value["group"]["name"]),
            repository_id=str(value["repository"]["id"]),
            repository=str(value["repository"]["repo"]),
            repository_name=str(value["repository"]["name"]),
            runs=[
                CrawlRun(
                    collected_at=str(run["collectedAt"]),
                    since=str(run["since"]),
                    observed_count=int(run["observedCount"]),
                    changed_count=int(run["changedCount"]),
                )
                for run in value.get("runs", [])
            ],
            signals=[Signal.from_dict(signal) for signal in value.get("signals", [])],
            events=[ObservationEvent.from_dict(event) for event in value.get("events", [])],
            context=(
                ProjectContext.from_dict(value["context"])
                if isinstance(value.get("context"), dict)
                else None
            ),
            news=(
                ProjectNewsSnapshot.from_dict(value["news"])
                if isinstance(value.get("news"), dict)
                else None
            ),
        )

    def to_dict(self) -> dict[str, Any]:
        return cast(
            dict[str, Any],
            _without_none(
                {
                    "version": 3,
                    "date": self.date,
                    "group": {"id": self.group_id, "name": self.group_name},
                    "repository": {
                        "id": self.repository_id,
                        "repo": self.repository,
                        "name": self.repository_name,
                    },
                    "context": self.context.to_dict() if self.context else None,
                    "news": self.news.to_dict() if self.news else None,
                    "runs": [run.to_dict() for run in self.runs],
                    "signals": [signal.to_dict() for signal in self.signals],
                    "events": [event.to_dict() for event in self.events],
                },
            ),
        )
