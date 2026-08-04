"""
PersonaDNA Engine Context

Shared execution context passed to every engine.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from uuid import uuid4

from personadna.models.knowledge_object import KnowledgeObject
from personadna.models.persona import Persona


@dataclass
class EngineContext:
    execution_id: str = field(default_factory=lambda: str(uuid4()))

    knowledge_object: KnowledgeObject | None = None

    persona: Persona | None = None

    metadata: dict = field(default_factory=dict)

    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))
