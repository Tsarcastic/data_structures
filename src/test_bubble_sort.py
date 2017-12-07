"""Test the bubbles."""

import pytest


def test_simple_sort():
    """Derp de derp."""
    from bubble_sort import bubble_sort 
    nums = [100, 20, 10, 1000]
    assert bubble_sort(nums) == [10, 20, 100, 1000]