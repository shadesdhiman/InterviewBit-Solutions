# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 12:02:36 2021

@author: Dhiman
"""


def subArraySum(arr,n,sum):
    for i in range(n):
        sum_arr = arr[i]
        j = i+1
        
        while(j<=n):
            if sum_arr == sum :
                print("the index is %d and %d"%(i,j-1))
                return 1
            if sum_arr > sum or j ==n:
                break
            sum_arr = sum_arr + arr[j]
            j=j+1
            
    print("No index found")
    return 0



arr = [15, 2, 4, 8, 9, 5, 10, 23] 
n = len(arr) 
sum = 23
  
subArraySum(arr, n, sum) 