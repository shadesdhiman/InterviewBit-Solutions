# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def insertionSortList(self, A):
        hs = None
        ts = None
        curr = A
        value = None

        while(curr):
            if value == None:
                value = curr.val
                ts = curr
                hs = ts
                curr = curr.next
                
            elif(curr.val >= value):
                ts.next = curr
                value = curr.val
                ts = ts.next
                curr = curr.next
                
            else:
                head = hs
                
                
                if head.val < curr.val:
                    while(head.val < curr.val):
                        prev = head
                        head = head.next
                    node = curr
                    curr = curr.next
                    prev.next = node
                    node.next = head
                
                    ts.next = curr
                        
                        
                else:
                    node = curr
                    curr = curr.next
                    ts.next = curr
                        
                    node.next = hs
                    hs = node
                    
                        
                    
            
        ts.next = None
        return hs
