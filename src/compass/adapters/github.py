import logging
from typing import TypedDict

from dotenv import load_dotenv
from selectolax.parser import HTMLParser

logger = logging.getLogger(__name__)

GITHUB_API = "https://api.github.com"
GITHUB_GRAPHQL_API = "https://api.github.com/graphql"
GITHUB_WEB = "https://github.com"

REPOS_PER_PAGE = 100


class TopicRepoRecord(TypedDict):
    owner: str
    name: str
    url: str
    description: str | None
    language: str | None
    topics: list[str]
    updated_at: str | None


def build_headers(token: str) -> dict[str, str]:
    return {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28",
    }


def parse_topic_article(article) -> TopicRepoRecord | None:
    heading = article.css_first("h3")

    if heading is None:
        return None

    repo_links = heading.css("a")

    if len(repo_links) < 2:
        return None

    repo_link = repo_links[-1]
    href = repo_link.attributes.get("href")

    if not href:
        return None

    description_node = article.css_first("p.color-fg-muted")
    language_node = article.css_first('[itemprop="programmingLanguage"]')
    updated_node = article.css_first("relative-time")

    return TopicRepoRecord(
        owner=repo_links[0].text(strip=True),
        name=repo_link.text(strip=True),
        url=f"{GITHUB_WEB}{href}",
        description=(
            description_node.text(strip=True)
            if description_node
            else None
        ),
        language=(
            language_node.text(strip=True)
            if language_node
            else None
        ),
        topics=[
            node.text(strip=True)
            for node in article.css("a.topic-tag")
        ],
        updated_at=(
            updated_node.attributes.get("datetime")
            if updated_node
            else None
        ),
    )


def parse_topic_page(tree: HTMLParser) -> list[TopicRepoRecord]:
    records = (
        parse_topic_article(article)
        for article in tree.css("article")
    )

    return [record for record in records if record is not None]


class GitHubClient:
    def __init__(self, token: str | None = None, timeout: float = 30) -> None:
        load_dotenv()

    def graphql_request(self,):
        pass

    def graphql_read_project(self):
        pass

    def graphql_read_issues(self):
        pass

    def graphql_read_topic(self):
        pass

    def graphql_read_user(self):
        pass

    def graphql_read_repo(self):
        pass
