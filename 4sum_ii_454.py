from collections import Counter


class Solution(object):

    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        N = len(A)
        found = 0

        left = [i + j for i in A for j in B]
        right = Counter([i + j for i in C for j in D])

        for elem in left:
            if -elem in right:
                found += right[-elem]

        return found
