# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 10:26:18 2021

@author: Dhiman
"""

class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        count = 0
        for i in range(32):
            if(A&(1<<i)):
                count = count+1
        return count
        
        

        
obj1 = Solution()
A=10
print(obj1.numSetBits(A))
