class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False

        charMap = [0 for i in range(26)]
        windowMap = [0 for i in range(26)]

        for c in s1:
            charMap[ord(c) - ord('a')] += 1

        for c in s2[:len(s1)]:
            windowMap[ord(c) - ord('a')] += 1

        begin = 0
        end = len(s1)

        if charMap == windowMap:
            return True

        while end < len(s2):
            windowMap[ord(s2[begin]) - ord('a')] -= 1
            windowMap[ord(s2[end]) - ord('a')] += 1

            if charMap == windowMap:
                return True

            end += 1
            begin += 1

        return False
