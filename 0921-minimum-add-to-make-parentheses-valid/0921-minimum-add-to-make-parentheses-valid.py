class Solution(object):
    def minAddToMakeValid(self, s):
        while "()" in s:
            s=s.replace("()","")
        return len(s)
        
        """
        :type s: str
        :rtype: int
        """
        