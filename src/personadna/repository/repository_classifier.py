"""
PersonaDNA Repository Classifier

Classifies repository files into
well-defined repository knowledge types.
"""

from pathlib import Path


class RepositoryClassifier:
    """Classify repository files."""

    def classify(self, path: Path) -> str:
        name = path.name.lower()

        if name == "readme.md":
            return "readme"

        if name.startswith("adr-"):
            return "adr"

        if name.startswith("pra-"):
            return "architecture"

        if "test_" in name:
            return "test"

        if path.suffix == ".py":
            return "python"

        if path.suffix == ".md":
            return "markdown"

        if path.suffix in {".yml", ".yaml"}:
            return "yaml"

        if path.suffix == ".json":
            return "json"

        if path.name == "Dockerfile":
            return "docker"

        if path.name == ".gitignore":
            return "git"

        return "file"
