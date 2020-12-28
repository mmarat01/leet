# Merge two sorted linked lists and return it as a new sorted list. 
# The new list should be made by splicing together the nodes of the first two lists.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        start = ListNode() # dummy to start, this is our head
        mptr = start # moving pointer reference to our start
        
        while l1 and l2: # while both lists are not None
            if l1.val <= l2.val:
                mptr.next = l1 # our next moving ptr is l1 curr
                l1 = l1.next # move l1 curr
            else:
                mptr.next = l2 # our next moving ptr is l2 curr
                l2 = l2.next # move l2 curr
            mptr = mptr.next # update moving ptr
           
        # still not empty? append rest
        if l1: 
            mptr.next = l1
        elif l2:
            mptr.next = l2
        
        return start.next #returning next because first was dummy
        
# trust me it works
