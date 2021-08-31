# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 15:28:09 2021

@author: wwwsh
"""

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None
"""
class Solution:
	# @param A : root node of tree
	# @return a list of integers
	def preorderTraversal(self, A):
        arr = []
        def preorder(A):
            if A:
                arr.append(A.val)
                preorder(A.left)
                
                preorder(A.right)
        preorder(A)
        return arr
"""
class Solution:
	# @param A : root node of tree
	# @return a list of integers
	def preorderTraversal(self, A):
        arr = []
        root = A
        stack = []
        if root:
            stack.append(root)
        else:
            return []
        while(stack):
            ele = stack.pop()
            arr.append(ele.val)
            if ele.right:
                stack.append(ele.right)
            if ele.left:
                stack.append(ele.left)
            
        return arr