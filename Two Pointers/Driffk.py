# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 22:51:08 2021

@author: Dhiman
"""

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        dic = {}.fromkeys(A,1)
        #print(dic)
        for i in range(len(A)):
            y = A[i]+B
            if y in dic:
                if B == 0:
                    if(A.count(A[i])<2):
                        return 0
                return 1
            
        return 0
    
    
    



A =[1,2,3]
B = 0
obj = Solution()
print(obj.diffPossible(A,B))