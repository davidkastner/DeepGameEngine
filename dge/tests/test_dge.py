"""
Unit and regression test for the dge package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import dge


def test_dge_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "dge" in sys.modules
