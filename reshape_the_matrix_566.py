class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        ar = len(nums)
        ac = len(nums[0])

        if r * c > ar * ac:
            return nums

        i = 0
        j = 0
        l = 0
        m = 0

        output = [[0 for u in range(c)] for v in range(r)]

        while True:
            output[l][m] = nums[i][j]
            j += 1
            m += 1

            if j == ac:
                i += 1
                j = 0

            if m == c:
                l += 1
                m = 0

            if l == r:
                break

        return output
