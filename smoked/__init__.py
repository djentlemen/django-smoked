# coding: utf-8
from __future__ import unicode_literals

import django
from django.conf import settings

from .registry import Registry

__version__ = '0.1-alpha.1'

__all__ = ['default_registry', 'register']

default_registry = Registry()
register = default_registry.register

default_app_config = 'smoked.apps.SmokedApp'

if settings.configured and django.VERSION[1] < 7:
    # Dj<1.7 doesn't have App registry
    from .loader import load_test_module
    load_test_module()
