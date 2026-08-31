import datetime
import os
from collections import defaultdict
from urllib.parse import quote

import httpx
from dotenv import load_dotenv
from selectolax.parser import HTMLParser

from compass.domain import TopicProject

load_dotenv()

GITHUB_API = "https://api.github.com"
GITHUB_WEB = "https://github.com"

CUTOFF_DATE = 3 * 365

token = os.environ["GITHUB_TOKEN"]

headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {token}",
    "X-GitHub-Api-Version": "2022-11-28",
}


def get_topics_frequencies(github_handle: str) -> list[tuple[str, int]]:
    frequencies: defaultdict[str, int] = defaultdict(int)

    now = datetime.datetime.now(datetime.timezone.utc)
    cutoff = now - datetime.timedelta(days=CUTOFF_DATE)

    with httpx.Client(
            base_url=GITHUB_API,
            headers=headers,
            timeout=30,
    ) as client:
        page = 1

        while True:
            response = client.get(
                f"/users/{github_handle}/repos",
                params={
                    "per_page": 100,
                    "page": page,
                    "sort": "updated",
                    "direction": "desc",
                },
            )
            response.raise_for_status()

            repos = response.json()

            if not repos:
                break

            reached_cutoff = False

            for repo in repos:
                updated_at = repo.get("updated_at")

                if not updated_at:
                    continue

                updated_at = datetime.datetime.fromisoformat(
                    updated_at.replace("Z", "+00:00")
                )

                if updated_at < cutoff:
                    reached_cutoff = True
                    break

                for topic in repo.get("topics", []):
                    frequencies[topic] += 1

            if reached_cutoff or len(repos) < 100:
                break

            page += 1

    return sorted(
        frequencies.items(),
        key=lambda item: item[1],
        reverse=True,
    )


def get_repo_stats(
        client: httpx.Client,
        owner: str,
        name: str,
) -> tuple[int, int]:
    response = client.get(f"/repos/{owner}/{name}")
    response.raise_for_status()

    data = response.json()

    return (
        data["stargazers_count"],
        data["forks_count"],
    )


def parse_topic_page(
        tree: HTMLParser,
        api_client: httpx.Client,
        seen: set[str],
) -> list[TopicProject]:
    projects: list[TopicProject] = []

    for article in tree.css("article"):
        heading = article.css_first("h3")

        if heading is None:
            continue

        repo_links = heading.css("a")

        if len(repo_links) < 2:
            continue

        owner_link = repo_links[0]
        repo_link = repo_links[-1]

        owner = owner_link.text(strip=True)
        name = repo_link.text(strip=True)

        href = repo_link.attributes.get("href")

        if not href:
            continue

        repo_url = f"{GITHUB_WEB}{href}"

        # GitHub can occasionally return duplicate projects across pages.
        if repo_url in seen:
            continue

        seen.add(repo_url)

        description_node = article.css_first("p.color-fg-muted")
        description = (
            description_node.text(strip=True)
            if description_node
            else None
        )

        topics = [
            node.text(strip=True)
            for node in article.css("a.topic-tag")
        ]

        language_node = article.css_first(
            '[itemprop="programmingLanguage"]'
        )
        language = (
            language_node.text(strip=True)
            if language_node
            else None
        )

        updated_node = article.css_first("relative-time")
        updated_at = (
            updated_node.attributes.get("datetime")
            if updated_node
            else None
        )

        stars, forks = get_repo_stats(
            client=api_client,
            owner=owner,
            name=name,
        )

        projects.append(
            TopicProject(
                owner=owner,
                name=name,
                url=repo_url,
                description=description,
                stars=stars,
                forks=forks,
                language=language,
                topics=topics,
                updated_at=updated_at,
            )
        )

    return projects


def get_topic_projects(
        topic: str,
        max_pages: int = 5,
) -> list[TopicProject]:
    projects: list[TopicProject] = []
    seen: set[str] = set()

    encoded_topic = quote(topic, safe="")

    with (
        httpx.Client(
            base_url=GITHUB_WEB,
            headers={
                "User-Agent": "Mozilla/5.0",
            },
            follow_redirects=True,
            timeout=30,
        ) as web_client,
        httpx.Client(
            base_url=GITHUB_API,
            headers=headers,
            timeout=30,
        ) as api_client,
    ):
        for page in range(1, max_pages + 1):
            response = web_client.get(
                f"/topics/{encoded_topic}",
                params={
                    "page": page,
                    "s": "stars",
                    "o": "desc",
                },
            )
            response.raise_for_status()

            print(
                f"Fetched topic={topic}, "
                f"page={page}, "
                f"url={response.url}"
            )

            tree = HTMLParser(response.text)

            page_projects = parse_topic_page(
                tree=tree,
                api_client=api_client,
                seen=seen,
            )

            if not page_projects:
                break

            projects.extend(page_projects)

    return projects
