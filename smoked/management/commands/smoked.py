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
        verbosity = int(options.get('verbosity', 1))
        start_time = time.time()

        if options.get('dry_run'):
            count = len(default_registry.tests)
            if verbosity:
                self.stdout.write('{0} smoke test(s) could be run'.format(count))
            else:
                self.stdout.write(str(count))
            return

        success = failure = 0
        for result in run_tests():
            positive = 'error' not in result
            if positive:
                success += 1
            else:
                failure += 1

            if verbosity > 1:
                output = 'Success' if positive else 'Fail!'
                self.stdout.write('{0}... {1}'.format(result['name'], output))

                if not positive:
                    self.stdout.write(str(result['error']))
            else:
                output = '.' if positive else 'F'
                self.stdout.write(output, ending='')

        stats = {
            'total': success + failure,
            'success': success,
            'failure': failure,
            'time': time.time() - start_time
        }
        if verbosity:
            self.stdout.write(stats_msg.format(**stats))
        else:
            self.stdout.write('')  # print out new line after dots
