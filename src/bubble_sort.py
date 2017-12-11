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
    """."""
    for i in range(1, len(nums)):
        cur = nums[i]
        tracker = i

        while tracker > 0 & nums[tracker] < nums[-1]:
            nums[tracker], nums[tracker - 1] = nums[tracker - 1], nums[tracker]
        nums[tracker] = cur
    return nums

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
