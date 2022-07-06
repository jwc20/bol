from typing import Optional


class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

    def display(self):
        printval = self
        lists = []
        while printval is not None:
            lists.append(printval.data)
            printval = printval.next
        print(lists)


def f(L1: Optional[ListNode], L2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = tail = ListNode()

    while L1 and L2:
        if L1.data < L2.data:
            tail.next = L1
            L1 = L1.next
        else:
            tail.next = L2
            L2 = L2.next
        tail = tail.next

    tail.next = L1 or L2
    return dummy.next


a = ListNode(2, ListNode(5, ListNode(7)))
b = ListNode(3, ListNode(11))

a.display()
b.display()

f(a, b).display()
