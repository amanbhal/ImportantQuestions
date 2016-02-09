"""
Given a binary tree, flatten it to a linked list in-place.

For example,
 Given
         1
        / \
       2   5
      / \   \
     3   4   6


The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6

"""

#=> In the flattened tree each node's right child points to the next node of a preorder traversal.

class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

def flatten(root):
    """
    :type root: TreeNode
    :rtype: void Do not return anything, modify root in-place instead.
    """
    stack = []
    p = root
    while p!=None or len(stack)!=0:
        if p.right!=None:
            stack.append(p.right)
        if p.left!=None:
            p.right = p.left
            p.left = None
        elif len(stack)!=0:
            temp = stack.pop()
            p.right = temp
        p = p.right