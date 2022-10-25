class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        def generate(wordlist):
            for word in wordlist:
                for char in word:
                    yield char
            yield None
        for c1,c2 in zip(generate(word1),generate(word2)):
            if  c1!=c2:
                return False
        return True
        
        
        
        
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        