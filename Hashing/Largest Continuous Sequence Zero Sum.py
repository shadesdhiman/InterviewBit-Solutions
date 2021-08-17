# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 21:45:14 2021

@author: Dhiman
"""

class Solution:
	# @param A : list of integers
	# @return a list of integers
    def lszero(self, A):
        if len(A)==1:
            if A[0]!=0:
                return []
            else:
                return A
        summ = 0
        max_len = 0
        dic = dict()
        test = 0
        for i in range(len(A)):
            #print(A[i], summ)
            summ += A[i]
            if summ == 0:
                max_len = i+1
                start = -1
                end = i
                test = 1
            if summ in dic:
                index = dic[summ]
                if i - index > max_len:
                    max_len = i-index
                    start = index
                    end= i
                    test = 1
            else:
                dic[summ] = i
        if test == 0:
            return []
        return A[start+1: end+1]
        
                
A = [ -19, 8, 2, -8, 19, 5, -2, -23 ]
obj = Solution()
print(obj.lszero(A))