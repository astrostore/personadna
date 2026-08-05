"""
PersonaDNA Repository Adapter

Converts a software repository into
Knowledge Objects.
"""

from pathlib import Path

from personadna.models.knowledge_object import KnowledgeObject
from personadna.repository.repository_classifier import RepositoryClassifier


class RepositoryAdapter:
    """Acquire repository files as Knowledge Objects."""

    def acquire(self, repository_path: str) -> list[KnowledgeObject]:
        root = Path(repository_path)

        classifier = RepositoryClassifier()

        knowledge_objects: list[KnowledgeObject] = []

        for path in root.rglob("*"):

            if not path.is_file():
                continue

            knowledge_objects.append(
                KnowledgeObject(
                    object_id=str(path.relative_to(root)),
                    object_type=classifier.classify(path),
                    source="repository",
                    content={
                        "name": path.name,
                        "path": str(path.relative_to(root)),
                        "size": path.stat().st_size,
                    },
                )
            )

        return knowledge_objects
