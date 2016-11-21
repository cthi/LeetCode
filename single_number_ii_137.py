class Solution(object):

    def singleNumber(self, nums):
        ht = {}

        for num in nums:
            if num in ht:
                ht[num] += 1

                if ht[num] > 3:
                    return num
            else:
                ht[num] = 1

        for key, value in ht.items():
            if value < 3:
                return key
