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


def f(L: ListNode) -> Optional[ListNode]:

    if L is None:
        return None

    # dummy heads
    even_ptr, odd_ptr = ListNode(0), ListNode(0)

    tails, turn = [even_ptr, odd_ptr], 0

    while L:
        tails[turn].next = L
        L = L.next
        tails[turn] = tails[turn].next
        turn ^= 1

    tails[1].next = None  # last odd node
    tails[0].next = odd_ptr.next  # last even node will point to the first odd node

    return even_ptr.next


a = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

# a.display()
f(a).display()
