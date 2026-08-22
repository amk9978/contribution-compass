# Contribution Compass — Product & Architecture Spec v2

**Status:** Directional specification for the next major rewrite
**Purpose:** Define the product thesis, discovery/evaluation model, recommendation semantics, architectural constraints, and validation plan for Contribution Compass.

## 1. Product Thesis

Contribution Compass helps a serious software engineer answer:

> **Which open-source projects are worth investing my limited engineering attention in, given my background, what I want to learn, what will strengthen my career, and where my work can actually matter?**

The product is not primarily an issue finder. It does not optimize for the easiest issue, `good first issue` count, or sending users across dozens of unrelated repositories.

The scarce resource is:

> **The developer's next several months of engineering attention.**

Contribution Compass is an **OSS investment recommender**, not an issue feed.

## 2. Core Product Inversion

Old:

```text
Configured repositories
→ collect activity
→ rank interesting-looking issues
→ recommend contribution leads
```

New:

```text
Developer
→ developer profile
→ semantic + ecosystem position
→ discover candidate repositories
→ evaluate projects as long-term investments
→ recommend a small portfolio
→ only then select a few concrete GitHub issues as calls to action
```

Fundamental rule:

> **Project first, issue second.**

A `good first issue`, documentation task, bug, RFC, test improvement, or small enhancement is considered only after its project is already judged worth investing in.

## 3. Product Promise

The best recommendation lies at the intersection of:

### Personal fit
- languages;
- topics;
- prior project history;
- dependencies repeatedly used;
- existing contribution experience;
- explicit interests;
- desired technical direction.

### Project investment value
- technical substance;
- ecosystem importance;
- momentum;
- external contributor absorption;
- community need;
- maintainer bandwidth;
- realistic contributor visibility;
- health sufficient to justify long-term attention.

### Opportunity value
- learning upside;
- career / resume signal;
- community impact;
- plausible concrete issue-level call to action;
- potential progression from small contribution to deeper ownership.

Product statement:

> **Find the open-source projects where your skills, growth, and community impact align.**

## 4. Design Principles

### 4.1 Few curated signals, used deeply

Avoid feature soup. A signal should exist only if it materially changes a recommendation decision.

Prefer a small number of signal families:

- personal fit;
- external-contributor absorption;
- project momentum / health;
- ecosystem / career upside;
- community need;
- learning surface;
- entry friction.

Optimize for:

```text
information gained per signal
recommendation quality per API call
usefulness per persisted byte
```

### 4.2 Taste is intentional

Contribution Compass should not pretend to be a neutral universal recommender.

Preferred layering:

```text
Evidence
→ objective measurements
→ versioned taste policy
→ personalized recommendation
```

Taste must be explicit, versioned, inspectable, regression-tested, and separate from factual evidence.

### 4.3 Taste should primarily be expressed as floors

The strongest product judgments should be non-negotiable conditions, not weights.

Examples:

```text
Do not recommend archived projects.
Do not recommend projects with no recent outsider contribution success.
Do not recommend projects where outsider PRs routinely disappear into a dead queue.
Do not recommend projects where evidence coverage is too weak to judge.
```

No amount of stars should compensate for a dead contribution climate.

Flow:

```text
hard floors
→ survivors
→ comparative evaluation
→ ranking
```

### 4.4 Zero infrastructure / near-zero cost

Preferred building blocks:

- GitHub REST / GraphQL;
- GitHub Search;
- GitHub Topics;
- GitHub Actions;
- GitHub Pages;
- GitHub Issues;
- local computation;
- static files;
- optional free public data sources through adapters.

Avoid unless clearly justified:

- database;
- hosted backend;
- queues;
- vector databases;
- required LLM inference;
- firehose ingestion;
- owned global dependency graph;
- large long-lived raw datasets.

GitHub remains the primary live source of truth.

## 5. Developer Profile

Possible evidence:

- GitHub username;
- owned repositories;
- repositories contributed to;
- starred repositories;
- languages;
- repository topics;
- repeated dependencies;
- organizations / ecosystems;
- explicit topic preferences;
- explicit language preferences;
- explicit seed repositories;
- previous recommendation outcomes.

Each inferred preference should preserve provenance.

Example:

