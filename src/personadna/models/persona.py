"""
PersonaDNA Persona Model

Represents the evolving cognitive identity of an individual.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from uuid import uuid4


@dataclass
class Persona:
    persona_id: str = field(default_factory=lambda: str(uuid4()))

    name: str = ""

    observations: list = field(default_factory=list)

    relationships: list = field(default_factory=list)

    metadata: dict = field(default_factory=dict)

    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))

    updated_at: datetime = field(default_factory=lambda: datetime.now(UTC))

    version: int = 1

    def add_observation(self, observation):

        self.observations.append(observation)

        self.updated_at = datetime.now(UTC)

    def add_relationship(self, relationship):

        self.relationships.append(relationship)

        self.updated_at = datetime.now(UTC)
