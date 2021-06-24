class Solution:
    # @param A : integer
    # @return a list of integers
    def primesum(self, A):
        import math
        pl = []
        pn = []
        if(A>100000):
            limit = int(math.sqrt(A))+1
        else:
            limit = A//2
        #print(limit)
        for i in range(limit+1):
            pl.append(1)
        for i in range(2,int(math.sqrt(limit))+1):
            if pl[i]==1:
                for j in range(2,limit ):
                    if(i*j>limit):
                        break
                    #print(i,j,i*j)
                    pl[i*j]=0
            
        pl[0]=0
        pl[1]=0
        #print(pl)        
        def isPrime(A):
        
            if(A==1):
                return 0
            if(A==2 or A==3):
                return 1
            upperlimit = int(math.sqrt(A))
            for i in range(2,upperlimit+1):
                if(A%i==0):
                    return 0
            return 1
        
        for i in range(len(pl)):
            if(pl[i]==1):
                pn.append(i)
        
        front =0
        #print(pn)
        for i in range(len(pn)):
            if(isPrime(A-pn[i])):
                return [pn[i],A-pn[i]]
        return 0
                        
            
            
            
                    
                    
                    
                
                
            
            
            
            
                    
            


obj1 = Solution()
A= 559
print(obj1.primesum(A))