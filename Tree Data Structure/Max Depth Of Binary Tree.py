# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 12:15:57 2021

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
	def maxDepth(self, A):

        def fun(A):
            if A == None:
                return 0
            else:
                return 1+max(fun(A.left), fun(A.right))


        return fun(A) 
