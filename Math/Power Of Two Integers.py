# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 01:58:19 2021

@author: Dhiman
"""


class Solution:
    # @param A : integer
    # @return an integer
    def isPower(self, A):
        import math
        
        for i in range(2,int(math.sqrt(A))+1):
            
            p = int(int(math.log2(A))//int(math.log2(i)))
            if(math.pow(i, p)==A):
                 return 1
        return 0
                
obj1 = Solution()
A= 10
print(obj1.isPower(A))