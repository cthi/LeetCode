import bisect


class Solution(object):

    def lengthOfLIS(self, nums):
        dp = []
        m = 0

        for num in nums:
            pos = bisect.bisect_left(dp, num)

            if pos == len(dp):
                dp.append(num)
                m += 1
            else:
                dp[pos] = num

        return m
