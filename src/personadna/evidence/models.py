"""
Evidence models for PersonaDNA.

This module defines the canonical data structures used by the
Evidence Engine. Evidence represents objective facts derived from
repository observations. It does not perform scoring or judgement.
"""

from dataclasses import dataclass, field
from datetime import datetime, UTC
from typing import Any


@dataclass(frozen=True)
class Evidence:
    """
    Represents a single piece of objective evidence.
    """

    id: str
    title: str
    description: str
    category: str
    severity: str
    confidence: float = 1.0
    source: str = "observation_engine"
    metadata: dict[str, Any] = field(default_factory=dict)
timestamp: datetime = field(default_factory=lambda: datetime.now(UTC))

@dataclass
class EvidenceCollection:
    """
    Container for multiple Evidence objects.
    """

    evidence: list[Evidence] = field(default_factory=list)

    def add(self, item: Evidence) -> None:
        """Add an evidence item."""
        self.evidence.append(item)

    def __len__(self) -> int:
        return len(self.evidence)
