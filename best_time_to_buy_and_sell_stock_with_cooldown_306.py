class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        buy = -prices[0]
        sell = float('-inf')
        wait = 0
        buy_l = 0
        sell_l = 0
        wait_l = 0

        for i, p in enumerate(prices):
            if i == 0:
                continue
            else:
                buy_l, sell_l, wait_l = buy, sell, wait
                buy = max(wait_l - p, buy_l)
                sell = max(buy_l + p, sell_l)
                wait = max(buy_l, sell_l, wait_l)

        return max(buy, sell, wait)
