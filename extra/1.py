from typing import List

def fun(A:List[int]) -> List[int]:
    left = 0
    curr = 1
    right = len(A) -1
    while curr <= right:
        if A[curr] % 2 == 0:
            A[curr] = A[left]
            A[left] = A[curr]
            left += 1
            curr += 1
        # odd
        else:
            curr += 1
    return A



print(fun([2,3,4,5]))
print(fun([1,2,1,4,7]))

