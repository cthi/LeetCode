from collections import Counter


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        occ = sorted(Counter(citations).items(), key=lambda x: x[0])

        h_index = 0
        N = len(citations)

        for k, v in occ:
            h_index = max(h_index, min(N, k))
            N -= v

        return h_index
