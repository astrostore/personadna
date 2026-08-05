"""
Tests for RepositoryClassifier.
"""

from personadna.classification.classifier import RepositoryClassifier
from personadna.evidence.engine import EvidenceEngine
from personadna.scoring.scorer import RepositoryScorer


def test_repository_classifier():

    observations = {
        "readme_exists": True,
        "license_exists": True,
        "python_files": 30,
    }

    evidence = EvidenceEngine().evaluate(observations)

    score = RepositoryScorer().score(evidence)

    classification = RepositoryClassifier().classify(score)

    assert classification.repository_type != "Unknown"
    assert classification.matched_profile != ""
    assert classification.confidence > 0.0
    assert len(classification.reasoning) >= 2
