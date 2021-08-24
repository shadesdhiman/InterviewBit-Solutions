# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 12:13:43 2021

@author: Dhiman
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return the root node in the tree
    def getSuccessor(self, A, B):
        def find(A,B):
            if A:
                if A.val == B:
                    return A
                elif A.val>B:
                    return find(A.left)
                else:
                    return find(A.right)
            else:
                return None
        def findmin(node):
            #case1
        
            node = node.right
            while node.left:
                node = node.left
            return node
            
            
       
        node = find(A,B)
        noddy = node
        if node.right!= None:
            return findmin(noddy)
        else:
            succ  =None
            anc = A
            while(anc != noddy): 
                 
                 if noddy.val < anc.val:
                     succ = anc
                     anc = anc.left
                 else:
                     anc = anc.right
            return succ
                     
                     
 