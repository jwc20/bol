import unittest
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return None

        _left = self.invertTree(root.left)
        _right = self.invertTree(root.right)

        root.right = _left
        root.left = _right

        return root
