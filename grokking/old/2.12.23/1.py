class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


def reverse_sub_list(head, p, q):
    curr, prev = head, None

    i = 0

    while curr is not None and i < p -1 :
        prev = curr
        curr = curr.next
        i += 1

    prev_sublist_last = prev
    reversed_sublist_last = curr


    i = 0
    
    while curr is not None and i < q - p + 1:
        curr.next, prev, curr = prev, curr, curr.next
        i += 1

    # prev_sublist_last.next = prev
    # if curr.next is not None:
    #     reversed_sublist_last.next = curr
    # else:
    #     reversed_sublist_last.next = None

    if prev_sublist_last is not None:
        prev_sublist_last.next = prev
    else: 
        head = prev

    reversed_sublist_last.next = curr 


    return head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Nodes of original LinkedList are: ", end="")
    head.print_list()
    result = reverse_sub_list(head, 2, 4)
    print("Nodes of reversed LinkedList are: ", end="")
    result.print_list()


main()
