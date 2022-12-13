from typing import List


def func(A: List[int], k: int) -> int:
    max_sum = 0
    window_start = 0
    window_sum = 0

    for window_end in range(len(A)):
        window_sum += A[window_end]

        if window_end >= k - 1:
            max_sum = max(max_sum, window_sum)
            window_sum -= A[window_start]
            window_start += 1

    return max_sum


a0 = [2, 1, 5, 1, 3, 2]
k0 = 3


print(func(a0, k0))
