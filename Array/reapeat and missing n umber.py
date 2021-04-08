class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        
 
   
        max_A = max(A)
      
        Repeat = None
        
        for i in A:
            if A.count(i)>1:
                Repeat = i
                break
            
        #print(Dict1)
                
        for i in range(1,max_A):
            if i in A:
                continue
            else:
                missing =i
                break
                
        return [Repeat,missing]
        
            
            
            
            
        











A = Solution()
L1 = [2]

print(A.repeatedNumber(L1))