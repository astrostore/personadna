"""
Classification models for PersonaDNA.
"""

from dataclasses import dataclass, field


@dataclass
class RepositoryClassification:
    """Result of repository classification."""

    repository_type: str = "Unknown"
    confidence: float = 0.0
    matched_profile: str = ""
    reasoning: list[str] = field(default_factory=list)
