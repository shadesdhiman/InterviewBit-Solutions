class Solution:
    # @param A : list of strings
    # @return an integer
    def solve(self, A):
        res = []
        
        def find_lcm(num1, num2):
            if(num1>num2):
                num = num1
                den = num2
            else:
                num = num2
                den = num1
            rem = num % den
            while(rem != 0):
                num = den
                den = rem
                rem = num % den
            gcd = den
            lcm = int(int(num1 * num2)/int(gcd))
            return lcm
             
        
        
        
        def swap(x,i):
            for itr in range(i+1):
                x.append(x[0])
                x.pop(0)
                
                
            
        def checker(org_x):
            org_x = list(org_x)
            
            x = []
            count = 0
            index = 0
            #print( org_x)
            while(x!= org_x):
                if count == 0:
                    x = org_x.copy()
                    
                index = count%len(org_x)
                
                swap(x,index)
                count+=1
                #print(x, index+1    , org_x)
            return count
                
            
                
           
                
                
               
        for i in A:
            res.append(checker(i))
            
       
        if len(res)>=2:
         
            num1 = res[0]
            num2 = res[1]
            lcm = find_lcm(num1, num2)
                 
            for i in range(2, len(res)):
                lcm = find_lcm(lcm, res[i]) 
                    
        
            
        else:
            return res[0]%(10**9+7)
        return lcm%(10**9+7)
                
        
obj = Solution()
A = [ "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "babaaaabbaba","aba"]
print(obj.solve(A))
