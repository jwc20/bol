from typing import List 
import random

def fun(s:int, A:List[int]) -> List[int]:
    for i in range(s):
        rand_i = random.randint(i, len(A) -1)
        A[i], A[rand_i] = A[rand_i], A[i]

    print(A)
    return A

print(fun(3, [1,2,3,61,5]))
