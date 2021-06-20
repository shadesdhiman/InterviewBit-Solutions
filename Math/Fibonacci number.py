# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 01:16:41 2021

@author: Dhiman
"""

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if A==0:
            return 0
        if A ==1:
            return 1
        a=0
        b=1
        while(A>1):
            sum = a+b
            a=b
            b = sum
            A = A-1
        return sum

obj1 = Solution()
A= 50

print(obj1.solve(A))