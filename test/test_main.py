import pytest
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import app.main as app

def test_equal():
    # Test for small integers with the same identity (cached by Python)
    a = 10
    b = 10
    assert app.equal(a, b)  # `is` works because of Python's integer caching for small values.

    # Test for two distinct integers
    assert not app.equal(1, 2)

    # Test for same object
    c = 42
    assert app.equal(c, c)  # An object always `is` itself.

