# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 12:27:27 2021

@author: wwwsh
"""

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        ans= []
        
        def fun(root, B):
            if root == None:
                return False
            if root.val == B:
                ans.insert(0,root.val)
                return True
            if fun(root.left, B):
                ans.insert(0, root.val)
                return True
            if fun(root.right, B):
                ans.insert(0, root.val)
                return True
        fun(A, B)
        return ans