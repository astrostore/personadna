from personadna.engines.relationship_engine import RelationshipEngine
from personadna.models.observation import Observation


def test_relationship_engine():

    observations = [
        Observation(
            engine="Test",
            category="A",
            name="One",
            value=1,
        ),
        Observation(
            engine="Test",
            category="B",
            name="Two",
            value=2,
        ),
    ]

    engine = RelationshipEngine()

    relationships = engine.process(observations)

    assert len(relationships) == 1

    assert relationships[0].relationship_type == "supports"
