class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        nums.sort()
        
        if N % 2 == 0:
            mid = N // 2
        else:
            mid = N // 2 + 1

        nums[::2], nums[1::2] = nums[:mid][::-1], nums[mid:][::-1]
