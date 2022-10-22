class Solution(object):
    def minWindow(self, s, t):
        need,missing=Counter(t),len(t)
        i=0
        end,start=0,0
        
        for j,c in enumerate(s,1):
            if need[c]>0:
                missing-=1
            need[c]-=1
            
            if not missing:
                while need[s[i]]<0:
                    need[s[i]]+=1
                    i+=1
                need[s[i]]+=1
                missing+=1
                if end==0 or j-i < end-start:
                    end,start=j,i
                i+=1
        return s[start:end]
        
        
        
        
        
        
        
        
        
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        