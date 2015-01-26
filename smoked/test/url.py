# coding: utf-8
from __future__ import unicode_literals

from django.utils.six.moves.urllib.request import urlopen
from django.utils.six.moves.urllib.error import HTTPError


def url_available(url=None, expected_code=200):
    """ Check availability (HTTP response code) of single resource """
    try:
        assert urlopen(url).getcode() == expected_code
    except HTTPError as e:
        assert e.code == expected_code
