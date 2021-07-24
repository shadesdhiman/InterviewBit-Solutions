# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 19:52:40 2021

@author: Dhiman
"""

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    def merge(self, A, B):
        len_A = len(A)
        len_B = len(B)
        res = []
        i = 0
        j = 0
        while(i<len_A and j<len_B):
            if(A[i]<B[j]):
                res.append(A[i])
                i +=1
            elif(A[i]>B[j]):
                res.append(B[j])
                j +=1
            else:
                res.append(A[i])
                res.append(B[j])
                i += 1
                j += 1
                
        if i<len_A:
            for x in range(i, len_A):
                res.append(A[x])
        elif j<len_B:
            for x in range(j, len_B):
                res.append(B[x])
                
        return res
                
                
                
                
                
                
                

        








obj = Solution()

A = [-4,-3] 
B = [0,1,5,9]

print(obj.merge(A,B))