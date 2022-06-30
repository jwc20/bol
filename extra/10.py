from typing import List 

def fun(A:List[int]) -> List[int]:
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] == 10:
            A[i] = 0
            A[i-1] += 1
    if A[0] == 10:
        A[0] = 1
        A.append(0)

    return A

print(fun([9,9,9,9]))
print(fun([9,9,9,0]))
