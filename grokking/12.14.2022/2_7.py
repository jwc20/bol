from typing import List
from collections import defaultdict


def func(A: List[int], k: int) -> int:

    window_start = 0
    max_length = 0
    max_freq_count = 0
    freq_map = defaultdict(set)

    for window_end in range(len(A)):
        right_item = A[window_end]
        if right_item not in freq_map:
            freq_map[right_item] = 0
        freq_map[right_item] += 1

        max_freq_count = max(max_freq_count, freq_map[right_item])

        if (window_end - window_start + 1 - max_freq_count) > k:
            left_item = A[window_start]
            freq_map[left_item] -= 1
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)
    return max_length


a0 = [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1]
k0 = 2
print(func(a0, k0))

a1 = [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1]
k1 = 3
print(func(a1, k1))
