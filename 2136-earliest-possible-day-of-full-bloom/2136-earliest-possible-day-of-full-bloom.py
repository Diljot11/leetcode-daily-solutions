class Solution(object):
    def earliestFullBloom(self, plantTime, growTime):
        res=0
        for grow,plant in sorted(zip(growTime,plantTime)):
            res=max(res,grow)+plant
        return res
        
        """
        :type plantTime: List[int]
        :type growTime: List[int]
        :rtype: int
        """
        