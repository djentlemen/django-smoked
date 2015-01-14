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
