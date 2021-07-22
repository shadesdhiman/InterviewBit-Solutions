4
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def findCount(self, A, B):
        
        def fun(low,high):
            print("888",low,high)
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
                    return fun(low,mid-1)
                else:
                    return fun(mid+1,len(A)-1)
        x = fun(0,len(A)-1)
        print(x)
        if x ==-1:
            return -1
        
        y=x
        times = 1
        print(x,y)
        while(x+1<len(A) and A[x+1]==B ):
            
            x= x+1
            times = times+1
        while(y-1>=0 and A[y-1]==B ):
            
            y = y-1
            times = times+1
        return times
            
obj1 = Solution()
A = [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10 ]
B = 6
print(obj1.findCount(A,B))