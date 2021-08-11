# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 08:48:31 2021

@author: Dhiman
"""

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):
        import heapq
        arr = []
        H = []
        heapq.heapify(H)
        min = -1
        
        A.sort(reverse = True)
        B.sort(reverse = True)
        
        for i in A:
            for j in B:
                
                temp = i+j
                if H:
                    heapq.heappush(H,temp)
                else:
                    heapq.heappush(H,temp)
                    
        arr.sort(reverse = True)                
        return arr[:C]
                
        




A = [1, 4, 2, 3]
B = [2, 5, 1, 6]
C = 4


obj = Solution()
print(obj.solve(A,B,C))