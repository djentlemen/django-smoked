# coding: utf-8
from __future__ import unicode_literals

import pytest
from collections import namedtuple
from mock import Mock

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
