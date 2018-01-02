"""A partition-exchange sort."""

def quick_sort(nums):
    """Standard quick sort."""
    the_length = len(nums)
    low_list = []
    high_list = []
    if the_length == 1:
        return nums
    elif the_length == 2:
        if nums[1] < nums[0]:
            nums[0], nums[1] = nums[1], nums[0]
        return nums
    elif the_length == 3:
        pass
    else:
