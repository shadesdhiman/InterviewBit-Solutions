# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 10:52:38 2021

@author: Dhiman
"""

class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return a list of list of integers
    def fourSum(self, A, B):

        A.sort()
        ans = []
        
        for i in range(len(A)-3):
            for j in range(i+1,len(A)-2):
                start = j+1
                end = len(A)-1
                sum1 = A[i]+A[j]
                rem = B-sum1
                
                while(start<end):
                    
                    if A[start]+A[end]>rem:
                        end-=1
                    elif A[start]+A[end]<rem:
                        start+=1
                    else:
                        x = [A[i],A[j],A[start],A[end]]
                        if x not in ans:
                            ans.append(x)
                        start = start+1
        return ans
        












A = [1, 0, -1, 0, -2, 2]
   # [-2,-1,0,0,1,2]
B = 0
obj = Solution()
print(obj.fourSum(A,B))