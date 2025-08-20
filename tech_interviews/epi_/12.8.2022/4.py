"""
    in: Array of distinct elements, size value 
    out: Subset of the array with the given size

    Questions: 
        - Does the returning subset need to be ordered in anyway? In order of input array? 
        - Can we use the python's random() method?

    A naive approach would be to use the random() method and append to a new sublist in k (input size) times. 
    I don't know the cost of random() for time complexity but it will take O(n-k) ~ O(n) space.

    A way to reduce space complexity would be to swap position of random elements with the elements at the end of the list and return the sliced list of size k.
    This way, we can reduce to O(1) space.
    
    # Corrections
        - We can use the python random.randint() method. 
        **It is not necessary to swap positions of random element with the end of the list when using a loop (swap position at i with random position).
"""


from random import randint
from typing import List


def func(A: List[int], k: int) -> List[int]:

    for i in range(k):
        r = randint(i, len(A) - 1)
        A[i], A[r] = A[r], A[i]

    return A[:k]


print(func([3, 7, 5, 11], 3))
