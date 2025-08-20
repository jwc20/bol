"""
Given the head of a singly linked list, return true if it is a 
palindrome
 or false otherwise.

 

Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false
 

Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9
 

Follow up: Could you do it in O(n) time and O(1) space?
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        Need to check if there is a cycle inside the ll.
        We can do this by assigning a slow and fast pointers.
        The tail needs to point back to head.

        We can also use two pointers, when not using a linked list, 
        and start from both ends.
        """
        s, f = head, head 

        while True:
            s = s.next 
            f = f.next.next 


























