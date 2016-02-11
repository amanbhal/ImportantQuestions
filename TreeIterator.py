"""
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
"""

#=> make use of the stack and traverse the tree in inorder fashion.

# Definition for a  binary tree node
class TreeNode(object):
 def __init__(self, x):
     self.val = x
     self.left = None
     self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        #initialize the stack and add the root along with all its left elements in the stack.
        self.stack = []
        if root==None:
            return None
        curr = root
        self.stack.append(curr)
        while curr.left!=None:
            self.stack.append(curr.left)
            curr = curr.left

    def hasNext(self):
        """
        :rtype: bool
        """
        if len(self.stack)!=0:
            return True

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            #same as in iterative inorder traversal.
            node = self.stack.pop()
            if node.right!=None:
                self.stack.append(node.right)
                curr = node.right
                while curr.left!=None:
                    self.stack.append(curr.left)
                    curr = curr.left
            return node.val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())