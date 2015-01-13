# coding: utf-8
from __future__ import unicode_literals
from importlib import import_module

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


def load_test_module():
    """
    Import test module and trigger registration of tests. Test module is
    defined in `SMOKE_TESTS` setting.
    """

    test_module = getattr(settings, 'SMOKE_TESTS')

    if not test_module:
        raise ImproperlyConfigured('Missing SMOKE_TESTS in settings.')

    try:
        import_module(test_module)
    except ImportError as e:
        msg = "Can't import '{0}' module. Exception: {1}"
        raise ImproperlyConfigured(msg.format(test_module, e))
