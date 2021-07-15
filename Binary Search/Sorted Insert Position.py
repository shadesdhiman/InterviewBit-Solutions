# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 11:30:48 2021

@author: Dhiman
"""

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def searchInsert(self, A, B):
        if(len(A)==0):
            return 0

        def index(low,high):
       
            if(low == high):
                if(A[low]<=B):
                    if(A[low]==B):
                        return low
                    return low+1
                else:
                    return low
            elif(high == low-1):
                print(low,high)  
                if(A[low]<=B and A[high]>=B):
                    if(A[high]==B):
                        return high
                    else:
                        return high-1
                elif(A[low]<=B and A[high]<B):
                    return low+1
                elif(A[low]>=B and A[high]>=B):
                    if(A[low]==B):
                        return low

            else:
                mid = (low+high)//2
             
                if(A[mid]>=B and A[mid-1]<B):
                    return mid
                elif(A[mid]>B):
                    return index(low,mid-1)
                else:
                    return index(mid+1,high)


        return(index(0,len(A)-1))










obj1 = Solution()
A = [1, 3, 5, 6]
B = 1
print(obj1.searchInsert(A,B))