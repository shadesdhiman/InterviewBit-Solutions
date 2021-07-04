# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 17:25:37 2021

@author: Dhiman
"""

class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        temp = []
        rev = []
        char = False
        A = list(A)
        x = len(A)-1
        while(x):
            if(A[x]!=" "):
                break
            else:
                A.pop(x)
                x=x-1
        
        #print("*",A)
        x = 0
        l = len(A)
        while(x<l):
            if(A[0]!=" "):
                #print("A",A)
                break
            else:
                A.pop(0)
                #print(x,A)
                x=x+1
        #print(A)
        C = ""
        A = C.join(A)
        #print(A)
        i = len(A)-1
        while(i>=0):
            while(i>=0 and A[i]!= " "):
                temp.append(A[i])
                i=i-1
            for j in range(len(temp)-1,-1,-1):
                rev.append(temp[j])
            temp.clear()
                
            while(i>=0 and A[i]==" " ):
                temp.append(A[i])
                i=i-1
            for j in range(min(1,len(temp))-1,-1,-1):
                rev.append(temp[j])
            temp.clear()
                
                
        
        
        
        #print(len(A))
        print(list(rev))
        
        C = ""
        return C.join(rev)
            
obj = Solution()
A = "qxkpvo  f   w vdg t wqxy ln mbqmtwwbaegx   mskgtlenfnipsl bddjk znhksoewu zwh bd fqecoskmo"
print(obj.solve(A))