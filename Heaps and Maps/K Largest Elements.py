# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 22:48:58 2021

@author: Dhiman
"""

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        import heapq
        heapq.heapify(A)
        return heapq.nlargest(B,A)





A = [11, 3, 4]
B = 2
obj = Solution()
print(obj.solve(A,B))