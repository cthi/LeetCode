class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = self.bsl(0, len(nums) - 1, nums, target, -1)
        right = self.bsr(0, len(nums) - 1, nums, target, -1)
        
        return [left, right]
        
    def bsl(self, start, end, nums, target, left):
        if start > end:
            return left
        else:
            mid = (start + end) // 2
            
            if nums[mid] > target:
                return self.bsl(start, mid - 1, nums, target, left)
            elif nums[mid] < target:
                return self.bsl(mid + 1, end, nums, target, left)
            else:
                return self.bsl(start, mid - 1, nums, target, mid)
                
    
    def bsr(self, start, end, nums, target, right):
        if start > end:
            return right
        else:
            mid = (start + end) // 2
            print(mid)
            if nums[mid] > target:
                return self.bsr(start, mid - 1, nums, target, right)
            elif nums[mid] < target:
                return self.bsr(mid + 1, end, nums, target, right)
            else:
                return self.bsr(mid + 1, end, nums, target, mid)
