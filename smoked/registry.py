# coding: utf-8
from __future__ import unicode_literals
from collections import namedtuple

SmokeTest = namedtuple('SmokeTest', 'func name description')


class Registry(object):
    _registry = []

    @property
    def tests(self):
        """ List of all registered tests """
        return self._registry

    def register(self, func=None, **kwargs):
        """
        Entry point for registering smoke tests. Accepts dotted path to smoke
        test, testing func or it can act as an decorator.

        Usage:
        1. Lazily loaded SmokeTest class
        register('module.SmokeTest')

        2. Registering ad-hoc function
        register(smoke_test, name='Smoke Test', description='Help text')

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

        def wrap(inner_func):
            self._register(func=inner_func, **kwargs)
            return inner_func

        if not func:
            return wrap

        if callable(func) and func.__name__ != '<lambda>':
            kwargs.setdefault('name', func.__name__)
            kwargs.setdefault('description', func.__doc__)

        self._register(func=func, **kwargs)
        return func

    def _register(self, func, name=None, description=None):
        """
        The *real* register method responsible for adding smoke test
        into registry.
        """
        self._registry.append(SmokeTest(func, name, description))
