

from typing import List 

"""
We need to return an array of primes from 1 to input n.

We can do this by iterating a number from 1-n and have conditionals 
to check to see if prime. 

A Naive approach would be to use the O(n(n-1) / 2) time method where 
we would take one element from the left and check to see if every subsequent
elements are divisible.

n=13
[2,3,4,5,6,7,8,9,10,11,12,13]
[2,3,0,5,0,7,0,9,0,11,0,13]

[2,3,0,5,7,0,0,0,11,0,13]

[2,3,5,7,11,13]

this will take O(n^2) time and O(n) space.

An approach to use only one loop will require a method to check prime numbers.
Then this will take O(n) time and space.

"""



def func(n: int) -> List[int]:

    return 


