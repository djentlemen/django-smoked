[![Build Status](https://travis-ci.org/djentlemen/django-smoked.svg)](https://travis-ci.org/djentlemen/django-smoked)
[![Coverage Status](https://coveralls.io/repos/djentlemen/django-smoked/badge.svg?branch=master)](https://coveralls.io/r/djentlemen/django-smoked?branch=master)

# django-smoked

Smoke tests framework for Django Web Framework

## Motivation

> Code without tests is broken by design. - Jacob Kaplan-Moss, Django core developer

Every successful deployment of an application must be followed by series of tests to ensure that website is up and works.

Compared to unit/integration/functional/performance/etc tests which runs in an isolated environment, smoke tests are designed to check safely the production environment. These tests only check the fundemantal functionality, ex. email sending is working, app is able to connect to the database, background queue accepts task, etc.

The goal is to create framework for **reusable** smoke tests which could be easily shared among projects.

## Work in progress

Smoke tests are simple function, which raise exception (ex. `AssertionError`)
on failures:

```python
def url_available(url=None, expected_code=200):
    """ Check availability (HTTP response code) of single resource """
    assert urlopen(url).getcode() == expected_code
```
 
 Smoke tests are registered manually in custom module:

```python
 # settings.py
 SMOKE_TESTS = 'myproject.smoked'
```

```python
 # myproject/smoked.py
 import smoked

 # Built-in test
 from smoked.test.url import url_available
 smoked.register(url_available)

 # ad-hoc function
 def smoke_test():
     ...
 smoked.register(smoke_test, name='Test my setup', description='...')

 # ad-hoc function using decorator
 @smoked.register(name='Verbose name', description='Long text')
 def smoke_test():
     ...

 # default name and description
 @smoked.register
 def smoke_test():  # name='smoke_test'
     """ Docstring will become description """
     ...

```

Test runner is trigger either by management command:

```shell
./manage.py smoked
```

or an API call:

```shell
curl http://myproject.io/_smoked/
```

## Available built-in tests

`smoked.test.url.url_available`

Check response of single URL and compare status code:

Params:
*url* URL to be requested
*code* HTTP status code of response (default: 200)

```python
import smoked
from smoked.test.url import url_available

# Check HTTP 200 response at https://github.com
smoked.register(url_available, params={'url': 'https://github.com'})

# Check HTTP 302 response
smoked.register(url_available, params={'url': 'https://github.com', 'code': 302})
```

## Licence

MIT
