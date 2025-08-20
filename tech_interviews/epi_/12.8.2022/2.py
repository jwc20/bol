""" 
    dutch national flag problem

    in: list of int and pivot value
    out: list of int 

    [0,1,2,0,2,1,1], p_i = 3 -> [0,0,1,2,2,1,1]
    [0,1,2,0,2,1,1], p_i = 2 -> [0,1,0,1,1,2,2] or [0,0,1,1,1,2,2]


    A naive approach would be to loop through the list and check each elements with the value at pivot index; afterwards, we can append to subarrays if the element is lesser, equal, or greater than the A[p_i]self.
    We can reduce space by using two pointers and swapping position of elements.
    We can use pointers called lesser, equal, and greater where the equal pointer will iterate through the list, check with pivot value, and swap with lesser or greater position depending on the situation.
    
    If lesser than pivot, then swap elements at l and e position and l++, e++
    If equal, then e++
    If greater, then g-- and swap

    [0, 1, 2, 0, 2, 1, 1], p_i = 2 <=> A[p_i] = 2
     ^l,e              ^g   swap
        ^l,e           ^g   swap
           ^l,e        ^g 
           ^l ^e       ^g   swap
    
    [0, 1, 0, 2, 2, 1, 1]
              ^l ^e    ^g 
              ^l    ^e ^g   swap 

    [0, 1, 0, 1, 2, 2, 1]
                 ^l    ^e,g swap

    [0, 1, 0, 1, 1, 2, 2]
"""

from typing import List


def func1(A: List[int], p_i: int) -> List[int]:
    l, e, g = 0, 0, len(A)
    pivot = A[p_i]

    while e < g:
        if A[e] < pivot:
            A[l], A[e] = A[e], A[l]
            l, e = l + 1, e + 1
        elif A[e] == pivot:
            e += 1
        else:  # A[e] is greater than pivot
            g -= 1
            A[g], A[e] = A[e], A[g]

    return A


print(func1([0, 1, 2, 0, 2, 1, 1], 3))
print(func1([0, 1, 2, 0, 2, 1, 1], 2))
