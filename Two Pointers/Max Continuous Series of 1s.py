# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 11:34:00 2021

@author: Dhiman
"""

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def maxone(self, A, B):
    
        j = -1
        count = 0
        ans = 0
        for i in range(len(A)):
            if (A[i]==0):
                count +=1
            while (count > B):
                j = j+1
                if(A[j]==0):
                    count = count -1
            temp = i-j
            if ans < temp:
                ans = temp
                new_start = j
                new_end = i
        return list(i for i in range(new_start+1, new_end+1))
            
        





        












A = [ 1,0,0,0, 1, 1, 1, 0, 0, 1, 1, 0,1]
M = 2
obj = Solution()

print(obj.maxone(A,M))