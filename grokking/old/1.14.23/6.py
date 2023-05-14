"""
1. Check if it contains a cycle 
2. If the ll contains a cycle, then calculate the length 
3. After getting the length, set two pointers to head of the ll and skip one of the pointers by the length.
4. After skipping, iterate both pointers. The start of cycle is identified when both pointers meet.

"""


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

        if slow == fast:
            cycle_length = get_cycle_length(slow)
            break

    return find_start_node(cycle_length, head)


def get_cycle_length(slow):
    curr = slow
    count = 0
    while True:
        curr = curr.next
        count += 1
        if curr == slow:
            break
    return count


def find_start_node(l, head):
    pointer1, pointer2 = head, head
    for _ in range(l):
        pointer1 = pointer1.next

    while pointer1 != pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next

    return pointer2


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
