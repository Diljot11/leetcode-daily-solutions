class Solution(object):
    def averageValue(self, nums):
        l=[]
        
        for i in nums:
            if i%2==0 and i%3==0:
                l.append(i)
        if len(l)==0:
            return 0
        return int(round(sum(l)/len(l)))
        
        
        
        
        
        """
        :type nums: List[int]
        :rtype: int
        """
        