class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self, A, B):
        self.A = A
        self.B = B
        if(min(A,B)==0):
            return max(A,B)
        def g(A,B):
            if(A%B==0):
                return min(A,B)
            if(A<=1 or B<=1):
                if(A<B):
                    return A
                else:
                    return B
            A = A%B
            if(A>B):   
                return(g(A,B))
            elif(A<B):
                return(g(B,A))
        return(g(A,B))

















obj1 = Solution()
A= 120
B = 0
print(obj1.gcd(A,B))
        