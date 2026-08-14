from __future__ import annotations

import json
from pathlib import Path

import httpx

from contribution_compass.adapters.discovery import (
    GitHubRepositoryDiscovery,
    RegistryRepositoryDiscovery,
)
from contribution_compass.application.setup import SetupDoctor, infer_repository
from contribution_compass.config import parse_config
from contribution_compass.domain.bootstrap import (
    DependencyReference,
    candidate,
    discover_manifest,
    initial_config_document,
)


def test_manifests_find_direct_github_modules_and_registry_dependencies(tmp_path: Path) -> None:
    package = tmp_path / "package.json"
    package.write_text(
        json.dumps(
            {
                "dependencies": {
                    "widget": "^2.0.0",
                    "direct": "git+https://github.com/acme/direct.git",
                }
            }
        )
    )
    package_result = discover_manifest(package)
    assert package_result.repositories[0].repository == "acme/direct"
    assert package_result.dependencies == (DependencyReference("npm", "widget"),)

    requirements = tmp_path / "requirements.txt"
    requirements.write_text(
        "httpx>=0.28\nthing @ git+https://github.com/acme/thing.git\n-r base.txt\n"
    )
    requirements_result = discover_manifest(requirements)
    assert requirements_result.repositories[0].repository == "acme/thing"
    assert requirements_result.dependencies == (DependencyReference("pypi", "httpx"),)

    go_mod = tmp_path / "go.mod"
    go_mod.write_text(
        "module example.test/app\n\nrequire (\n github.com/acme/runtime/v2 v2.1.0\n golang.org/x/sync v0.1.0\n)\n"
    )
    assert discover_manifest(go_mod).repositories[0].repository == "acme/runtime"


def test_registry_metadata_resolves_only_unambiguous_github_repositories() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.host == "registry.npmjs.org":
            return httpx.Response(
                200,
                json={"repository": {"type": "git", "url": "https://github.com/acme/widget"}},
            )
        return httpx.Response(
            200,
            json={"info": {"project_urls": {"Source": "https://github.com/acme/runtime"}}},
        )

    discovery = RegistryRepositoryDiscovery(
        client=httpx.Client(transport=httpx.MockTransport(handler))
    )
    resolved, unresolved = discovery.resolve(
        (DependencyReference("npm", "widget"), DependencyReference("pypi", "runtime"))
    )
    assert [item.repository for item in resolved] == ["acme/widget", "acme/runtime"]
    assert unresolved == []


def test_starred_repositories_are_bounded_and_normalized() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        assert request.url.path == "/user/starred"
        return httpx.Response(
            200,
            json=[
                {"full_name": "acme/widget", "name": "widget"},
                {"full_name": "acme/runtime", "name": "runtime"},
            ],
        )

    discovery = GitHubRepositoryDiscovery(
        "token",
        client=httpx.Client(
            base_url="https://api.github.test", transport=httpx.MockTransport(handler)
        ),
    )
    assert [item.repository for item in discovery.starred(1)] == ["acme/widget"]


def test_generated_config_is_explicit_valid_and_handles_duplicate_repo_names() -> None:
    document = initial_config_document(
        [
            candidate("one/runtime", source="test"),
            candidate("two/runtime", source="test"),
        ],
        group_id="interests",
        group_name="My Interests",
    )
    config = parse_config(document)
    repos = config.repo_groups[0].repos
    assert [repo.id for repo in repos] == ["one-runtime", "two-runtime"]
    assert document["contributions"]["weights"]["maintainer_invitation"] == 60  # type: ignore[index]


class FakeRemoteInspector:
    def get(self, repository: str, endpoint: str) -> tuple[int, dict[str, object] | None]:
        assert repository == "acme/compass"
        values = {
            "actions/permissions": {"enabled": True},
            "actions/permissions/workflow": {"default_workflow_permissions": "write"},
            "pages": {"build_type": "workflow"},
        }
        return 200, values[endpoint]


def test_doctor_checks_local_workflows_and_remote_settings(tmp_path: Path) -> None:
    workflows = tmp_path / ".github/workflows"
    workflows.mkdir(parents=True)
    (workflows / "compass.yml").write_text("workflow_dispatch:\ncontents: write\n")
    (workflows / "pages.yml").write_text("actions/deploy-pages\npages: write\n")
    config = parse_config(
        {
            "repo_groups": {
                "tools": {
                    "name": "Tools",
                    "repos": [{"id": "widget", "repo": "acme/widget", "name": "Widget"}],
                }
            }
        }
    )
    report = SetupDoctor(FakeRemoteInspector()).inspect(
        config,
        root=tmp_path,
        token_present=True,
        repository="acme/compass",
    )
    assert report.ok
    assert all(check.status == "pass" for check in report.checks)
    assert infer_repository("git@github.com:acme/compass.git") == "acme/compass"


def test_doctor_fails_for_missing_token_workflows_and_pages(tmp_path: Path) -> None:
    class MissingPages:
        def get(self, repository: str, endpoint: str) -> tuple[int, dict[str, object] | None]:
            return (404, None)

    config = parse_config(
        {
            "repo_groups": {
                "tools": {
                    "name": "Tools",
                    "repos": [{"id": "widget", "repo": "acme/widget", "name": "Widget"}],
                }
            }
        }
    )
    report = SetupDoctor(MissingPages()).inspect(
        config,
        root=tmp_path,
        token_present=False,
        repository="acme/compass",
    )
    assert not report.ok
    assert {check.id for check in report.checks if check.status == "fail"} >= {
        "github-token",
        "pages",
    }
