# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 19:45:27 2021

@author: Dhiman
"""

class Solution:
    # @param A : integer
    # @return a list of list of integers
    def solve(self, A):
        l1 = []
        for i in range(A):
            l1.append([])
        for i in range(A):
            for j in range(i+1):
                if(j<i):
                    if(j==0):
                        l1[i].append(1)
                    else:
                        l1[i].append(l1[i-1][j]+l1[i-1][j-1])
                
                    
                
                elif(i==j):
                    l1[i].append(1)
        print(l1)
        
        

obj1 = Solution()
x=5
obj1.solve(x)