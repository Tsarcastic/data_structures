"""A partition-exchange sort."""


def quick_sort(nums):
    """Standard quick sort."""
    the_length = len(nums)
    if the_length == 1:
        return nums
    elif the_length == 2:
        if nums[1] < nums[0]:
            nums[0], nums[1] = nums[1], nums[0]
        return nums
    else:
        low_list = []
        high_list = []
        final_list = []
        piv_low = nums[0]
        piv_high = nums[-1]
        piv_avg = (piv_low + piv_high) / 2
        for item in nums:
            if item <= piv_avg:
                low_list.append(item)
            else:
                high_list.append(item)
        low_list = quick_sort(low_list)
        for item in low_list:
            final_list.append(item)
        high_list = quick_sort(high_list)
        for item in high_list:
            final_list.append(item)
        return final_list
