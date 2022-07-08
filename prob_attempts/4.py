from typing import List
import random

def fun(A:List[int], s:int) -> List[int]:
    for i in range(0, len(A) - s):
        r = random.randint(0, s)
        # print(i, r, A[r])
        del A[r]

    return A


print(fun([1,2,3,4], 2))
print(fun([3,7,5,11], 3))
print(fun([3,1,2,3,4,6,1,6,8,1,3,4,8,2,23,1,1,23,7,5,11], 3))
print(fun([1,2,3,4,5,6,7,8,9,10,11,12,13,14], 5))
