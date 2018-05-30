from collections import defaultdict

class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        last = defaultdict(int)
        result = []
        start = 0
        end = 0

        for i, x in enumerate(S):
            last[x] = i

        for i, x in enumerate(S):
            end = max(end, last[x])

            if i == end:
                result.append(i - start + 1)
                start = i + 1
                end = i + 1

        return result
