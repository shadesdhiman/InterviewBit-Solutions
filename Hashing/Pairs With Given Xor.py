# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 22:41:33 2021

@author: Dhiman
"""

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        res = 0
        dic = dict()
        for i in A:
            dic[i] = 1
        for i in range(len(A)):
            #print(A[i]^B)
            if A[i]^B in dic:
                res+=1
       # print(res)
        return res//2
    
    
A = [5, 4, 10, 15, 7, 6]
B = 5
obj = Solution()
print(obj.solve(A,B))