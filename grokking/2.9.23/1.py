class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left


def find_sum_of_path_numbers(root):
    return dfs(root, 0)


def dfs(node, path_sum):

    if node is None:
        return 0

    path_sum = path_sum * 10 + node.val

    if node.left is None and node.right is None:
        return path_sum

    return dfs(node.left, path_sum) + dfs(node.right, path_sum)


def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))


main()
