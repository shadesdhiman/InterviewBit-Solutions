# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 21:48:56 2021

@author: Dhiman
"""

class Solution:
	# @param A : string
	# @param B : tuple of strings
	# @return a list of integers
    def findSubstring(self, A, B):
        ans = []
        if len(A)==0:
            
            return [0]
        if len(B)== 0:
            return [0]
        dic1 = dict()
        for i in range(len(B)):
            if B[i] in dic1:
                dic1[B[i]] +=1
            else:
                dic1[B[i]] = 1
        word_len = len(B[0])
        arr_len = len(B)
        
        for i in range(len(A)-arr_len*word_len):
            dic2 = dict()
            for j in range(arr_len):
                word_index= i+j * word_len
                word = A[word_index : word_index+word_len]
                print(word)
                
                if word not in dic1:
                    break
                if word in dic2:
                    dic2[word]+=1
                else:
                    dic2[word] = 1
                if dic1[word] < dic2[word] :
                    break
                #print(j)
                if j+1 == arr_len:
                    ans.append(i)
        return ans
            







obj  = Solution()
A= "barfoothefoobarman"
B= ["foo", "bar"]
print(obj.findSubstring(A,B))