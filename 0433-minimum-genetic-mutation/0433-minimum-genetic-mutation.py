import copy
class Solution(object):
    def minMutation(self, s, e, bank):
        queue = []
        queue.append((s,0))
        bankSet = set(bank)
        
        while queue:
            curr, step = queue.pop(0)
            if curr == e:
                return step
            for i in range(len(curr)):
                for c in "AGCT":
                    mutation = curr[:i] + c + curr[i+1:]
                    if mutation in bankSet:
                        bankSet.remove(mutation)
                        queue.append((mutation,step+1))
                        
        return -1
        
            
                
                    
            
                
                
            
        
        
        
        
        
        
        """
        :type startGene: str
        :type endGene: str
        :type bank: List[str]
        :rtype: int
        """
        