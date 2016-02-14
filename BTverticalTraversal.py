"""
Traverse a binary tree in vertical order. Nodes at same horizontal distance are considered in same vertical traversal.
example:
           1
        /    \
       2      3
      / \    / \
     4   5  6   7
             \   \
              8   9


The output of print this tree vertically will be:
4
2
1 5 6
3 8
7
9
"""

#=> The idea is to traverse the tree once and get the minimum and maximum horizontal distance with respect to root.
#   For the tree shown above, minimum distance is -2 (for node with value 4) and maximum distance is 3 (For node with
#   value 9).
#=> Once we have maximum and minimum distances from root, we iterate for each vertical line at distance minimum to
#   maximum from root, and for each vertical line traverse the tree and print the nodes which lie on that vertical line.

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def verticalTraversal(root):
    if root==None:
        return
    global minDist
    minDist = 0
    global maxDist
    maxDist = 0
    #find the horizontal distances from the root
    findHorizontalDist(root,0)
    #for each horizontal distance print all the nodes at that distance
    for verticalLineNumber in range(minDist,maxDist+1):
        printVerticalTree(root,verticalLineNumber,0)
        print

def findHorizontalDist(root,dist):
    global minDist
    global maxDist
    if root==None:
        return
    if dist<minDist:
        minDist = dist
    if dist>maxDist:
        maxDist = dist
    findHorizontalDist(root.left, dist-1)
    findHorizontalDist(root.right, dist+1)

def printVerticalTree(root,line,dist):
    if dist==line:
        print root.val,
    if root.left!=None:
        printVerticalTree(root.left,line,dist-1)
    if root.right!=None:
        printVerticalTree(root.right,line,dist+1)

root = TreeNode(4)
root.left = TreeNode(2)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right = TreeNode(7)
root.right.left = TreeNode(6)

verticalTraversal(root)