```yaml
distributed-systems:
  affinity: 0.87
  evidence:
    - contributed: some/repo
    - owns: another/repo
    - explicit: true
```

Explicit preferences should be able to steer or override inference.

## 6. Topics as the Semantic Coordinate System

GitHub Topics remain a first-class concept.

They are not merely metadata attached to already-selected repositories. They provide the main semantic coordinate system for:

- developer interests;
- project neighborhoods;
- topic similarity;
- topic distance;
- exploration;
- explanation.

But Topics are **not the only recall source**.

```text
semantic model ≠ candidate source
```

Topics define much of the semantic map while candidates may enter through several mechanisms.

## 7. Discovery Sources

### 7.1 Topic intersections

Prefer topic pairs/intersections where useful.

Example:

```text
topic:rust
+
topic:distributed-systems
```

Eight strong profile topics produce only 28 pairs, making this cheap enough to use aggressively.

Single-topic searches remain useful for breadth.

### 7.2 Dependency relationships

Use:

- manifests in the developer's repositories;
- dependencies of candidate projects;
- projects depending on important subject packages.

These relationships reveal the user's actual technical neighborhood.

### 7.3 Curated priors

Supplementary recall sources may include:

- GitHub Explore / Collections;
- `awesome-*` repositories;
- explicit seeds;
- known high-quality ecosystems.

These are priors, not final recommendations.

### 7.4 Trending / momentum sources

Trending or recent-growth sources can feed exploration, but every candidate still passes normal evaluation.

## 8. Topic Graph

No complete global ontology is required.

Relevant topic structure can be derived lazily from co-occurrence:

```text
ai-agents
↔ mcp
↔ agent-runtime
↔ code-execution
↔ sandboxing
```

Useful computations:

- topic co-occurrence;
- IDF weighting;
- hub suppression;
- synonym aliases;
- conditional asymmetry;
- hop distance.

Hub topics such as `python`, `api`, `cli`, and `docker` should carry less discriminative weight than rare topics such as `raft`, `consensus`, or `sandboxing`.

## 9. Personal Fit

Use IDF-weighted topic vectors and cosine similarity as a simple explainable fit model.

Additional evidence may include:

- language match;
- repeated dependency overlap;
- previous ecosystem experience;
- explicit interests;
- topic distance.

Fit explanations should cite the actual matching evidence.

## 10. Exploration + Exploitation

### Exploitation
- known topics;
- previous contributions;
- repeated dependencies;
- explicit seeds;
- successful prior recommendations.

### Exploration
- adjacent topic neighborhoods;
- dependency layers above or below;
- emerging ecosystems;
- unusual but relevant topic combinations;
- controlled semantic distance.

Initially use a **deterministic exploration quota**, not a probabilistic bandit.

Example:

```text
10 recommendations total
3 exploration slots
7 exploitation slots
```

Later, if meaningful feedback exists, adaptive exploration may operate at the topic-neighborhood level.

## 11. Candidate Slices

Do not sort every topic by stars.

Sample multiple useful slices:

- established high-star projects;
- medium-star projects;
- recent growth;
- recently created but healthy projects;
- active external contributor communities;
- strong project momentum;
- language-specific subsets;
- adjacent-topic subsets.

The interesting OSS investment often lives between celebrity and obscurity.

## 12. Health / Taste Floors

Initial floors may include:

- not archived;
- not deprecated;
- meaningful recent activity;
- recent release/tag or equivalent release activity;
- recent outsider PR merge;
- outsider review latency below a ceiling;
- enough measured evidence to judge.

Missing evidence means `unknown`, not `average`.

Do not impute weakly observed repositories into the middle of the ranking.

## 13. Three Core Evaluation Axes

After floors, collapse evaluation into exactly three axes.

### Fit
How appropriate is this project for this developer?

Possible inputs:
- IDF-weighted topic similarity;
- language overlap;
- dependency proximity;
- prior ecosystem experience;
- explicit interests;
- profile distance.

### Absorption
How well does this project absorb serious outside contributors?

Possible inputs:
- outsider PR merge rate;
- recent first-time-contributor merge;
- outsider close-without-merge rate;
- first-review latency;
- p90 review latency;
- PR queue depth;
- distinct active reviewers;
- newcomer readiness;
- external-contributor share.

### Upside
How worthwhile is the investment if the contributor succeeds?

