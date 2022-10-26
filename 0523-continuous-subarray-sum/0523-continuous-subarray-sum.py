class Solution(object):
    def checkSubarraySum(self, nums, k):
        dicti={0:0}
        s=0
        for i in range(len(nums)):
            s+=nums[i]
            if s%k not in dicti :
                dicti[s%k]=i+1
            elif dicti[s%k]<i:
                return True
        return False
                
        
        
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        