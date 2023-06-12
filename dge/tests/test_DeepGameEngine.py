"""
Unit and regression test for the DeepGameEngine package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import DeepGameEngine


def test_DeepGameEngine_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "DeepGameEngine" in sys.modules
