from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_successor(root, key):

    if root is None:
        return 0

    queue= deque() 
    queue.append(root)

    while queue:
        curr_level = []
        for _ in range(len(queue)):
            curr_node = queue.popleft() 
            curr_level.append(curr_node.val)

            if curr_node.left: queue.append(curr_node.left)
            if curr_node.right: queue.append(curr_node.right)

            if curr_node.val == key:
                return queue.popleft()




def main():
  root = TreeNode(1);
  root.left = TreeNode(2);
  root.right = TreeNode(3);
  root.left.left = TreeNode(4);
  root.left.right = TreeNode(5);
  
  result = find_successor(root, 3)
  if result:
    print(result.val)

  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  
  result = find_successor(root, 9)
  if result:
    print(result.val)
  
  result = find_successor(root, 12)
  if result:
    print(result.val)


main()
