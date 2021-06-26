# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 10:44:42 2021

@author: Dhiman
"""

class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        count = 0
        temp = []
        for i in range(32):
            if(A&(1<<i)):
                temp.append(i)
        
        #print(temp)
        
        for i in range(len(temp)):
            count = count + 2**(31-temp[i])
            
        return (count)
            
            
        
        
        
        
        
        
        
        
        
        
        
        
obj1 = Solution()
A=10
print(obj1.reverse(A))
