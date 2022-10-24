class Solution(object):
    def maxLength(self, A):
        dp = [set()]
        for a in A:
            if len(set(a)) < len(a): continue
            a = set(a)
            # print a,dp
            for c in dp[:]:
                if a & c: 
                    # print a,c, a|c
                    continue
                
                dp.append(a | c)
        return max(len(a) for a in dp)
        """
        :type arr: List[str]
        :rtype: int
        """
        