# coding: utf-8
from __future__ import unicode_literals

from django.utils.six.moves.urllib.request import urlopen


def url_available(url=None, expected_code=200):
    """ Check availability (HTTP response code) of single resource """
    assert urlopen(url).getcode() == expected_code
