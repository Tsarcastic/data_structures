"""Sort with bubbles."""


def bubble_sort(nums):
    """Sort those numbers up."""
    i = 0
    length = len(nums)
    for i in range(length -1):
            for i in range(length - 1):
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
    return nums
