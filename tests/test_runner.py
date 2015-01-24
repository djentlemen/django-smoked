# coding: utf-8
from __future__ import unicode_literals
from mock import call

from smoked import register, Registry
from smoked.runner import run_tests


def test_run_output(valid_test):
    valid_test.__doc__ = 'Mocked description'

    register(valid_test, params={'key': 'value'})
    results = list(run_tests())

    expected_output = {
        'name': 'Mocked Test',
        'description': 'Mocked description'
    }

    assert valid_test.called
    assert valid_test.call_args == call(key='value')
    assert len(results) == 1
    assert results[0] == expected_output


def test_success_run(valid_test):
    # Register and run test
    register(valid_test)
    results = list(run_tests())

    assert len(results) == 1
    assert 'error' not in results[0]


def test_failed_run(invalid_test):
    # Register and run test
    register(invalid_test)
    results = list(run_tests())

    assert len(results) == 1
    assert str(results[0]['error']) == 'Failed test'


def test_custom_registry(valid_test, invalid_test):
    # Fill custom registry
    register(valid_test)

    # ... and then check the custom registry is filled and run
    custom_registry = Registry()
    custom_registry.register(valid_test)
    custom_registry.register(invalid_test)

    results = list(run_tests(custom_registry))

    assert len(results) == 2
