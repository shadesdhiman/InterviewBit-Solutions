# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 18:14:30 2021

@author: Dhiman
"""

class Solution:
    # @param A : string
    # @return an integer
    def findRank(self, N,K):
        per = []
        val = []
        ans = []
        for i in range(N):
            val.append(i+1)
        per.append(0)
        for i in range(1,N):
            if(i==1):
                per.append(i)
                #print(per)
            else:
                per.append(per[i-1]*i)
        for i in range(N,0,-1):
           # print(i)
            if(i==1):
                ans.append(val[-1])
                break
            #print('per[i-1]=',per[i-1])
            index = K//per[i-1]
            #print(index)
            if(K%per[i-1]==0):
                index = index-1
                #print("i",i)
            #print("index",index)
            #print("val",val[index])
            ans.append(val[index])
            val.pop(index)
            K= K- per[i-1]*index
            #print('K',K)
            
        return ans
            
                
                
            
            
        
       
        
        
obj1 = Solution()
K = 4 
N = 3
print(obj1.findRank(N,K))