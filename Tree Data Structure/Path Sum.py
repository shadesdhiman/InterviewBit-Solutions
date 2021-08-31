# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 12:23:06 2021

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
	# @param B : integer
	# @return an integer
	def hasPathSum(self, A, B):

        def fun(A,B):
            if A==None:
                return 0
            if (A.left == None and A.right == None and A.val == B):
                return 1
            else:
                l = fun(A.left,B-A.val)
                r  = fun(A.right, B-A.val)
                return l or r
        return fun(A,B)



