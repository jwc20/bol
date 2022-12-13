"""
Problem Statement
=================================
Given an array of positive integers and a number ‘S,’ find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. 
Return 0 if no such subarray exists.

Example 1:
=================================
Input: [2, 1, 5, 2, 3, 2], S=7
Output: 2
Explanation: The smallest subarray with a sum greater than or equal to ‘7’ is [5, 2].


Solution
=================================
- Need to keep a running length of smallest subarray.
- Naive approach would involve two loops => O(n^2)

- We can use sliding window technique and check with the input s.
- if the window sum is equal or greater than s, then we can move onto the next window start.

- Edge case involves an empty list or list with one element.


Evaluation
=================================
- Could not remember to use window_end - window_start + 1, instead tried to use count and tried to increment for each step.
"""

from typing import List
import math


def f(A: List[int], s: int) -> int:
    window_sum, window_start, min_length = 0, 0, math.inf
    for window_end in range(len(A)):
        window_sum += A[window_end]
        while window_sum >= s:
            min_length = min(min_length, window_end - window_start + 1)
            window_sum, window_start = window_sum - A[window_start], window_start + 1

    if min_length == math.inf:
        return 0

    return min_length


print(f([2, 1, 5, 2, 3, 2], 7))
