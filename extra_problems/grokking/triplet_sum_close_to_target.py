import math


def triplet_sum_close_to_target(arr, target_sum):
    arr.sort()
    smallest_difference = math.inf
    for i in range(len(arr) - 2):
        left = i + 1
        right = len(arr) - 1
        while left < right:
            target_diff = target_sum - arr[i] - arr[left] - arr[right]
            if target_diff == 0:
                return target_sum

            if abs(target_diff) < abs(smallest_difference):
                smallest_difference = target_diff

            if target_diff > 0:
                left += 1
            else:
                right -= 1

    return target_sum - smallest_difference
