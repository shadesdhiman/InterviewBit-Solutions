# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 23:25:29 2021

@author: Dhiman
"""

class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        i = 0
        j = 1
        length = len(A)
        while(j<length):
            if (A[i] == A[j]):
                j = j+1
            elif(A[i]<A[j]):
                i = i+1
                temp = A[i]
                A[i]=A[j]
                A[j]=temp
                j = j+1
        
        while(length-1 > i):
            A.pop(length-1)
            length = length -1
        
        return length  
                
                
            







A =[ 0,0, 1, 1, 1, 1, 1,2,3,4,4,4,5]
print(len(A))

obj = Solution()

print(obj.removeDuplicates(A))