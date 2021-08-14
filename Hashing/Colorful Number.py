# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 08:35:45 2021

@author: Dhiman
"""
from copy import deepcopy
class Solution:
	# @param A : integer
	# @return an intege
    def colorful(self, A):
        A = str(A)
       
        arr = []
        self.arr = arr
        def ss(A,i,j, subset,arr):
            if i == len(A):
                x = deepcopy(subset)
                arr.append(x)
                return 
            
            if j == len(A)+1:
                i = i+1
                j = i+1
                
            subset.append(A[i:j])
            ss(A,i,j+1,subset,arr)
        
            
        
        
        
        i = 0
        j = 1
        ss(A,0,j,[],arr)
        
        
        

        arr = arr[0]
        #print(arr)
        
        dic = dict()
        
        def check(x):
            num = 1
            for index in range(len(x)):
                num = num*int(x[index])
                
            if num in dic:
                return False
            else:
                dic[num] = 1
                return True
            
            
        
        for i in range(len(arr)):
            if check(arr[i]):
                pass
            else:
                return 0
        return 1
        
        
       
            
           
        
        
        
        
        
A = 145
obj  = Solution()
print(obj.colorful(A))
				

