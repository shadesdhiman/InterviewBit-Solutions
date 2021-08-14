# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 13:21:29 2021

@author: Dhiman
"""

# Definition for singly-linked list with a random pointer.
class RandomListNode:
     def __init__(self, x):
         self.label = x
         self.next = None
         self.random = None



class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        h = head
        new_head = RandomListNode(h.label)
        nh = new_head
        dic = dict()
        while(h.next):
            dic[h] = nh
            h = h.next
            nh.next = RandomListNode(h.label)
            nh = nh.next
        
    
        h = head
        nh  = new_head
        
        while(h):
            if h.random:
                nh.random = dic[h.random]
            h = h.next
            nh = nh.next
        return new_head