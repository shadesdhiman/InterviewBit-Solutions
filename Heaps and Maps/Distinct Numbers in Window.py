# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 08:41:18 2021

@author: Dhiman
"""

class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return a list of integers
    def dNums(self, A, B):
        arr = []
        
        dic = dict()
        for i in range(B):
            if A[i] in dic:
                dic[A[i]] += 1
            else:
                dic[A[i]] = 1
        l = len(dic)
        arr.append(l)
        i = 0
        j = B

        while(j<len(A)):
            if A[j]!=A[i]:
                if dic[A[i]]>1:
                    dic[A[i]]-=1
                    
                else:
                    del dic[A[i]]
                    l=l-1
                if A[j] in dic:
                    dic[A[j]]+=1
                else:
                    dic[A[j]] =1
                    l=l+1
                arr.append(l)
            else:
                print(A[i],A[j])
                arr.append(l)
            i=i+1
            j=j+1
        return arr
                

                


A = [ 1, 2, 1, 3, 4, 3 ]
B = 3
obj = Solution()
print(obj.dNums(A,B))        

