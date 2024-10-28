# https://leetcode.com/problems/search-in-a-binary-search-tree/description/
# 700. Search in a Binary Search Tree

# Definition for a binary tree node.


from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
         Input: root = [4,2,7,1,3], val = 2
         Output: [2,1,3]


         the naive approach would be to traverse the tree from root to the leaf nodes which will take O(n) where n is the number of nodes in the tree.

         we traverse the tree checking if the target val is equal to the current node and also check if the current node and it's children satisfy the binary tree property.

         the right subtree must be greater than the current node and the left subtree must be smaller than the current node.

        if we find a a child node where the value is equal to the target value. then we get that subtree and insert to an array.

         if the current node is greater or lesser than the target val, than we perform a recursive search.

        """

        if not root:
            return None

        curr_node = root.val

        if curr_node < val:
            # target value is greater, we go traverse to the right child
            return self.searchBST(root.right, val)

        elif curr_node > val:
            return self.searchBST(root.left, val)

        else:
            return root


# tests created by claude
def create_tree(values: List[int]) -> Optional[TreeNode]:
    """Helper function to create a BST from a list of values"""
    if not values:
        return None

    root = TreeNode(values[0])
    for val in values[1:]:
        current = root
        while True:
            if val < current.val:
                if current.left is None:
                    current.left = TreeNode(val)
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = TreeNode(val)
                    break
                current = current.right
    return root


def tree_to_list(root: Optional[TreeNode]) -> List[int]:
    """Helper function to convert tree to list for easy verification"""
    if not root:
        return []

    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


if __name__ == "__main__":
    # Test case 1: [4,2,7,1,3], val = 2
    solution = Solution()

    # Create test tree 1
    test_tree1 = create_tree([4, 2, 7, 1, 3])
    result1 = solution.searchBST(test_tree1, 2)
    print("Test 1 Result:", tree_to_list(result1))  # Expected: [2, 1, 3]

    # Test case 2: [4,2,7,1,3], val = 5
    test_tree2 = create_tree([4, 2, 7, 1, 3])
    result2 = solution.searchBST(test_tree2, 5)
    print("Test 2 Result:", tree_to_list(result2))  # Expected: []

    # Additional test case 3: empty tree
    result3 = solution.searchBST(None, 1)
    print("Test 3 Result:", tree_to_list(result3))  # Expected: []

    # Additional test case 4: search for root value
    test_tree4 = create_tree([4, 2, 7, 1, 3])
    result4 = solution.searchBST(test_tree4, 4)
    print("Test 4 Result:", tree_to_list(result4))  # Expected: [4, 2, 7, 1, 3]
