from typing import List


def func(A: List[int]) -> List[int]:
    """
    in: [1,2,9]
    out: [1,3,0]

    Need to increment a number in array form.

    Integers 0-8 are simple, just +1 to the last element of the array.

    We can reverse loop through the array and check to see if the element
    is a 9 or something else.

    When we reach the last digit that is a 9, then we need to
    append a 1 to the array.

    9, 2, 1
    0, 3, 1

    - check to see if element is 9
        - if true, set the element to 0 and move to next element.
        - else, add 1 and return
    """
    A[-1] += 1

    for i in range(len(A) - 1, 0, -1):
        # print(A[i])
        if A[i] == 10:
            A[i] = 0
            A[i - 1] += 1
        # else:
        #     A[i] += 1

    if A[0] == 10:
        A[0] = 1
        A.append(0)

    return A


print(func([1, 2, 9]))
print(func([1, 9, 9]))
print(func([9, 9, 9]))
