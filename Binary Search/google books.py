# -*- coding: utf-8 -*-
"""
Created on Tue May 25 16:39:05 2021

@author: Dhiman
"""

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def books(self, A, B):
        ans = 0
        
        fl= []
        fl.append(0)
        if(len(A)==1 and A[0]==0):
            return -1
        if(B==0):
            return -1
        if(B==1):
            return sum(A)
        if(len(A)<B):
            return -1
            
        
        if(len(A)==B):
            return max(A)
        
        def checker(left,mid,right,ans):
           
            fill =[]
            fill.append(0)
            row = 0
         
            for i in range(len(A)):
                if(row<B):
                    if(fill[row]+A[i]<=mid):
                        fill[row] =fill[row]+A[i]
                    else:
                        row = row+1
                        if(row<B):
                            fill.append(A[i])
                        else:
                            return False
            if(ans<max(fill)):
                ans = max(fill)
                fl[0]=ans
            return True
                        
            
                        
                        
                        
                        
                        
                    
            
            
            
            
        left =0
        right = sum(A)
        while(left<right):
            mid = (left+right)//2
            if(checker(left,mid,right,ans)==True):
                right = mid
            else:
                left = mid+1
        return fl[0]
                
        
        
        
        
        
        
A = [12, 34, 67, 90]
B = 2
obj1 = Solution()
print(obj1.books(A, B))