# -*- coding: utf-8 -*-
"""
Created on Thu May 27 19:41:05 2021

@author: Dhiman
"""

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def compareVersion(self, A, B):
        l_a = len(A)
        l_b = len(B)
        A_arr = []
        B_arr = []
        temp =0
        for i in range(l_a):
            if(temp>0):
                temp -=1
                continue
            if(A[i]=="."):
                i=i+1
                continue
            #print("i",i)
            num =0
            while(i<l_a and A[i]!="." ):
                num = num*10+int(A[i])
                i=i+1
                temp = temp+1
            A_arr.append(num)
        #print(A_arr)
        temp =0 
        for i in range(l_b):
            if(temp>0):
                temp -=1
                continue
            if(B[i]=="."):
                i=i+1
                continue
            #print("i",i)
            num =0
            
            while(i<l_b and B[i]!="." ):
                num = num*10+int(B[i])
                i=i+1
                temp = temp+1
            B_arr.append(num)
        #print(B_arr)
        
        arr_al = len(A_arr)
        arr_bl = len(B_arr)
        
        for i in range(min(arr_al,arr_bl)):
            if(A_arr[i]>B_arr[i]):
                return 1
            if(A_arr[i]<B_arr[i]):
                return -1
      
        if(arr_al>arr_bl):
            if(A_arr[-1]==0):
                return 0
            else:
                return 1
        elif(arr_al<arr_bl):
            if(B_arr[-1]==0):
                return 0
            else:
                return -1
        else:
            return 0
            
        
        
        
        
        
obj = Solution()
A= "01"
B= "1"
print(obj.compareVersion(A,B))