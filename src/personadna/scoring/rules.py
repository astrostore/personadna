"""
Scoring rules for PersonaDNA.

Maps Evidence identifiers to scoring dimensions
and point values.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class ScoringRule:
    """Defines how one evidence item contributes to a score."""

    evidence_id: str
    dimension: str
    points: int


SCORING_RULES = {
    "README_PRESENT": ScoringRule(
        evidence_id="README_PRESENT",
        dimension="documentation",
        points=30,
    ),

    "LICENSE_PRESENT": ScoringRule(
        evidence_id="LICENSE_PRESENT",
        dimension="documentation",
        points=20,
    ),

    "TEST_SUITE_PRESENT": ScoringRule(
        evidence_id="TEST_SUITE_PRESENT",
        dimension="testing",
        points=50,
    ),

    "PYTHON_SOURCE_PRESENT": ScoringRule(
        evidence_id="PYTHON_SOURCE_PRESENT",
        dimension="architecture",
        points=20,
    ),
}
