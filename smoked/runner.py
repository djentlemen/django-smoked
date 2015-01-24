from smoked import default_registry


def run_tests(registry=None):
    if not registry:
        registry = default_registry

    for test in registry.tests:
        output = {
            'name': test.name,
            'description': test.description,
        }

        params = test.params or {}
        try:
            test.func(**params)
        except Exception as e:
            output['error'] = e

        yield output
