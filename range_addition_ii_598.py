class Solution:
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if not ops:
            return m * n

        unzipped = list(zip(*ops))
        return min(unzipped[0]) * min(unzipped[1])
