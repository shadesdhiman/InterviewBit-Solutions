# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 09:03:21 2021

@author: Dhiman
"""

class Solution:
	# @param A : list of integers
	# @return a list of integer
    def equal(self, A):
        i = 0
        j = len(A)-1
        
        dic = dict()
        
        ans = []
        for i in range(len(A)-1):
            for j in range(i+1, len(A)):
                p = A[i]
                q = A[j]
                summ = p+q
                if summ in dic:
                    a = dic[summ][0]
                    b =dic[summ][1]
                    c = i
                    d = j
                    if a == c or b == d or b == c or a == d:
                        pass
                    else:
                        ans.append([a,b,c,d])
                else:
                    dic[summ] = [i,j]
                    
                    
       
        return min(ans)
        
        
    

                    
                
                    
        
















A = [ 0, 0, 1, 0, 2, 1 ]
obj = Solution()
print(obj.equal(A))