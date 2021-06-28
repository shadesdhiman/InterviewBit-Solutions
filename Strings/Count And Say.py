# -*- coding: utf-8 -*-
"""
Created on Wed May 26 19:39:28 2021

@author: Dhiman
"""

class Solution:
    # @param A : integer
    # @return a strings
    def countAndSay(self, A):
        self.A = A
        arr = []
        c = []
        c.append(0)
        def count_num(A,next_loc):
            print(A,next_loc,arr)
            c.clear()
            c.append(0)
            num = arr[next_loc]
            limit = len(arr)
            print(next_loc+1< limit)
            print(arr[next_loc +1] != num)
            while(((next_loc+1) < limit) and ((arr[next_loc +1]) != num)):
                print((next_loc+1) < limit)
                c[0 ]= c[0]+1
                next_loc+=1
            if (next_loc+1) >= limit:
                return c[0],-1

            return c[0],next_loc
        def fun(n):
            if(n==1):
                arr.append(1)
                return arr
            if(n==2):
                arr.append(1)
                return arr
            next_loc =0
            while(next_loc!=-1):
                count,next_loc = count_num(A,next_loc)
                num = arr[next_loc]
                arr.append(count_num)
                arr.append(num)
            return arr
        for i in range(1,A):
            res = fun(i)
        return res
                
                
                
        
       
        
        
        
obj = Solution()
A = 5
print(obj.countAndSay(A))
