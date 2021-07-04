# -*- coding: utf-8 -*-
"""
Created on Wed May 26 15:08:36 2021

@author: Dhiman
"""

class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        if(len(A)==0 or len(A)==1):
            return 1
        alpha_numeric = []
        for i in range(0,10):
            alpha_numeric.append(str(i))
        for i in range(26):
            alpha_numeric.append(chr(65+i))
            alpha_numeric.append(chr(97+i))
        
        alpha_numeric_dict = {}.fromkeys(alpha_numeric,1)
        
        l = 0
        r = len(A)-1
        while(l!=r):
            if(r<l):
                    return 1
            print(l,r)
            print(A[l],A[r])
            if((A[l].upper()==(A[r]).upper())):
                l = l+1
                r = r-1
                if(r<l):
                    return 1
            else:
                if(A[l] in alpha_numeric_dict and A[r] in alpha_numeric_dict):
              
                    return 0
                elif (A[l] in alpha_numeric_dict or A[r] in alpha_numeric_dict) == False:
                    l = l+1
                    r = r-1
                else:
                    if (A[l] in alpha_numeric_dict):
                        r = r-1
                    elif (A[r] in alpha_numeric_dict):
                        l = l+1
        return 1
                        
                    
                

        






obj = Solution()
A = "A man, a plan, a canal: Panama"
print(obj.isPalindrome(A))