from typing import List


def remove_element(A: List[int], k: int) -> int:
    l, r, count = 0, len(A) - 1, 0
    while l < r:
        if A[l] == k:
            A[l], A[r] = A[r], A[l]
            r -= 1
        else:
            count, l = count + 1, l + 1
    return count


arr = [3, 2, 3, 6, 3, 10, 9, 3]
key = 3
arr1 = [2, 11, 2, 2, 1]
key1 = 2


print(remove_element(arr, key))
print(remove_element(arr1, key1))
