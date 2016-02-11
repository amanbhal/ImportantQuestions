"""
Do in-order traversal of the binary tree in iterative way.
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def inorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if root==None:
        return []
    curr = root
    stack = [curr]
    result = []
    while curr.left!=None:
        stack.append(curr.left)
        curr = curr.left
    while len(stack)!=0:
        node = stack.pop()
        result.append(node.val)
        if node.right!=None:
            stack.append(node.right)
            curr = node.right
            while curr.left!=None:
                stack.append(curr.left)
                curr = curr.left
    return result