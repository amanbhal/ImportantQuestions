# coding=utf-8
"""
Given a singly linked list L: L0->L1->…->Ln-1->Ln,
 reorder it to: L0->Ln->L1->Ln-1->L2->Ln-2->…

You must do this in-place without altering the nodes values.

For example,
 Given {1,2,3,4}, reorder it to {1,4,2,3}.

"""

#=> Step1. Find the middle of the whole list using slow pointer and fast pointer method.
#=> Step2. Reverse the second list
#=> Add the second list to the first list
#   example: 1-2-3-4-5-6-7
#            Step1: 1-2-3-4     5-6-7
#            Step2: 1-2-3-4     7-6-5
#            Step3: | | |-------|-|-|
#                   | |---------|-|
#                   |-----------|
#            Result:1-7-2-6-3-5-4

def reorderList(head):
    """
    :type head: ListNode
    :rtype: void Do not return anything, modify head in-place instead.
    """
    if head==None or head.next==None or head.next.next==None:
        pass
    else:
        #find middle of the list using slow and fast pointer approach
        curr = head
        middle = head
        while(curr.next!=None and curr.next.next!=None):
            middle = middle.next
            curr = curr.next.next
        secondHead = middle.next
        middle.next = None
        secondHead = reverseList(secondHead)
        addHere = head
        nex = addHere.next
        addingThis = secondHead
        while addHere!=None and addingThis!=None:
            addHere.next = addingThis
            addingThis = addingThis.next
            addHere.next.next = nex
            addHere = nex
            if addHere!=None:
                nex = addHere.next

def reverseList(head):
    if head==None or head.next==None:
        return head
    curr = head
    next = curr.next
    prev = None
    while curr!=None:
        curr.next = prev
        prev = curr
        curr = next
        if curr!=None:
            next = curr.next
    return prev