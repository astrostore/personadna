"""
Evidence Rules.

Transforms observations into objective evidence.

Each rule is independent and returns either:
- an Evidence object
- or None
"""

from typing import Callable

from .models import Evidence
from . import registry


def rule_readme_present(observations: dict):
    """Generate evidence if a README is present."""
    if observations.get("readme_exists", False):
        return Evidence(
            id=registry.README_PRESENT,
            title="README Present",
            description="Repository contains a README file.",
            category="documentation",
            severity="positive",
        )
    return None


def rule_license_present(observations: dict):
    """Generate evidence if a LICENSE is present."""
    if observations.get("license_exists", False):
        return Evidence(
            id=registry.LICENSE_PRESENT,
            title="License Present",
            description="Repository contains a license file.",
            category="documentation",
            severity="positive",
        )

    return Evidence(
        id=registry.LICENSE_MISSING,
        title="License Missing",
        description="Repository does not contain a license file.",
        category="documentation",
        severity="warning",
    )


def rule_python_source(observations: dict):
    """Generate evidence if Python source files exist."""
    if observations.get("python_files", 0) > 0:
        return Evidence(
            id=registry.PYTHON_SOURCE_PRESENT,
            title="Python Source Detected",
            description="Repository contains Python source code.",
            category="source",
            severity="positive",
            metadata={
                "python_files": observations.get("python_files", 0)
            }
        )
    return None


RULES: list[Callable] = [
    rule_readme_present,
    rule_license_present,
    rule_python_source,
]
