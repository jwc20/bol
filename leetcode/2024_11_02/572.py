import unittest
from typing import Optional, List


"""

- Check the tree (root) and check if the current node value equals the subRoot value.
    - maybe use bfs here?


- after finding the node value, use recursive dfs to check the node values of the root with the node values with the subRoot 

"""



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        return False





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


class TestSubtree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        """
        Test case 1: Basic subtree example
        Root:     3                SubRoot:     4
                 / \                           / \
                4   5                         1   2
               / \
              1   2
        Expected: True
        """
        root = create_tree_from_list([3, 4, 5, 1, 2])
        subRoot = create_tree_from_list([4, 1, 2])
        self.assertTrue(self.solution.isSubtree(root, subRoot))

    def test_example2(self):
        """
        Test case 2: Similar but not identical subtree
        Root:     3                SubRoot:     4
                 / \                           / \
                4   5                         1   2
               / \                               /
              1   2                            0
                 /
                0
        Expected: False
        """
        root = TreeNode(3)
        root.left = TreeNode(4)
        root.right = TreeNode(5)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(2)
        root.left.right.left = TreeNode(0)

        subRoot = TreeNode(4)
        subRoot.left = TreeNode(1)
        subRoot.right = TreeNode(2)
        subRoot.right.left = TreeNode(0)

        self.assertFalse(self.solution.isSubtree(root, subRoot))

    def test_empty_trees(self):
        """
        Test case 3: Both empty trees
        Root: None    SubRoot: None
        Expected: True
        """
        self.assertTrue(self.solution.isSubtree(None, None))

    def test_empty_subtree(self):
        """
        Test case 4: Empty subtree
        Root:     1        SubRoot: None
                / \
               2   3
        Expected: True
        """
        root = create_tree_from_list([1, 2, 3])
        self.assertTrue(self.solution.isSubtree(root, None))

    def test_empty_root(self):
        """
        Test case 5: Empty root tree
        Root: None    SubRoot:  1
                             /   \
                            2     3
        Expected: False
        """
        subRoot = create_tree_from_list([1, 2, 3])
        self.assertFalse(self.solution.isSubtree(None, subRoot))

    def test_single_node_trees(self):
        """
        Test case 6: Single node trees
        Root: 1    SubRoot: 1
        Expected: True
        """
        root = TreeNode(1)
        subRoot = TreeNode(1)
        self.assertTrue(self.solution.isSubtree(root, subRoot))

    def test_subtree_in_left(self):
        """
        Test case 7: Subtree in left branch
        Root:     5            SubRoot:  3
                / \                     / \
               3   2                   6   7
              / \
             6   7
        Expected: True
        """
        root = TreeNode(5)
        root.left = TreeNode(3)
        root.right = TreeNode(2)
        root.left.left = TreeNode(6)
        root.left.right = TreeNode(7)

        subRoot = TreeNode(3)
        subRoot.left = TreeNode(6)
        subRoot.right = TreeNode(7)

        self.assertTrue(self.solution.isSubtree(root, subRoot))

    def test_subtree_in_right(self):
        """
        Test case 8: Subtree in right branch
        Root:     5            SubRoot:  2
                / \                     / \
               1   2                   6   7
                  / \
                 6   7
        Expected: True
        """
        root = TreeNode(5)
        root.left = TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)

        subRoot = TreeNode(2)
        subRoot.left = TreeNode(6)
        subRoot.right = TreeNode(7)

        self.assertTrue(self.solution.isSubtree(root, subRoot))

    def test_similar_values_different_structure(self):
        """
        Test case 9: Similar values but different structure
        Root:     1            SubRoot:  1
                / \                       \
               1   1                      1
                    \                     /
                     1                   1
        Expected: False
        """
        root = TreeNode(1)
        root.left = TreeNode(1)
        root.right = TreeNode(1)
        root.right.right = TreeNode(1)

        subRoot = TreeNode(1)
        subRoot.right = TreeNode(1)
        subRoot.right.left = TreeNode(1)

        self.assertFalse(self.solution.isSubtree(root, subRoot))

    def test_larger_tree_identical_subtree(self):
        """
        Test case 10: Larger tree with identical subtree
        Root:         10                SubRoot:    4
                    /    \                        /   \
                   4      6                     1     2
                  / \    / \                   /     / \
                 1   2  3   5                 0     7   8
                /    / \
               0    7   8
        Expected: True
        """
        root = TreeNode(10)
        root.left = TreeNode(4)
        root.right = TreeNode(6)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(2)
        root.left.left.left = TreeNode(0)
        root.left.right.left = TreeNode(7)
        root.left.right.right = TreeNode(8)
        root.right.left = TreeNode(3)
        root.right.right = TreeNode(5)

        subRoot = TreeNode(4)
        subRoot.left = TreeNode(1)
        subRoot.right = TreeNode(2)
        subRoot.left.left = TreeNode(0)
        subRoot.right.left = TreeNode(7)
        subRoot.right.right = TreeNode(8)

        self.assertTrue(self.solution.isSubtree(root, subRoot))


if __name__ == "__main__":
    unittest.main()
