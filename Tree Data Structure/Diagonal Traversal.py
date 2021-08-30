# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 00:49:26 2021

@author: wwwsh
"""

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, A):
        root = A
        queue = []
        queue.append(root)
        ans = []
        while(queue):
            ele = queue.pop(0)
            while ele:
                if ele.left:
                    queue.append(ele.left)
                ans.append(ele.val)
                ele = ele.right   
        return ans
