"""Sort with bubbles."""
import timeit
import random


def bubble_sort(nums):
    """Sort those numbers up."""
    i = 0
    length = len(nums)
    for i in range(length - 1):
            for i in range(length - 1):
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
    return nums

    short = [0, 1, 2, 3, 4, 5]
    longer = random.sample(range(1, 10000), 100)


def insertion_sort(nums):
    """Fuck this noise."""
    for i in range(1, len(nums)):
        cur = nums[i]
        tracker = i

        while tracker > 0 & nums[tracker] < nums[tracker - 1]:
            nums[tracker], nums[tracker - 1] = nums[tracker - 1], nums[tracker]
        return nums

def merge_sort(nums):
    """Half and half."""
    if len(nums) == 1:
        return nums
    if len(nums) == 2:
        if nums[1] < nums[0]:
            nums[1], nums[0] = nums[0], nums[1]
    half = len(inp) / 2
    first_half = inp[:half]
    second_half = inp[half:]

    output = []
    left_ct = 0
    right_ct = 0
    while left_ct < len(first_half) & right_ct > len(second_half):
        
    if len(first_half) > 1:
        first_half = merge_sort(first_half)
    if len(second_half) > 1:
        second_half = merge_sort(second_half)
    full = []
    while 









if __name__ == '__main__':
    short = [0, 1, 2, 3, 4, 5]
    longer = random.sample(range(1, 10000), 100)
    print("\nBubblesort is the lead standard of sorting algorithms.\n")
    print("Input: [0, 1, 2, 3, 4, 5]")
    b1 = timeit.timeit("bubble_sort(short[:])",
                       "from __main__ import bubble_sort, short",
                       number=200)
    print("\tBubble Sort --> 200 runs --> average time:{:4e}\n".format(b1 / 200))
    print("Input: [100 random numbers from 1 to 10,000]")
    b2 = timeit.timeit("bubble_sort(longer[:])",
                       "from __main__ import bubble_sort, longer",
                       number=200)
    print("\tBubble Sort --> 200 runs --> average time:{:4e}\n".format(b2 / 200))
