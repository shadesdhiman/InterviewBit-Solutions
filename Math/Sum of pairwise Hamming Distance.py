# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 12:16:19 2021

@author: Dhiman
"""

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def hammingDistance(self, A):
        n = len(A)
        ans  = 0
        for i in range(32):
            count = 0
            for j in range(n):
                if(A[j]&(1<<i)):
                    count = count+1
            ans =ans + (count * (n-count)*2)
        return ans%1000000007
        

        




obj1 = Solution()
A= [2,4,6]
print(obj1.hammingDistance(A))