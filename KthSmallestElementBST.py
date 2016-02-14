"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 <= k <= BST's total elements.

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently?
How would you optimize the kthSmallest routine?
"""

# Definition for a binary tree node.
class TreeNode(object):
 def __init__(self, x):
     self.val = x
     self.left = None
     self.right = None

def kthSmallest(self, root, k):
    """
    :type root: TreeNode
    :type k: int
    :rtype: int
    """
    if root==None:
        return 0
    global result
    result = 0
    global counter
    counter = 0
    self.inorder(root,k)
    return result

def inorder(self,root,k):
    global counter
    global result
    if root.left!=None:
        self.inorder(root.left,k)
    counter += 1
    if counter==k:
        result = root.val
    if root.right!=None:
        self.inorder(root.right,k)
