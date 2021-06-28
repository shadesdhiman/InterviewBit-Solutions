# -*- coding: utf-8 -*-
"""
Created on Wed May 26 23:12:43 2021

@author: Dhiman
"""

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def strStr(self, A, B):
        l_a = len(A)
        l_b = len(B)
        def check(i):
            for j in range(l_b):
                #print(A[i+j],B[j])
                if(A[i+j]!=B[j]):
                    return -1
            return i
        for i in range(l_a-l_b+1):
            x = check(i)
            if(x>=0):
                return x

        return -1
            
            
            

        





obj = Solution()
A = "abdfehjkghkdkf"
B = "dfh"
print(obj.strStr(A,B))