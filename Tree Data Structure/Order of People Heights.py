# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 10:55:15 2021

@author: Dhiman
"""

class Solution():
    def solve(self,A,B):
        l_a = len(A)
        dic = dict()
        for i in range(l_a):
            dic[A[i]] = B[i]
        A.sort(reverse = True)
        
        for i in range(l_a):
            B[i] = dic[A[i]]
        #print(A,B)
        queue =[]
        for i in range(l_a):
            queue.insert(B[i], A[i])
        return queue
        
        
        
        
        
        
        
        
A = [5,3,2,6,1,4]
B = [0,1,2,0,3,2]
obj = Solution()
print(obj.solve(A,B))