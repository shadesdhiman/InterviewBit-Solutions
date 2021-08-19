# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 08:51:42 2021

@author: Dhiman
"""

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        sol = []
        l = len(A)
        res = []
        ss = 2**l
        for i in range(ss):
            string = []
            for j in range(l):
                if(i&1<<j > 0):
                    string.append(A[j])
            if string:
                res.append(string)
        
    
        for i in range(len(res)):
            if res[i].count(B) == res[i].count(C):
                sol.append(res[i])
        return res
        








A = [1, 2, 1]
B = 1
C = 2
obj = Solution()
print(obj.solve(A,B,C))