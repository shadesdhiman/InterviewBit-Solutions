# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 18:34:31 2021

@author: Dhiman
"""

class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):

        temp1 = 0
        
        for i in range(len(A)):
            if(i<len(A)-1):    
                temp = ord(A[i])-64
                temp = temp * (26**(len(A)-1-i))
                temp1 = temp1+temp
                #print(temp)
            else:
                temp1 = temp1 +ord(A[i])-64
        return temp1
                
                
                
                
        
        
        
        
        
        
obj1 = Solution()
A= "AZ"
print(obj1.titleToNumber(A))