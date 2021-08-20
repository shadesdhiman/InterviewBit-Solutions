# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 07:54:21 2021

@author: Dhiman
"""
class Solution:
	# @param A : tuple of strings
	# @return an integer
    def isValidSudoku(self, A):
        dic = dict()
        for i in range(len(A)):
            for j in range(len(A)):
                if A[i][j] ==".":
                    continue 
                box = (i//3) * 3 + j//3
                string_row  = "row"+str(i)+A[i][j]
                if string_row in dic:
                    return 0
                dic[string_row ] = 1
                string_col  = "col"+str(j)+A[i][j]
                if string_col in dic:
                    return 0
                dic[string_col ] = 1
                string_box  = "box"+str(box)+A[i][j]
                if string_box in dic:
                    return 0
                dic[string_box ] = 1
        return 1
                












A = ["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"]
obj = Solution()
print(obj.isValidSudoku(A))

