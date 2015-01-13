import os.path
import sys


def pytest_configure(config):
    sys.path.insert(0, os.path.dirname(__file__))
