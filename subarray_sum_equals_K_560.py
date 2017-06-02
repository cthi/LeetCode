from collections import defaultdict


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sums = 0
        total = 0
        occs = defaultdict(int)

        for n in nums:
            sums += n

            if sums == k:
                total += 1

            total += occs[sums - k]
            occs[sums] += 1

        return total
