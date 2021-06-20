# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 17:26:00 2021

@author: Dhiman
"""

class Solution:
    # @param A : integer
    # @return a list of strings
    def fizzBuzz(self, A):
        l1 = []
        for i in range(1,A):
            if(i%3==0 and i%5==0):
                l1.append("FizzBuzz")
            elif(i%3 ==0):
                l1.append("Fuzz")
            elif(i%5==0):
                l1.append("Buzz")
            else:
                l1.append(i)
        
        return l1
            
obj1 = Solution()
A= 5
print(obj1.fizzBuzz(A))