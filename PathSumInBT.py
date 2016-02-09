"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
For example:
 Given the below binary tree and sum = 22,               5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1


return

[
   [5,4,11,2],
   [5,8,4,5]
]

"""

#=> Data structures used:
#       1. result list: it will store all the paths that have the desired sum.
#       2. parent dict: it will store the information of the parent for each node. It will help in finding the path.
#       3. sumNode dict: for a node, it will store the sum of the path till that node.
#=> Use DFS to traverse all paths in the tree. If a leaf node is found then see whether that path has the sum equal
#   to the desired sum. If it is equla the call addPath function to add that path into result list.

class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    result = []
    parent = {} #{child:parent}
    sumNode = {}    #{node:sum}
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        #feed the whole tree to dfs
        if root==None:
            return []
        self.result = []    #we need to re-initialize the global or class instance variables everytime a new instance
                            #is created so that the information from the last instance is deleted
        self.parent = {}
        self.sumNode = {}
        self.parent[root] = -1
        self.sumNode[root] = root.val
        self.dfs(root,sum)
        return self.result

    def dfs(self,root,sum):
        if root.right==None and root.left==None:
            if self.sumNode[root]==sum:
                print "Path found at",root.val
                self.addPath(root)
            return
        if root.left!=None:
            self.parent[root.left] = root
            self.sumNode[root.left] = self.sumNode[root] + root.left.val
            self.dfs(root.left,sum)
        if root.right!=None:
            self.parent[root.right] = root
            self.sumNode[root.right] = self.sumNode[root] + root.right.val
            self.dfs(root.right,sum)

    def addPath(self,root):
        temp = [root.val]
        while root!=-1:
            if self.parent[root]!=-1:
                temp.append(self.parent[root].val)
            root = self.parent[root]
        temp.reverse()
        self.result.append(temp)