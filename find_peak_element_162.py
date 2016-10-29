class Solution(object):
    def findPeakElement(self, nums):
        if len(nums) == 1:
            return 0
        else:
            return self.fpe(0, len(nums) - 1, nums)
        

    def fpe(self, start, end, nums):
        middle = (start + end) // 2
        
        if (middle == 0 and nums[middle] > nums[middle + 1]) or (middle == len(nums) - 1 and nums[middle] > nums[middle - 1]):
            return middle
        elif nums[middle] > nums[middle + 1] and nums[middle] > nums[middle - 1]:
            return middle
        elif nums[middle] < nums[middle + 1]:
            return self.fpe(middle + 1, end, nums)
        else:
            return self.fpe(start, middle - 1, nums)
        
