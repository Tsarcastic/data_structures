"""Test the bubbles."""

import pytest
import random


def test_simple_sort():
    """Derp de derp."""
    from quick_sort import quick_sort
    nums = [100, 20, 10, 1000]
    assert quick_sort(nums) == [10, 20, 100, 1000]


def test_random_list():
    """Make some random numbers."""
    from quick_sort import quick_sort
    nums = random.sample(range(1, 1000), 20)
    assert quick_sort(nums) == sorted(nums)

def test_random_lists():
    """Make some lists of random numbers."""
    from quick_sort import quick_sort
    for i in range(100):
        nums = random.sample(range(10000), 100)
        assert quick_sort(nums) == sorted(nums)
