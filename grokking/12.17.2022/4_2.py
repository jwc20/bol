from typing import List


def func(A: List[int]) -> int:
    """
    Remove duplicates from a sorted array.

    We use two pointers starting from the left side.

    If the items in the left and right pointers are not the same, then
    delete that item and move the left pointer to the right pointer position
    and increment the right pointer.

    If the items are same, then increment the right pointer.
    Finish the loop when the right pointer reaches the end of the array.
    """

    l, r = 0, 1
    count = 1

    while r < len(A):
        if A[l] == A[r]:
            r += 1
        else:
            count += 1
            l = r
            r += 1

    return count


a0 = [2, 3, 3, 3, 6, 9, 9]
a1 = [2, 2, 2, 11]

print(func(a0))
print(func(a1))
