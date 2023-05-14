
class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def find_path(root, sequence):
    return dfs(root,sequence, [], [])

def dfs(node, sequence, curr_path, all_paths):
    if node is None: return False

    curr_path.append(node.val)
    print(all_paths)
    if sequence in all_paths:
        return True

    if node.left is None and node.right is None:
        all_paths.append(list(curr_path))


    else:
        dfs(node.left, sequence, curr_path, all_paths)
        dfs(node.right, sequence, curr_path, all_paths)

    del curr_path[-1]


    

    
def main():

  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)

  print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
  print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


main()
