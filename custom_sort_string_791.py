from collections import Counter

class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        t_count = Counter(T)
        out = ""

        for c in S:
            if t_count[c] > 0:
                out += t_count[c] * c
                t_count[c] = 0

        for k, v in t_count.items():
            if v != 0:
                out += k * v

        return out
