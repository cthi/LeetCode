class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp = [0 for i in range(len(cost))]

        for i in range(2, len(cost)):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])

        return min(dp[len(cost) - 1] + cost[len(cost) - 1], dp[len(cost) - 2] + cost[len(cost) - 2])
