"""
Trees

Example and comments for Trees.
"""

# Trees
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
print(root.value, root.left.value, root.right.value)