Possible inputs:
- topic-relative stars / forks;
- ecosystem importance;
- momentum;
- technical depth;
- governance quality;
- contributor visibility;
- community demand;
- contributor concentration;
- expected learning surface.

## 14. Statistical Treatment

### 14.1 Percentiles within peer groups

Heavy-tailed metrics such as stars and forks should be interpreted within relevant topic pools.

Prefer:

```text
87th percentile among distributed-systems peers
```

over:

```text
4,000 stars
```

For heavy-tailed counts:

```text
winsorize
→ log-transform
→ empirical CDF
```

Health floors happen before percentile calculation.

### 14.2 Confidence-adjusted rates

Do not rank `3/3` outsider PR merges above `57/80` merely because `100% > 71%`.

For proportions, rank by a lower confidence bound such as Wilson.

For latency:
- use medians;
- report p50 and p90;
- require a minimum sample size;
- treat low-N as unknown.


### 14.3 Deterministic taste calibration and signal balancing

Contribution Compass does **not** train a recommendation model.

There is initially no reliable training dataset, and the product should not pretend that its trade-offs were learned objectively.

Instead, recommendation behavior is a deterministic combination of:

```text
measured facts
    ↓
peer-relative normalization
    ↓
hard taste floors
    ↓
hand-authored signal importance / weights
    ↓
Fit / Absorption / Upside
    ↓
Pareto filtering + balanced ordering
```

The weights and thresholds are **product taste**.

They should be:

- authored deliberately;
- versioned;
- visible in policy;
- regression-tested against the golden fixture set;
- changed only when the resulting recommendations are judged better.

Example raw signals may include:

```text
stars
forks
active contributor count
contributor concentration
recent growth
release activity
outsider merge rate
review latency
first-time-contributor success
topic fit
dependency proximity
```

Raw values should not be combined directly because they live on incompatible scales.

First convert them into comparable measurements, usually in `[0, 1]`, using the statistical treatment in §14.1–14.2.

For example:

```text
stars = 87th percentile among topic peers
forks = 79th percentile among topic peers
active contributors = 64th percentile
contributor distribution = 82nd percentile
```

Then the taste policy determines how much those signals matter.

A possible axis-level combination is a **weighted geometric mean** rather than a weighted arithmetic sum:

```text
axis_score =
    Π(signal_i ^ weight_i) ^ (1 / Σ weights)
```

This lets the policy express that, for example, contributor absorption matters more than raw popularity while still penalizing a project that collapses on one important signal.

The exact formula is less important than these invariants:

1. **No learned weights are implied.** The weights are curator taste.
2. **Hard floors apply before balancing.** A catastrophic weakness cannot be bought off by stars.
3. **Signals are normalized relative to appropriate peers.**
4. **Contributor count is never interpreted alone.** It must be paired with concentration/distribution evidence.
5. **The final recommendation remains explainable in terms of the underlying measurements.**
6. **Policy changes are tested against known-good and known-bad recommendation fixtures.**

The product should therefore be able to say:

```text
Why this project ranked highly:
- stars: 88th percentile in its topic
- forks: 81st percentile
- healthy contributor distribution
- outsider merge rate above peers
- review latency well below peers

Taste policy:
- accessibility weighted more heavily than raw popularity
- projects failing the review-latency floor are excluded entirely
```

This is the intended substitute for a trained recommender: **deterministic multi-criteria selection whose weights and thresholds encode explicit product taste.**

## 15. Harmony and Pareto Filtering

The system should reward balanced strength.

Use a three-dimensional skyline / Pareto filter over:

```text
Fit
Absorption
Upside
```

Do not extend the skyline to many raw dimensions.

## 16. Ordering Within the Frontier

A geometric mean is an acceptable default:

```text
(Fit × Absorption × Upside)^(1/3)
```

because a near-zero axis strongly penalizes the result.

Avoid a simple weighted arithmetic sum as the primary model.

## 17. Recommendation Buckets

Recommendations must be **disjoint**. One repository appears in one bucket only.

### 17.1 Career Signal

This should mean:

> **Prestigious projects with unexpectedly credible outsider absorption.**

Not merely “famous repositories are prestigious.”

Characteristics:
- strong ecosystem / resume signal;
- recognized technical value;
- high topic-relative prominence;
- harder contribution surface;
- demonstrated outsider path.

