# coding: utf-8
from __future__ import unicode_literals

from django.apps import AppConfig


class SmokedApp(AppConfig):
    name = 'smoked'

    def ready(self):
        from smoked.loader import load_test_module
        load_test_module()