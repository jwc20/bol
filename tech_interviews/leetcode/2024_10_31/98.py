

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right




class Solution:

    def helper(root):


        return 

    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        """
        first, we need to know what a binary search tree is.

        The key property of BST is that the value of nodes in the left subtree must be smaller than the root 
        and every node in the right subtree must be greater than the root.


        so we have the tree:

             5
            / \
           1   4
              / \
             3   6

        we will start at the root of the tree and traverse the binary tree recursively in depth wise (in other words we are fucking using DFS)

        start: root.val = 5
        - at this point we want to check the base case.
        - if the value is not null, then we move on
        - else, return True (this is either the root or a leaf)

        Next, we call a recursive function to check if the left and right subtrees are valid BST.
        - e.g. _left = isValidBST(root.left)



        Now we will have some kind of process to check if the node satisfy the BST property.

        - right subtree is a valid subtree
        - left subtree is a valid subtree
        - the value of the left subtree is lesser than the current node
        - the value of the right subtree is greater than the current node


        
        Im not too sure on what the time and space complexity is.
        But it's probably is linear time and space.


        """

        if not root: return True

        _left = self.isValidBST(root.left)
        _right = self.isValidBST(root.right)

        # to make it easier, we can create a helper function to return boolean value to check the left and right side.
        

        return True

