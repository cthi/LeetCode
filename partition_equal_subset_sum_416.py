class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        N = sum(nums)

        if N % 2 != 0:
            return False

        goal = sum(nums) // 2

        return self.canPartition_h(nums, goal, 0, 0, {})

    def canPartition_h(self, nums, goal, acc, i, memo):
        if (acc, i) in memo:
            return memo[(acc, i)]
        elif acc == goal:
            return True
        elif i == len(nums):
            return False

        res = self.canPartition_h(
            nums,
            goal,
            acc + nums[i],
            i + 1,
            memo) or self.canPartition_h(
            nums,
            goal,
            acc,
            i + 1,
            memo)
        memo[(acc, i)] = res
        return res
