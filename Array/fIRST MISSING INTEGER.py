# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 09:44:30 2021

@author: Dhiman
"""

class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        self.A = A
        
        for i in range(len(A)):
            
            min_A = min(A)
            B=A.copy()
            B.sort()
            print("\n",A)
            print(B)
            B.remove(min_A)
            print(B)
            min_A2 = min(B)
            check = min_A+1
            if(check != min_A2):
                if(check >0):    
                    return check
                else:
                    
            
                
                
            
    






A = Solution()
L1 = [3,4,-1,1]

print(A.firstMissingPositive(L1))