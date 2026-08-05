from pathlib import Path

from personadna.repository.repository_adapter import RepositoryAdapter


def test_repository_adapter():
    adapter = RepositoryAdapter()

    repository = Path(__file__).parents[2]

    objects = adapter.acquire(str(repository))

    assert len(objects) > 0

    assert any(obj.object_type == "python" for obj in objects)
