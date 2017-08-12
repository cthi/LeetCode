class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = len(nums) - 1

        while start < end:
            mid = (start + end) // 2

            if mid % 2 == 0:
                if nums[mid + 1] == nums[mid]:
                    start = mid + 1
                else:
                    end = mid
            else:
                if nums[mid - 1] == nums[mid]:
                    start = mid + 1
                else:
                    end = mid

        return nums[start]
