class Solution(object):
    def isValid(self, s):
        l={"]":"[","}":"{",")":"("}
        stack=[]
        for i in s:
            if i in l.values():
                stack.append(i)
            elif i in l.keys():
                if stack==[] or stack.pop()!=l[i]:
                    return False
            else:
                return False
        return stack==[]
    
                    
            
                
    
        
        
        
        
        
        """
        :type s: str
        :rtype: bool
        """
        