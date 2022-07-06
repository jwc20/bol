


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



def func(L: ListNode, s: int, f: int) -> Optional[ListNode]:
    # start = s 
    # end = f 

    # count = 0
    # while L and count <= s:
    #     count += 1
    #     L.next 

    # previous = L 
    # current = L.next 
    # print(previous, current)
    # 
    # while start < end:
    #     current.next, previous, current = previous, current, current.next 
    #     start += 1

    # return previous

    current, previous = L, None

    count = 0
    while L and count < s-1:
        previous, current.next = current, previous
        count += 1

    
    while s < f:
        current.next, previous, current = previous, current, current.next 
        s += 1

    return previous

a = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

# func(a, 1, 2).display()
ListNode(0, a).display()
