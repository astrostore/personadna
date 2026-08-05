"""
Scoring models for PersonaDNA.

Defines the canonical scoring model produced from
EvidenceCollection objects.
"""

from dataclasses import dataclass, field


@dataclass
class RepositoryScore:
    """Represents quantitative repository assessment."""

    documentation: int = 0
    testing: int = 0
    architecture: int = 0
    maintainability: int = 0
    repository_health: int = 0

    positive_findings: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    critical_findings: list[str] = field(default_factory=list)

    confidence: float = 1.0
