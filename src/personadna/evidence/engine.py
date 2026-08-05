"""
Evidence Engine.

Executes all registered evidence rules and collects the
resulting Evidence objects into an EvidenceCollection.
"""

from .models import EvidenceCollection
from .rules import RULES


class EvidenceEngine:
    """Runs all evidence rules."""

    def evaluate(self, observations: dict) -> EvidenceCollection:
        collection = EvidenceCollection()

        for rule in RULES:
            evidence = rule(observations)

            if evidence is not None:
                collection.add(evidence)

        return collection
