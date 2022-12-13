
import math
from typing import List 

def func(A:List[int], S: int) -> int:


    """
    Find the length of smallest contiguous subarray
    whose sum is greater than or equal to ‘S’

    Input: [2, 1, 5, 2, 3, 2], S=7 
    Output: 2

    We can use the sliding window to check each element from left to right
    Take one element and add all the subsequent elements.
    If the sum is greater, then shrink and move the window. 
        We can have the smallest size of the window and compare it.
    If the sum is lesser, then move the window end to the next element.
    """

    # min_length = float('inf')
    min_length = math.inf
    windowStart = 0 
    windowSum = 0

    for windowEnd in range(0,len(A)):
        windowSum += A[windowEnd]

        while windowSum >= S:
            min_length = min(min_length, windowEnd - windowStart + 1)
            windowSum -= A[windowStart]
            windowStart += 1

    if min_length == math.inf:
        return 0

    return min_length


print(func([2,1,5,2,3,2], 7))
