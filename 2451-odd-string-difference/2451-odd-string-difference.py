class Solution(object):
    def oddString(self, words):
        a={'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p':15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
        
        
        
        
        n=len(words[0])
        yo=defaultdict(list)
        y=0
        b=0
        for i in words:
            l=[]
            for j in range(n-1):
                # print a[str(i[j+1])]
                ap=a[i[j+1]]-a[i[j]]
                l.append(ap)
            if str(l) in yo:
                yo[str(l)]+=i
                # a=i
                
                
            else:
                yo[str(l)]=i
                if not b:b=str(l)
                else:y=str(l)
        if len(yo[y])<len(yo[b]):
            return yo[y]
        else:
            return yo[b]
                    
                    
                    
                
        
        
        # res=[]
        # for i in yo:
        #     if yo[i]==1:
        #         res=i
        # return res
                
                
                
                
            
        
        
        
        """
        :type words: List[str]
        :rtype: str
        """
        