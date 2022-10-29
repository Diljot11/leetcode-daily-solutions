class Solution(object):
    def twoEditWords(self, queries, dictionary):
        res=[]
        for q in queries:
            if any(sum(c1!=c2 for c1,c2 in zip(q,d))<=2 for d in dictionary):
                res.append(q)
        return res
    
                
        
        
        
#         n=len(queries[0])
#         if n<=2:
#             return queries
#         def d(s1,s2):
#             count=0
#             for i in range(n):
#                 if s1[i]!=s2[i]:
#                     count+=1
#             return count
        
#         res=[]
#         for i in range(len(queries)):
#             for j in range(len(dictionary)):
                
#                 if d(queries[i],dictionary[j])<=2:
#                     if queries.count(queries[i]) < res.count(queries[i]) or queries[i] not in res :
#                         res.append(queries[i])
#         return res
                    
                    
            
        
        
        
        
        
        
        """
        :type queries: List[str]
        :type dictionary: List[str]
        :rtype: List[str]
        """
        