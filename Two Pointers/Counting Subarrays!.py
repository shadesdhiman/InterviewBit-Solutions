# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 14:04:49 2021

@author: Dhiman
"""

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        count  = 0
        res = []
        len_A = len(A)
        j = 0
        for i in range(len(A)):
            if i == j:
                j = j+1
                temp = A[i]
            while(j<len_A and temp<B):
                temp  = temp + A[j]
                res.append(temp)
                
            if i<j and j<len_A:
                temp = []
                for i in range(i, j+1):
                    temp.append(A[i])
                res.append(temp)
                
        

        return res




A = [2, 5, 6]
B = 10
obj = Solution()

print(obj.solve(A,B))