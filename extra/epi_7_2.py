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


def func(L: ListNode, start: int, finish: int) -> Optional[ListNode]:
    dummy = previous = ListNode(0, L)

    for _ in range(1, start):
        previous = previous.next
    current = previous.next

    for _ in range(finish - start):
        temp = current.next
        current.next, temp.next, previous.next = (temp.next, previous.next, temp)
    

    return dummy.next
    


a = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
ListNode(0, a).display()

func(a, 2, 4).display()
