

from typing import List

"""

- sorted array 
- return same size array
- remove duplicates

This could be a sliding window problem where we would have two pointers,
left and right pointers of the window.

If the right side matches the left side, then we delete that element 
and move the right pointer.

If the elements are different, then move the left pointer to the 
right pointer position.

The problem i have now is shifting the elements in the array.
Empty elements to the right and elements with value to left (sorted).


[2,3,5,5,7,11,11,11,13]
     ^ ^  
[2,3,5,0,7,11,11,11,13]
     ^   ^
         ^ ^
           ^  ^
[2,3,5,0,7,11, 0,11,13]
            ^     ^
[2,3,5,0,7,11, 0, 0,13]
           ^         ^

Want:[2,3,5,7,11,13,0,0,0]

The naive approach to return this sorted would be to use another loop 
and two pointers to swap places.

But there could be a way to use one loop.

We could use two pointers to reprensent the ends of sliding window and 
another pointer that is at the end of the array. 

We can use a similar method above but also check to see if the right side 
of the window is greater than the left.

## Corrections
DID NOT READ THE PROBLEMS CORRECTLY 
We only need to return the number of valid entries
We can do this by having a count for every duplicates.

"""

def func(A:List[int]) -> int:
    l = 0 
    r = 1 
    end = len(A) - 1

#    while l < end:
#        if A[l] == A[r]: 
#            A[r] = 0
#            end -= 1
#        else:
#            if A[l] > A[r]:
#                A[l], A[r] = A[r], A[l] 
#                r += 1
#
#            l += 1
#
    valid = 1
    while r < len(A):
        if A[l] == A[r]:
            A[r] = 0
            r += 1
        else:
            valid += 1
            l = r
            r += 1
    
    # l = 0
    # while l < end:
    #     if A[l] == 0:
    #         A[l]
    return valid


print(func([2,3,5,5,7,11,11,11,13]))
