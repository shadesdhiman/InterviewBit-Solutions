# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 09:37:40 2021

@author: Dhiman
"""

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer 
    def solve(self, A, B):
        i= -1
        j = -1
        odd = 0
        count = 0
        while(True):
            #acquire
            i = i+1
            if count<B:
                if A[i]%2!=0:
                    count+=1
            if count==B:
                if j == -1:
                    count += (len(A)-i)
                    j = j+1
                else:
                    if A[j]%2==0:
                        
            
                
                
                
            

        












A = [4, 3, 2, 3, 4]
B = 2
obj = Solution()
print(obj.solve(A,B))