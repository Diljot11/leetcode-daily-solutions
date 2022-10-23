
class Solution(object):
    def subarrayGCD(self, nums, k):
        def gcd(a, b):
            if(b == 0):
                return a
            else:
                return gcd(b, a % b)
        res=0
        n=len(nums)
        for i in range(n):
            s=0
            for j in range(i,n):
                s=gcd(s,nums[j])
                if s==k:
                    res+=1
                    
            
            
        return res
                
                
                
        
        
        
        
        
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        