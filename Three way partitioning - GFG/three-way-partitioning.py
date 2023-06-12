#User function template for Python

class Solution:
    #Function to partition the array around the range such 
    #that array is divided into three parts.
	def threeWayPartition(self, array, a, b):
	    array.sort()
	    # code here 
	   # n=len(array)
	   # if a in array:
	   #     inda=array.index(a)
    #     else:
    #         inda=0
	   # if b in array:
	   #     indb=array.index(b)
	   # else:
	   #     indb=n-1
	    
	   ## print (n, inda, indb,array,a,b)
	   # for i in range(n) :
	   #    print(inda,indb)
	   #    if indb >inda:
	   #         if array[-i-1] < a :
	   #             array[-i-1], array[inda]=a, array[-i-1]
	   #             inda= n - i + 1
	   #         if array[i] > b:
	   #            # print (array[i], array[indb])
	   #             array[i],array[indb]= b,array[i]
	   #            # print (array[i], array[indb])
	   #             indb=i
	   #    elif indb<inda:
	   #         if array[-i-1] < b :
	   #             array[-i-1],array[indb]=b, array[-i-1]
	   #             indb= n - i + 1
	   #         if array[i] > a:
	   #             array[i], array[inda]=a,array[i]
	   #             inda=i
	           


#{ 
 # Driver Code Starts
#Initial template for Python

from collections import Counter

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        array = list(map(int, input().strip().split()))
        original = Counter(array)
        a,b = list(map(int, input().strip().split()))
        ob = Solution()
        ob.threeWayPartition(array, a, b)

        k1 = k2 = k3 = 0
        for e in array:
            if e > a:
                k3+=1
            elif e<=a and e>=b:
                k2+=1
            elif e<a:
                k1+=1

        m1 = m2 = m3 = 0
        for e in range(k1):
            if array[e]<a:
                m1+=1
        for e in range(k1, k1+k2):
            if array[e]<=a and array[e]>=b:
                m2+=1
        for e in range(k1+k2, k1+k2+k3):
            if array[e]>=a:
                m3+=1

        flag = False
        if k1==m1 and k2==m2 and k3==m3:
            flag = True
        for e in range(len(array)):
            original[array[e]]-=1
        for e in range(len(array)):
            if original[array[e]]!=0:
                flag = False
        if flag:
            print(1)
        else:
            print(0)

# } Driver Code Ends