If this bucket cannot reliably produce **accessible prestige**, it should eventually fold into Best Investment.

### 17.2 Best Investment

The primary category.

Projects with unusually good expected value relative to effort.

Strong balance of:
- fit;
- absorption;
- learning;
- momentum;
- community need;
- technical quality;
- visibility;
- career value.

### 17.3 Fresh Breeze

Projects deliberately somewhat distant from the current profile.

Examples:

```text
distributed systems → storage engines
backend → runtimes
AI infrastructure → inference engines
observability → eBPF / networking
agent systems → sandboxing / security
```

This category exists to prevent technical filter bubbles.

## 18. Bucket Assignment

Bucket semantics:

```text
Career Signal:
prestige relative to accessibility

Best Investment:
expected value relative to effort

Fresh Breeze:
useful distance from current profile
```

Apply quotas and enforce:

```text
one repository → one bucket
```

## 19. Portfolio Diversity

After ranking, enforce diversity.

A lightweight MMR-style pass can use similarity based on:

- topic Jaccard;
- shared dependencies;
- same owning organization;
- same technical niche.

The final portfolio should represent meaningfully different investment options.

## 20. Dependency-Chain Discovery

Contribution Compass should understand approximate technical layers.

Example:

```text
Application
↓
Framework
↓
Runtime / SDK
↓
Protocol / middleware
↓
Infrastructure
↓
OS / networking
```

The product should surface:

```text
↑ one layer above
● current neighborhood
↓ one layer below
```

## 21. Lazy Dependency Queries

Do not build a global dependency graph.

### Downward: what does this project depend on?

Read manifests such as:
- `pyproject.toml`;
- `requirements*.txt`;
- `package.json`;
- `go.mod`;
- `Cargo.toml`.

Resolve important package identities to repositories.

### Upward: who depends on this project?

Query dependency information lazily through:
- GitHub manifest/code search;
- package/dependency indexes;
- optional external dependency adapters.

Important distinctions:
- runtime vs dev dependency;
- direct vs transitive;
- manifest vs lockfile;
- package identity vs repository identity;
- real active project vs tutorial/toy repository.

## 22. High-Value Contribution-Climate Signals

Priority signals:

### Recent first-time-contributor merge
Direct evidence that genuinely new contributors can still land work.

### PR queue depth
Approximate:

```text
open PRs / merged PRs per month
```

### Outsider close-without-merge rate
Measure rejection separately from acceptance speed.

### Review latency
Use p50 and p90.

### Maintainer response breadth
How many distinct humans actively review outsider work?

### Newcomer readiness
Cheap repository checks such as:
- `CONTRIBUTING.md`;
- `ARCHITECTURE.md`;
- `.devcontainer/`;
- `Makefile`;
- `docker-compose.yml`.

### Stale good-first-issue detection
Old abandoned beginner tickets are a negative signal.

### Governance
Well-documented or foundation-backed governance can signal structural openness.

### CLA / DCO friction
Surface process/legal friction early.

### Bot filtering
Dependabot, Renovate, release bots, etc. must be filtered before aggregate measurements.

## 23. Contributor Concentration

Raw contributor count is insufficient.

Combine:

```text
active contributor count
+
distribution / concentration
```

The ideal target is often:

> **A healthy project with enough contributor distribution to be open, but not so crowded that meaningful individual visibility disappears.**

## 24. Concrete Issue Recommendations

Project recommendation alone is not sufficient.

For every recommended project, Contribution Compass should surface a **small number of concrete GitHub issues** that give the user an immediate call to action.

Target:

```text
recommended project
    ↓
2–4 concrete GitHub issues
    ↓
user can investigate or start contributing
```

These issues are selected **after** the project has already passed project-level evaluation.

The direction must never invert back to:

```text
interesting issue
    ↓
therefore recommend its repository
```

The correct order remains:

```text
project worth investing in
    ↓
inspect that project's open issues
    ↓
select the best concrete issues for this developer
```

### 24.1 Issue selection criteria

A surfaced issue should have evidence for as many of the following as possible:

