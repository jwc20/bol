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


def f(l1: ListNode, l2: ListNode) -> Optional[ListNode]:
    def check_len(ll):
        leng = 0
        while ll:
            leng += 1
            ll = ll.next
        return leng

    l1_len, l2_len = check_len(l1), check_len(l2)

    if l1_len > l2_len:
        l1, l2 = l2, l1

    for _ in range(abs(l1_len - l2_len)):
        l2 = l2.next

    while l1 and l2 and l1 is not l2:
        l1, l2 = l1.next, l2.next

    return l1


a = ListNode(1, ListNode(2, ListNode(3, ListNode(5, ListNode(6)))))
b = ListNode(0, ListNode(1, ListNode(2, ListNode(5, ListNode(6)))))
c = ListNode(
    0,
    ListNode(
        1, ListNode(2, ListNode(3, ListNode(4, ListNode(4, ListNode(5, ListNode(6))))))
    ),
)

a.display()
b.display()
c.display()

d = ListNode(4, ListNode(1, ListNode(8, ListNode(4, ListNode(5)))))
e = ListNode(5, ListNode(6, ListNode(1, ListNode(8, ListNode(4, ListNode(5))))))

# f(a, c).display()

f(a,d).display()
