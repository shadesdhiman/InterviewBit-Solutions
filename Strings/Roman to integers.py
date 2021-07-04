# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 09:53:46 2021

@author: Dhiman
"""

class Solution:
    # @param A : string
    # @return an integer
    def romanToInt(self, A):
        arr = ['I','V','X','L','C','D','M']
        res = 0
        val_dic = dict(())
        val_dic[arr[0]] = 1
        val_dic[arr[1]] = 5
        val_dic[arr[2]] = 10
        val_dic[arr[3]] = 50
        val_dic[arr[4]] = 100
        val_dic[arr[5]] = 500
        val_dic[arr[6]] = 1000
       
        
        for i in range(len(A)-1):
           
            if(val_dic[A[i]]>val_dic[A[i+1]]):
                res += val_dic[A[i]]
                #print("a",res)
            elif(val_dic[A[i]]<val_dic[A[i+1]]):
                res -= val_dic[A[i]]
                #print("b",res)
            else:
                res += val_dic[A[i]]
                #print("c",res)
        res+=val_dic[A[-1]]
        return res

obj = Solution()
A = "MMMCCLXXXVII"
print(obj.romanToInt(A))
    
                
        
