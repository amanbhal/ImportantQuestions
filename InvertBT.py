"""
Invert a binary tree.

     4
   /   \
  2     7
 / \   / \
1   3 6   9
to
     4
   /   \
  7     2
 / \   / \
9   6 3   1
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def invertTree(root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    if root!=None:
        helper(root)
    return root
def helper(root):
    temp = root.left
    root.left = root.right
    root.right = temp
    if root.left!=None:
        helper(root.left)
    if root.right!=None:
        helper(root.right)