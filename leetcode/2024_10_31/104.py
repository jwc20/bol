import unittest
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        """
        max depth is the height of the tree.

        There are couple ways to approach this problem,
            - recursive, iterative dfs
            - and the bfs approach

        the most clear implementation would be the recursive dfs.

        The recursive dfs would take O(n) Time because at the worst case (degenerative binary tree) we are going to visit every node


        and O(h) Space because every time we make a recursive function call, we create a stack (function call stack).


        The iterative approach would involvce using a stack

        """

        # first we check the base case.
        if not root:
            return 0

        _left = self.maxDepth(root.left)
        _right = self.maxDepth(root.right)

        # now how do we get the depth?
        # >> for each node traveled, we increment by one.

        # afterwards, we get the maximum of the height on left and right subtrees

        height = max(_left, _right) + 1

        return height


class TestMaxDepth(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_tree(self):
        """Test case for empty tree"""
        self.assertEqual(self.solution.maxDepth(None), 0)

    def test_single_node(self):
        """Test case for tree with single node"""
        root = TreeNode(1)
        self.assertEqual(self.solution.maxDepth(root), 1)

    def test_complete_binary_tree(self):
        """Test case for complete binary tree
        Tree structure:
             1
           /   \
          2     3
         / \   / \
        4   5 6   7
        """
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        self.assertEqual(self.solution.maxDepth(root), 3)

    def test_left_skewed_tree(self):
        """Test case for left-skewed tree
          Tree structure:
              1
             /
            2
           /
          3
         /
        4
        """
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(4)
        self.assertEqual(self.solution.maxDepth(root), 4)

    def test_right_skewed_tree(self):
        """Test case for right-skewed tree
        Tree structure:
        1
         \
          2
           \
            3
             \
              4
        """
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        root.right.right.right = TreeNode(4)
        self.assertEqual(self.solution.maxDepth(root), 4)

    def test_unbalanced_tree(self):
        """Test case for unbalanced tree
        Tree structure:
            1
           / \
          2   3
         /     \
        4       5
         \
          6
        """
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.right.right = TreeNode(5)
        root.left.left.right = TreeNode(6)
        self.assertEqual(self.solution.maxDepth(root), 4)


if __name__ == "__main__":
    unittest.main()
