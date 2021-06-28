# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 10:29:19 2021

@author: Dhiman
"""

class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def addBinary(self, A, B):
        len_A = len(A)
        len_B = len(B)
        res = []
        carry = 0
        for i in range(-1,-min(len_A, len_B)-1,-1):
           
            if (A[i]==B[i]=='0'):
                ##print("8998")
                if carry ==1:
                    res.insert(0,'1')
                    carry = 0
                else:
                    res.insert(0,'0')
                
            elif(A[i]==B[i]=='1'):
                if carry == 0:
                    res.insert(0,'0')
                    carry = 1
                    #print("equal 1",res, carry)
                else:
                    res.insert(0,'1')
                    carry = 1
                    #print("equal 1",res, carry)
            else:
                if(carry == 0):
                    res.insert(0,'1')
                    #print("not equal ",res, carry)
                else:
                    res.insert(0,'0')
                    
                    #print("not equal ",res, carry)
                    
        ##print(len(A), len(B), res)
        if(len_A > len_B):
            rem = len_A - len_B
            for i in range(rem-1,-1,-1):
               
                if carry == 0:
                    res.insert(0,A[i])
                else:
                    if A[i]=='0':
                        res.insert(0,str(carry))
                        carry = 0
                    else:
                        res.insert(0,'0')
        elif(len_A < len_B):
            rem = len_B - len_A
            ##print("**********")
            for i in range(rem-1,-1,-1):
                if carry == 0:
                    res.insert(0,B[i])
                else:
                    if B[i]=='0':
                        res.insert(0,str(carry))
                        carry = 0
                    else:
                        res.insert(0,'0')
        ##print(res)
        if carry == 1:
            res.insert(0,'1')
        C = ""
        return C.join(res)
                    
                    
                    
obj = Solution()
A = "100100111"
B = "101001"
print(obj.addBinary(A,B))