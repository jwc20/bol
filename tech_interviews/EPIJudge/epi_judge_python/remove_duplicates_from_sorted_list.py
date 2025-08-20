from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def remove_duplicates(L: ListNode) -> Optional[ListNode]:
    return
    # if not L:
    #     return 0
    # write_index = 1 
    # for i in range(1, len(L)):
    #     if L[write_index - 1] != L[i]:
    #         L[write_index] = L[i]
    #         write_index += 1
    # return write_index 

    # left = 0 
    # right = 1 
    # mr = len(L) - 1

    # while left < mr:
    #     if L[left] != L[right]:
    #         left += 1
    #         right += 1
    #     else:
    #         if L[right] == L[mr]:
    #             L[mr] = 0
    #             right -= 1
    #             mr -= 1
    #         L[right] = L[mr]
    #         L[mr] = 0
    #         mr -= 1
    #         right += 1

    # return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'remove_duplicates_from_sorted_list.py',
            'remove_duplicates_from_sorted_list.tsv', remove_duplicates))
