from pathlib import Path

from personadna.engines.repository_observation_engine import (
    RepositoryObservationEngine,
)
from personadna.repository.repository_adapter import RepositoryAdapter


def test_repository_observation_engine():

    adapter = RepositoryAdapter()

    repository = Path(__file__).parents[2]

    objects = adapter.acquire(str(repository))

    engine = RepositoryObservationEngine()

    observations = engine.process(objects)

    assert len(observations) > 0

    assert any(observation.category == "repository" for observation in observations)
