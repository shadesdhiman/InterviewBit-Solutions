# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 10:50:57 2021

@author: Dhiman
"""


class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):

        if len(A)==1:
            return 1
        dic = dict()
        for i in range(len(A)):
            if A[i] in dic:
                dic[A[i]]+=1
            else:
                dic[A[i]] = 1
        
        time = 0
        for key in dic.keys():
            
            if dic[key]%2!=0:
                time+=1
            if time>1:
                return 0
        return 1







A = "abbaeeeeop"
obj = Solution()
print(obj.solve(A))