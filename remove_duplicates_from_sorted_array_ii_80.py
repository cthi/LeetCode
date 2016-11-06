class Solution(object):
    def removeDuplicates(self, nums):
        ht = {}
        insert = 0
        
        for num in nums:
            if num in ht:
                ht[num] += 1
            else:
                ht[num] = 1
                
            if ht[num] > 2:
                continue
            else:
                nums[insert] = num
                insert += 1
                
        return insert
