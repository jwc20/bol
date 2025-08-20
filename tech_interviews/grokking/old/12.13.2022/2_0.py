from typing import List


def func(A: List[float], K: int) -> List[float]:
    """
    Given an array, find the average of each subarray of ‘K’ contiguous elements in it.
    Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5

    We have to set pointers representing the two ends of the sliding window
    that are 4 elements apart.

    After calculating the average, we can append it to another empty array.

    This will take O(n*K) time and O(n) space.

    To not take additional space, we can add the averages to the existing
    input array.

    Since we are moving the sliding window from left to right, we can
    replace the elements from the left with the averages and when the
    loops ends we can slice the array.

    The below code will run O(n*K) time and O(1) space.

    """

    left = 0
    right = 4

    def get_average(start, end):
        summ = 0.0
        for i in range(start, end):
            summ += A[i]
        return summ / K

    while right < len(A):
        if right == len(A) - 1:
            A[left] = get_average(left, left + K)
            return A[: left + 1]
        else:
            A[left] = get_average(left, left + K)
            left += 1
            right += 1

    return A


# Solution
def sol(A: List[float], K: int) -> List[float]:
    result = []
    windowSum, windowStart = 0.0, 0

    for windowEnd in range(len(A)):
        windowSum += A[windowEnd]

        if windowEnd >= K - 1:
            result.append(windowSum / K)
            windowSum -= A[windowStart]
            windowStart += 1

    return result


a0 = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k0 = 5

print("solution: ", sol(a0, k0))
print("my answer: ", func(a0, k0))
