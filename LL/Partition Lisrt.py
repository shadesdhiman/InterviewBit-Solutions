# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def partition(self, A, B):
        hs = None
        hg = None
        ts = None
        tg = None
        hsf = False
        hgf = False
        curr = A
        while(curr):
            if curr.val<B:
                if (hsf==False):
                    hs = curr
                    ts = curr
                    hsf = True
                else:
                    ts.next = curr
                    ts = ts.next 
                
            else:
                if(hgf== False):
                    hg = curr
                    tg = curr
                    hgf = True
                else:
                    tg.next = curr
                    tg = tg.next
            
            curr = curr.next
            
        if (hs == None):
            return hg
        if (hg == None):
            return hs
        ts.next = hg
        tg.next = None
        return hs
        