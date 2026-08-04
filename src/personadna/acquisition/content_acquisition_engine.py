"""
Content Acquisition Engine

Every external source enters PersonaDNA through this engine.
"""

from uuid import uuid4

from personadna.models.knowledge_object import KnowledgeObject


class ContentAcquisitionEngine:

    name = "Content Acquisition Engine"

    def create(
        self,
        source: str,
        object_type: str,
        content,
        metadata=None,
    ):

        if metadata is None:
            metadata = {}

        ko = KnowledgeObject(
            object_id=str(uuid4()),
            object_type=object_type,
            source=source,
            content=content,
            metadata=metadata,
        )

        ko.log("Content Acquisition")

        return ko
