# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 07:28:05 2021

@author: Dhiman
"""

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if(A<0):
            A=-A
        times = 0
        n= 0
        if(A==0):
            return 0

        while(n<A):
            n=n*2

           # print(n)
        if(n==A):
            return times
        if((n-A)%2==0):
            return times
        else:
            times = times+1
            n=n+times
            if((n-A)%2==0):
                return times
            else:
                return times+1
obj1 = Solution()
num = -35
print(obj1.solve(num))            
        