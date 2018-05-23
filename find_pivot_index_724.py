class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0

        l_sums = []
        r_sums = []

        sofar = 0

        for n in nums:
            sofar += n
            l_sums.append(sofar)

        sofar = 0

        for n in reversed(nums):
            sofar += n
            r_sums.append(sofar)
        r_sums = list(reversed(r_sums))

        for i, (x, y) in enumerate(zip(r_sums, l_sums)):
            if x == y:
                return i

        return -1
