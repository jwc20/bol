from typing import List
from collections import deque
from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_depth_order(head):
    result, curr_depth_nodes = [], deque([head])

    while curr_depth_nodes:
        next_depth_nodes = deque([])
        this_level = []

        while curr_depth_nodes:
            curr = curr_depth_nodes.popleft()
            if curr:
                this_level.append(curr.data)
                next_depth_nodes += [curr.left, curr.right]
                print([curr.left, curr.right])

        if this_level:
            result.append(this_level)

        curr_depth_nodes = next_depth_nodes

    return result


def create_binary_tree():
    # Create all nodes
    # depth 0
    root = BinaryTreeNode(314)

    # depth 1
    root.left = BinaryTreeNode(6)
    root.right = BinaryTreeNode(6)

    # depth 2
    root.left.left = BinaryTreeNode(271)
    root.left.right = BinaryTreeNode(561)
    root.right.left = BinaryTreeNode(2)
    root.right.right = BinaryTreeNode(271)

    # depth 3
    root.left.left.left = BinaryTreeNode(28)
    root.left.left.right = BinaryTreeNode(0)
    root.left.right.right = BinaryTreeNode(3)
    root.right.left.right = BinaryTreeNode(1)
    root.right.right.right = BinaryTreeNode(28)

    # depth 4
    root.left.right.right.left = BinaryTreeNode(17)
    root.right.left.right.left = BinaryTreeNode(401)
    root.right.left.right.right = BinaryTreeNode(257)

    # depth 5
    root.right.left.right.left.left = BinaryTreeNode(641)

    return root


# Helper function to print the tree (for verification)
def print_tree(node, level=0, prefix="Root: "):
    if node is not None:
        print(" " * (level * 2) + prefix + str(node.data))
        if node.left or node.right:
            print_tree(node.left, level + 1, "L--- ")
            print_tree(node.right, level + 1, "R--- ")


# Test the implementation
if __name__ == "__main__":
    tree = create_binary_tree()
    # print_tree(tree)
    # binary_tree_depth_order(tree)
    print(binary_tree_depth_order(tree))

# def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:

#     result: List[List[int]] = []
#     if not tree:
#         return result

#     curr_depth_nodes = [tree]
#     while curr_depth_nodes:
#         result.append([curr.data for curr in curr_depth_nodes])
#         curr_depth_nodes = [
#             child for curr in curr_depth_nodes
#             for child in (curr.left, curr.right) if child
#         ]
#     return result


# def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:

#     result: List[List[int]] = []
#     if not tree:
#         return result

#     curr_depth_nodes = [tree]
#     print("initial ", curr_depth_nodes)
#     while curr_depth_nodes:

#         # result.append([curr.data for curr in curr_depth_nodes])

#         nodes_at_this_depth = []
#         for curr in curr_depth_nodes:
#             nodes_at_this_depth.append(curr.data)
#         result.append(nodes_at_this_depth)

#         # print("nodes ", curr_depth_nodes, "result ", result)

#         # curr_depth_nodes = [
#         #     child for curr in curr_depth_nodes
#         #     for child in (curr.left, curr.right) if child
#         # ]

#         next_depth = []
#         for curr in curr_depth_nodes:
#             for child in (curr.left, curr.right):
#                 if child:
#                     next_depth.append(child)

#         curr_depth_nodes = []  # empty the queue

#         print(next_depth)

#         for node in next_depth:
#             curr_depth_nodes.append(node)

#     return result


# bt = BinaryTreeNode(3)
# bt.left = BinaryTreeNode(9)
# bt.right = BinaryTreeNode(20)

# bt.right.left = BinaryTreeNode(15)
# bt.right.right = BinaryTreeNode(7)
# # bt.left = BinaryTreeNode(2)
# # bt.left.left = BinaryTreeNode(6)
# # bt.left.right = BinaryTreeNode(6)
# # bt.right = BinaryTreeNode(3)
# # bt.right.right = BinaryTreeNode(4)
# # bt.right.left = BinaryTreeNode(5)

# print(binary_tree_depth_order(bt))


# """
# if __name__ == '__main__':
#     exit(
#         generic_test.generic_test_main('tree_level_order.py',
#                                        'tree_level_order.tsv',
#                                        binary_tree_depth_order))
#         """
