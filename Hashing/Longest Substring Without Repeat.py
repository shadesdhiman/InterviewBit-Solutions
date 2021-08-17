# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 16:04:10 2021

@author: Dhiman
"""

class Solution:
	# @param A : string
	# @return an integer
    def lengthOfLongestSubstring(self, A):
        dic = dict()
        l = 0
        index =0
        for i in range(len(A)):
            if A[i] in dic:          
                l = max(l,len(dic))     
                while(A[i] !=A[index]):
                      del dic[A[index]]
                      index+=1
                del dic[A[index]]
                index+=1   
                dic[A[i]] = i
            else:
                dic[A[i]] = i
        
        
        
        l = max(l,len(dic))
        if l==0 and A:
            return len(A)
        
        return l


A = "abcabcbb"
obj = Solution()
print(obj.lengthOfLongestSubstring(A))