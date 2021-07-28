# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def solve(self, A, B):
        curr = A
        times = 0
        prev_lp= None
        prev = None
        lp = None
        prev_ curr= none
        while(curr):
            if(B + B*times == Curr):
                if times%2 == 0:
                    if prev_lp == None:
                        prev_lp = curr.next
                        node = curr
                        node2  = A
                        node2.next = curr.next
                        curr =  curr.next
                        node.next = A.next 
                        A = node
                        
                    
                    
                    
                    
                    times +=1
                else:
                    continue
                
            prev_curr = curr
            curr = curr.next
                
                
