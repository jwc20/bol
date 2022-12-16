from typing import List


def func(A: List[int], k: int) -> int:
    """
    We don't have to use hashmap.

    Similar to previous problem.
    """

    window_start = 0
    max_length = 0
    most_repeat_ones_count = 0

    for window_end in range(len(A)):
        right_item = A[window_end]
        if right_item == 1:
            most_repeat_ones_count += 1
        # most_repeat_ones_count = max(most_repeat_ones_count, freq_map.ones)

        if (window_end - window_start + 1 - most_repeat_ones_count) > k:
            left_item = A[window_start]
            if left_item == 1:
                most_repeat_ones_count -= 1
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)

    return max_length


a0 = [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1]
k0 = 2
a1 = [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1]
k1 = 3

print(func(a0, k0))
print(func(a1, k1))
