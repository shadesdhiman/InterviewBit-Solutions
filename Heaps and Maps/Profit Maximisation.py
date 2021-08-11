# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 22:58:57 2021

@author: Dhiman
"""

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        import heapq
        H = []
        heapq.heapify(H)
        for i in range(len(A)):
            heapq.heappush(H, -1 * A[i])
        profit = 0
        for i in range(B):
            x= -1*heapq.heappop(H)
            profit+=x
            x=x-1
            heapq.heappush(H, -x)
        return profit

        











A = [2, 3]
B = 3
obj = Solution()
print(obj.solve(A,B))