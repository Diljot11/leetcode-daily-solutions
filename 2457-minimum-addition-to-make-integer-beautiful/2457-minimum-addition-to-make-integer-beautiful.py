class Solution(object):
    def makeIntegerBeautiful(self, n, target):
        def round_up(n, decimals = 0):
            multiplier = 10 ** decimals
            return math.ceil(n * multiplier) / multiplier
        ln=len(str(n))
        
        # print round_up(19,-2)
        def  sumi(m):
            l=[]
            for i in str(m):
                l.append(int(i))
            # print l
            return sum(l)
            
        if sumi(n)<=target:
            # print l
            return 0
        else:
            # print l,round_up(n,-(ln-1)),n
            if ln>1:
                temp=n
                for i in range(1,15):
                    
                    temp=int(round(round_up(n,-(i-1)))-n) + n
                    # print temp
                    # print(temp,sumi(int(temp)),round(round_up(n,-(i-1))),n)
                    if sumi(int(temp))<=target:
                        return abs(n-temp)
                    
            else:
                return int(round_up(n,-1)-n)
            
            
            
            
            
            
        
        
        
        
        
        
        """
        :type n: int
        :type target: int
        :rtype: int
        """
        