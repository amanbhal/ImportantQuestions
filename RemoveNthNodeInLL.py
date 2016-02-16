"""
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.
"""

#=> Main idea is to keep one pointer behind the node we want to delete.

# Definition for singly-linked list.
class ListNode(object):
 def __init__(self, x):
     self.val = x
     self.next = None

def removeNthFromEnd(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    #if head is None
    if head==None:
        return None
    #ptr1 is None to handle if n is equal to length of the linked list
    ptr1 = None
    ptr2 = head
    count = 1
    #we need ptr1 to be behind the node we need to remove therefore we use count<n
    while count<n:
        ptr2 = ptr2.next
        count += 1
    #print ptr2.val
    while ptr2!=None and ptr2.next!=None:
        if ptr1==None:
            ptr1 = head
            ptr2 = ptr2.next
        else:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
    if ptr1==None:
        head = head.next
    else:
        ptr1.next = ptr1.next.next
    return head