- still open;
- currently unassigned or otherwise plausibly available;
- no active linked PR already solving it;
- recent enough that it is likely still relevant;
- explicit maintainer/community demand where available;
- scope understandable from the issue and linked context;
- technically meaningful rather than pure busywork;
- appropriate for the user's background;
- useful learning value;
- connection to an important subsystem or project direction;
- reasonable expected review path.

`good first issue` and `help wanted` labels are evidence, but neither is sufficient by itself.

A stale two-year-old `good first issue` with no maintainer activity should generally rank below a recent unlabelled issue with clear maintainer demand.

### 24.2 Issue mix

Avoid returning several nearly identical trivial tasks.

For each recommended project, aim for a small mix such as:

```text
Issue A — lower-friction concrete contribution
Issue B — more technically meaningful contribution
Issue C — deeper / higher-upside task
```

The exact number and mix should remain small enough to preserve high conviction.

### 24.3 Issue-level output

Each surfaced issue should explain why it was selected.

Example:

```text
#1842 — Fix replication behavior during membership change

Why this issue:
- open and unassigned
- maintainer requested help 8 days ago
- no linked open PR
- touches the replication subsystem
- similar outsider PRs were reviewed within 4 days
- strong match with your distributed-systems background

Suggested action: INVESTIGATE
```

Possible action states:

```text
START
INVESTIGATE
ASK_MAINTAINER
AVOID
```

The system should be conservative about `START`; if scope or ownership is ambiguous, `ASK_MAINTAINER` or `INVESTIGATE` is more honest.

### 24.4 Issue recommendation is a separate evaluation problem

Project-level evaluation asks:

```text
Is this repository worth months of attention?
```

Issue-level evaluation asks:

```text
Which concrete open issues inside this already-good project are worth acting on now?
```

These should have separate policies and measurements.

## 25. Evidence vs Judgment

Keep a strict seam:

```text
raw/public evidence
→ normalized factual features
→ versioned derived measurements
------------------------------
taste / recommendation policy
→ personalized recommendation
```

A measurement envelope should include:

```json
{
  "metric": "external_pr_first_review_latency",
  "value": 4.2,
  "unit": "days",
  "window_days": 90,
  "n": 43,
  "coverage": 0.705,
  "source": "github",
  "as_of": "..."
}
```

Live GitHub evidence wins when a live check is available.

## 26. Persistence Philosophy

Rule:

> **Do not persist something merely because GitHub returned it.**

Persist only what supports:
- synchronization;
- reproducibility;
- explanation;
- evaluation of past recommendations;
- user feedback.

Avoid:
- full issue bodies;
- repeated raw snapshots;
- giant daily repository dumps;
- full Signals inside events;
- redundant source data GitHub already owns.

## 27. Recommendation History

Persist the actual recommendations made.

Example:

```text
recommendations/
  2026-08-21.json
```

Store:
- bucket;
- measurements as-of that date;
- policy version;
- explanation;
- discovery provenance;
- user profile fingerprint.

This allows the product to later ask:

> **Were our INVEST calls actually good?**

## 28. Taste Regression Fixtures

Maintain a curated fixture set:

```text
developer
repository
expected verdict
expected bucket
important explanation
```

Initial target:
- ~20 known-good repositories;
- ~10 known-bad or misleading repositories;
- several ambiguous cases.

A policy change should fail tests if it unexpectedly flips important judgments.

## 29. GitHub Issues as Sparse Working Memory

Use GitHub Issues selectively.

Do not mirror every upstream issue.

Possible mapping:

```text
one materialized recommendation / serious opportunity
→ one Compass mirror issue
```

Issue body:
- upstream URL;
- bucket;
- why it surfaced;
- measurements;
- discovery provenance;
- suggested issue-level action;
- current status.

Labels:

```text
bucket:career-signal
bucket:best-investment
bucket:fresh-breeze

topic:...
lang:...

cc:saved
cc:investigating
cc:contributing
cc:landed
cc:not-for-me
```

## 30. Primary Product Surface

The long-term primary product surface should be **local/personalized execution**, not a generic shared static catalog.

Likely invocation:

```bash
uvx contribution-compass --github <username>
```

The static website becomes:
- public dogfooding;
- documentation;
- proof;
- shareable output.

## 31. CLI Direction

Possible commands:

