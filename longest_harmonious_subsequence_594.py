from collections import Counter


class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numsOcc = sorted(Counter(nums).items(), key=lambda x: x[0])
        best = 0

        for i in range(len(numsOcc) - 1):
            if numsOcc[i + 1][0] - numsOcc[i][0] == 1:
                best = max(best, numsOcc[i][1] + numsOcc[i + 1][1])

        return best
