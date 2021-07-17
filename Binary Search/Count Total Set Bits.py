# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 10:01:17 2021

@author: Dhiman
"""

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        i=0
        count = 0
        def fun(A):
            #print("A",A)
            if(A==0):
                return 0
            i=0
            while(True):
                if(A+1>=1<<i+1):
                    i=i+1
                    count = (2**(i-1))*i
                    #print("i",i)
                    
                    
                else:
          
                    if(A-((2**i)-1)>=1):
                        #print(count)
                        count = count + A-((2**i)-1)
                        #print("count",count)
                        return count + fun(A-((2**i)))
                    else:
                        return count
                        
            
        return fun(A)
        
        
    
        




obj1 = Solution()
A=5
print(obj1.solve(A))
