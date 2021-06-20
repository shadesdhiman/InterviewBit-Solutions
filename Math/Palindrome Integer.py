# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 23:08:25 2021

@author: Dhiman
"""

class Solution:
    # @param A : integer
    # @return an integer
    def isPalindrome(self, A):
        if(A%10==0 and A!=0):
            return 0
        if(A<10 and A>=0):
            return 1
        if(A<0):
            return 0
        rev = 0
        index = 1
        AA = A
        while(AA>rev):
            rev = rev*10+ (A%10)
            #print(rev)
            A= A//10
            
            
        
        if(AA == rev):
            return 1
        else:
            return 0
            
            
        
        
        
        
        
        
        
        
        
        
        

obj1 = Solution()
A= 123
print(obj1.isPalindrome(A))
        
