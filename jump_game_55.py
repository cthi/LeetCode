class Solution(object):
    def canJump(self, nums):
        m = 0
        
        for i, n in enumerate(nums):
            if n == 0 and i != len(nums) - 1 and i >= m:
                return False
                
            m = max(m, i + n)
                
        return True
                    
