"""Test the bubbles."""

import pytest


def test_simple_sort():
    """Derp de derp."""
    from bubble_sort import bubble_sort
    nums = [100, 20, 10, 1000]
    assert bubble_sort(nums) == [10, 20, 100, 1000]


def test_more_i_guess():
    """Numbers."""
    from bubble_sort import bubble_sort
    nums = [1, 2, 9, 13, 0, 42, -5]
    assert bubble_sort(nums) == [-5, 0, 1, 2, 9, 13, 42]


def test_numbers():
    """More numbers."""
    from bubble_sort import bubble_sort
    nums = [100, 200, 1, 3]
    assert bubble_sort(nums) == [1, 3, 100, 200]

def test_insertion():
    """Insert it."""
    from bubble_sort import insertion_sort
    nums = [100, 20, 10, 1000]
    assert insertion_sort(nums) == [10, 20, 100, 1000]