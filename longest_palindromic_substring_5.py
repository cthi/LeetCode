class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        N = len(s)
        dp = [[0 for i in range(N)] for i in range(N)]
        longestLen = 0
        longestI = 0
        longestJ = 0

        for i in range(N):
            for j in range(N // 2 + 1):
                if i - j >= 0 and i + j < N and s[i + j] == s[i - j]:
                    if j == 0:
                        dp[i][i] = 1
                    else:
                        dp[i - j][i + j] = dp[i - j + 1][i + j - 1] + 2

                    if dp[i - j][i + j] > longestLen:
                        longestLen = dp[i - j][i + j]
                        longestI = i - j
                        longestJ = i + j
                else:
                    break

        for i in range(N - 1):
            for j in range(N // 2 + 1):
                if s[i] == s[i + 1] and i - j >= 0 and i + \
                        j + 1 < N and s[i - j] == s[i + j + 1]:
                    if j == 0:
                        dp[i][i + 1] = 2
                    else:
                        dp[i - j][i + j + 1] = dp[i - j + 1][i + j] + 2

                    if dp[i - j][i + j + 1] > longestLen:
                        longestLen = dp[i - j][i + j + 1]
                        longestI = i - j
                        longestJ = i + j + 1
                else:
                    break

        return s[longestI:longestJ + 1]
