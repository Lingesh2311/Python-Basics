# Basic Context Manager Framework
from contextlib import contextmanager


@contextmanager
def simple_context_manager(obj):
    try:
        # do something
        obj.some_property += 1
        yield
    finally:
        # wrap up
        obj.some_property -= 1
