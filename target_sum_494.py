class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        return self.findTargetSumWays_h(0, nums, S, {})

    def findTargetSumWays_h(self, i, nums, S, memo):
        if (i, S) in memo:
            return memo[(i, S)]

        if i == len(nums):
            if S == 0:
                return 1
            else:
                return 0

        memo[(i, S)] = self.findTargetSumWays_h(i + 1, nums, S - nums[i],
                                                memo) + self.findTargetSumWays_h(i + 1, nums, S + nums[i], memo)
        return memo[(i, S)]
