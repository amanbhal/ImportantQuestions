"""
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
"""

#=> If you are given an array, the problem is quite straightforward. But things get a little more complicated
#   when you have a singly linked list instead of an array. Now you no longer have random access to an element
#   in O(1) time. Therefore, you need to create nodes bottom-up, and assign them to its parents. The bottom-up
#   approach enables us to access the list in its order at the same time as creating nodes.

#=> Advice: manually try to do 2-3 iterations of the helper function to understand the code better.

# Definition for singly-linked list.
 class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

# Definition for a binary tree node.
 class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    #pointer to help building the tree in bottom up manner
    h = None
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head==None:
            return None
        #calculate length of the linked list
        self.h = head
        length = 1
        curr = head
        while curr!=None:
            length += 1
            curr = curr.next
        return self.helper(0,length-1)

    #function to build the tree from bottom up manner.
    def helper(self,start,end):
        if start>end or self.h==None:
            return None
        mid = (start+end)/2
        left = self.helper(start,mid-1)
        root = TreeNode(self.h.val)
        self.h = self.h.next
        right = self.helper(mid+1,end)
        root.left = left
        root.right = right
        return root