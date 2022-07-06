
from typing import Optional

class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next 
    def display(self):
        printval = self 
        lists = []
        while printval is not None:
            lists.append(printval.value)
            printval = printval.next 
        print(lists)


def f(head: Node) -> Optional[Node]:
    def cycle_length(end):
        start, step = end, 0
        while True:
            start = start.next 
            step += 1
            if start is end:
                return step 

    slow = fast = head 
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next 
        if slow is fast:
            pointer = head 
            for _ in range(cycle_length(slow)):
                pointer = pointer.next 
            it = head 
            while it is not pointer:
                it = it.next 
                pointer = pointer.next 

            return it 
    return None 


# a = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
# a.next = a.next.next
# 
# print(f(a))


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

head.next.next.next.next.next.next = head.next.next
print("LinkedList cycle start: " + str(f(head).value))

head.next.next.next.next.next.next = head.next.next.next
print("LinkedList cycle start: " + str(f(head).value))

head.next.next.next.next.next.next = head
print("LinkedList cycle start: " + str(f(head).value))


