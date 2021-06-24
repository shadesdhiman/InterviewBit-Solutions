# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 09:05:04 2021

@author: Dhiman
"""

class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        
        def bs(left,right):
            if(left==right):
                if(left**2 <= A and (left+1)**2>A):
                    return left
            elif(right == left+1):
                if(left**2 <= A and (left+1)**2>A):
                    return left
                else:
                    return right
            else:
                mid = (left+right)//2
                if(mid**2<=A and (mid+1)**2>A):
                    return mid
                elif(mid**2>A):
                    return bs(left,mid-1)
                else:
                    return bs(mid+1,right)
        return bs(0,A)
                    
                    
                    

        
    
obj1 = Solution()
num = 930675566
print(obj1.sqrt(num))



        