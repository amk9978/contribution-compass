import datetime
from uuid import UUID

from compass.domain import (
    Bucket,
    Evaluation,
    Recommendation,
    RecommendationGroup,
    TopicProject,
)

AS_OF = datetime.datetime(2026, 9, 5, tzinfo=datetime.UTC)
POLICY_VERSION = "taste-policy-0.1.0"

DJANGO = TopicProject(
    owner="django",
    name="django",
    url="https://github.com/django/django",
    description="The Web framework for perfectionists with deadlines.",
    language="Python",
    topics=["python", "web", "framework", "orm"],
    stars=84200,
    forks=32400,
    pushed_at=datetime.datetime(2026, 9, 4, tzinfo=datetime.UTC),
    archived=False,
    license="BSD-3-Clause",
    external_merged_prs_last_90_days=184,
    merged_prs_last_90_days=311,
    median_pr_merge_days=12.0,
    commits_last_90_days=402,
    contributor_concentration=0.08,
)

HTTPX = TopicProject(
    owner="encode",
    name="httpx",
    url="https://github.com/encode/httpx",
    description="A next generation HTTP client for Python.",
    language="Python",
    topics=["python", "http", "asyncio", "web"],
    stars=14600,
    forks=980,
    pushed_at=datetime.datetime(2026, 8, 30, tzinfo=datetime.UTC),
    archived=False,
    license="BSD-3-Clause",
    external_merged_prs_last_90_days=27,
    merged_prs_last_90_days=41,
    median_pr_merge_days=21.0,
    commits_last_90_days=63,
    contributor_concentration=0.34,
)

DUCKDB = TopicProject(
    owner="duckdb",
    name="duckdb",
    url="https://github.com/duckdb/duckdb",
    description="An in-process SQL OLAP database management system.",
    language="C++",
    topics=["database", "olap", "analytics", "sql"],
    stars=26800,
    forks=2140,
    pushed_at=datetime.datetime(2026, 9, 5, tzinfo=datetime.UTC),
    archived=False,
    license="MIT",
    external_merged_prs_last_90_days=96,
    merged_prs_last_90_days=290,
    median_pr_merge_days=6.0,
    commits_last_90_days=871,
    contributor_concentration=0.19,
)

SAMPLE_GROUP = RecommendationGroup(
    id=UUID("11111111-1111-1111-1111-111111111111"),
    as_of=AS_OF,
    recommendations=[
        Recommendation(
            id=UUID("22222222-2222-2222-2222-222222222222"),
            project=DJANGO,
            bucket=Bucket.CAREER_SIGNAL,
            evaluation=Evaluation(fit=0.81, absorption=0.74, upside=0.35),
            explanation=(
                "Merged 184 outside pull requests in 90 days at a median of "
                "12 days, and no contributor holds more than 8 percent of "
                "commits."
            ),
            policy_version=POLICY_VERSION,
            as_of=AS_OF,
        ),
        Recommendation(
            id=UUID("33333333-3333-3333-3333-333333333333"),
            project=HTTPX,
            bucket=Bucket.ALIGNED,
            evaluation=Evaluation(fit=0.93, absorption=0.52, upside=0.44),
            explanation=(
                "Merged 27 outside pull requests in 90 days, though one "
                "contributor holds 34 percent of commits and the median merge "
                "takes 21 days."
            ),
            policy_version=POLICY_VERSION,
            as_of=AS_OF,
        ),
        Recommendation(
            id=UUID("44444444-4444-4444-4444-444444444444"),
            project=DUCKDB,
            bucket=Bucket.FRESH_BREEZE,
            evaluation=Evaluation(fit=0.22, absorption=0.68, upside=0.79),
            explanation=(
                "Merged 96 outside pull requests in 90 days at a median of "
                "6 days, in an analytics ecosystem your profile has not "
                "touched."
            ),
            policy_version=POLICY_VERSION,
            as_of=AS_OF,
        ),
    ],
)
