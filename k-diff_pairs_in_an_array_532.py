from collections import Counter


class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        if k < 0:
            return 0

        numsSet = set(nums)
        numsOcc = Counter(nums)
        ans = set()

        for n in numsSet:
            if k == 0:
                if numsOcc[n] >= 2:
                    ans.add((n, n))
            else:
                if n - k in numsSet and (n - k, n) not in ans:
                    ans.add((n - k, n))
                if n + k in numsSet and (n, n + k) not in ans:
                    ans.add((n, n + k))

        return len(ans)
