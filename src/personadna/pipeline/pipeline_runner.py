"""
PersonaDNA Pipeline Runner

Runs the complete cognitive pipeline.
"""

from personadna.acquisition.content_acquisition_engine import (
    ContentAcquisitionEngine,
)
from personadna.core.engine_context import EngineContext
from personadna.engines.observation_engine import ObservationEngine
from personadna.engines.persona_engine import PersonaEngine
from personadna.engines.relationship_engine import RelationshipEngine


class PipelineRunner:

    def __init__(self):

        self.acquisition = ContentAcquisitionEngine()

        self.observation_engine = ObservationEngine()

        self.relationship_engine = RelationshipEngine()

        self.persona_engine = PersonaEngine()

    def process(
        self,
        source: str,
        object_type: str,
        content: str,
    ):

        knowledge_object = self.acquisition.create(
            source=source,
            object_type=object_type,
            content=content,
        )

        context = EngineContext(knowledge_object=knowledge_object)

        observations = self.observation_engine.process(context)

        relationships = self.relationship_engine.process(observations)

        persona = self.persona_engine.process(
            observations,
            relationships,
        )

        return persona
