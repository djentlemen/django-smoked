def register(*args, **kwargs):
    """
    Entry point for registering smoke tests. Accepts dotted path to smoke test,
    testing func or it can act as an decorator.

    Usage:
    1. Lazily loaded SmokeTest class
    register('module.SmokeTest')

    2. Registering ad-hoc function
    register(smoke_test, name='Smoke Test', description='Explaining message')

    3. Simple decorator, taking description from doctest when available
    @register
    def smoke_test():
        " Description from doctest "
        pass

    4. Explicitly set name and description of decorated smoke test
    @register(name='Smoke Test', description='Explaining message')
    def smoke_test():
        pass

    """
    pass


def _register(func, name=None, description=None):
    """
    The *real* register method responsible for adding smoke test
    into registry.
    """
    pass
