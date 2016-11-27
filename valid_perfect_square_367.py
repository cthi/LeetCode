class Solution(object):

    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        start = 1

        while num > 0:
            num -= start
            start += 2

        return num == 0
