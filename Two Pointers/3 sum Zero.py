class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def threeSum(self, A):
        A.sort()
        #print(A)
        ans = []
        sol =  set()
        
        for i in range(len(A)-2):
            
            x =  A[i]
            y = i+1
            z = len(A)-1
            
            while(y<z):
                if(-(x) > A[y]+A[z] ):
                    y = y+1    
                elif(-(x) < A[y]+A[z]):
                    z =z-1
                else:
                    ans.append(x)
                    ans.append(A[y])
                    ans.append(A[z])
                
                    #print(ans)
                    l1 = tuple(ans.copy())
                    
                    ans.clear()
                   
                    sol.add(l1)
                    y = y+1
                    z = z-1
        sol = list(sol)   
        sol1=[]        
        for i in range(len(sol)-1,-1,-1):
            sol1.append(list(sol[i]))
        
        return sol1
    
    
    
    


obj = Solution()
A = [ 1, -4, 0, 0, 5, -5, 1, 0, -2, 4, -4, 1, -1, -4, 3, 4, -1, -1, -3 ]
print(obj.threeSum(A))