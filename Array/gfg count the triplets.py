# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 01:11:29 2021

@author: Dhiman
"""

def countTriplet( arr, n):
    num=0
    dict1= dict(())
    m = max(arr)
    for i in range(m+1):
            dict1[i]=0
    for i in arr:
        dict1[i]=1

    for i in range(n-1):
        for j in range(i+1,n):
            sum1 = arr[i]+arr[j]
            if(sum1<=m):
                if(dict1[sum1]==1):
                    num = num+1
    return num
    
arr = [1, 2,3,4,5]
countTriplet(arr,len(arr))
    