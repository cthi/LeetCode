class Solution(object):

    def findDisappearedNumbers(self, nums):
        i = 0

        while i < len(nums):
            if nums[i] != i + 1:
                tmp = nums[nums[i] - 1]
                if nums[i] == tmp:
                    i += 1
                    continue
                nums[nums[i] - 1] = nums[i]
                nums[i] = tmp
            else:
                i += 1

        res = []

        for i, e in enumerate(nums):
            if i + 1 != e:
                res.append(i + 1)

        return res
