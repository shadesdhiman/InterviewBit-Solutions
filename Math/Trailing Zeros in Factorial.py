# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 01:37:55 2021

@author: Dhiman
"""

class Solution:
    # @param A : integer
    # @return an integer
    def trailingZeroes(self, A):
        no2 = 0
        no5 = 0
        B= A
        C = A
        while(A>1):
            A= A//2
            no2 = no2 + A
        while(B>1):
            B= B//5
            no5 = no5+ B
        return(min(no2,no5))
        
        
        
            

        













obj1 = Solution()
A=1
print(obj1.trailingZeroes(A))