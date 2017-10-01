class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def isPalin(s, l, r):
            while (l <= r):
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1

            return True

        def findPartitions(s, start, found, indicies):
            if start == len(s):
                found.append([s[x:y + 1] for x, y in indicies])

            for i in range(start, len(s)):
                if (isPalin(s, start, i)):
                    indicies.append((start, i))
                    findPartitions(s, i + 1, found, indicies)
                    indicies.pop()

        found = []
        findPartitions(s, 0, found, [])
        return found
