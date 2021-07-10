# -*- coding: utf-8 -*-
"""
Created on Wed May 26 00:07:55 2021

@author: Dhiman
"""

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def paint(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C
        fl = []
        fl.append(0)
        ans = 0
        if(A==0):
            return -1
        if(A==1):
            return (sum(C)*B)%10000003
        if(len(C)==0):
            return 0
        if(A>=len(C)):
            return max(C)*B
        
        def checker(low,mid,high,ans):
            print(low,mid,high,ans)
           
            f_l = []
            f_l.append(0)
            row = 0
            for i in range(len(C)):
                if(row<A):
                    if(f_l[row]+C[i]<mid):
                        f_l[row]+= C[i]
                    else:
                        row = row+1
                        if(row<A):
                            f_l.append(C[i])
                            
                            
                        else:
                            return False
         
                    
            if(ans<max(f_l)):
                ans = max(f_l)
                fl[0]=ans
            return True
            
        
        
        left =0
        right = sum(C)
        while(left<right):
            mid = (left+right)//2
            if(checker(left,mid,right,ans)==True):
                right = mid-1
            else:
                left = mid+1
        return (fl[0]*B)%10000003   
        
        
        
        
        
A = 1
B = 1000000
C = [ 1000000, 1000000 ]

obj = Solution()
print(obj.paint(A,B,C))
