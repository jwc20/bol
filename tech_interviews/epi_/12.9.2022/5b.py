from typing import List


def func0(A: List[int]) -> List[int]:
    """
    in: array of integers
    out: array with even integers first

    [1,2,3,4,5] -> [2,4,1,3,5]

    We can use two pointers(left and right pointers) on each sides of the array and check to see if even.

    [1,2,3,4,5]
    [5,2,3,4,1]
    [4,2,3,5,1]

    If odd, then swap entries on left and right position and decrement right.
    If even, then increment left pointer.
    """
    l, r = 0, len(A) - 1

    while l < r:
        if A[l] % 2 == 0:
            l += 1
        else:
            A[l], A[r] = A[r], A[l]
            r -= 1

    return A


print(func0([1, 2, 3, 4, 5]))
print(func0([1, 2, 3, 1, 3, 7, 7, 5, 4]))
