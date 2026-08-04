"""
PersonaDNA Relationship Engine

Creates relationships between observations.
"""

from personadna.core.base_engine import BaseEngine
from personadna.models.relationship import Relationship
from personadna.models.observation import Observation


class RelationshipEngine(BaseEngine):

    name = "Relationship Engine"

    def validate(self, observations: list[Observation]) -> bool:
        return len(observations) >= 2

    def observe(self, observations):
        return observations

    def enrich(self, observations):
        return observations

    def finalize(self, relationships):
        return relationships

    def process(
        self,
        observations: list[Observation],
    ) -> list[Relationship]:

        if not self.validate(observations):
            return []

        relationships = []

        for i in range(len(observations) - 1):

            relationships.append(
                Relationship(
                    source_id=observations[i].observation_id,
                    target_id=observations[i + 1].observation_id,
                    relationship_type="supports",
                    confidence=1.0,
                )
            )

        return self.finalize(relationships)
