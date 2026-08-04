from personadna.models.observation import Observation
from personadna.models.persona import Persona
from personadna.models.relationship import Relationship


def test_create_persona():

    persona = Persona(name="Sandy")

    obs = Observation(
        engine="WritingDNA",
        category="style",
        name="sentence_length",
        value=17,
    )

    rel = Relationship(
        source_id="A",
        target_id="B",
        relationship_type="supports",
    )

    persona.add_observation(obs)

    persona.add_relationship(rel)

    assert persona.name == "Sandy"

    assert len(persona.observations) == 1

    assert len(persona.relationships) == 1

    assert persona.version == 1
