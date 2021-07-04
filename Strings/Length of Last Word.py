# -*- coding: utf-8 -*-
"""
Created on Wed May 26 23:46:42 2021

@author: Dhiman
"""
class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        temp =0
        temp =0
        c=0
        if(len(A)==0):
            return 0
        if(len(A)==1):
            return 1    
        for i in range(len(A)-1,-1,-1):
            if(A[i]==" " ):

                if(temp==0):
                    c=c+1
                    continue
                return temp
            else:
                temp+=1
        return len(A)-c
                
obj = Solution()
A= "Hello   e "
print(obj.lengthOfLastWord(A))