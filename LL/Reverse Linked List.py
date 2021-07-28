# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 17:37:39 2021

@author: Dhiman
"""

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class LL:
    def __init__(self):
        self.head = None
    
    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.val)
            temp = temp.next
    def inserting(self,val):
        temp = self.head
   
        while(temp.next!=None):
            temp = temp.next
        node = Node(val)
        temp.next = node






    def reverseList(self):
        prev = None
        current = self.head
        while(current):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
       
            
            
            
            
            
            





if __name__ == '__main__':
    l1 = LL()
    l1.head = Node(1)
    l1.reverseList()
    l1.printlist()
            
            
            