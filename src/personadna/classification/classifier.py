"""
Repository classifier.

Matches repository scores against known repository profiles.
"""

from personadna.scoring.models import RepositoryScore

from .models import RepositoryClassification
from .profiles import PROFILES


class RepositoryClassifier:
    """Classifies repositories by profile similarity."""

    def classify(
        self,
        score: RepositoryScore,
    ) -> RepositoryClassification:

        best_profile = None
        best_difference = float("inf")

        for profile in PROFILES:

            difference = (
                abs(score.documentation - profile.documentation)
                + abs(score.testing - profile.testing)
                + abs(score.architecture - profile.architecture)
                + abs(score.maintainability - profile.maintainability)
            )

            if difference < best_difference:
                best_difference = difference
                best_profile = profile

        max_difference = 400

        confidence = max(
            0.0,
            1.0 - (best_difference / max_difference)
        )

        result = RepositoryClassification(
            repository_type=best_profile.name,
            matched_profile=best_profile.name,
            confidence=confidence,
        )

        result.reasoning.append(
            f"Best profile match: {best_profile.name}"
        )

        result.reasoning.append(
            f"Profile difference: {best_difference}"
        )

        return result
