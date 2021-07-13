# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 05:43:08 2021

@author: Dhiman
"""

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        if(len(A)==0):
            return -1
        left = None
        right = None
        
        
        
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
        
        
            

        
        if(A[0]>A[-1]):
           
            left = 0
            right = 1
            while(right*2 <=len(A)-1):
                #print(left,right)
                if(A[left]<A[right]):
                    left = right
                    right = right*2
                else:
                    break
            if(A[left]>A[right]):
                for i in range(left,right):
                    if(A[i+1]<A[i]):
                        num= i+1     
                        
            else:
                for i in range(right,len(A)-1):
                    if(A[i+1]<A[i]):
                        num= i+1     
                    
                
        #print(num)
        if(left == None and right == None):
            return in_i(0,len(A)-1)
        else:
            x = in_i(0,num)
            y = in_i(num,len(A)-1)
            if(x==-1):
                return y
            else:
                return x
                
                
           
                    
                    
                
           
            
        
              
            

                
            
                
        
     
        
obj1 = Solution()   
#A = [2,1,0]
A = [ 9, 10, 11, 12, 14, 15, 17, 19, 24, 25, 30, 39, 40, 44, 46, 48, 51, 53, 54, 56, 59, 60, 69, 70, 73, 75, 80, 87, 88, 89, 92, 93, 97, 99, 104, 107, 109, 110, 111, 117, 123, 124, 125, 126, 127, 128, 135, 136, 137, 141, 148, 153, 154, 161, 166, 167, 169, 175, 177, 180, 181, 182, 185, 186, 189, 193, 198, 202, 1, 2, 6, 7 ]
B = 198
#A = [7,7,8]



print(obj1.search(A, B) )
