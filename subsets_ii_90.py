class Solution(object):

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subsets = {tuple()}
        nums = sorted(nums)
        self._subsetsWithDup(0, nums, [], subsets)
        return list(subsets)

    def _subsetsWithDup(self, pos, nums, cur, subsets):
        for i in range(pos, len(nums)):
            cur.append(nums[i])
            subsets.add(tuple(cur))
            self._subsetsWithDup(i + 1, nums, cur, subsets)
            cur.pop()
