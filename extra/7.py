from typing import List

# def fun(A: List[int], pi: int) -> List[int]:
def fun123(p_i: int, A: List[int]) -> List[int]:
    pivot = A[p_i]
    l = 0
    e = 0
    g = len(A) - 1

    while e <= g:
        if A[e] < pivot:
            # A[l] = A[e]
            #A[e] = A[l]
            A[l], A[e] = A[e], A[l]
            l += 1
            e += 1
        elif A[e] > pivot:
            # A[g] = A[e]
            # A[e] = A[g]

            A[g], A[e] = A[e], A[g]
            g -= 1
        else:
            e += 1

    print(A)

    return A


print(fun123(2, [1, 0, 2, 3, 0, 2]))
