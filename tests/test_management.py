# coding: utf-8
from __future__ import unicode_literals

from django.core.management import call_command
from django.utils.six import StringIO
from smoked import register

line = lambda s: s + '\n'


def test_verbose_command(valid_test, invalid_test):
    # Generate test suit
    register(valid_test)
    register(valid_test)
    register(invalid_test)
    register(valid_test)
    register(invalid_test)

    stdout = StringIO()
    call_command('smoked', stdout=stdout)

    stdout.seek(0)
    output = stdout.readlines()

    assert line('..F.F') in output
    assert line('Total: 5') in output
    assert line('Success: 3') in output
    assert line('Failure: 2') in output


def test_smoked_dry_run(valid_test, invalid_test):
    assert not valid_test.called
    assert not invalid_test.called

    # Generate test suit
    register(valid_test)
    register(valid_test)
    register(invalid_test)
    register(valid_test)
    register(invalid_test)

    stdout = StringIO()
    call_command('smoked', dry_run=True, stdout=stdout)

    stdout.seek(0)
    output = stdout.readlines()

    assert not valid_test.called
    assert not invalid_test.called
    assert line('5 smoke test(s) could be run') in output
