"""
Problem Statement
========================================
Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.

Example 1:
========================================
Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].


Solution
========================================
- A naive approach would be to generate all possible combination of sums in the list of size k and is contiguous.
- We need to keep a running max of all the sums and compare it with other element in the list.
- This can be done with 2 loops, but I dont remember why.
=> O(n^2), O(1)
Correction: O(n * k) time


Improved solution
========================================
- A better approach is to use sliding window.
- We can keep a running sum of the elements inside the window and "slide" it by subtract the element that is first in the window and add in the next element in the list.
=> O(n), O(1)
"""

from typing import List


def fun(A: List[int], k: int) -> int:
    window_start, max_sum = 0, 0
    for i in range(len(A) - k + 1):
        window_sum = 0
        for j in range(i, i + k):
            window_sum += A[j]
        max_sum = max(window_sum, max_sum)
    return max_sum


def fun1(A: List[int], k: int) -> int:
    window_start, window_sum, max_sum = 0, 0, 0

    for window_end in range(len(A)):
        window_sum += A[window_end]

        if window_end >= k - 1:
            max_sum, window_sum, window_start = (
                max(window_sum, max_sum),
                window_sum - A[window_start],
                window_start + 1,
            )

    return max_sum


print(fun1([2, 1, 5, 1, 3, 2], 3))
