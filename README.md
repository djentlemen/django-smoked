[![Build Status](https://travis-ci.org/djentlemen/django-smoked.svg)](https://travis-ci.org/djentlemen/django-smoked)

# django-smoked

Smoke tests framework for Django Web Framework

## Motivation

> Code without tests is broken by design. - Jacob Kaplan-Moss, Django core developer

Every successful deployment of an application must be followed by series of tests to ensure that website is up and works.

Compared to unit/integration/functional/performance/etc tests which runs in an isolated environment, smoke tests are designed to check safely the production environment. These tests only check the fundemantal functionality, ex. email sending is working, app is able to connect to the database, background queue accepts task, etc.

## Idea

Create framework for **reusable** smoke tests which could be easily shared among projects.

Each test is defined by a name and an action to be taken:

```python
class DatabaseTest(SmokeTest):
    name = 'Database test'
    description = 'Check all database connection are valid'

    def test(self):
        ...
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
 smoked.register('smoked.DatabaseTest')

 # Custom test
 smoked.register('myproject.MessageQueueTest')

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
curl -d"TOKEN=VerySecretToken" http://myproject.io/_smoked/
```

## Licence

MIT
