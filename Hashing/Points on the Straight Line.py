class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def maxPoints(self, A, B):
        dic = dict()
        if len(A)==0 and len(B) == 0:
            return 0
        maxi = 0
        for i in range(len(A)-maxi-1):
            i_max = 0
            for j in range(i+1,len(A)):
                if A[j]-A[i] == 0:
                    slope =  10000001
                else:
                    slope = float(B[j] - B[i]) / float(A[j] - A[i])
                if slope in dic:
                    dic[slope ] +=1
                else:
                    dic[slope] = 1


                i_max = i_max if i_max>dic[slope] else dic[slope]
            
            dic.clear()
            maxi = maxi if maxi>i_max else i_max
        return maxi+1


obj  = Solution()
A = [1,1]
B = [2,2]
print(obj.maxPoints(A,B))
