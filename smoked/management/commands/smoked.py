# coding: utf-8
from __future__ import absolute_import, unicode_literals
from optparse import make_option

import time
from django.core.management.base import NoArgsCommand
from smoked import default_registry

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
    option_list = NoArgsCommand.option_list + (
        make_option(
            '-n', '--dry-run', dest='dry_run',
            action='store_true', default=False,
            help="Only collect test, don't execute them."),
        )

    def handle_noargs(self, **options):
        start_time = time.time()

        if options.get('dry_run'):
            count = len(default_registry.tests)
            self.stdout.write('{0} smoke test(s) could be run'.format(count))
            return

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
