# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        h = None
        head = None
        if A == None:
            return None
        if A.next == None:
            return A
        while(A):
            temp = A.val
            
            if A.next!=None and A.next.val == temp:
                while(A and A.val == temp):
                    A = A.next
            else:
                if head == None:
                    head = A
                    A=A.next
                    h = head
                    h.next = None
                    head.next = None
                    
                else:
                    head.next =A
                    A=A.next
                    head = head.next
                    head.next = None
        return h
            