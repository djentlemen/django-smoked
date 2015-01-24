# coding: utf-8
from __future__ import unicode_literals

import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

from smoked import __version__

test_requirements = [
    'pytest',
    'pytest-django',
    'pytest-mock',
]

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        sys.exit(pytest.main(self.test_args))

setup(
    name='django-smoked',
    version=__version__,
    license='MIT',

    author='Tomáš Ehrlich',
    author_email='tomas.ehrlich@gmail.com',

    description='Smoke tests framework for Django Web Framework',
    long_description=open('README.md').read(),
    url='https://github.com/djentlemen/django-smoked',

    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'django',
    ],

    cmdclass={'test': PyTest},
    tests_require=test_requirements,
    extras_require={
        'tests': test_requirements,
        'qa': [
            'pytest-cov',
            'coveralls'
        ],
    },

    classifiers=(
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing',
    ),
)
