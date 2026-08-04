from personadna.core.engine_context import EngineContext
from personadna.models.knowledge_object import KnowledgeObject


def test_create_engine_context():

    obj = KnowledgeObject(
        object_id="1",
        object_type="text",
        source="demo",
        content="Hello PersonaDNA",
    )

    ctx = EngineContext(knowledge_object=obj)

    assert ctx.knowledge_object.object_id == "1"

    assert ctx.execution_id != ""

    assert ctx.persona is None
