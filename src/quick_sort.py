"""A partition-exchange sort."""
import timeit
import random

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

if __name__ == '__main__':
    short = [0, 1, 2, 3, 4, 5]
    longer = random.sample(range(1, 10000), 100)
    print("\nQuick Sort is a sophisticated divide and conquer sort.\n")
    print("Input: [0, 1, 2, 3, 4, 5]")
    b1 = timeit.timeit("quick_sort(short[:])",
                       "from __main__ import quick_sort, short",
                       number=200)
    print("\tQuick Sort --> 200 runs --> average time:{:4e}\n".format(b1 / 200))
    print("Input: [100 random numbers from 1 to 10,000]")
    b2 = timeit.timeit("quick_sort(longer[:])",
                       "from __main__ import quick_sort, longer",
                       number=200)
    print("\tQuick Sort --> 200 runs --> average time:{:4e}\n".format(b2 / 200))