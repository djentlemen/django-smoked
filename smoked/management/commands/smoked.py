# coding: utf-8
from __future__ import absolute_import, unicode_literals

import time
from django.core.management.base import NoArgsCommand

from smoked.runner import run_tests

stats_msg = """
Results
=======
Total: {total}
Success: {success}
Failure: {failure}
--------
Time: {time}
"""


class Command(NoArgsCommand):
    def handle_noargs(self, **options):
        start_time = time.time()

        success = failure = 0
        for result in run_tests():
            if 'error' in result:
                failure += 1
                output = 'F'
            else:
                success += 1
                output = '.'

            self.stdout.write(output, ending='')

        stats = {
            'total': success + failure,
            'success': success,
            'failure': failure,
            'time': time.time() - start_time
        }
        self.stdout.write(stats_msg.format(**stats))
