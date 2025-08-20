from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if root is None: return result

        queue = deque()
        queue.append(root)

        level = 1
        while queue:
            curr_level = deque()

            for _ in range(len(queue)):
                curr_node = queue.popleft()

                if level % 2 != 0:
                    curr_level.append(curr_node.val)
                else:
                    curr_level.appendleft(curr_node.val)

                if curr_node.left: queue.append(curr_node.left)
                if curr_node.right: queue.append(curr_node.right)

            level += 1
            result.append(list(curr_level))

        return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    print("Zigzag traversal: " + str(Solution().zigzagLevelOrder(root)))


main()
