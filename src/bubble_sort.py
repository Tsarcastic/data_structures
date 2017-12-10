"""Sort with bubbles."""
import timeit

def bubble_sort(nums):
    """Sort those numbers up."""
    i = 0
    length = len(nums)
    for i in range(length - 1):
            for i in range(length - 1):
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
    return nums

if __name__ == '__main__':
    start_time = timeit.default_timer()
    print(bubble_sort(range(1, 10000, 500)))
    print(timeit.default_timer() - start_time)