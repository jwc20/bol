import unittest
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
We can use multipl approach to solve this problem.

The optimal approach would be to use a recursive DFS 
and keep count of the diameter of the binary tree.

We can do this by having a global state to keep count.

- To get the diameter, we need get the distance of the left most and right most nodes.

        1
       / \
      2   3
     / \
    4   5

- we start at 1 at traverse the left and keep traversing the
left subtree until we reach the left-most leaf
    - as we are traversing, we update the count and increment each time we 
    traverse to a node

- for example the path from node 1 to node 4 is 2.

- Afterwards, traverse to the right-most leaf node.
- (end when we reach node.right = null)
- count the number of nodes traversed.

> the path from node 1 to node 3 is 1

- as we are using dfs to traverse to count variable will be 3.

- The time complexity, at the worst case, will be linear since we are 
traversing every node.

- the space complexity will be O(h) where h is the height 
    - for this problem it will be O(n) space for non-balanced binary tree 
    and O(log n) if its a balanced binary tree.

"""


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0

        def dfs(node):
            nonlocal result
            if not node:
                return 0

            left_path = dfs(node.left)
            right_path = dfs(node.right)

            result = max(result, left_path + right_path)

            return max(left_path, right_path) + 1

        dfs(root)
        return result


##-----------------------------------------------------------------
##-----------------------------------------------------------------
##-----------------------------------------------------------------
##-----------------------------------------------------------------
##-----------------------------------------------------------------


def create_tree_from_list(values: List[int], index: int = 0) -> Optional[TreeNode]:
    """Helper function to create a binary tree from a list representation"""
    if not values or index >= len(values) or values[index] is None:
        return None

    root = TreeNode(values[index])
    root.left = create_tree_from_list(values, 2 * index + 1)
    root.right = create_tree_from_list(values, 2 * index + 2)
    return root


class TestBinaryTreeDiameter(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        """Test case from Example 1: [1,2,3,4,5]"""
        root = create_tree_from_list([1, 2, 3, 4, 5])
        self.assertEqual(self.solution.diameterOfBinaryTree(root), 3)

    def test_example2(self):
        """Test case from Example 2: [1,2]"""
        root = create_tree_from_list([1, 2])
        self.assertEqual(self.solution.diameterOfBinaryTree(root), 1)

    def test_empty_tree(self):
        """Test case with empty tree"""
        self.assertEqual(self.solution.diameterOfBinaryTree(None), 0)

    def test_single_node(self):
        """Test case with single node"""
        root = TreeNode(1)
        self.assertEqual(self.solution.diameterOfBinaryTree(root), 0)

    def test_left_heavy_tree(self):
        """Test case with left-heavy tree: [1,2,None,3,None,4]"""
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(4)
        self.assertEqual(self.solution.diameterOfBinaryTree(root), 3)

    def test_right_heavy_tree(self):
        """Test case with right-heavy tree: [1,None,2,None,3,None,4]"""
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        root.right.right.right = TreeNode(4)
        self.assertEqual(self.solution.diameterOfBinaryTree(root), 3)

    def test_balanced_complete_tree(self):
        """Test case with balanced complete tree: [1,2,3,4,5,6,7]"""
        root = create_tree_from_list([1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(self.solution.diameterOfBinaryTree(root), 4)

    def test_zigzag_path(self):
        """Test case with zigzag path: [1,2,3,None,4,5,None,None,6]"""
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right.left = TreeNode(5)
        root.left.right.right = TreeNode(6)
        self.assertEqual(self.solution.diameterOfBinaryTree(root), 5)


if __name__ == "__main__":
    unittest.main()
