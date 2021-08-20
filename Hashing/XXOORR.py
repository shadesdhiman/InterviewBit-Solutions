# cook your dish here
try:
    def checking(n,k,arr):
        count = 0
        if n == 0 or k ==0:
            return 0
        p = 0
        while(True):
            temp = k   
           
            for i in range(n):
                flag = 1
                if arr[i] == 0:
                    continue
                if temp>0:
                    x = arr[i]^(2**p)
                    
                    if (x < arr[i]):
                        if flag ==1 and temp ==k :
                            flag =0
                            count+=1
                        
                        arr[i] = x
                        temp -=1
                        #print(i,temp,arr,count)
                        
                    if temp == 0:
                        temp = k
                        flag = 1
           
            
            p=p+1
            if max(arr) == 0:
                return count
   

    
    testcase = int(input())
    for i in range(testcase):
        n,k= map(int,input().split())
        arr= list(map(int,input().split()))
        print(checking(n,k,arr))
except:
    pass