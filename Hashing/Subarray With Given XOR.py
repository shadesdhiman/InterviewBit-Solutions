# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 18:30:51 2021

@author: Dhiman
"""

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        xor = 0
        count = 0
        dic = dict()
        for i in range(len(A)):
            xor = xor^A[i]
            if xor in dic:
                dic[xor]+=1
            else:
                dic[xor] = 1
            if xor == B:
                count +=1
            else:
                y = B^xor
                if y in dic:
                    count+=dic[y]
        return count
                
                
            
        









obj  = Solution()
A =  [ 4,2,2,6,4 ]
B = 6
print(obj.solve(A,B))