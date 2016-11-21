class Solution(object):

    def findDuplicates(self, nums):
        i = 0
        res = set()

        while i < len(nums):
            if nums[i] != i + 1:
                tmp = nums[nums[i] - 1]
                if nums[i] == tmp:
                    res.add(tmp)
                    i += 1
                    continue
                nums[nums[i] - 1] = nums[i]
                nums[i] = tmp
            else:
                i += 1

        return list(res)
