class Solution(object):
    def groupAnagrams(self, strs):
        yo=defaultdict(list)
        
        for word in strs:
            yo[tuple(sorted(word))].append(word)
        return list(yo.values())
        
        
            
        
        
        
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        