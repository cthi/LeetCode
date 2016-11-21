class Solution(object):

    def wordBreak(self, s, wordDict):
        memo = {}
        return self.wordBreakHelper(0, s, wordDict, memo)

    def wordBreakHelper(self, start, s, wordDict, memo):
        if start == len(s):
            return True

        if start in memo:
            return memo[start]

        cur = ""

        for i in range(start, len(s)):
            cur += s[i]

            if cur in wordDict:
                memo[start] = self.wordBreakHelper(i + 1, s, wordDict, memo)

                if memo[start]:
                    return True

        return False
