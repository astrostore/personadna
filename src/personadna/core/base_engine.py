"""
Base class for every PersonaDNA engine.
"""

from abc import ABC, abstractmethod

from personadna.models.knowledge_object import KnowledgeObject


class BaseEngine(ABC):

    name = "Base Engine"

    @abstractmethod
    def process(self, knowledge_object: KnowledgeObject) -> KnowledgeObject:
        pass
