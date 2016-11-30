class Solution(object):

    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        diffs = []

        for i in range(len(nums) - 1):
            res = nums[i + 1] - nums[i]
            if res != 0:
                diffs.append(res)

        count = len(diffs)

        for i in range(len(diffs) - 1):
            if ((diffs[i] > 0) == (diffs[i + 1] > 0)):
                count -= 1

        return count + 1
