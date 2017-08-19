class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def expBySqr(x, n):
            if n == 1:
                return x
            if n % 2 == 1:
                return x * expBySqr(x * x, (n - 1) / 2)
            else:
                return expBySqr(x * x, n / 2)

        if n == 0:
            return float(1)
        if n < 0:
            return 1 / expBySqr(x, -1 * n)
        else:
            return expBySqr(x, n)
