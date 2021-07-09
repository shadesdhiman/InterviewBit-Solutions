# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 11:09:14 2021

@author: Dhiman
"""

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def books(self, A, B):
        ans = 0
        f= []
        f.append(0)
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
        
        def check(left,right,mid,ans):
            #print(ans)
           # print(left,mid,right)
            fill = []
            fill.append(0)
            row = 0
            if(left == right):
                return False
            
            else:
                
                for i in range(len(A)):
                    
                    
                    if(row<=B-1):
                        #`print("mid = ",mid)
                        
                        if((fill[row]+A[i])<=mid):
                            fill[row]= fill[row]+A[i]
                            #print("limuit",fill)
                        else:
                            row = row +1
                            if(row<=B-1):
                                fill.append(A[i])
                                #print("adding",fill)
                                #print("*")
                            else:
                                #print("exiting",fill)
                                return False
                if(ans<max(fill)):
                    ans = max(fill)
                    #print(fill,"\t",ans)
                    f[0] = ans

                #print("ans = ",ans)
                return True
            
        left = 0
        right = sum(A)
        while(left<right):
            mid = (left+right)//2
            if(check(left,right,mid,ans) == True):
                #print(ans)
                right = mid
                #print("=")
            else:
                left = mid+1
                #print("p")
            
        
        return f[0]
                   
                
                     

obj1 = Solution()
A = [ 73, 58, 30, 72, 44, 78, 23, 9 ]
B =5
print(obj1.books(A,B))
                    