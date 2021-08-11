# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 17:41:34 2021

@author: Dhiman
"""

class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        arr = []
        for i in range(len(A)):
            for j in range(len(A[0])):
                arr.append(A[i][j])
        arr.sort()
        return arr
        
            
        
        

        
        
A = [ [1, 2, 3],
      [2, 4, 6],
      [0, 9, 10]
    ]

obj = Solution()
print(obj.solve(A))