```bash
contribution-compass init --github <username>
contribution-compass profile
contribution-compass discover
contribution-compass discover --topic ai-agents
contribution-compass recommend
contribution-compass explain owner/repo
contribution-compass neighbors owner/repo
contribution-compass enter owner/repo
contribution-compass mirror
```

Mental model:

```text
profile
→ discover
→ evaluate
→ recommend
→ enter
```

## 32. MCP Direction

Possible tools:

```text
find_projects_for_me
explore_topic
explain_project_fit
show_ecosystem_neighbors
find_recommended_issues
compare_recommendations
```

MCP should expose user questions, not catalog/database primitives.

## 33. Static Site Direction

Possible homepage:

```text
YOUR OSS COMPASS

Best Investments
────────────────
1. ...
2. ...
3. ...

Career Signal
─────────────
1. ...
2. ...

Fresh Breeze
────────────
1. ...
2. ...

Your Topic Map
──────────────
...

Ecosystem Neighbors
───────────────────
↑ one layer above
↓ one layer below
```

Each project page should answer:
- Why does this fit me?
- Why does this project matter?
- What would I learn?
- How strong is the career signal?
- How well are outsiders absorbed?
- What does contribution friction look like?
- How crowded is the contributor surface?
- Which 2–4 concrete open GitHub issues should I investigate first?
- What evidence supports the recommendation?

Prefer comparative facts over unexplained point totals.

## 34. Candidate Funnel

Stage expensive work:

```text
large candidate universe
→ cheap topic/profile/dependency filtering
→ plausible candidate pool
→ hard floors
→ deep evaluation of survivors
→ Pareto shortlist
→ 5–10 recommendations
```

Most explored candidates should be discarded and not persisted.

## 35. Validation Before Large Rewrite

### 35.1 20-repository recall set
Write down ~20 repositories already believed to be excellent contribution targets.

Test:
- Did discovery find them?
- Did evaluation keep them?
- Did the right projects survive the floors?

### 35.2 Evaluation experiment
Use a known candidate universe and ask:

> **Can Compass distinguish the projects actually worth investing in?**

### 35.3 Discovery experiment
Once evaluation works:

> **Can Compass discover a genuinely worthwhile project the user did not already know about?**

### 35.4 N=1 end-to-end test

```text
Compass recommends an unfamiliar project
→ developer investigates it
→ developer starts contributing
→ PR lands
```

### 35.5 Five-developer hand test
Run manual/semi-manual recommendations for ~5 developers.

Ask:

> Did this surface something you had not considered and would seriously investigate?

## 36. MVP Strategy

### Experiment 0 — evaluation MVP

```text
developer manifests
+
starred repos
+
manual seeds
→ ~100–200 candidates
→ deep contribution-climate evaluation
→ hard floors
→ 5 recommendations
```

Goal:

> **Can the evaluation model produce high-quality picks?**

### Product MVP — discovery + evaluation

```text
developer profile
→ topic intersections
+ dependency neighbors
+ curated priors
→ candidate universe
→ floors
→ Fit / Absorption / Upside
→ Pareto shortlist
→ disjoint buckets
→ portfolio diversity
→ 2–4 concrete recommended issues per selected project
```

Goal:

> **Can Compass find something excellent the developer would not have found alone?**

## 37. What the Current Prototype Keeps

Keep:
- Python;
- domain/application/adapter separation;
- ports;
- GitHub integration patterns;
- GitHub Actions;
- GitHub Pages;
- Jinja templates;
- static generation;
- MCP transport;
- manifest parsing;
- package → repository resolution;
- evidence / inference separation;
- lightweight dependency footprint.

## 38. What the Current Prototype Replaces

Replace or remove:
- fixed `repo_groups` as the universe;
- `ProjectSensor` as the core entity;
- `ContributionLead` as the main product object;
- `TriageLead`;
- current issue scoring;
- current `importance_score()`;
- large `RepositoryDataset`;
- full Signal snapshot persistence;
- Observation Events containing full Signals;
- giant `.state/github.json`;
- exhaustive daily repository datasets;
- catalog overlays built around fixed configured repos;
- current browser-only My Compass filtering;
- catalog-shaped CLI;
- catalog-shaped MCP tools.

Delete Hacker News from the core product. RSS and non-GitHub forge expansion are deferred.

## 39. Suggested New Domain

