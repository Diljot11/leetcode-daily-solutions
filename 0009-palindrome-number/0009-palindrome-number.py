class Solution(object):
    def isPalindrome(self, x):
        
        if x<0 or (x>0 and x%10==0):
            return False
        res=0
        while x>res:
            res=res*10+x%10
            x=x//10
        return True if (x==res or x==res//10) else False
        
        
#         x=str(x)
#         i=0
#         j=len(x)-1
#         while i<j:
#             if x[i]!=x[j]:
            
#                 return False
#             i+=1
#             j-=1
#         return True
        
        
        
        
        """
        :type x: int
        :rtype: bool
        """
        