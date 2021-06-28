# -*- coding: utf-8 -*-
"""
Created on Fri May 28 12:53:33 2021

@author: Dhiman
"""

class Solution:
    # @param A : string
    # @return an integer
    def atoi(self, A):
        A = A.strip()
        sym_arr=[]
        num = []
        ans = []
        res = ""
        limit =0
        for i in range(10):
            sym_arr.append(str(i))
        sym_arr.append("-")
        sym_arr.append("+")
        
        num_dict = {}.fromkeys(sym_arr,1)
        
        if(A[0] not in num_dict):
            return 0
        for i in range(len(A)):
            if(A[i] not in num_dict ):
                
                limit = i
                break
            if((A[i]=="-" or A[i]=="+") and i!=0):
                return 0
            if(i == len(A)-1):
                if(A[0]=="+"):
                    if A[1]==" ":
                        return 0
                    for i in range(1,len(A)):
                        ans.append(A[i])
                        return res.join(ans)
                else:
                    if A[1]==" ":
                        return 0
                    X = res.join(A)
                    X = int(X)
                    if(X <= -2147483648):
                        return "INT_MIN"
                
                
        if(limit == 1):
            if(A[limit-1]=="-" or A[limit-1]=="+"  ):
                return 0
        if(limit== 0):
            limit = len(A)

        for i in range(limit):
            #print(i)
            if(A[i]=="-" and i==0):
                ans.append("-")
            elif(A[i]=="+" and i==0):
                pass
            else:
                ans.append(str(A[i]))
        #print(ans)
        X = res.join(ans)
        
        #print(X)
        X = int(X)
        if(X>= 2147483647):
            return "INT_MAX"
        elif(X <= -2147483648):
            return "INT_MIN"
        else:
            return X
        
                
        
        
        
        
            
            
            
            
            
obj = Solution()
A= "78"
print(obj.atoi(A))