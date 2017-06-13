class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set()
        mx = 0

        for i, n in enumerate(nums):
            if n not in seen:
                mx = max(mx, self.findNestingLen(i, nums, seen))

        return mx

    def findNestingLen(self, pos, nums, seen):
        count = 0

        while True:
            pos = nums[pos]

            if pos in seen:
                return count
            else:
                seen.add(pos)
                count += 1
