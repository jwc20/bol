class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_sum_of_path_numbers(root):
    total_sum = 0
    return dfs_travel(root, [], [], total_sum)


def dfs_travel(node, curr_path, all_paths, total_sum):
    if node is None:
        return 0

    curr_path.append(node.val)

    if node.left is None and node.right is None:
        size = len(curr_path)
        curr_sum = 0
        for i in reversed(range(size)):
            curr_sum += curr_path[size - i - 1] * (10**i)

        total_sum += curr_sum
        all_paths.append(list(curr_path))
        # print(all_paths, total_sum)

    else:
        dfs_travel(node.left, curr_path, all_paths, total_sum)
        dfs_travel(node.right, curr_path, all_paths, total_sum)

    del curr_path[-1]
    total_sum += total_sum
    return total_sum


def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))


main()
