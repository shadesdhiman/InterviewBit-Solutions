# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 09:10:49 2021

@author: Dhiman
"""

class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArea(self, A):
        maxi = 0
        i = 0
        j  = len(A)-1
        while(i<j):
            #print(i,j)
            temp = min(A[i],A[j])*(j-i)
            if temp > maxi:
                maxi = temp
            if (A[i]<A[j]):
                i = i+1
            elif(A[i]>A[j]):
                j = j-1
            else:
                i = i+1
        return maxi
                
            
            

        










A =[1, 1, 4,6, 3]


obj = Solution()

print(obj.maxArea(A))