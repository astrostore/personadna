"""
Tests for RepositoryScorer.
"""

from personadna.evidence.engine import EvidenceEngine
from personadna.scoring.scorer import RepositoryScorer


def test_repository_scorer():

    observations = {
        "readme_exists": True,
        "license_exists": True,
        "python_files": 30,
    }

    evidence = EvidenceEngine().evaluate(observations)

    score = RepositoryScorer().score(evidence)

    assert score.documentation == 50
    assert score.testing == 0
    assert score.architecture == 20

    assert score.repository_health >= 0
