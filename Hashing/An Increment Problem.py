# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 17:46:13 2021

@author: Dhiman
"""

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        dic = dict()
        for i in range(len(A)):
            print(A[i], dic)
            if A[i] in dic:
                A[dic[A[i]]]+=1
            else:
                dic[A[i]] = i
           
        return A


obj  = Solution()
A =  [ 1, 2, 3, 2, 3, 1, 4, 2, 1, 3 ]
print(obj.solve(A))