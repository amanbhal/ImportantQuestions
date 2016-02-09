"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
"""

#=> As it is given that we have to make a height balanced BST therefore the middle element of the array should be
#   the root and elements to left of it will be in left sub-tree and elements to right of it will be in the right
#   sub-tree.

class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


def sortedArrayToBST(nums):
    """
    :type nums: List[int]
    :rtype: TreeNode
    """
    if len(nums)==0:
        return None
    low = 0
    high = len(nums)-1
    mid = low + (high-low)/2
    root = TreeNode(nums[mid])
    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid+1:])
    return root