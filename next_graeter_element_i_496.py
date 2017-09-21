from collections import defaultdict


class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        decreasing = []
        nge = defaultdict(lambda: -1)

        for n in nums:
            if not decreasing:
                decreasing.append(n)
            else:
                while decreasing and n > decreasing[-1]:
                    nge[decreasing.pop()] = n
                decreasing.append(n)

        return [nge[x] for x in findNums]
