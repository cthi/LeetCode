class Solution(object):
    def arrangeCoins(self, n):
        rows = 0
        counter = 1
        while n - counter >= 0:
            n -= counter
            rows += 1
            counter += 1
            
        return rows
