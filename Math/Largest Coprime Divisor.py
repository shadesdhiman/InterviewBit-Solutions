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
            if(x%y==0):
                return y
            if(y%x ==0):
                return x
            if(x==1 or y==1):
                if(x<y):
                    return y
                else:
                    return x
            elif(x>y):
                
                return gcd(y,x-y)
            else:
               
                return gcd(x,y-x)
        
        
        for i in range(1,(A//2)+1):
            if(A%i==0):
                l1.append(i)
        l1.append(A)
        print(l1)
        
        for i in range(len(l1)-1,-1,-1):
            if(gcd(l1[i],B)==1):
                return l1[i]
        
        
        
        
        
        
        
        
        
        
        
        
obj1 = Solution()
A = 26
B = 12
print(obj1.cpFact(A,B))
                