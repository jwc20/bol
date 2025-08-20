"""

- the first left and right children node values should be the same

- the next generation of children nodes should follow this logic:
    - root.left.right == root.right.left 
    - root.left.left == root.right.right

            

            1 
          2   2
        3 4   4 3
       5   6 6   5

"""


import unittest
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isMirror(root, root)

    def isMirror(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False

        return (
            left.val == right.val and 
            self.isMirror(left.left, right.right) and 
            self.isMirror(left.right, right.left)
        )


## - Test Cases: --------------------------------------------------------------------------------------------
## ----------------------------------------------------------------------------------------------------------
## ----------------------------------------------------------------------------------------------------------
## ----------------------------------------------------------------------------------------------------------
## ----------------------------------------------------------------------------------------------------------



def create_tree_from_list(values: List[int], index: int = 0) -> Optional[TreeNode]:
    if not values or index >= len(values) or values[index] is None:
        return None

    root = TreeNode(values[index])
    root.left = create_tree_from_list(values, 2 * index + 1)
    root.right = create_tree_from_list(values, 2 * index + 2)
    return root


class TestSymmetricTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        """Test case 1: Symmetric tree
                1
               / \
              2   2
             / \ / \
            3  4 4  3
        Expected: True
        """
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(3)
        self.assertTrue(self.solution.isSymmetric(root))

    def test_example2(self):
        """Test case 2: Non-symmetric tree
                1
               / \
              2   2
               \   \
                3   3
        Expected: False
        """
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        root.left.right = TreeNode(3)
        root.right.right = TreeNode(3)
        self.assertFalse(self.solution.isSymmetric(root))

    def test_empty_tree(self):
        """Test case 3: Empty tree
        None
        Expected: True
        """
        self.assertTrue(self.solution.isSymmetric(None))

    def test_single_node(self):
        """Test case 4: Single node tree
             1
        Expected: True
        """
        root = TreeNode(1)
        self.assertTrue(self.solution.isSymmetric(root))

    def test_deep_symmetric_tree(self):
        """Test case 5: Deep symmetric tree
                 1
               /   \
              2     2
             / \   / \
            3   4 4   3
           /           \
          5             5
        Expected: True
        """
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(3)
        root.left.left.left = TreeNode(5)
        root.right.right.right = TreeNode(5)
        self.assertTrue(self.solution.isSymmetric(root))

    def test_different_values(self):
        """Test case 6: Similar structure but different values
                1
               / \
              2   3
             / \ / \
            4  5 5  4
        Expected: False
        """
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(5)
        root.right.right = TreeNode(4)
        self.assertFalse(self.solution.isSymmetric(root))

    def test_unbalanced_tree(self):
        """Test case 7: Unbalanced tree
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
        self.assertTrue(self.solution.isSymmetric(root))

    def test_different_structure(self):
        """Test case 8: Different structure on left and right
                1
               / \
              2   2
             /   / \
            3   4   3
        Expected: False
        """
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        root.left.left = TreeNode(3)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(3)
        self.assertFalse(self.solution.isSymmetric(root))

    def test_negative_values(self):
        """Test case 9: Tree with negative values
                 0
               /   \
             -1    -1
             / \   / \
            2  -2 -2  2
        Expected: True
        """
        root = TreeNode(0)
        root.left = TreeNode(-1)
        root.right = TreeNode(-1)
        root.left.left = TreeNode(2)
        root.left.right = TreeNode(-2)
        root.right.left = TreeNode(-2)
        root.right.right = TreeNode(2)
        self.assertTrue(self.solution.isSymmetric(root))

    def test_large_values(self):
        """Test case 10: Tree with large values
                999999
               /     \
            88888  88888
            /  \   /  \
          777  1 1   777
        Expected: True
        """
        root = TreeNode(999999)
        root.left = TreeNode(88888)
        root.right = TreeNode(88888)
        root.left.left = TreeNode(777)
        root.left.right = TreeNode(1)
        root.right.left = TreeNode(1)
        root.right.right = TreeNode(777)
        self.assertTrue(self.solution.isSymmetric(root))


if __name__ == "__main__":
    unittest.main()
