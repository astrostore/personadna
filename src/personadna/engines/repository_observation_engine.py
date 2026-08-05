"""
PersonaDNA Repository Observation Engine

Produces evidence-based observations from
repository Knowledge Objects.
"""

from personadna.core.base_engine import BaseEngine
from personadna.models.observation import Observation


class RepositoryObservationEngine(BaseEngine):
    """Generate repository observations."""

    def process(self, knowledge_objects):

        observations = []

        counts = {}

        evidence = {}

        for obj in knowledge_objects:

            counts[obj.object_type] = counts.get(obj.object_type, 0) + 1

            evidence.setdefault(obj.object_type, []).append(obj.object_id)

        mapping = {
            "python": (
                "repository",
                "Python Source Present",
                "Repository contains Python source files.",
            ),
            "test": (
                "testing",
                "Unit Tests Present",
                "Repository contains automated unit tests.",
            ),
            "architecture": (
                "architecture",
                "Architecture Documentation Present",
                "Repository contains architecture documents.",
            ),
            "adr": (
                "architecture",
                "Architecture Decisions Present",
                "Repository contains ADR documents.",
            ),
            "markdown": (
                "documentation",
                "Markdown Documentation Present",
                "Repository contains Markdown documentation.",
            ),
            "yaml": (
                "configuration",
                "YAML Configuration Present",
                "Repository contains YAML configuration files.",
            ),
            "json": (
                "configuration",
                "JSON Configuration Present",
                "Repository contains JSON configuration files.",
            ),
            "docker": (
                "deployment",
                "Docker Support Present",
                "Repository contains Docker configuration.",
            ),
            "readme": (
                "documentation",
                "README Present",
                "Repository contains a README document.",
            ),
        }

        for object_type, total in counts.items():

            if object_type not in mapping:
                continue

            category, name, description = mapping[object_type]

            observations.append(
                Observation(
                    engine="RepositoryObservationEngine",
                    category=category,
                    name=name,
                    value=description,
                    confidence=1.0,
                    evidence=evidence.get(object_type, []),
                    metadata={
                        "count": total,
                        "object_type": object_type,
                    },
                )
            )

        return observations
