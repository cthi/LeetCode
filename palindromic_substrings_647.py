class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ss = 0

        for i in range(len(s)):
            for j in range(len(s) // 2 + 1):
                if i - j >= 0 and i + j < len(s) and s[i - j] == s[i + j]:
                    ss += 1
                else:
                    break

        for i in range(len(s) - 1):
            for j in range(len(s) // 2 + 1):
                if s[i] == s[i + 1] and i - j >= 0 and i + \
                        j + 1 < len(s) and s[i - j] == s[i + 1 + j]:
                    ss += 1
                else:
                    break

        return ss
