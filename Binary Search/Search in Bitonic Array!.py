# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 12:00:44 2021

@author: Dhiman
"""

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        left = 0
        right = 1
        
        
        def in_i(low,high):
            #print("in_i",low,high)
            if(low == high):
                if(A[low]==B):

                    return low
                else:
                    return -1
            elif(high == low+1):
                if(A[low]==B):
                    return low
                elif(A[high]==B):
                    return high
                else:
                    return -1
            else:
                mid = (low+high)//2
                if(A[mid]==B):
                    return mid
                elif(A[mid]<B):
                    return in_i(mid+1,high)
                else:
                    return in_i(low,mid-1)
                
                
        def in_d(low,high):
            #print("in_i",low,high)
            if(low == high):
                if(A[low]==B):

                    return low
                else:
                    return -1
            elif(high == low+1):
                if(A[low]==B):
                    return low
                elif(A[high]==B):
                    return high
                else:
                    return -1
            else:
                mid = (low+high)//2
                if(A[mid]==B):
                    return mid
                elif(A[mid]>B):
                    return in_d(mid+1,high)
                else:
                    return in_d(low,mid-1)
        
        while(A[left]<A[right]):
            if(right*2<len(A)-1):
                left = right
                right = right*2
                
            else:
                break
      
        
        if(A[left]<A[right]):
            while(A[left]<A[right]):
                left =left+1
                
        else:
            print(left,right)
            for i in range(right,len(A)-1):
                if(A[left]<A[right]):
                    left +=1
        if(A[left]>A[left+1]):
            maxi = left
        else:
            maxi = left+1
     
        
        

        
        x = in_i(0,maxi)
        y = in_d(maxi,len(A)-1)
        if(x==-1):
            return y
        else:
            return x
        





obj1 = Solution()
A = [ 10, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11 ]
B = 12

print(obj1.solve(A,B))