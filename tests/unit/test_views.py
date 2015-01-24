# coding: utf-8
from __future__ import unicode_literals

import pytest
from django.core.urlresolvers import reverse

from smoked.runner import run_tests


class TestSmokeResultsView:
    @pytest.fixture
    def url(self):
        return reverse('smoked:results')

    def test_html_output(self, client, url, filled_registry):
        response = client.get(url)

        expected_context = {
            'total': 5,
            'success': 3,
            'failure': 2,
            'results': list(run_tests())
        }
        assert response.status_code == 200
        for key, item in expected_context.items():
            assert response.context[key] == item
