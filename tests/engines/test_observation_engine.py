from personadna.acquisition.content_acquisition_engine import (
    ContentAcquisitionEngine,
)
from personadna.core.engine_context import EngineContext
from personadna.engines.observation_engine import ObservationEngine


def test_observation_engine():

    acquisition = ContentAcquisitionEngine()

    obj = acquisition.create(
        source="demo",
        object_type="text",
        content="Hello",
    )

    context = EngineContext(knowledge_object=obj)

    engine = ObservationEngine()

    observations = engine.process(context)

    assert len(observations) == 1

    assert observations[0].name == "object_type"

    assert observations[0].value == "text"
