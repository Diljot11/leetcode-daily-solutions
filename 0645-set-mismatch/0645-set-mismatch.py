class Solution(object):
    def findErrorNums(self, nums):
        
        for i in nums:
            if nums.count(i)==2:
                a=i
                break
        
                
            
        for i in range(len(nums)):
            if i+1 not in nums:
                b=i+1
                break
        return [a,b]
                
            
            
                
            
            
                
            
            
            
        
        
        
        
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        