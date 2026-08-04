from personadna.engines.persona_engine import PersonaEngine
from personadna.models.observation import Observation
from personadna.models.relationship import Relationship


def test_persona_engine():

    observations = [
        Observation(
            engine="Test",
            category="content",
            name="type",
            value="text",
        )
    ]

    relationships = [
        Relationship(
            source_id="1",
            target_id="2",
            relationship_type="supports",
        )
    ]

    engine = PersonaEngine()

    persona = engine.process(
        observations,
        relationships,
    )

    assert persona.name == "Generated Persona"

    assert len(persona.observations) == 1

    assert len(persona.relationships) == 1
