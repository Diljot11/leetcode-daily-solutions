class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        yo={}
        i,j=0,len(nums)-1
        while i<j:
            # print i,j
            if nums[i]==nums[j] :
                # print i,j,2
                if abs(i-j)<=k:
                    # print i,j,6
                    return True
            if nums[i] in yo :
                if abs(i-yo[nums[i]])<=k:
                    # print i,j,3
                    return True
            if nums[j] in yo :
                if abs(j-yo[nums[j]])<=k:
                    # print i,j,4
                    return True
                
            else:
                # print i,j,5
                yo[nums[i]]=i
                yo[nums[j]]=j
                
                # print i,j,1
            i+=1
            j-=1
                
        return False
                
            
            
        
        
        
        
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        