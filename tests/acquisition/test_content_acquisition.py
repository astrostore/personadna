from personadna.acquisition.content_acquisition_engine import (
    ContentAcquisitionEngine,
)


def test_create_knowledge_object():

    engine = ContentAcquisitionEngine()

    obj = engine.create(
        source="handwritten_note.jpg",
        object_type="image",
        content="image-placeholder",
    )

    assert obj.object_type == "image"

    assert obj.source == "handwritten_note.jpg"

    assert len(obj.processing_history) == 1
