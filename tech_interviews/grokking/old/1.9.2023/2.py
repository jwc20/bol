

class Node:
    def __init__(self, value, next=None):
        self.value=value
        self.next = next 

def find_middle_of_linked_list(head: Node) -> Node:
    slow, fast = head, head 
    count = 0
    while fast is not None and fast.next is not None:
        fast = fast.next 
        count += 1
    
    if count % 2 == 0:
        mid = count // 2 
    elif count % 2 != 0:
        mid = ((count // 2 + 1) + (count // 2)) // 2 

    for _ in range(mid):
        slow = slow.next 

    return slow


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)

  print("Middle Node: " + str(find_middle_of_linked_list(head).value))

  head.next.next.next.next.next = Node(6)
  print("Middle Node: " + str(find_middle_of_linked_list(head).value))

  head.next.next.next.next.next.next = Node(7)
  print("Middle Node: " + str(find_middle_of_linked_list(head).value))


main()


