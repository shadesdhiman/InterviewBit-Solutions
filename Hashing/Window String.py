# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 11:06:24 2021

@author: Dhiman
"""

class Solution:
	# @param A : string
	# @param B : string
	# @return a strings
    def minWindow(self, A, B):
        ans = []
        pans = []
        dic2 = dict()
        for i in range(len(B)):
            if B[i] in dic2:
                dic2[B[i]] +=1
            else:
                dic2[B[i]] = 1
        mc = 0
        dmc = len(B)
        
        dic1 = dict()
        i = -1
        j = -1
        
        while(True):
            #acquire
            f1 = False
            f2 = False
            while(i<len(A)-1 and mc<dmc):
                i = i+1
                ch = A[i]
                if ch in dic1:
                    dic1[ch] +=1
                else:
                    dic1[ch] = 1
                
                if ch in dic2:
                    if dic1[ch] <= dic2[ch]:
                        mc +=1
                f1 = True
            #collect ans and release
            while(j<i and mc == dmc):
                pans = A[j+1:i+1]
                if len(ans)==0 or len(pans) <len(ans):
                    ans = pans
                j = j+1
                ch = A[j]
                if ch in dic1:
                    if dic1[ch]==1:
                        del dic1[ch]
                    else:
                        dic1[ch]-=1
                if ch in dic2:
                    if ch not in dic1:
                        mc -=1
                    else:
                        if dic1[ch]<dic2[ch]:
                            mc-=1
                f2 = True
            if f1 ==False and f2 ==False:
                break
        return "".join(ans)
            
 



        


S = "ADOBECODEBANC"
T = "ABC"
obj = Solution()
print(obj.minWindow(S,T))