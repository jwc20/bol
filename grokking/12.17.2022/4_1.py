from typing import List


def func(A: List[int], target_sum: int) -> List[int]:
    """
    Given an array of sorted numbers and a target sum,
    find a pair in the array whose sum is equal to the given target.

    """

    l, r = 0, len(A) - 1
    result = []

    while l < r:
        curr_sum = A[l] + A[r]
        if curr_sum - target_sum > 0:
            r -= 1
        elif curr_sum - target_sum < 0:
            l += 1
        elif curr_sum - target_sum == 0:
            return [A[l], A[r]]
        else:
            return []


print(func([1, 2, 3, 4, 5], 9))  # => [4,5]
print(func([1, 2, 3, 4, 5], 5))  # => [1,5]
