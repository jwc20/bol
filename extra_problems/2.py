



"""
Input: two sorted arrays
Output: one array 

Given two sorted arrays, merge them together into a single, sorted array.

EX: 
    a = [1,2,3]
    b = [2,5,5]
    
    => [1,2,2,3,5,5]

The Naive approach is to merge one list to another and sort it.
This would take O((n+m) log(n+m)) time and O(n + m) space where n and m are the length of the list a and b.

Another brute force approach is to take element from one of the list and compare it with all elements from the other list. And append appropriately from there to an empty list.
This will take O(n*m) time and O(n+m) space.

A better approach is to use Linked List, where we start with a dummy node, check the two lists value, and make the nodes point to increasing order.

Eval:
27 min, had trouble figuring out that I had to convert list to linked list.

"""

from typing import Optional

class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data 
        self.next = next
    def display(self):
        printval = self
        lists = []
        while printval:
            lists.append(printval.data)
            printval = printval.next
        print(lists)
            

# From stackoverflow
def list_2_linked_list(lst):
    cur = dummy = ListNode(0)
    for e in lst:
        cur.next = ListNode(e)
        cur = cur.next
    return dummy.next



def f(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = tail = ListNode()

    a = list_2_linked_list(l1)
    b = list_2_linked_list(l2)
    while a and b:
        if a.data <= b.data:
            tail.next, a = a, a.next 
        else:
            tail.next, b = b, b.next 
        tail = tail.next 

    tail.next = a or b
    return dummy.next 


a = [1,2,3]
b = [2,5,5]
c = [1,5,7,7]
d = [0,1,2,3]


f(a,b).display()
f(c,d).display()

