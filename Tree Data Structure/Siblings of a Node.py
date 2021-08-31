# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 01:19:01 2021

@author: Dhiman
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
        queue = []
        parent = []
        if A.val == B:
            return []
        queue.append(A)
        parent .append(0)
        while(queue):   
            l = len(queue)
            while(l):
                l = l-1
                ele = queue.pop(0)
                parent.pop(0)
                if ele.left != None:
                    queue.append(ele.left)
                    parent.append(A)
                if ele.right != None:
                    queue.append(ele.right)
                    parent.append(A)
            
            par =-1
            for i in range(len(parent)):
                if (queue[i]).val == B:
                    par = parent[i]
                    break
            if par != -1:
                ans = []
                for x in range(len(parent)):
                    if parent[x]!=par:
                        ans.append((queue[x]).val)
                return ans
                
        

