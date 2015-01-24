# coding: utf-8
from __future__ import unicode_literals

SMOKE_TESTS = 'tests.smoke_tests.simple'

ROOT_URLCONF = 'smoke_tests.urls'
INSTALLED_APPS = ['smoked']
SECRET_KEY = 'must not be empty'
