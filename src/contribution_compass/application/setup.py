from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Literal, Protocol

from contribution_compass.domain.models import CompassConfig

CheckStatus = Literal["pass", "warning", "fail"]


@dataclass(frozen=True, slots=True)
class DoctorCheck:
    id: str
    status: CheckStatus
    message: str
    remediation: str | None = None


@dataclass(frozen=True, slots=True)
class DoctorReport:
    checks: tuple[DoctorCheck, ...]

    @property
    def ok(self) -> bool:
        return not any(check.status == "fail" for check in self.checks)


class RemoteSetupInspector(Protocol):
    def get(self, repository: str, endpoint: str) -> tuple[int, dict[str, object] | None]: ...


def infer_repository(remote_url: str) -> str | None:
    match = re.search(r"github\.com[/:]([^/\s]+)/([^/\s]+?)(?:\.git)?$", remote_url.strip())
    return f"{match.group(1)}/{match.group(2)}" if match else None


class SetupDoctor:
    """Inspect local and optional GitHub deployment readiness without mutating settings."""

    def __init__(self, remote: RemoteSetupInspector | None = None) -> None:
        self._remote = remote

    @staticmethod
    def _workflow_check(root: Path, relative: str, terms: tuple[str, ...]) -> DoctorCheck:
        path = root / relative
        if not path.exists():
            return DoctorCheck(
                f"workflow:{relative}",
                "fail",
                f"Missing {relative}",
                "Restore the workflow from the Contribution Compass template.",
            )
        text = path.read_text(encoding="utf-8")
        missing = [term for term in terms if term not in text]
        if missing:
            return DoctorCheck(
                f"workflow:{relative}",
                "fail",
                f"{relative} is missing: {', '.join(missing)}",
                "Restore the expected workflow triggers and permissions.",
            )
        return DoctorCheck(f"workflow:{relative}", "pass", f"{relative} is ready")

    def inspect(
        self,
        config: CompassConfig,
        *,
        root: Path,
        token_present: bool,
        repository: str | None,
    ) -> DoctorReport:
        project_count = sum(len(group.repos) for group in config.repo_groups)
        checks = [
            DoctorCheck(
                "config",
                "pass" if project_count else "warning",
                f"Configuration is valid with {project_count} Project Sensors",
                "Add repositories to config.yml before collecting." if not project_count else None,
            ),
            DoctorCheck(
                "github-token",
                "pass" if token_present or not project_count else "fail",
                "GITHUB_TOKEN is available"
                if token_present
                else "GITHUB_TOKEN is not available for repository collection",
                'Run export GITHUB_TOKEN="$(gh auth token)" for a local scan.'
                if project_count and not token_present
                else None,
            ),
            self._workflow_check(
                root,
                ".github/workflows/compass.yml",
                ("workflow_dispatch", "contents: write"),
            ),
            self._workflow_check(
                root,
                ".github/workflows/pages.yml",
                ("actions/deploy-pages", "pages: write"),
            ),
        ]
        if repository is None:
            checks.append(
                DoctorCheck(
                    "github-repository",
                    "warning",
                    "GitHub repository could not be inferred; remote settings were not checked",
                    "Pass --repository owner/repository to inspect Actions and Pages.",
                )
            )
            return DoctorReport(tuple(checks))
        checks.append(
            DoctorCheck(
                "site-url",
                "pass",
                f"Expected Pages URL: https://{repository.split('/', 1)[0]}.github.io/{repository.split('/', 1)[1]}/",
            )
        )
        if self._remote is None:
            checks.append(
                DoctorCheck(
                    "remote-settings",
                    "warning",
                    "Remote GitHub settings were not checked",
                    "Provide a GitHub token with repository administration read access.",
                )
            )
            return DoctorReport(tuple(checks))

        actions_status, actions = self._remote.get(repository, "actions/permissions")
        if actions_status == 200 and actions is not None:
            checks.append(
                DoctorCheck(
                    "actions-enabled",
                    "pass" if actions.get("enabled") is True else "fail",
                    "GitHub Actions is enabled"
                    if actions.get("enabled") is True
                    else "GitHub Actions is disabled",
                    None
                    if actions.get("enabled") is True
                    else "Enable Actions in Settings → Actions → General.",
                )
            )
        else:
            checks.append(
                DoctorCheck(
                    "actions-enabled",
                    "warning",
                    f"Could not inspect Actions permissions (HTTP {actions_status})",
                    "Use a token with repository Administration read permission.",
                )
            )

        workflow_status, workflow = self._remote.get(repository, "actions/permissions/workflow")
        if workflow_status == 200 and workflow is not None:
            permission = str(workflow.get("default_workflow_permissions", "unknown"))
            checks.append(
                DoctorCheck(
                    "workflow-permissions",
                    "pass" if permission == "write" else "warning",
                    f"Default GITHUB_TOKEN permission is {permission}",
                    None
                    if permission == "write"
                    else "The workflow requests contents: write explicitly; confirm owner policy allows it.",
                )
            )
        else:
            checks.append(
                DoctorCheck(
                    "workflow-permissions",
                    "warning",
                    f"Could not inspect default workflow permissions (HTTP {workflow_status})",
                    "Use a token with repository Administration read permission.",
                )
            )

        pages_status, pages = self._remote.get(repository, "pages")
        if pages_status == 200 and pages is not None:
            build_type = str(pages.get("build_type", "unknown"))
            checks.append(
                DoctorCheck(
                    "pages",
                    "pass" if build_type == "workflow" else "warning",
                    f"GitHub Pages is configured with build type {build_type}",
                    None
                    if build_type == "workflow"
                    else "Select GitHub Actions as the Pages source in Settings → Pages.",
                )
            )
        else:
            checks.append(
                DoctorCheck(
                    "pages",
                    "fail" if pages_status == 404 else "warning",
                    "GitHub Pages is not configured"
                    if pages_status == 404
                    else f"Could not inspect GitHub Pages (HTTP {pages_status})",
                    "Select GitHub Actions as the Pages source in Settings → Pages.",
                )
            )
        return DoctorReport(tuple(checks))
