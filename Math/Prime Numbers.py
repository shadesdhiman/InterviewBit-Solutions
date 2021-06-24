# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 16:45:34 2021

@author: Dhiman
"""

class Solution:
	# @param A : integer
	# @return a list of integers
    def sieve(self, A):
        import math
        self.A = A
        prime = []
        final = []
        for i in range(A+1):
            prime.append(1)
        
        for i in range(2,int(math.sqrt(A))+1):
            if(prime[i]==1):
                for j in range(2,A):
                    if i*j > A:
                        break
                    prime[i*j]=0
                    
        prime[0]=0
        prime[1] = 0
        #print(prime)
        for i in range(len(prime)):
            if(prime[i]==1):
                final.append(i)
        return final
                
        
            
            
            

obj1 = Solution()
A= 10
print(obj1.sieve(A))