# coding: utf-8
from __future__ import unicode_literals

import pytest
from collections import namedtuple
from mock import Mock
from django.utils.six.moves.urllib.error import URLError

from smoked.test.url import url_available

Request = namedtuple('Request', 'request response')


class TestUrl:
    @pytest.fixture
    def url(self):
        return 'http://google.com'

    @pytest.fixture
    def mocked_request(self, mocker):
        response = Mock()
        response.getcode.return_value = 200
        request = mocker.patch('smoked.test.url.urlopen')
        request.return_value = response
        return Request(request, response)

    @pytest.fixture(params=['200', '301', '404'])
    def status_code(self, request):
        return int(request.param)

    def test_url_available(self, url, mocked_request, status_code):
        mocked_request.response.getcode.return_value = status_code
        try:
            url_available(url=url, expected_code=status_code)
        except AssertionError as e:
            pytest.fail(e.message)

        assert mocked_request.request.called
        mocked_request.request.assert_called_with(url)

    def test_url_not_available(self, url, mocked_request):
        with pytest.raises(AssertionError):
            url_available(url, expected_code='500')

    def test_google_available(self, url):
        try:
            url_available(url)
        except AssertionError as e:
            pytest.fail(e.message)

    def test_nonexisting_url(self):
        try:
            url_available('http://google.com/doesnnotexist', expected_code=404)
        except AssertionError as e:
            pytest.fail(e.message)

    def test_nonexisting_domain(self):
        """
        Non-existing domain still raises exception
        """
        with pytest.raises(URLError):
            url_available('http://reallydoesnotexist.com/', expected_code=404)
