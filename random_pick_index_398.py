import random


class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        index = 0
        seen = 0

        for i, num in enumerate(self.nums):
            if num == target:
                seen += 1
                if random.randint(0, seen - 1) == 0:
                    index = i

        return index
