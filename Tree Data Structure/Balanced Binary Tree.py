# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 12:52:57 2021

@author: wwwsh
"""

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @return an integer

    def isBalanced(self, A):
        root = A
        bal= []
        bal.append(0)
        unst = []
        unst.append(1)
        arr =[]
        def fun(root):
            if root == None:
                return 0
   
            if root:
                l = fun(root.left)
                r = fun(root.right)
                bal[0]=abs(l-r)
                
                if bal[0]>=2:
                    unst[0] = 0
                    
                height =  1 + max(l,r)
                return height
            
        height = fun(root)
        return unst[0]
        
        
    

    
