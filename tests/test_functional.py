from smoked import default_registry


def test_non_empty_registry():
    # Tests are loaded from tests.functional.simple
    assert len(default_registry._registry)
