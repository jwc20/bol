
from typing import List

def fun(A: List[int]) -> int:

    if len(A) == 0:
        return 0

    count = 1
    curr = 0
    next = 1
    end = len(A) -1
    while curr < end:
        if A[curr] != A[next]:
            count += 1
            curr += 1
            next += 1
        else:
            A[next] = A[end]
            A[end] = 0
            next += 1
            end -= 1
    print(A)
    return count

l1 = [2,3,5,5,7,11,11,11,13]
print(fun(l1))

l3 = [1,2,3,4]
print(fun(l3))
l2 = [1,1,1,1,1,1,1,3,4, 20]
print(fun(l2))
