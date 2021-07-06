# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 15:50:04 2021

@author: Dhiman
"""

class Solution:
    # @param A : integer
        # @return an integer
        def solve(self, A):
            count =0
            def binary(num):
                arr = []
                while(num):
                    arr.append(num%2)
                    num = num//2        
                arr.reverse()  
                print(arr)
                return arr
            
            A = binary(A)
            for i in range(len(A)-1,-1,-1):
                if A[i]== 1:
                    break
                else:
                    count +=1
            return count
        
obj = Solution()
A = 10
print(obj.solve(A))