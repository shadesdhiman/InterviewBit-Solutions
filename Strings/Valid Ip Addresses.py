# -*- coding: utf-8 -*-
"""
Created on Fri May 28 16:39:08 2021

@author: Dhiman
"""

class Solution:
    # @param A : string
    # @return a list of strings
    def restoreIpAddresses(self, A):
        res = []
        def isvalid(x):
            if(len(x)>3):
                return False
            if(x.startswith("0")==True and len(x)>1):
                return False
            if(int(x)<=255):
                return True
            else:
                return False
            
        str_len = len(A) 
        
        for i in range(1,4):
            if(i<str_len):
                first = A[0:i]
               
                if(isvalid(first)):
                    for j in range(1,4):
                        if(i+j<str_len):
                            second = A[i:i+j]
                            
                            if(isvalid(second)):
                                for k in range(1,4):
                                    if(i+j+k<str_len):
                                        #print("i,j,k = ",i,j,k)
                                        third = A[i+j:i+j+k]
                                        fourth = A[i+j+k:]
                                        #print("first = ",first , "second = ",second,"Third = ",third,"Fourth = ",fourth)
                                        if(isvalid(third) and isvalid(fourth)):
                                            res.append(str(first +"."+ second +"."+ third + "." + fourth))
        return res
                            
            
        

        





            
obj = Solution()
A= "25525511135"
print(obj.restoreIpAddresses(A))