from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


import collections

class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left 
        self.right = right


def is_balanced_binary_tree(root: BinaryTreeNode) -> bool:
    
    BalancedStatusWithHeight = collections.namedtuple("BalancedStatusWithHeight", ("balanced", "height"))

    def check_balanced(tree):
        if not tree:
            return BalancedStatusWithHeight(balanced=True, height=-1)
        left_result = check_balanced(tree.left)
        right_result = check_balanced(tree.right)

        balanced = abs(left_result.height - right_result.height) <= 1
        height = max(left_result.height, right_result.height) + 1
        return BalancedStatusWithHeight(left_result.balanced and right_result.balanced and balanced, height)


    return check_balanced(root).balanced


# class Node(object):
#   def __init__(self, val, left=None, right=None):
#     self.val = val
#     self.left = left
#     self.right = right
# 
# 
# def _is_balanced_helper(n):
#     if not n:
#       return (True, 0)
# 
#     lBalanced, lHeight = _is_balanced_helper(n.left)
#     rBalanced, rHeight = _is_balanced_helper(n.right)
#     return (lBalanced and rBalanced and abs(lHeight - rHeight) <= 1,
#             max(lHeight, rHeight) + 1)
# 
# def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
#     return _is_balanced_helper(tree)[0]



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
