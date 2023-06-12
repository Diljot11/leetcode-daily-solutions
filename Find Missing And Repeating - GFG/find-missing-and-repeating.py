#User function Template for python3

class Solution:
    def findTwoElement( self,arr, n): 
        # code here
        arr.sort()
        
        for i in range(n-1):
            # print (i+1, arr[i])
            if arr[i]==arr[i+1]:
                B=arr[i]
                
        # print (A,B)
        s=n*(n+1)/2
        A = s-sum(arr) + B
        return B, int(A)
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends