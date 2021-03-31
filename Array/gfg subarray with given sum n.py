# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 12:21:30 2021

@author: Dhiman
"""


def subArraySum(arr,n,s):
    arr_sum = 0
    start = 0
    
    
    for i in range(n-1):
        if(arr_sum < s):
            print("inside less", arr_sum)
            arr_sum = arr_sum + arr[i]
           
            
            
           
        if(arr_sum +arr[i]> s):
            
            while(arr_sum>s): 
                print("inside greater", arr_sum)
                arr_sum = arr_sum - arr[start]
                start = start + 1
                
                if(s!= arr_sum):
                    i= i-1
                
        
                
        if (arr_sum == s):
            print("under equal")
            return [start+1,i+1]
                
        
    return [-1]

arr = [135,101,170,125, 79, 159, 163, 65, 106, 146, 82, 28, 162, 92, 196, 143, 28, 37, 192, 5, 103, 154, 93, 183, 22, 117, 119, 96, 48, 127, 172, 139, 70, 113, 68, 100, 36, 95, 104, 12, 123, 134] 
n = len(arr)  
sum =697
print(subArraySum(arr, n, sum)) 