# coding: utf-8
from __future__ import unicode_literals

import pytest
from mock import call

from smoked import register, default_registry
from smoked.registry import SmokeTest


@pytest.fixture
def mocked_registry(mocker):
    return mocker.patch('smoked.registry.Registry._register')


def test_register_lazy(mocked_registry):
    """ Register smoke test class from module path """
    register('mytest.SmokeTest')
    mocked_registry.assert_called_with(func='mytest.SmokeTest')


def test_register_func(mocked_registry):
    """ Register ad-hoc function as smoke test """

    # Dummy testing func
    check_func = lambda: True

    register(check_func)
    register(check_func, name='Check func')
    register(check_func, name='Check func', description='Long story')

    expected = [
        call(func=check_func),
        call(func=check_func, name='Check func'),
        call(func=check_func, name='Check func', description='Long story'),
    ]
    mocked_registry.assert_has_calls(expected)


def test_register_decorator(mocked_registry):
    """ Register test using decorator """

    @register(name='Check func', description='Long story')
    def check_func():
        pass

    mocked_registry.assert_called_with(
        func=check_func, name='Check func', description='Long story')


def test_register_decorator_minimal(mocked_registry):
    """ Register test using decorator without any arguments """

    @register
    def check_func():
        """Long story"""
        pass

    mocked_registry.assert_called_with(
        func=check_func, name='check_func', description='Long story')


def test_registry_fill_ad_hoc():
    smoke_test = lambda: 42

    register(smoke_test)
    register(smoke_test, name='Smoke Test')
    register(smoke_test, description='Help text')
    register(smoke_test, name='Smoke Test', description='Help text')
    register(smoke_test, params={'url': 'http://example.com'})

    assert len(default_registry._registry) == 5
    assert all(isinstance(test, SmokeTest)
               for test in default_registry._registry)

    first, second, third, fourth, fifth = default_registry._registry
    # SmokeTest(func, params, name, description)
    assert first == SmokeTest(smoke_test, None, None, None)
    assert second == SmokeTest(smoke_test, None, 'Smoke Test', None)
    assert third == SmokeTest(smoke_test, None, None, 'Help text')
    assert fourth == SmokeTest(smoke_test, None, 'Smoke Test', 'Help text')
    assert fifth == SmokeTest(smoke_test, params={'url': 'http://example.com'},
                              name=None, description=None)


def test_registry_get_tests():
    smoke_test = lambda: 42

    register(smoke_test)
    register(smoke_test, name='Smoke Test')
    register(smoke_test, name='Smoke Test', description='Help text')

    assert default_registry.tests == default_registry._registry
