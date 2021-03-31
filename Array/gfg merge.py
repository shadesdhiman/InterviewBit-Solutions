# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 11:36:01 2021

@author: Dhiman
"""

class Solution:
    
    #Function to merge the arrays.
    def merge(self,arr1,arr2,m,n):
        fl = []
        if(m==0):
            return arr1
        elif(n==0):
            return arr2
        for i in range(m+n-1):
            if(len(arr1)!=0 and len(arr2)!=0):
                if(arr1[0]<=arr2[0]):
                    fl.append(arr1[0])
                    arr1.pop(0)
                    #print("Arr1 arr1 pop", arr1)
                else:
                    fl.append(arr2[0])
                    arr2.pop(0)
                    #print("Arr2 arr2 pop", arr2)

        
        if(len(arr1)>len(arr2)):
            for i in range(len(arr1)):
                fl.append(arr1[0])
                arr1.pop(0)
        else:
            for i in range(len(arr2)):
                fl.append(arr2[0])
                arr2.pop(0)
        
      
        
        for i in range(m+n):
          
            if(i<n-1):
                arr1.append(fl[i])
            else:
                arr2.append(fl[i])
        
        
        
        
obj = Solution()
A = [1, 3, 5, 7]
B = [0, 2, 6, 8, 9]

print(obj.merge(A,B,len(A),len(B)))