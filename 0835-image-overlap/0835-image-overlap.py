class Solution(object):
    def largestOverlap(self, A, B):
        d=collections.defaultdict(int)
        a,b=[],[]
        res=0
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j]:
                    a.append((i,j))
                if B[i][j]:
                    b.append((i,j))
        for t1 in a:
            for t2 in b:
                t3=(t2[0]-t1[0],t2[1]-t1[1])
                d[t3]+=1
                
                res=max(res,d[t3])
                
        return res
                
        
        
        
        
        """
        :type img1: List[List[int]]
        :type img2: List[List[int]]
        :rtype: int
        """
        