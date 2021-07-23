# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 00:10:01 2021

@author: Dhiman
"""

class Solution:
    # @param A : list of integers
    # @return A after the sort
    def sortColors(self, A):
        start  = 0
        length = len(A)
        end = length-1
        index = 0
        while(index <= end and start < end ):
            if A[index] == 0:
                A[index] = A[start]
                A[start] = 0
                start = start+1
                index+=1
            elif A[index] == 2:
                
                A[index] = A[end]
                A[end] = 2
                end = end -1
                
            else:
                index+=1
        return A
            


A =[ 0,2,0,1,2,1,1,2]
print(len(A))

obj = Solution()

print(obj.sortColors(A))