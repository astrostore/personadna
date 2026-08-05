"""
Repository classification profiles.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class RepositoryProfile:
    """Expected score profile for a repository archetype."""

    name: str
    documentation: int
    testing: int
    architecture: int
    maintainability: int


PROFILES = [

    RepositoryProfile(
        name="Core Intelligence Library",
        documentation=90,
        testing=80,
        architecture=90,
        maintainability=90,
    ),

    RepositoryProfile(
        name="Application Service",
        documentation=70,
        testing=70,
        architecture=80,
        maintainability=80,
    ),

    RepositoryProfile(
        name="Framework / SDK",
        documentation=80,
        testing=70,
        architecture=85,
        maintainability=85,
    ),
]
