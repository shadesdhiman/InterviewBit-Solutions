# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 00:39:54 2021

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
    # @return a list of integers
    def solve(self, A):
        queue = []
        queue.append(A)
        ans = []
        while(queue):
            l = len(queue)
            ans.append(queue[0].val)
            while(l):
                l-=1
                ele = queue.pop(0)
                if ele.right!=None:
                    queue.append(ele.right)
                if ele.left!=None:
                    queue.append(ele.left)
        return ans
