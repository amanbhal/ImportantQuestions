"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then
right to left for the next level and alternate between).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""

#=> we can either use two stacks to change the direction of bfs on each level or can use a single stack.

# Definition for a binary tree node.
class TreeNode(object):
 def __init__(self, x):
     self.val = x
     self.left = None
     self.right = None

class Solution(object):
    def zigzagLevelOrderOneQueue(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root==None:
            return []
        result = [[root.val]]
        queue = [root,None]
        leftToRight = False
        prev = root
        while len(queue)!=0:
            node = queue.pop(0)
            if node==None and prev==None:
                break
            if node==None:
                if leftToRight:
                    #print "L-R",queue[:len(queue)]
                    if len(queue)!=0:
                        x = []
                        for i in queue[:len(queue)]:
                            x.append(i.val)
                        result.append(x)
                        leftToRight = False
                else:
                    #print "R-L",queue[::-1]
                    if len(queue)!=0:
                        x = []
                        for i in queue[::-1]:
                            x.append(i.val)
                        result.append(x)
                        leftToRight = True
                queue.append(None)
            else:
                if node.left!=None:
                    queue.append(node.left)
                if node.right!=None:
                    queue.append(node.right)
            prev = node
        return result


    def zigzagLevelOrderTwoStack(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root==None:
            return []
        result = []
        leftToRight = [root]
        rightToLeft = []
        while len(leftToRight)!=0 or len(rightToLeft)!=0:
            x = []
            while len(leftToRight)!=0:
                node = leftToRight.pop()
                x.append(node.val)
                if node.left!=None:
                    rightToLeft.append(node.left)
                if node.right!=None:
                    rightToLeft.append(node.right)
            if len(x)!=0:
                result.append(x)
            x = []
            while len(rightToLeft)!=0:
                node = rightToLeft.pop()
                x.append(node.val)
                if node.right!=None:
                    leftToRight.append(node.right)
                if node.left!=None:
                    leftToRight.append(node.left)
            if len(x)!=0:
                result.append(x)
        return result


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.right = TreeNode(5)
instance = Solution()
print instance.zigzagLevelOrderOneQueue(root)
print instance.zigzagLevelOrderTwoStack(root)