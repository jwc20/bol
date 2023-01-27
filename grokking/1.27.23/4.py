from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def traverse(root):
    result = []

    if root is None:
        return result

    queue = deque()
    queue.append(root)

    while queue:
        curr_level = len(queue)
        _sum = 0

        for _ in range(curr_level):
            curr_node = queue.popleft()
            _sum += curr_node.val

            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)

        _avg = _sum / curr_level
        result.append(_avg)

    return result


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    print("Level order traversal: " + str(traverse(root)))


main()
