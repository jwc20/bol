from __future__ import print_function


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end="")
            temp = temp.next
        print()


def find_cycle_start(head):
    slow, fast = head, head 

    while fast and fast.next:
        fast = fast.next.next 
        slow = slow.next 

        # There exists a cycle
        if slow == fast:
            cycle_length = get_cycle_length(slow)
            break 

    return get_start_node(cycle_length, head)

def get_cycle_length(slow):
    length = 0  
    curr = slow 
    while True:
        length += 1
        curr = curr.next 
        if curr == slow:
            return length


def get_start_node(cycle_length, head):
    pointer1, pointer2 = head, head

    # move pointer2 ahead 'cycle_length' nodes
    for i in range(cycle_length):
        pointer2 = pointer2.next

    # increment both pointers until they meet at the start of the cycle
    while pointer1 != pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))


main()
