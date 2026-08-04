"""
PersonaDNA Relationship Model

Relationships connect Knowledge Objects, Observations and Personas.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from uuid import uuid4


@dataclass
class Relationship:
    relationship_id: str = field(default_factory=lambda: str(uuid4()))

    source_id: str = ""

    target_id: str = ""

    relationship_type: str = ""

    confidence: float = 1.0

    metadata: dict = field(default_factory=dict)

    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))

    version: int = 1
