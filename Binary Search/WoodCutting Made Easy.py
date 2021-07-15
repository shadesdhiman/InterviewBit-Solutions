# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 15:42:05 2021

@author: Dhiman
"""

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        min_a = min(A)
        max_a = max(A)
        low = max_a
        high =max_a-1
        res = -1
        i=1
        def check(low,high):
            summ = 0 
            for i in range(len(A)):
                if(A[i]>high):
                    summ = summ +A[i]-high
            
            if(summ >= B):
                return 1
            else:
                return -1
            
        while(res==-1 or high-2*i>0):
            
            res = check(low,high)
            
            if(res == -1):
                i= i*2
                high  = high-i
            else:
                break
        
        
        print(low,high)
        x = check(low,high+1)
        if(x==1):
            i=1
            while(True):
                temp = check(low,high)
                if(temp==1):
                    high = high +1
                else:
                    high = high-1
                    break
        return high
            
            
                        
                    
            
                
            
                
                
        
        
        
        

        









obj1 = Solution()
A = [4, 42, 40, 26, 46]
B = 20
print(obj1.solve(A,B))