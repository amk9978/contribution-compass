from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from contribution_compass.domain.candidates import CandidateRepository

DependencyScope = Literal["runtime", "development", "optional", "unknown"]


@dataclass(frozen=True, slots=True)
class DependencyReference:
    ecosystem: str
    name: str
    scope: DependencyScope
    manifest: str


@dataclass(frozen=True, slots=True)
class ManifestDiscovery:
    repositories: tuple[CandidateRepository, ...]
    dependencies: tuple[DependencyReference, ...]
