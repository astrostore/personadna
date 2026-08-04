"""
PersonaDNA Knowledge Object

Universal information unit used throughout the platform.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Any


@dataclass
class KnowledgeObject:
    object_id: str
    object_type: str
    source: str

    content: Any

    owner: str | None = None

    language: str | None = None

    metadata: dict = field(default_factory=dict)

    observations: list = field(default_factory=list)

    relationships: list = field(default_factory=list)

    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    version: int = 1

    processing_history: list = field(default_factory=list)

    def add_observation(self, observation) -> None:
        self.observations.append(observation)

    def add_relationship(self, relationship) -> None:
        self.relationships.append(relationship)

    def log(self, stage: str) -> None:
        self.processing_history.append(
            {
                "stage": stage,
                "time": datetime.now(UTC).isoformat(),
            }
        )
