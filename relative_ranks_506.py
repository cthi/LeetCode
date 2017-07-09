class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ranks = {}
        copy = sorted(nums[:], reverse=True)

        for i, c in enumerate(copy):
            if i == 0:
                ranks[c] = "Gold Medal"
            elif i == 1:
                ranks[c] = "Silver Medal"
            elif i == 2:
                ranks[c] = "Bronze Medal"
            else:
                ranks[c] = str(i + 1)

        return [ranks[x] for x in nums]
