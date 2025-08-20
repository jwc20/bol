
from typing import List 
from random import randint

def func(A:List[int], k: int) -> List[int]:

    """
    We can use a random number generator r (0 <= r < k) to pick a number to swap values within the array.
    We can loop over the array using a for i loop and swap places with element at random number position. 
    [1,2,3,4], r = 3, k = 3
    [4,2,3,1], r = 2
    [4,3,2,1], r = 3 
    [4,3,1]
    """

    for i in range(k):
        r = randint(i, k) 
        A[i], A[r] = A[r], A[i] 

    return A[:k]


print(func([1,2,3,4,5], 3))
print(func([1,2,3,4,5], 4))
