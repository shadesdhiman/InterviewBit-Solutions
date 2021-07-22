# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 22:06:53 2021

@author: Dhiman
"""

class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def intersect(self, A, B):
        len_A = len(A)
        len_B = len(B)
        i = 0
        j = 0
        res = []
        while(i< len_A and j< len_B):
            if A[i]==B[j]:
                res.append(A[i])
                i += 1
                j += 1
            elif A[i]<B[j]:
                i = i+1
            elif A[i]>B[j]:
                j+=1
        return res
            

        







A = [1,2, 3, 3, 4, 5, 6]
B = [3, 3, 5]
obj = Solution()

print(obj.intersect(A,B))