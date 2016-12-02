class Solution(object):

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        k = k % N

        res = []

        for i in range(N - k, N):
            res.append(nums[i])

        for i in range(N - k):
            res.append(nums[i])

        for i in range(N):
            nums[i] = res[i]
