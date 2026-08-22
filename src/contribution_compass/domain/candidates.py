from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class DiscoveryEvidence:
    source: str
    detail: str


@dataclass(frozen=True, slots=True)
class CandidateRepository:
    repository: str
    name: str
    evidence: tuple[DiscoveryEvidence, ...]
