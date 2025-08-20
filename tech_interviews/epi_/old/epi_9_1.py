
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


# level 0
t = BinaryTreeNode(314)

# level 1
t.left = BinaryTreeNode(6)
t.right = BinaryTreeNode(6)

# level 2
t.left.left = BinaryTreeNode(271)
t.left.right = BinaryTreeNode(561)
t.right.left = BinaryTreeNode(2)
t.right.right = BinaryTreeNode(271)

# level 3
t.left.left.left = BinaryTreeNode(28)
t.left.left.right = BinaryTreeNode(0)
t.left.right.right = BinaryTreeNode(3)
t.right.left.right = BinaryTreeNode(1)
t.right.right.right = BinaryTreeNode(28)

# level 4
t.left.right.right.left = BinaryTreeNode(17)
t.right.left.right.left = BinaryTreeNode(401)
t.right.left.right.right = BinaryTreeNode(257)

# level 5
t.right.left.right.left.right = BinaryTreeNode(641)


print(is_balanced_binary_tree(t))

