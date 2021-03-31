# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 09:45:42 2021

@author: Dhiman
"""

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self,A):
        n= len(A)
        msf = 0
        meh=0
        for i in range(n):
            meh = meh + A[i]
            if(meh<0):
                meh = 0
            elif(meh>msf):
                msf = meh
        return msf
        

obj = Solution()
A = [10,-6, -3, 5, 2, 4, 5,-7]

print(obj.solve(A))