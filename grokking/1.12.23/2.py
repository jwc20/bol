"""
Reverse a Sub-list (medium)
Given the head of a LinkedList and two positions ‘p’ and ‘q’, 
reverse the LinkedList from position ‘p’ to ‘q
"""
# 1->2->3->4->5->None
# prev->1->2->3->4->5->None
# prev->1->2->3->4->5->None
# 1<-2->3->4->5->None
# 1<-2<-3->4->5->None
# 1<-2<-3<-4->5->None


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

    # edge case
    if p == q:
        return head

    # reach node at position p - 1
    while curr and i < p - 1:
        prev = curr
        curr = curr.next
        # prev, curr = curr, curr.next
        i += 1

    # remember the node at position p - 1 to be used later to connect with the reversed sublist
    last_node_of_first_part = prev
    last_node_of_sub_list = curr

    i = 0
    # reverse sublist between p and q
    while curr and i < q - p + 1:
        curr.next, prev, curr = prev, curr, curr.next
        i += 1

    # connect with the first part
    if last_node_of_first_part is not None:
        # prev is now the first node of the sublist
        last_node_of_first_part.next = prev
    # change the first node (head) of the LinkedList
    else:
        head = prev

    last_node_of_sub_list.next = curr

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
