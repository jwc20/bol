import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Returns the number of valid entries after deletion.
def delete_duplicates(A: List[int]) -> int:

    if not A:
        return 0

    x = 1
    for i in range(len(A) - 1):
        if A[i] != A[i+1]:
            A[x] = A[i+1]
            x+=1
    return x

    # count = 1
    # c = 0
    # n = 1
    # r = len(A) -1 
    # while c < r:
    #     print(A)
    #     if A[c] != A[n]:
    #         count += 1
    #         c += 1
    #         n = c+1
    #     else:
    #         if A[n] == A[r]:
    #             A[n] = 0
    #             A[r] = 0
    #             r -=1
    #             n +=1
    #         A[n] = A[r]
    #         A[r] = 0
    #         r -=1
    #         n+=1
    # return count


    # left = 0
    # right = 1
    # mr = len(A) - 1
    # count = 0

    # while left < mr:
    #     if A[left] != A[right]:
    #         left += 1
    #         right += 1
    #     else:
    #         if A[right] == A[mr]:
    #             count += 1
    #             A[mr] = 0
    #             right -= 1
    #             mr -= 1
    #         else:
    #             count += 1
    #             A[right] = A[mr]
    #             A[mr] = 0
    #             mr -= 1
    #             right += 1

    # return count

    # if not A:
    #     return 0

    # write_index = 1
    # for i in range(1, len(A)):
    #     print(
    #         "i: ",
    #         i,
    #         ", wi: ",
    #         write_index,
    #         ", A[write_index - 1]: ",
    #         A[write_index - 1],
    #         ", A[i]: ",
    #         A[i],

    #     )
    #     if A[write_index - 1] != A[i]:
    #         A[write_index] = A[i]
    #         write_index += 1
    # return write_index


print(delete_duplicates([2, 3, 5, 5, 7, 11, 11, 11, 13]))


@enable_executor_hook
def delete_duplicates_wrapper(executor, A):
    idx = executor.run(functools.partial(delete_duplicates, A))
    return A[:idx]


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "sorted_array_remove_dups.py",
            "sorted_array_remove_dups.tsv",
            delete_duplicates_wrapper,
        )
    )
