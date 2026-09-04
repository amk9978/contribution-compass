import json
import os
from pathlib import Path
from typing import Annotated

import typer

from compass.adapters import GitHubClient
from compass.application import get_topic_projects, get_topics_frequencies
from compass.domain import TopicProject

app = typer.Typer()

TOPICS_FILE = Path("topics.json")
TEST_TOPIC = "github-actions"


def format_github_handle(gitub_handle: str) -> str:
    formatted_handle = gitub_handle.replace("https://github.com/", "")
    formatted_handle = formatted_handle.replace("http://github.com/", "")
    formatted_handle = formatted_handle.replace("github.com/", "")
    formatted_handle = formatted_handle.replace("@", "")
    return formatted_handle.lower()


def collect_topics(
        github_handle: str,
        github: GitHubClient,
) -> list[tuple[str, int]]:
    formatted_github_handle = format_github_handle(github_handle)
    typer.echo(f"Fetching your topics at {formatted_github_handle}...")

    topics = get_topics_frequencies(
        github_handle=formatted_github_handle,
        github=github,
    )
    typer.echo(topics)

    return topics


@app.command()
def get_topics(
        github_handle: Annotated[str, typer.Argument()],
) -> list[tuple[str, int]]:
    with GitHubClient() as github:
        return collect_topics(github_handle=github_handle, github=github)


def load_existing_pages() -> dict[str, list[dict]]:
    if not TOPICS_FILE.exists():
        return {}

    with TOPICS_FILE.open() as file:
        return json.load(file)


def write_into_file(topics: dict[str, list[dict]]) -> None:
    temp_file = TOPICS_FILE.with_suffix(".json.tmp")

    with temp_file.open("w") as file:
        json.dump(topics, file, indent=4)
        file.flush()
        os.fsync(file.fileno())

    os.replace(temp_file, TOPICS_FILE)


@app.command()
def get_topics_pages(
        github_handle: Annotated[str, typer.Argument()],
) -> dict:
    pages = load_existing_pages()

    with GitHubClient() as github:
        topics = collect_topics(github_handle=github_handle, github=github)

        for topic, _ in topics:
            if topic in pages:
                continue
            if topic != TEST_TOPIC:
                continue

            result: list[TopicProject] = get_topic_projects(
                topic=topic,
                github=github,
                max_pages=10,
            )

            pages[topic] = [
                project.model_dump(mode="json")
                for project in result
            ]

            write_into_file(pages)

    return pages


if __name__ == '__main__':
    app()
