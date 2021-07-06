# -*- coding: utf-8 -*-
"""
Created on Thu May 27 23:47:27 2021

@author: Dhiman
"""

class Solution:
    # @param A : string
    # @return an integer
    def isNumber(self, A):
        count_e = 0
        num_arr=[]
        A=A.strip()
        if(len(A)==0):
            return 0
        if(A[0]=="."):
            return 0
        for i in range(10):
            num_arr.append(str(i))
        num_arr.append(".")
        num_arr.append("e")
        num_arr.append("-")
            
        Num_dict = {}.fromkeys(num_arr,1)
        loc_e =0
        
        for i in range(len(A)):
            if A[i] not in Num_dict:
                return 0
            if(Num_dict[A[i]]==1):
                
                if(A[i]=="e"):
                    if count_e<2:
                        loc_e = i
                        count_e +=1
                    else:
                        return 0
                
        if(A[-1]=="."):
            return 0
        if loc_e !=0:
          
            for i in range(loc_e+1,len(A)):
            
                
                if(A[i]=="."):
                    return 0
                if(loc_e == len(A)-1):
                    return 0
                if(loc_e == len(A)-2 and A[loc_e+1] =="-"):
                   
                    return 0
                if(loc_e == (len(A)-3)):
                    if (A[loc_e+1]== "." ):
                     
                        return 0
                    if (A[loc_e+2]==("-" or "0" )):
                      
                        return 0

        for i in range(len(A)):
            if(A[i]=="."):
                return 1
    
            
        return 1
        

        











      
        
obj = Solution()
A= "2e10"
print(obj.isNumber(A))