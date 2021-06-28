# -*- coding: utf-8 -*-
"""
Created on Wed May 26 22:39:12 2021

@author: Dhiman
"""

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        self.A= A
        dict1 = dict(())
        dict1["A"]=1
        dict1["E"]=1
        dict1["I"]=1
        dict1["O"]=1
        dict1["U"]=1
        dict1["a"]=1
        dict1["e"]=1
        dict1["i"]=1
        dict1["o"]=1
        dict1["u"]=1
        sum = 0
        right = 0
        length = len(A)
        for i in range(len(A)):
            if(A[i] in dict1):
                right = length - i - 1
                #print(right)
                sum+= right+1
        return sum
            
        
        
        
        
        
        
        
obj = Solution()
A = " Awefvio"
print(obj.solve( A))