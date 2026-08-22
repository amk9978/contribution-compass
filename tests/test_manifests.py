from __future__ import annotations

from pathlib import Path

from contribution_compass.adapters.manifests import discover_manifest, github_repository


def test_github_repository_accepts_slugs_and_urls() -> None:
    assert github_repository("open-telemetry/opentelemetry-collector") == (
        "open-telemetry/opentelemetry-collector"
    )
    assert github_repository("git+https://github.com/astral-sh/uv.git") == "astral-sh/uv"
    assert github_repository("https://example.com/not-github") is None


def test_package_manifest_preserves_dependency_scope_and_repository_provenance(
    tmp_path: Path,
) -> None:
    manifest = tmp_path / "package.json"
    manifest.write_text(
        '{"dependencies":{"fast":"github:owner/fast","react":"^19"},'
        '"devDependencies":{"vitest":"^3"},"optionalDependencies":{"fsevents":"^2"}}',
        encoding="utf-8",
    )

    result = discover_manifest(manifest)

    assert result.repositories[0].repository == "owner/fast"
    assert result.repositories[0].evidence[0].source == f"manifest:{manifest}"
    assert [(item.name, item.scope) for item in result.dependencies] == [
        ("react", "runtime"),
        ("vitest", "development"),
        ("fsevents", "optional"),
    ]


def test_pyproject_discovers_runtime_and_optional_dependencies(tmp_path: Path) -> None:
    manifest = tmp_path / "pyproject.toml"
    manifest.write_text(
        '[project]\ndependencies = ["httpx>=0.28"]\n'
        '[project.optional-dependencies]\ndev = ["pytest>=8"]\n',
        encoding="utf-8",
    )

    result = discover_manifest(manifest)

    assert [(item.name, item.scope) for item in result.dependencies] == [
        ("httpx", "runtime"),
        ("pytest", "optional"),
    ]
