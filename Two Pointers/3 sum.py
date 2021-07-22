# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 11:18:18 2021

@author: Dhiman
"""

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
        diff = 9999999999
        small = 9999999
        def dis(desired, loc, diff,small):
            print("inside dis")
            #print(desired, loc, diff)
            if diff >  abs(loc-desired):
                diff =  abs(loc-desired)
                small = loc
            return diff,small
                
                
            
        
        if len(A)<3:
            return -1
        
        A.sort()
        
        
        for i in range( len(A)-2):
            print("In lopp",i)
            x = A[i]
            j = i+1
            k = len(A)-1
            while(j<k):
                print("Inside while",i,j,k)
                summ  = x+A[j]+A[k]
                diff,small = dis(B,summ,diff,small)
                if summ < B:
                    j = j+1
                    
                elif summ>B:
                    k = k-1
                    
                else:
                    diff,small = dis(B,summ,diff,small)
                    return small
        return small
                
                
                
        

        












obj = Solution()
A = [ -5, 1, 4, -7,6,78,25,2]
B = -1
print(obj.threeSumClosest(A,B))