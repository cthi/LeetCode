class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        best = 0
        run = 0
        
        for n in nums:
            if n == 1:
                run += 1
            else:
                run = 0
                
            if run > best:
                best = run
            
        return best
