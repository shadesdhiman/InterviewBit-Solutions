# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 18:37:19 2021

@author: Dhiman
"""
class Solution:
    # @param A : integer
    # @return a strings
    def findDigitsInBinary(self, A):
        self.A =A
        val1 =0
        temp = 1
        x = 0
        while(A!=0):
            x=A%2
            val = x*temp
            val1 = val1+val
            temp = temp*10
            A = A//2

    
        return val1


obj1 = Solution()
A= 10
print(obj1.findDigitsInBinary(A))