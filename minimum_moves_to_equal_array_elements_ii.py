class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        median = nums[len(nums) // 2]
        diff = 0
        
        for num in nums:
            diff += abs(median - num)
            
        return diff
