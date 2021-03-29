# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 11:07:54 2021

@author: Dhiman
"""




class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A):
        self.A=A
        l1 = {}
        for i in range(len(A)):
            if( l1.get(A[i])==1):
                return A[i]
            else:
                l1[A[i]] = 1
        
            
        return -1

obj = Solution()
A = [-6, -3, 5, 2, 4, 5]

print(obj.solve(A))