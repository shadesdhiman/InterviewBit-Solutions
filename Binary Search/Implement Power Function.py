# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 13:02:32 2021

@author: Dhiman
"""


class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, x, n, d):
        if(n==0):
            return x%d
        if(x<0):
            return x%d
        while(n):
             n = n//2
             x = x*2
        return x
        
        










obj1 = Solution()
x = 2
n = 3

d = 3
print(obj1.pow(x,n,d))