# coding: utf-8
from __future__ import unicode_literals

from django.template.response import TemplateResponse
from smoked.runner import run_tests


def smoked_results(request):
    results = list(run_tests())

    total = len(results)
    success = sum(1 for item in results if 'error' not in item)

    ctx = {
        'results': results,
        'total': total,
        'success': success,
        'failure': total - success,
    }

    return TemplateResponse(request, 'smoked/results.html', ctx)
