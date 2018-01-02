"""A partition-exchange sort."""
import timeit
import random


def merge_sort(nums):
    """A comparison based sorting algorithm."""
    the_length = len(nums)
    left_list = []
    right_list = []
    final_list = []
    if the_length == 1:
        return nums
    i = 0
    for item in nums:
        if i < round(the_length / 2):
            left_list.append(item)
            i += 1
        else:
            right_list.append(item)

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)

    while left_list and right_list:
        if left_list[0] <= right_list[0]:
            final_list.append(left_list[0])
            left_list = left_list[1:]
        else:
            final_list.append(right_list[0])
            right_list = right_list[1:]

    while left_list:
        final_list.append(left_list[0])
        left_list = left_list[1:]

    while right_list:
        final_list.append(right_list[0])
        right_list = right_list[1:]

    return final_list


if __name__ == '__main__':
    short = [0, 1, 2, 3, 4, 5]
    longer = random.sample(range(1, 10000), 100)
    print("\nMerge Sort is a sophisticated divide and conquer sort.\n")
    print("Input: [0, 1, 2, 3, 4, 5]")
    b1 = timeit.timeit("merge_sort(short[:])",
                       "from __main__ import merge_sort, short",
                       number=200)
    print("\tMerge Sort --> 200 runs --> average time:{:4e}\n".format(b1 / 200))
    print("Input: [100 random numbers from 1 to 10,000]")
    b2 = timeit.timeit("merge_sort(longer[:])",
                       "from __main__ import merge_sort, longer",
                       number=200)
    print("\tMerge Sort --> 200 runs --> average time:{:4e}\n".format(b2 / 200))