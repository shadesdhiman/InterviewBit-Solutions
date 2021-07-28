# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, A, B):
        curr_A = A
        prev_A = None
        curr_B= B
        
        while(curr_A and  curr_B):
            if curr_A.val <curr_B.val:
                prev_A = curr_A
                curr_A = curr_A.next
            else:
                if prev_A == None:
                    Node = curr_B
                    curr_B = curr_B.next
                    prev_A = Node
                    A=prev_A
                    prev_A.next  = curr_A
                else:
                    Node = curr_B
                    curr_B = curr_B.next
                    prev_A.next = Node
                    Node.next = curr_A
                    prev_A = Node
        
        if curr_B:
           
            prev_A.next = curr_B
        return A
            
               
                
                
