import datetime

import pydantic


class TopicProject(pydantic.BaseModel):
    owner: str
    name: str
    url: str

    description: str | None = None
    language: str | None = None
    topics: list[str] = []

    stars: int = 0
    forks: int = 0

    created_at: datetime.datetime | None = None
    updated_at: datetime.datetime | None = None
    pushed_at: datetime.datetime | None = None

    archived: bool = False
    latest_release_at: datetime.datetime | None = None

    contributors_count: int | None = None
    open_pr_count: int | None = None

    has_external_prs: bool | None = None
    external_commit_ratio: float | None = None
    watchers_count: int | None = None

    default_branch: str | None = None

    license: str | None = None

    last_commit_at: datetime.datetime | None = None

    releases_count: int | None = None

    commits_last_90_days: int | None = None
    merged_prs_last_90_days: int | None = None
    external_merged_prs_last_90_days: int | None = None

    median_pr_merge_days: float | None = None

    open_issues_count: int | None = None

    contributor_concentration: float | None = None


class ProjectIssue(pydantic.BaseModel):
    project_name: str
    project_url: str

    title: str
    url: str
    description: str | None = None

    language: str | None = None
    topics: list[str] = []

    state: str
    labels: list[str] = []

    created_at: datetime.datetime | None = None
    updated_at: datetime.datetime | None = None

    participants_count: int | None = None
    comments_count: int = 0

    has_assignee: bool = False
    has_linked_pr: bool = False
    assignees_count: int = 0

    author_association: str | None = None
    linked_pr_count: int = 0

    reactions_count: int = 0

    is_locked: bool = False
    is_good_first_issue: bool = False
    is_help_wanted: bool = False
