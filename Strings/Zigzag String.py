# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 10:32:49 2021

@author: Dhiman
"""

class Solution:
    # @param A : string
    # @param B : integer
    # @return a strings
    def convert(self, A, B):
        arr = []
        down = True
        for i in range(len(A)):
            if down  == True:
                if (i <B) and i<len(A):
                    for j in range(B):
                        arr.append(list(A[i]))
                        print(arr)
                    down = False
            
                else:
                    for j in range(B):
                        arr[i].append(list(A[i]))
                        print(arr)
                    down = False
            
            
            if down == False and i<len(A):
                for j in range(B, 2*B-1):
                    arr[i].append(list(A[i]))
                    print(arr)
                down = True
                
                
        












obj = Solution()
A = "PAYPALISHIRING"
print(len(A))
B = 3                                                                                                                                                                        
print(obj.convert(A,B))