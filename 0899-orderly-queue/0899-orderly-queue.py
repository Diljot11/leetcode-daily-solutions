class Solution(object):
    def orderlyQueue(self, s, k):
        if k>1:
            return "".join(sorted(s))
        else:
            return min(s[i:]+s[:i] for i in range(len(s)))
                

        
        
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        