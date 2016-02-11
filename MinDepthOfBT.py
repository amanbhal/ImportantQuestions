"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
"""

#=> use BFS iterative version and stop at first leaf.


# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

def minDepth(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root==None:
        return 0
    #use BFS iteratively.
    depth = 1
    stack = [root,None]     #use None to indicate that a level of the tree is over
    while len(stack)!=0:
        node = stack.pop(0)
        if node==None:
            depth += 1      #increase depth because an level is over
            stack.append(None)      #add another None because when we reach a None we are sure that all the
                                    #nodes in its lower level are already in the queue therefore we end the next
                                    #level also.
            continue
        if node.left==None and node.right==None:
            return depth
        if node.left!=None:
            stack.append(node.left)
        if node.right!=None:
            stack.append(node.right)
