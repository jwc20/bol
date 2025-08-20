"""
assuming this is a singly linked list

1 -> 2 -> 3 -> 4 -> 5 -> X

1 -/> 2 -/> 3 -> 4 -> 5 -> X         remove the pointers pointing at and from 2
1 -/> 2 -/> 3 -/> 4 -/> 5 -> X       remove the pointers pointing at and from 2


- node 1 should now point at node 4 
- node 3 should point at node 2


- node 4 should now point at node 3 
- node 2 should now point at node 5


use a for loop


to get the position to swap, get the length of the linked list.

since we were not given the length we need to iterate through the list and stop at index k in order of the linked list and use another loop in reversed order of the linked list.


we need to keep the surrounding nodes of the node at position k (k-1 and k+1)

"""

import unittest
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head

        for _ in range(k - 1):
            curr = curr.next

        left = curr
        right = head

        while curr.next:
            curr = curr.next
            right = right.next

        left.val, right.val = right.val, left.val

        return head


def create_linked_list(values: List[int]) -> Optional[ListNode]:
    """Helper function to create a linked list from a list of values"""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_array(head: Optional[ListNode]) -> List[int]:
    """Helper function to convert linked list to array for easy comparison"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


class TestSwapNodes(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic_case(self):
        """Test basic case with odd number of nodes"""
        # Input: head = [1,2,3,4,5], k = 2
        # Output: [1,4,3,2,5]
        head = create_linked_list([1, 2, 3, 4, 5])
        result = self.solution.swapNodes(head, 2)
        self.assertEqual(linked_list_to_array(result), [1, 4, 3, 2, 5])

    def test_single_node(self):
        """Test list with single node"""
        # Input: head = [1], k = 1
        # Output: [1]
        head = create_linked_list([1])
        result = self.solution.swapNodes(head, 1)
        self.assertEqual(linked_list_to_array(result), [1])

    def test_two_nodes(self):
        """Test list with two nodes"""
        # Input: head = [1,2], k = 1
        # Output: [2,1]
        head = create_linked_list([1, 2])
        result = self.solution.swapNodes(head, 1)
        self.assertEqual(linked_list_to_array(result), [2, 1])

    def test_same_node(self):
        """Test when k points to middle node (same node from start and end)"""
        # Input: head = [1,2,3], k = 2
        # Output: [1,2,3]
        head = create_linked_list([1, 2, 3])
        result = self.solution.swapNodes(head, 2)
        self.assertEqual(linked_list_to_array(result), [1, 2, 3])

    def test_even_length(self):
        """Test list with even number of nodes"""
        # Input: head = [1,2,3,4,5,6], k = 2
        # Output: [1,5,3,4,2,6]
        head = create_linked_list([1, 2, 3, 4, 5, 6])
        result = self.solution.swapNodes(head, 2)
        self.assertEqual(linked_list_to_array(result), [1, 5, 3, 4, 2, 6])

    def test_first_and_last(self):
        """Test swapping first and last nodes"""
        # Input: head = [1,2,3,4], k = 1
        # Output: [4,2,3,1]
        head = create_linked_list([1, 2, 3, 4])
        result = self.solution.swapNodes(head, 1)
        self.assertEqual(linked_list_to_array(result), [4, 2, 3, 1])

    def test_adjacent_nodes(self):
        """Test swapping adjacent nodes"""
        # Input: head = [1,2,3,4], k = 2
        # Output: [1,3,2,4]
        head = create_linked_list([1, 2, 3, 4])
        result = self.solution.swapNodes(head, 2)
        self.assertEqual(linked_list_to_array(result), [1, 3, 2, 4])


if __name__ == "__main__":
    unittest.main()
