# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 20:30:53 2021

@author: Dhiman
"""


class Solution:
    # @param A : integer
    # @return a strings
    def convertToTitle(self, A):
        l1 = []
        while(A>0):
            temp = A%26
            if(temp ==0):
                A= A-1
                temp = 26
            #print(temp)
            l1.append(chr(temp+64))
            A=A//26
        l1.reverse()
        s = "".join(l1)
        
        return s
        
        
        
            










obj1 = Solution()
A= 943566
print(obj1.convertToTitle(A))