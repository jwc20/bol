import unittest
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q:
            return True

        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        else: return False


def create_tree_from_list(values: List[int], index: int = 0) -> Optional[TreeNode]:
    if not values or index >= len(values) or values[index] is None:
        return None

    root = TreeNode(values[index])
    root.left = create_tree_from_list(values, 2 * index + 1)
    root.right = create_tree_from_list(values, 2 * index + 2)
    return root


class TestSameTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        """
        Test case 1: Identical simple trees
            1         1
           / \       / \
          2   3     2   3
        Expected: True
        """
        p = create_tree_from_list([1, 2, 3])
        q = create_tree_from_list([1, 2, 3])
        self.assertTrue(self.solution.isSameTree(p, q))

    def test_example2(self):
        """
        Test case 2: Different values
            1         1
           /           \
          2             2
        Expected: False
        """
        p = TreeNode(1, TreeNode(2), None)
        q = TreeNode(1, None, TreeNode(2))
        self.assertFalse(self.solution.isSameTree(p, q))

    def test_example3(self):
        """
        Test case 3: Different values
            1         1
           / \       / \
          2   1     1   2
        Expected: False
        """
        p = create_tree_from_list([1, 2, 1])
        q = create_tree_from_list([1, 1, 2])
        self.assertFalse(self.solution.isSameTree(p, q))

    def test_empty_trees(self):
        """
        Test case 4: Both empty trees
        None    None
        Expected: True
        """
        self.assertTrue(self.solution.isSameTree(None, None))

    def test_one_empty_one_not(self):
        """
        Test case 5: One empty, one not
        None      1
        Expected: False
        """
        p = None
        q = TreeNode(1)
        self.assertFalse(self.solution.isSameTree(p, q))

    def test_single_nodes_same(self):
        """
        Test case 6: Single nodes with same value
        1        1
        Expected: True
        """
        p = TreeNode(1)
        q = TreeNode(1)
        self.assertTrue(self.solution.isSameTree(p, q))

    def test_single_nodes_different(self):
        """
        Test case 7: Single nodes with different values
        1        2
        Expected: False
        """
        p = TreeNode(1)
        q = TreeNode(2)
        self.assertFalse(self.solution.isSameTree(p, q))

    def test_complex_identical_trees(self):
        """
        Test case 8: Complex identical trees
            5         5
           / \       / \
          3   7     3   7
         / \       / \
        1   4     1   4
        Expected: True
        """
        p = create_tree_from_list([5, 3, 7, 1, 4])
        q = create_tree_from_list([5, 3, 7, 1, 4])
        self.assertTrue(self.solution.isSameTree(p, q))

    def test_same_values_different_structure(self):
        """
        Test case 9: Same values but different structure
            1           1
           / \         /
          2   3       2
                       \
                        3
        Expected: False
        """
        p = create_tree_from_list([1, 2, 3])
        q = TreeNode(1)
        q.left = TreeNode(2)
        q.left.right = TreeNode(3)
        self.assertFalse(self.solution.isSameTree(p, q))

    def test_deep_trees_different_at_bottom(self):
        """
        Test case 10: Deep trees, different at bottom
                1                1
               / \              / \
              2   3            2   3
             /     \          /     \
            4       5        4       6
        Expected: False
        """
        p = TreeNode(1)
        p.left = TreeNode(2)
        p.right = TreeNode(3)
        p.left.left = TreeNode(4)
        p.right.right = TreeNode(5)

        q = TreeNode(1)
        q.left = TreeNode(2)
        q.right = TreeNode(3)
        q.left.left = TreeNode(4)
        q.right.right = TreeNode(6)  # Different value here

        self.assertFalse(self.solution.isSameTree(p, q))


if __name__ == "__main__":
    unittest.main()
