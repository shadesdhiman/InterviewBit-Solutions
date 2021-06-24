# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 18:14:30 2021

@author: Dhiman
"""

class Solution:
    # @param A : string
    # @return an integer
    def findRank(self, A):
        per = []
        AA= []
        per.append(0)
        for i in range(1,26):
            if(i==1):
                per.append(i)
                #print(per)
            else:
                per.append(per[i-1]*i)
        #print(per)
        alpha = []
        for i in range(26):
            alpha.append(0)
        
        for i in range(len(A)):
            if(A[i].upper() !=A[i]):
                AA.append(A[i].upper())
            else:
                AA.append(A[i])
                
        for i in range(len(AA)):
                
            alpha[ord(AA[i])-65]=1
        #print(alpha)
        
        n= len(A)-1
        count = 0
        val = 0
        
        for i in range(len(AA)):
            count = 0
            for j in range(ord(AA[i])-64):
                #print("j = ",j)
                alpha[ord(AA[i])-65] = 0
                #print(alpha)
                if(alpha[j]==1):
                    
                    count = count+1
               
                
                #print("count -",count)
                #print(val)
                
            
            val = val +per[n-i]*count
           
           #print("val =",val)
        
        return val+1
        
        
obj1 = Solution()
A = "CAB"
print(obj1.findRank(A))