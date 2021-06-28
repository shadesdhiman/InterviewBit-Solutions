# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 14:52:04 2021

@author: Dhiman
"""

class Solution:
    # @param A : list of integers
    # @return an integer
    def cntBits(self, A):
        
       
        ans =[]
        for i in range(len(A)):
            curr =0
            for j in range(i, len(A)):
                curr ^= A[j]
               
                ans.append(curr)
        
        curr = 0
        for i in range(len(ans)):
            
            curr ^= ans[i]
                
        return curr
        
       
                        
                    
                    
                
        
                
                
                    
        
                

        








obj = Solution()
A = [3,4,5]
print(obj.cntBits(A))