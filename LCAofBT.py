"""
Given a binary tree, find the lowest common ancestor LCA of two given nodes in the tree.

According to the definition of LCA on wikipedia: The lowest common ancestor is defined between two nodes v and
w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3. Another example is LCA of nodes 5 and 4 is 5,
since a node can be a descendant of itself according to the LCA definition.
"""

#=> Use DFS to find the path from root to first node and second node.
#=> Use path information to find the first common node.



# Definition for a binary tree node.
class TreeNode(object):
 def __init__(self, x):
     self.val = x
     self.left = None
     self.right = None

def lowestCommonAncestor(root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    global parent
    parent = {root:-1}     #{node:parent}
    #use dfs to fill parent dictionary
    dfs(root,p)
    dfs(root,q)
    #mark the path of node p from root in parentP array.
    parentP = [p]
    node = p
    while node!=-1:
        node = parent[node]
        parentP.append(node)
    #mark the path of node q from root in parentQ dictionary. We use dictionary to find LCA in O(1) time.
    parentQ = {q:0}
    node = q
    index = 0
    while node!=-1:
        node = parent[node]
        index += 1
        parentQ[node] = index
    #finding the lowest common ancestor
    for node in parentP:
        if node in parentQ.keys():
            return node

def dfs(self,root,node):
    if root==node:
        return
    if root.left!=None:
        parent[root.left] = root
        self.dfs(root.left,node)
    if root.right!=None:
        parent[root.right] = root
        self.dfs(root.right,node)