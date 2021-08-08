# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 16:31:06 2021

@author: Dhiman
"""

class Solution:
	# @param A : integer
	# @return an integer
    def solve(self, A):
        import math
        from math import comb
        M= 1000000007
        dp = [-1]*(A+1)
        #print(dp)
        
        
        
        def choose(n,r):
            
            def fact(n): 
                if n ==1:
                    return 1
                if n == 2:
                    return 2
                res = 1
                  
                for i in range(2, n+1): 
                    res = res * i 
                      
                return res 
            return int (fact(n) // (fact(r)  * fact(n - r))) 
  
# Returns factorial of n 
            
            
                
            
            
        
        def noofnodesonleft(n):
            if n == 0:
                return 0
            h = int(math.log2(n))
            x = ((1<<(h-1))-1)
            y = min((1<<(h-1)), (n - ((1<<h)-1)))
            return int(x)+int(y)
        
        def getnumofmaxheap(n,dp):
           
            if n <=1:
                return 1
            if dp[n] != -1:
                return dp[n]
            left = noofnodesonleft(n)
            waystochooseL = choose(n-1,left)
            maxheapusingL = getnumofmaxheap(left,dp)
            maxheapusingR = getnumofmaxheap(n-1-left,dp)
            ans = ((waystochooseL % M)*(maxheapusingL *maxheapusingR ))% M
            dp[n] = ans
            return ans
        
            
        return getnumofmaxheap(A,dp)
            

A = 100

obj = Solution()
print(obj.solve(A))        


