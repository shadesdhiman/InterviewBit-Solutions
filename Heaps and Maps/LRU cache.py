# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 10:03:03 2021

@author: Dhiman
"""




class Solution():
    def solve(self,A,B):
        dic = dict()
        index = 0
        arr = [-1]*B
        arr =[]
        pf = 0
        for i in range(len(A)):
            if A[i] in dic:
                dic[A[i]]+=1
                arr.remove(A[i])
                if dic[A[i]] == 1:
                    del dic[A[i]]
                else:
                    dic[A[i]]-=1
                arr.insert(0, A[i])
            else:
                dic[A[i]] =1
                pf +=1
                if index < B:
                    arr.insert(0, A[i])
                    index+=1
                else:
                    arr.insert(0, A[i])
                    temp = arr.pop()
                    if dic[temp] == 1:
                        del dic[temp]
                    else:
                        dic[temp]-=1
        return pf
                    
                    
                    
                
                
        









A = [1,2,3,4,2,1,5,6,2,1,2,3,7,6,3,2,1,2,3,6]
B = 4
obj = Solution()
print(obj.solve(A,B))