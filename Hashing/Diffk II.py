# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 12:35:22 2021

@author: Dhiman
"""

class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return an integer
    def diffPossible(self, A, B):
        dic= dict()
        for i in range(len(A)):
            if A[i] in dic:
                pass
            else:
                dic[A[i]] = i
        
        for i in range(len(A)):
            temp = A[i]-B
            if temp in dic and dic[temp]!=i:
                return 1
            
        return 0
            

        
        










A = [ 25, 19, 92, 71, 82, 35, 71, 65, 91, 45, 64, 47, 11, 68, 85, 3, 28, 21, 94, 73, 8, 78, 54, 53, 31, 94, 20, 68, 26, 42 ]
B = 11
obj = Solution()
print(obj.diffPossible(A,B))