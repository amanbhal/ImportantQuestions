"""
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

For example:
Given the following binary tree,
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
You should return [1, 3, 4].
"""

#=> This can be done by level order traversal. Whenever we hit the end of one level we print the value of
#   previous node visited, because in each level only one node can be seen from the right side and that will
#   be the last node of that level.


# Definition for a binary tree node.
class TreeNode(object):
 def __init__(self, x):
     self.val = x
     self.left = None
     self.right = None

def rightSideView(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if root==None:
        return []
    result = []
    queue = [root,None]
    prev = root
    while len(queue)!=0:
        node = queue.pop(0)
        if prev==None and node==None:
            break
        if node==None:
            result.append(prev.val)
            queue.append(None)
            prev = None
            continue
        if node.left!=None:
            queue.append(node.left)
        if node.right!=None:
            queue.append(node.right)
        prev = node
    return result

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

list = rightSideView(root)
print list