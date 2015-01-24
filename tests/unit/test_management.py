# coding: utf-8
from __future__ import unicode_literals

from django.core.management import call_command
from django.utils.six import StringIO

line = lambda s: s + '\n'


def capture_command(*args, **kwargs):
    stdout = StringIO()
    call_command(*args, stdout=stdout, **kwargs)

    stdout.seek(0)
    return stdout.readlines()


def test_verbose_command(filled_registry):
    output = capture_command('smoked')

    assert line('..F.F') in output
    assert line('Total: 5') in output
    assert line('Success: 3') in output
    assert line('Failure: 2') in output


def test_verbose_command_silent(filled_registry):
    output = capture_command('smoked', verbosity=0)

    assert line('..F.F') in output
    assert line('Results') not in output


def test_verbose_command_verbose(filled_registry):
    output = capture_command('smoked', verbosity=2)

    assert line('..F.F') not in output
    assert line('Mocked Test... Success') in output
    assert line('Mocked Test... Fail!') in output


def test_smoked_dry_run(filled_registry, valid_test, invalid_test):
    assert not valid_test.called
    assert not invalid_test.called

    output = capture_command('smoked', dry_run=True)

    assert line('5 smoke test(s) could be run') in output


def test_smoked_dry_run_silent(filled_registry, valid_test, invalid_test):
    assert not valid_test.called
    assert not invalid_test.called

    output = capture_command('smoked', dry_run=True, verbosity=0)

    assert line('5') in output
