# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 16:25:06 2021

@author: Dhiman
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 15:37:11 2021

@author: Dhiman
"""

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def cpFact(self, A, B):
        
        l1 = []
        
        def gcd(x,y):
            while(y):
                x, y = y, x % y
  
            return x
        
        
        while(gcd(A,B)!=1):
            A = A//gcd(A,B)
        return A
        
        
        
        
        
        
        
        
        
        
        
        
obj1 = Solution()
A = 100
B = 26
print(obj1.cpFact(A,B))
                