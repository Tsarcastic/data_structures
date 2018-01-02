"""Test the bubbles."""

import pytest


def test_simple_sort():
    """Derp de derp."""
    from quick_sort import quick_sort
    nums = [100, 20, 10, 1000]
    assert quick_sort(nums) == [10, 20, 100, 1000]