```text
domain/
    profile.py
    topics.py
    candidates.py
    evidence.py
    measurements.py
    evaluation.py
    recommendations.py
    issues.py
    dependencies.py
```

Core concepts:

```text
DeveloperProfile
TopicAffinity
TopicRelation
CandidateRepository
DiscoveryEvidence
ProjectEvidence
Measurement
ProjectEvaluation
Recommendation
RecommendationBucket
RecommendedIssue
DependencyRelation
```

## 40. Suggested New Application Flow

```text
BuildDeveloperProfile
→ DiscoverCandidates
→ CheapCandidateFilter
→ CollectProjectEvidence
→ ApplyTasteFloors
→ EvaluateProjects
→ BuildParetoFrontier
→ AssignRecommendationBuckets
→ DiversifyPortfolio
→ SelectRecommendedIssues
→ PersistRecommendationSnapshot
→ OptionalMirror
```

## 41. North Star Metric

Do not optimize for:
- repos indexed;
- issues collected;
- signals emitted;
- page views;
- recommendations generated.

Meaningful funnel:

```text
recommendation viewed
→ repository investigated
→ contribution started
→ PR submitted
→ PR merged
```

North Star:

> **How often does Contribution Compass help someone land a worthwhile OSS contribution?**

Secondary outcomes:
- meaningful learning;
- repeat contributions;
- maintainer relationships;
- sustained participation;
- career/interview value.

## 42. Promotion Philosophy

Promotion stays lightweight while the engine is weak.

Useful early promotion:
- public dogfooding;
- interesting discoveries;
- transparent methodology;
- case studies;
- examples of unexpected but defensible recommendations.

Best proof:

```text
Compass recommendation
→ developer invests
→ meaningful PR
→ merged
```

Long term, community traction and measurable successful contributions may make GitHub itself a reasonable amplification partner.

## 43. Non-Goals

Contribution Compass should not become:
- a universal repository search engine;
- a generic GitHub recommender;
- a `good first issue` aggregator;
- an OSS activity dashboard;
- a news monitor;
- a giant data warehouse;
- a required hosted SaaS;
- an ML recommender without meaningful training data;
- a leaderboard of famous repositories.

## 44. Open Questions for Review

The following are intentionally **not yet design decisions**.

### 44.1 What, if anything, should complement concrete issue recommendations?

The committed call-to-action mechanism is:

> **For each recommended project, surface a few concrete GitHub issues.**

The broader phrase **entry point** is intentionally left open for review.

Please evaluate whether Contribution Compass should eventually surface any additional forms of actionable entry point **alongside issues**, and if so, which ones are genuinely useful for a serious contributor.

Questions:

- Are GitHub issues sufficient as the main call to action?
- What useful contribution opportunities are commonly not represented by issues?
- Should the product ever surface specific subsystems, RFCs, roadmap items, discussion threads, missing integrations, maintainer requests, or other objects?
- How can a non-issue entry point remain concrete enough to be actionable rather than becoming vague advice?
- Should any non-issue entry point be part of the MVP, or only introduced after issue recommendations work well?
- What evidence would be required before surfacing a non-issue entry point confidently?

Do not assume that every suggested category belongs in the product. The goal is to discover whether there is a **small number of additional actionable primitives** that materially improve on concrete issue recommendations.

### 44.2 Does Career Signal survive as a separate bucket?

Career Signal currently means **prestige with unexpectedly credible outsider accessibility**.

If this category repeatedly overlaps with Best Investment or produces obvious celebrity repositories, it should be folded into Best Investment rather than retained for taxonomy's sake.

### 44.3 What is the minimum viable issue-selection model?

Please critique §24 specifically.

What is the smallest factual set required to select 2–4 concrete issues reliably without recreating the old `good first issue` scoring system?

---

## 45. Final Product Principle

Contribution Compass should not try to out-GitHub GitHub.

GitHub already contains the ecosystem.

Contribution Compass should:

```text
understand the developer
→ map their semantic and technical neighborhood
→ explore OSS intelligently
→ apply explicit product taste
→ identify a few projects worth serious investment
→ show how to enter them successfully
```

The product should feel less like:

> **"Here are 200 contribution opportunities."**

and more like:

> **"These are the few open-source projects where your next six months of effort are most likely to teach you something, matter to the community, and strengthen your engineering career — and here is the evidence."**
