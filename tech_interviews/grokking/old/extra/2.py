


from typing import List


def max_sub_array_of_size_k(k: int, A: List[int]) -> int:
    w_sum, max_sum, w_st = 0,0,0

    for w_end in range(len(A)):
        w_sum += A[w_end]
        if w_end >= k- 1:
            max_sum = max(max_sum, w_sum)
            w_sum -= A[w_st]
            w_st += 1
    return max_sum


print(max_sub_array_of_size_k(3, [2,1,5,1,3,2]))
