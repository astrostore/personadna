"""
Repository Scoring Engine.

Converts EvidenceCollection into RepositoryScore.
"""

from personadna.evidence.models import EvidenceCollection

from .models import RepositoryScore
from .rules import SCORING_RULES


class RepositoryScorer:
    """Calculates repository scores from evidence."""

    def score(self, evidence: EvidenceCollection) -> RepositoryScore:
        result = RepositoryScore()

        for item in evidence.evidence:

            rule = SCORING_RULES.get(item.id)

            if rule is None:
                continue

            current = getattr(result, rule.dimension)
            setattr(result, rule.dimension, current + rule.points)

            if item.severity == "positive":
                result.positive_findings.append(item.title)

            elif item.severity == "warning":
                result.warnings.append(item.title)

            elif item.severity == "critical":
                result.critical_findings.append(item.title)

        # Normalize scores to 0–100
        result.documentation = min(result.documentation, 100)
        result.testing = min(result.testing, 100)
        result.architecture = min(result.architecture, 100)
        result.maintainability = min(result.maintainability, 100)

        result.repository_health = (
            result.documentation +
            result.testing +
            result.architecture +
            result.maintainability
        ) // 4

        return result
