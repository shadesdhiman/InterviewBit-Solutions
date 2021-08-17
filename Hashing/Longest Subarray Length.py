# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 11:19:27 2021

@author: Dhiman
"""

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        summ = 0
        maxlen = 0
        
        dic= dict()
        
        for i in range(len(A)):
            if A[i] == 0:
                summ -=1
            else:
                summ +=1
            if summ ==1:
                maxlen = i+1
            else:
                if summ in dic:
                    pass
                else:
                    dic[summ] = i
                    
            if summ-1 in dic:
                ind = dic[summ-1]
                if maxlen < i-ind:
                    maxlen = i-ind
        return maxlen
        









A = [1,1,0,1,0,1,1,1,1,1,1,1,1,0,0]
obj = Solution()
print(obj.solve(A))