"""
    [1,2,3,4] -> [4,3,2,1]
    
    in: list of int
    out: list of int

    Naive approach would be to start from the end of the list and append to new list using a loop with python's reversed method.
    This will take O(n) time and space.

    A better approach would be to use the same idea but swap elem. position in the list using two pointers.
"""


from typing import List


def func1(A: List[int]) -> List[int]:
    l, r = 0, len(A) - 1
    while l < r:
        A[l], A[r] = A[r], A[l]
        l, r = l + 1, r - 1
    return A


print(func1([1, 2, 3, 4]))
