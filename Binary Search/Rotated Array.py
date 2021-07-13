# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 09:14:19 2021

@author: Dhiman
"""

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def findMin(self, A):
        x = 0
        y=1
        if(len(A)==1):
            return A[0]
        if(len(A)==0):
            return 0
        if(len(A)==2):
            if(A[0]<A[1]):
                return A[0]
            else:
                return A[1]
        while(A[x]<A[y] and  2*y <= len(A)-1):
            x = y
            y = 2*y
        #print(x,y)
        #print("A[x]",A[x])
        #print("A[y]",A[y])
        if(A[x]>=A[y]):
            for i in range(x,y+1):
                if(A[i]<A[i-1]):
                    return A[i]
                
                
        if(2*y>=len(A)-1):
            for i in range(y+1,len(A)):
                #print(A[y])
                if(A[i-1]>A[i]):
                    return A[i]
                
                
                
        return A[0]




obj1 = Solution()
A =  [ 5137, 5525, 9511, 13269, 16255, 16700, 19870, 23034, 29247, 29934,
      34583, 41585, 42598, 44113, 46035, 50147, 50737, 57084, 65916, 76905,
      84098, 85912, 92081, 92257, 95449 ]
print(obj1.findMin(A))