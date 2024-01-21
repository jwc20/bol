

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def get_sum(self, root):
        result = 0
        self.dfs(root, result, [])
        return result

    def dfs(self, node, summ, nums):
        nums.append(node.val)

        if node.left is None and node.right is None:
            summ += int(" ".join(nums))

        else:
            self.dfs(node.left, summ - nums.pop(), nums.pop())
            self.dfs(node.right, summ - nums.pop(), nums.pop())





