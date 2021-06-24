# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 05:38:34 2021

@author: Dhiman
"""

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        dis = 0
        #\ below d
        if(A>=B):   
            dis = dis+(8-A)+B-1
        else:
            dis = dis +(8-B)+A-1
        if(A+B)<=9:
            #/ above d
            dis = dis +(A+B)-2
        else:
            #/ bellow d
            dis= dis+(8-A)
            dis= dis+(8-B)
            
        return dis
        
obj1 = Solution()
A=7
B=5
print(obj1.solve(A,B))