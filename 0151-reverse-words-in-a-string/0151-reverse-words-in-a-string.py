class Solution(object):
    def reverseWords(self, s):
        
        l=s.split()
        s=" ".join(l[::-1])
        return s
        
        
        """
        :type s: str
        :rtype: str
        """
        