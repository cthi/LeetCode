class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = 1
        mut = 1

        for i in range(n):
            if i == 0:
                mut = 9
            else:
                if 10 - i < 0:
                    break
                mut *= 10 - ia
            nums += mut

        return nums
