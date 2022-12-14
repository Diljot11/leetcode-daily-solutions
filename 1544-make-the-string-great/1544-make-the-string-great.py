class Solution(object):
    def makeGood(self, s):
        stack = []
        for c in s: 
            if stack and ord(stack[-1]) ^ ord(c) == 32: stack.pop() #pop "bad"
            else: stack.append(c) #push "good"
        return "".join(stack) 
        
        
        
        
        
        
        """
        :type s: str
        :rtype: str
        """
        