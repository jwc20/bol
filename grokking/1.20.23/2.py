"""
Start of LinkedList Cycle (medium)

Problem Statement
Given the head of a Singly LinkedList that contains a cycle, write a function to find the starting node of the cycle.
"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def find_cycle_start(head):
    slow, fast = head, head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if slow == fast:
            cycle_length = find_cycle_length(slow)
            break
    return find_start_of_cycle(head, cycle_length)


def find_cycle_length(slow):
    curr, count = slow, 0

    while True:
        curr = curr.next
        count += 1
        if curr == slow:
            break

    return count


def find_start_of_cycle(head, cycle_length):
    ptr1, ptr2 = head, head

    for _ in range(cycle_length):
        ptr2 = ptr2.next

    # while ptr1 and ptr1.next:
    while True:
        if ptr1 == ptr2:
            break
        ptr1, ptr2 = ptr1.next, ptr2.next

    return ptr1


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
