class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        l = 1
        best = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                l += 1
            else:
                l = 1

            best = max(best, l)

        return best
