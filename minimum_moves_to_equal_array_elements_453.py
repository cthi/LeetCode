class Solution(object):

    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        smallest = min(nums)
        return sum([n - smallest for n in nums])
