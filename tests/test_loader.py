import pytest
from django.core.exceptions import ImproperlyConfigured

from smoked import loader


def test_testing_module_settings_missing(settings):
    settings.SMOKE_TESTS = ''

    with pytest.raises(ImproperlyConfigured):
        loader.load_test_module()


def test_testing_module_invalid(settings):
    settings.SMOKE_TESTS = 'unknown.module'

    with pytest.raises(ImproperlyConfigured):
        loader.load_test_module()


def test_testing_module_valid():
    # No exception raised means successful test pass
    loader.load_test_module()
