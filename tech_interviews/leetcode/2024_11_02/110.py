

import unittest
from typing import Optional, List
from collections import namedtuple



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        BinaryTree = namedtuple('BinaryTree', ('balanced', 'ht'))

        def dfs(node):
            if not node: return BinaryTree(True, -1)

            left, right = dfs(node.left), dfs(node.right)

            if not left.balanced:
                return BinaryTree(False, 0)

            if not right.balanced:
                return BinaryTree(False, 0)

            is_balanced = abs(left.ht - right.ht) <= 1
            height = max(left.ht, right.ht) + 1

            return BinaryTree(is_balanced, height)

        return dfs(root).balanced


def create_tree_from_list(values: List[int], index: int = 0) -> Optional[TreeNode]:
    if not values or index >= len(values) or values[index] is None:
        return None
    
    root = TreeNode(values[index])
    root.left = create_tree_from_list(values, 2 * index + 1)
    root.right = create_tree_from_list(values, 2 * index + 2)
    return root

class TestBalancedBinaryTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        """
        Test case 1: Balanced tree
           3
          / \
         9  20
            / \
           15  7
        Expected: True
        """
        root = create_tree_from_list([3,9,20,None,None,15,7])
        self.assertTrue(self.solution.isBalanced(root))

    def test_example2(self):
        """
        Test case 2: Unbalanced tree
             1
            / \
           2   2
          / \
         3   3
        / \
       4   4
        Expected: False
        """
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(3)
        root.left.left.left = TreeNode(4)
        root.left.left.right = TreeNode(4)
        self.assertFalse(self.solution.isBalanced(root))

    def test_empty_tree(self):
        """
        Test case 3: Empty tree
        None
        Expected: True
        """
        self.assertTrue(self.solution.isBalanced(None))

    def test_single_node(self):
        """
        Test case 4: Single node
        1
        Expected: True
        """
        root = TreeNode(1)
        self.assertTrue(self.solution.isBalanced(root))

    def test_left_heavy(self):
        """
        Test case 5: Left-heavy unbalanced tree
        1
         \
          2
           \
            3
        Expected: False
        """
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        self.assertFalse(self.solution.isBalanced(root))

    def test_nearly_balanced(self):
        """
        Test case 6: Nearly balanced tree
           1
          / \
         2   2
        /     \
       3       3
        Expected: True
        """
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        root.left.left = TreeNode(3)
        root.right.right = TreeNode(3)
        self.assertTrue(self.solution.isBalanced(root))

    def test_complete_balanced(self):
        """
        Test case 7: Complete balanced tree
              1
            /   \
           2     3
          / \   / \
         4   5 6   7
        Expected: True
        """
        root = create_tree_from_list([1,2,3,4,5,6,7])
        self.assertTrue(self.solution.isBalanced(root))

    def test_zigzag_unbalanced(self):
        """
        Test case 8: Zigzag unbalanced tree
           1
          /
         2
          \
           3
            \
             4
        Expected: False
        """
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.right = TreeNode(3)
        root.left.right.right = TreeNode(4)
        self.assertFalse(self.solution.isBalanced(root))

if __name__ == '__main__':
    unittest.main()
