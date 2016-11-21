class Solution(object):

    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        count = 0
        g = sorted(g)
        s = sorted(s)

        start = 0

        for cookie in s:
            if start == len(g):
                break

            if g[start] <= cookie:
                count += 1
                start += 1

        return count
