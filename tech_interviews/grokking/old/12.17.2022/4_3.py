from typing import List


def func(A: List[int]) -> List[int]:

    """
    Given a sorted array, create a new array containing squares
    of all the numbers of the input array in the sorted order.

    A naive approach of this would be to square all element in the array
    and sort it using python's quick sort method.
    This will cost O(n log(n))

    A better approach would be to sort the array by observing the absolute
    values of each items and returning array with squared values.

    We can do this by first setting the pointers from each sides of the array.
    Then we can compare the absolute values of the items from each side.

    If the item on the right is greater or equal, then decrement the right pointer.

    If the item on the left is greater, then swap positions and increment the right side.

    """
    l, r = 0, len(A) - 1

    if all(n < 0 for n in A):
        return [A[i] ** 2 for i in reversed(range(len(A)))]

    while l < r:
        if A[l] == 0 and A[r] == 0:
            l += 1
        elif (A[l] ** 2) > (A[r] ** 2):
            A[l], A[r] = A[r], A[l] ** 2
            r -= 1
        elif (A[l] ** 2) <= (A[r] ** 2):
            A[r] = A[r] ** 2
            r -= 1
    return A


a0 = [-2, -1, 0, 2, 3]
a1 = [-3, -1, 0, 1, 2]


print(func(a0))
print(func(a1))
