# coding: utf-8
from __future__ import unicode_literals

import pytest
from mock import call

from smoked import register


@pytest.fixture
def mocked_registry(mocker):
    return mocker.patch('smoked.registry._register')


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
