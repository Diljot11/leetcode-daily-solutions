class Solution(object):
    def longestPalindrome(self, words):
        done=Counter(words)
        count=0
        # print done
        for i in done:
            
            rev=i[::-1]
            if rev==i:
                m=done[i]-done[i]%2
                done[i]=done[i]-m
                count+=m
            elif rev in words:
                if done[i] >0 and done[rev]>0:
                    m=min(done[i],done[rev])
                    done[i]=done[i]-m
                    done[rev]=done[rev]-m
                    count+=2*m
            # print i,count
        for i in done:
            if i==i[::-1] and done[i]>0:
                done[i]-=1
                count+=1
                # print count,i
                break
        return 2*count
            
            
        
                    
        
        
                
        
        
        
        
        
        """
        :type words: List[str]
        :rtype: int
        """
        