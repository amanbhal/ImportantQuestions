"""
Convert Binary Tree to Doubly Linked List in inorder fashion.
"""

class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def btToDLL(root):
    if root==None:
        return None
    global linkedListHead
    linkedListHead = None
    global prev
    prev = None
    helper(root)
    return linkedListHead

def helper(root):
    global linkedListHead
    global prev
    if root==None:
        return
    helper(root.left)
    if prev==None:
        linkedListHead = root
    else:
        root.left = prev
        prev.right = root
    prev = root
    helper(root.right)

#testing
root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.right = Node(9)
head = btToDLL(root)

curr = head
while curr!=None:
    print curr.val
    curr = curr.right