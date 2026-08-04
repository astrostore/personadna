"""
PersonaDNA Persona Engine

Builds a Persona from observations and relationships.
"""

from personadna.core.base_engine import BaseEngine
from personadna.models.observation import Observation
from personadna.models.persona import Persona
from personadna.models.relationship import Relationship


class PersonaEngine(BaseEngine):

    name = "Persona Engine"

    def validate(
        self,
        observations: list[Observation],
    ) -> bool:
        return len(observations) > 0

    def observe(self, observations):
        return observations

    def enrich(self, persona):
        return persona

    def finalize(self, persona):
        return persona

    def process(
        self,
        observations: list[Observation],
        relationships: list[Relationship],
    ) -> Persona:

        if not self.validate(observations):
            return Persona()

        persona = Persona(name="Generated Persona")

        for observation in observations:
            persona.add_observation(observation)

        for relationship in relationships:
            persona.add_relationship(relationship)

        return self.finalize(persona)
