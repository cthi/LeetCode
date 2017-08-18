class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for i in range(n + 1)]

        for i in range(1, n + 1):
            if i < 4:
                dp[i] = i
            elif math.sqrt(i) - int(math.sqrt(i)) == 0:
                dp[i] = 1
            else:
                least = float('inf')
                j = 1

                while i - j * j > 0:
                    least = min(least, dp[i - j * j] + 1)
                    j += 1

                dp[i] = least

        return dp[n]
