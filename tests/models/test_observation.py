from personadna.models.observation import Observation


def test_create_observation():

    obs = Observation(
        engine="WritingDNA",
        category="style",
        name="sentence_length",
        value=18.4,
        confidence=0.95,
    )

    assert obs.engine == "WritingDNA"

    assert obs.category == "style"

    assert obs.confidence == 0.95

    assert obs.version == 1
