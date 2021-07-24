# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 07:23:57 2021

@author: Dhiman
"""

class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        length = len(A)
        i = -1
        j = 0
        end = length-1
        while(j<=end-2):
            count = 0
            if (A[j] != A[j+1] or A[j]!=A[j+2]):
                if A[j] != A[j+1]:
                    i = i+1
                    A[i]=A[j]
                    j = j+1
                    check = A[j-1]
                    
                else:
                    i = i+1
                    A[i]=A[j]
                    i = i+1
                    A[i]= A[j+1]
                  
                    j = j+2
                    check = A[j-1]
            else:
                j = j+1
          
        if (j<=end):
            if (A[i]!=A[j]):
                i = i+1
                A[i]= A[j]
                j = j+1
        if (j<=end):
            
                i =i +1
                A[i]= A[j]
                j= j+1
         
        A=A[:i+1]
                    
        return i+1
            
                
            

        









A =[ 0, 0, 0, 1, 1, 2, 2,3]


obj = Solution()

print(obj.removeDuplicates(A))