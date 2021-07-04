# -*- coding: utf-8 -*-
"""
Created on Fri May 28 11:34:44 2021

@author: Dhiman
"""

class Solution:
    # @param A : integer
    # @return a strings
    def intToRoman(self, A):
        ans =[]
        res =""
        
        while(A):
            #print("Before 1000 A = ",A)
            while(A//1000):
                times = A//1000
                #print(times)
                A = A%1000
                for i in range(times):
                    ans.append("M")
            
            #print("Before 500 A = ",A)
            while(A//500):
               
                if(A >= 900):
                    ans.append("CM")
                    A=A%900
                    break
                
                times = A//500
               
                A = A%500
                for i in range(times):
                    ans.append("D")
            
            #print("Before 100 A = ",A)
            while(A//100):
               
                if(A >= 400):
                    ans.append("CD")
                    A=A%400
                    break
                
                times = A//100
                #print(times)
               
                A = A%100
                for i in range(times):
                    ans.append("C")
                    
            #print("Before 50 A = ",A)
            while(A//50):
             
                if(A >= 90):
                    ans.append("XC")
                    A=A%90
                    break
                times = A//50
               
                A = A%50
                for i in range(times):
                    ans.append("L")
                    
            #print("Before 10 A = ",A)
            while(A//10):
                
                if(A >= 40):
                    ans.append("XL")
                    A=A%40
                    break
                
                times = A//10
                
                A = A%10
                for i in range(times):
                    ans.append("X")
            #print("Before 5 A = ",A)
            while(A//5):
                if(A == 9):
                    ans.append("IX")
                    A=0
                    break
                    
                times = A//5
                
                A = A%5
                for i in range(times):
                    ans.append("V")
            if(A==4):
                ans.append("IV")
                A=0
                
                
            if(A==3):
                ans.append("III")
                A=0
                
                
            if(A==2):
                ans.append("II")
                A=0
               
                
            if(A==1):
                ans.append("I")
                A= 0
        return res.join(ans)
            
    
obj = Solution()
A= 40
print(obj.intToRoman(A))