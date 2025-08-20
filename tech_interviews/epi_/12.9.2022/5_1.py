
from typing import List

def func(A: List[int], pivot_index: int) -> List[int]:
    """
        Use three pointers: lesser, equal, and greater. We use the equal pointer to iterate the array and swap places with either the element in 
        lesser or greater pointers when compared to the pivot value. 
        [0,3,1,1] , p_i = 2
        [0,3,1,1]
        []
    """
    
    l, e, g = 0, 0, len(A)
    pivot = A[pivot_index]

    while e < g:
        if A[e] < pivot:
            A[l], A[e] = A[e], A[l]
            l += 1
            e += 1
        elif A[e] == pivot:
            e += 1
        else: # larger than pivot 
            g -=1 
            A[e], A[g] = A[g] , A[e]


    return A

arr = [0,1,2,0,2,1,1]

print(func(arr, 3))
