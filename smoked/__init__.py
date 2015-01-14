from .registry import Registry

__version__ = '0.1a'

__all__ = ['default_registry', 'register']

default_registry = Registry()
register = default_registry.register
