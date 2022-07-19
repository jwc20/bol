from typing import List
import math


def min_subarray_smallest_k(A: List[int], S: int) -> int:

    w_sum, w_start = 0, 0
    min_length = math.inf

    for w_end in range(len(A)):
        w_sum += A[w_end]
        while w_sum >= S:
            min_length = min(min_length, w_end - w_start + 1)
            w_sum -= A[w_start]
            w_start += 1

    return min_length


print(min_subarray_smallest_k([2, 1, 5, 2, 3, 2], 7))
