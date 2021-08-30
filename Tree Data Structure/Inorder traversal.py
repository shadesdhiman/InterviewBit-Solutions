# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 14:53:19 2021

@author: wwwsh
"""

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

"""class Solution:
	# @param A : root node of tree
	# @return a list of integers
	def inorderTraversal(self, A):
        arr = []
        if A:
            def inorder(root):
                if root:
                    inorder(root.left)
                    arr.append(root.val)
                    inorder(root.right)
            inorder(A)
            return arr

"""
class Solution:
	# @param A : root node of tree
	# @return a list of integers
	def inorderTraversal(self, root):
        arr = []
        notdone= True
        stack = []
        while(notdone):
            if root:
                stack.append(root)
                root = root.left
            elif stack :
                ele = stack.pop()
                arr.append(ele.val)
                root =ele.right
            else:
                notdone = False
        return arr
        

