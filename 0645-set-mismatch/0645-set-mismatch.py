class Solution(object):
    def findErrorNums(self, nums):
        a,b=0,0
        res=Counter(nums)
        for i in res:
            if res[i]==2:
                a=i
                break
        for i in range(len(nums)):
            
            if nums.count(i+1)==0:
                b=i+1
                break
        return [a,b]
            
        
        
        
        
        
#          a,b=0,0
#         for i in nums:
#             if nums.count(i)==2:
#                 a=i
#                 break
        
                
            
#         for i in range(len(nums)):
            

            
            
#             if i+1 not in nums:
#                 b=i+1
            
                
#         return [a,b]
                
            
            
                
            
            
                
            
            
            
        
        
        
        
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        