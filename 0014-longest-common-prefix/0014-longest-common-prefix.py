class Solution(object):
    def longestCommonPrefix(self, strs):
        
        shorty=min(strs,key=len)
        
        ans=""
        # yo=len(shorty)
        for i,k in enumerate(shorty):
            
            for other in strs:
                if other[i]!=k:
                    return shorty[:i]
        return shorty
            
        
        
        
        
        """
        :type strs: List[str]
        :rtype: str
        """
        