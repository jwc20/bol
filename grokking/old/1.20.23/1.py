"""
LinkedList Cycle (easy)

Problem Statement
Given the head of a Singly LinkedList, write a function to determine if the LinkedList has a cycle in it or not.



Problem 1: 
Given the head of a LinkedList with a cycle, find the length of the cycle.
"""


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


# def has_cycle(head):
def find_cycle_length(head):
    slow, fast = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            # return True
            return calc_cycle_length(slow)
    return False


def calc_cycle_length(slow):
    curr = slow
    count = 0

    while True:
        curr = curr.next
        count += 1
        if curr == slow:
            # return count
            break
    return count 


# def main():
#     head = Node(1)
#     head.next = Node(2)
#     head.next.next = Node(3)
#     head.next.next.next = Node(4)
#     head.next.next.next.next = Node(5)
#     head.next.next.next.next.next = Node(6)
#     print("LinkedList has cycle: " + str(has_cycle(head)))
#
#     head.next.next.next.next.next.next = head.next.next
#     print("LinkedList has cycle: " + str(has_cycle(head)))
#
#     head.next.next.next.next.next.next = head.next.next.next
#     print("LinkedList has cycle: " + str(has_cycle(head)))
#
#
# main()


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle length: " + str(find_cycle_length(head)))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle length: " + str(find_cycle_length(head)))


main()
