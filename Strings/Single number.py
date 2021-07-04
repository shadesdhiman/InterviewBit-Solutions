# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 13:56:09 2021

@author: Dhiman
"""


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        dic = dict(())
        for i in range(len(A)):
            if A[i] not in dic:
                dic[A[i]]=1
            else:
                dic[A[i]]+=1
        for i in dic:
            if(dic[i]<2):
                return i

obj = Solution()
A = [1, 2, 2, 3, 1]
print(obj.singleNumber(A))