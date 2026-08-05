from pathlib import Path

from personadna.repository.repository_classifier import RepositoryClassifier


def test_repository_classifier():

    classifier = RepositoryClassifier()

    assert classifier.classify(Path("README.md")) == "readme"

    assert classifier.classify(Path("PRA-100-System-Overview.md")) == "architecture"

    assert classifier.classify(Path("ADR-001-Test.md")) == "adr"

    assert classifier.classify(Path("test_engine.py")) == "test"

    assert classifier.classify(Path("engine.py")) == "python"

    assert classifier.classify(Path("config.yaml")) == "yaml"

    assert classifier.classify(Path("config.json")) == "json"
