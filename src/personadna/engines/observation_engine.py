"""
PersonaDNA Observation Engine

Base engine responsible for creating observations from
Knowledge Objects.
"""

from personadna.core.base_engine import BaseEngine
from personadna.core.engine_context import EngineContext
from personadna.models.observation import Observation


class ObservationEngine(BaseEngine):

    name = "Observation Engine"

    def validate(self, context: EngineContext) -> bool:
        return context.knowledge_object is not None

    def observe(self, context: EngineContext) -> list[Observation]:

        obj = context.knowledge_object

        observation = Observation(
            engine=self.name,
            category="content",
            name="object_type",
            value=obj.object_type,
            confidence=1.0,
        )

        return [observation]

    def enrich(self, observations: list[Observation]) -> list[Observation]:
        return observations

    def finalize(self, observations: list[Observation]) -> list[Observation]:
        return observations

    def process(self, context: EngineContext):

        if not self.validate(context):
            return []

        observations = self.observe(context)

        observations = self.enrich(observations)

        return self.finalize(observations)
