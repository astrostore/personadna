"""
PersonaDNA Observation Model

Observations are evidence produced by intelligence engines.
They never modify the Persona directly.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Any
from uuid import uuid4


@dataclass
class Observation:
    observation_id: str = field(default_factory=lambda: str(uuid4()))

    engine: str = ""

    category: str = ""

    name: str = ""

    value: Any = None

    confidence: float = 1.0

    evidence: list = field(default_factory=list)

    metadata: dict = field(default_factory=dict)

    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))

    version: int = 1
