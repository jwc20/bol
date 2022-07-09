from typing import List


class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:

    result: List[List[int]] = []
    if not tree:
        return result

    curr_depth_nodes = [tree]
    print("initial ", curr_depth_nodes)
    while curr_depth_nodes:

        # result.append([curr.data for curr in curr_depth_nodes])

        nodes_at_this_depth = []
        for curr in curr_depth_nodes:
            nodes_at_this_depth.append(curr.data)
        result.append(nodes_at_this_depth)

        # print("nodes ", curr_depth_nodes, "result ", result)

        # curr_depth_nodes = [
        #     child for curr in curr_depth_nodes
        #     for child in (curr.left, curr.right) if child
        # ]

        next_depth = []
        for curr in curr_depth_nodes:
            for child in (curr.left, curr.right):
                if child:
                    next_depth.append(child)

        curr_depth_nodes = []  # empty the queue

        print(next_depth)

        for node in next_depth:
            curr_depth_nodes.append(node)

    return result


bt = BinaryTreeNode(3)
bt.left = BinaryTreeNode(9)
bt.right = BinaryTreeNode(20)

bt.right.left = BinaryTreeNode(15)
bt.right.right = BinaryTreeNode(7)
# bt.left = BinaryTreeNode(2)
# bt.left.left = BinaryTreeNode(6)
# bt.left.right = BinaryTreeNode(6)
# bt.right = BinaryTreeNode(3)
# bt.right.right = BinaryTreeNode(4)
# bt.right.left = BinaryTreeNode(5)

print(binary_tree_depth_order(bt))
