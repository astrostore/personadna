from personadna.models.relationship import Relationship


def test_create_relationship():

    rel = Relationship(
        source_id="obs-001",
        target_id="obs-002",
        relationship_type="supports",
        confidence=0.92,
    )

    assert rel.source_id == "obs-001"

    assert rel.target_id == "obs-002"

    assert rel.relationship_type == "supports"

    assert rel.confidence == 0.92

    assert rel.version == 1
