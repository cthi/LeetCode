from collections import defaultdict

class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        occ = defaultdict(list)

        for i, n in enumerate(nums):
            occ[n].append(i)

        most = max(len(x) for x in occ.values())
        candidates = [k for k, v in occ.items() if len(v) == most]
        return min(occ[x][-1] - occ[x][0] + 1 for x in candidates)
