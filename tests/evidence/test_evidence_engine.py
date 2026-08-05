"""
Tests for the Evidence Engine.
"""

from personadna.evidence.engine import EvidenceEngine


def test_evidence_engine_generates_expected_evidence():
    """Evidence engine should generate evidence from observations."""

    observations = {
        "readme_exists": True,
        "license_exists": False,
        "python_files": 30,
    }

    engine = EvidenceEngine()
    collection = engine.evaluate(observations)

    assert len(collection) == 3

    ids = {item.id for item in collection.evidence}

    assert "README_PRESENT" in ids
    assert "LICENSE_MISSING" in ids
    assert "PYTHON_SOURCE_PRESENT" in ids
