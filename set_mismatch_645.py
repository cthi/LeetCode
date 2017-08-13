class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            if nums[i] != i + 1:
                cur = nums[i]

                while True:
                    replace = nums[cur - 1]

                    if replace == cur:
                        break
                    else:
                        nums[cur - 1] = cur
                        nums[i] = replace
                        cur = replace

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return (nums[i], i + 1)
