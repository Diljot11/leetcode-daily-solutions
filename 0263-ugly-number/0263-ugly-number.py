class Solution(object):
    def isUgly(self, n):
        if n ==0:
            return False
        while n%2==0:
            n/=2
            # print n
        while n%3==0:
            n/=3
            # print n
        while n%5==0:
            n/=5
        # print n
        return n==1

        
#         for i in (2,3,5):
#             while n%i==0<n:
#                 n/=i
#         return n==1
        
        
        
        
        
        """
        :type n: int
        :rtype: bool
        """
        