# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 09:23:03 2021

@author: Dhiman
"""

class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return a list of integers
    def twoSum(self, A, B):
        dic = dict(())
        
        
        for i in range(len(A)):
            temp = B - A[i]
            
            if temp in dic:
                return [dic[temp]+1, i+1]
                
            
            if A[i] not in dic:
                dic[A[i]] = i
                
 
        
    
    
A = [ 4, 7, -4, 2, 2, 2, 3, -5, -3, 9, -4, 9, -7, 7, -1, 9, 9, 4, 1, -4, -2, 3, -3, -5, 4, -7, 7, 9, -4, 4, -8 ]
B = -3
obj = Solution()
print(obj.twoSum(A,B))