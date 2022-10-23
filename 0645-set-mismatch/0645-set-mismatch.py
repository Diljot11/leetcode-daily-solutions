class Solution(object):
    def findErrorNums(self, nums):
        
        n = len(nums)
        s = n*(n+1)//2
        miss = s - sum(set(nums))
        duplicate = sum(nums) + miss - s
        return [duplicate, miss]
        
#         n=len(nums)
#         s=sum(set(nums))
        
#         return[sum(nums)-s,n*(n+1)//2 - s]
#         a,b=0,0
#         res=Counter(nums)
#         for i in res:
#             if res[i]==2:
#                 a=i
#                 break
#         for i in range(len(nums)):
            
#             if nums.count(i+1)==0:
#                 b=i+1
#                 break
#         return [a,b]
            
        
        
        
        
        
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
        